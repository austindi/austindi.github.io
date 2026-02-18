<template>
  <article class="prefect-card card">
    <h3 class="prefect-card__title">Pipeline metrics</h3>
    <div v-if="stats" class="prefect-card__body">
      <p class="prefect-card__updated">
        Last updated: {{ formatDate(stats.updated_at) }}
      </p>
      <div class="prefect-card__grid">
        <div
          v-for="m in metrics"
          :key="m.key"
          class="prefect-card__item"
        >
          <div class="prefect-card__label-wrap">
            <span class="prefect-card__label prefect-card__label--with-tip"
              >{{ m.label }}<span class="prefect-card__tip-icon" aria-hidden="true">ⓘ</span></span>
            <span
              class="prefect-card__tooltip"
              role="tooltip"
            >{{ m.tooltip }}</span>
          </div>
          <span
            :class="['prefect-card__value', m.pct && 'prefect-card__value--pct']"
          >
            {{ m.display }}
          </span>
        </div>
      </div>
    </div>
    <div v-else class="prefect-card__body">
      <p v-if="loadError" class="section__desc prefect-card__error">Unable to load pipeline metrics.</p>
      <p v-else class="section__desc">Loading…</p>
    </div>
  </article>
</template>

<script setup lang="ts">
interface Reliability {
  success_rate: number;
  p95_runtime_minutes: number;
}

interface Operations {
  runs_monitored: number;
  active_flows: number;
}

interface PrefectStats {
  updated_at?: string;
  reliability?: Reliability;
  operations?: Operations;
}

const stats = ref<PrefectStats | null>(null);
const loadError = ref(false);

const METRIC_DEFS: Array<{
  key: string;
  label: string;
  tooltip: string;
  getValue: (s: PrefectStats) => number | undefined;
  format: (n: number) => string;
  pct?: boolean;
}> = [
  {
    key: "success_rate",
    label: "Success rate",
    tooltip: "Share of pipeline runs that completed successfully (no failure or crash).",
    getValue: (s) => s.reliability?.success_rate,
    format: (n) => formatPct(n),
    pct: true,
  },
  {
    key: "p95_runtime",
    label: "P95 runtime",
    tooltip: "95th percentile run duration; 95% of runs finish within this many minutes.",
    getValue: (s) => s.reliability?.p95_runtime_minutes,
    format: (n) => `${n} min`,
    pct: false,
  },
  {
    key: "runs_monitored",
    label: "Runs monitored",
    tooltip: "Total number of pipeline runs tracked in the monitoring window.",
    getValue: (s) => s.operations?.runs_monitored,
    format: (n) => formatRuns(n),
    pct: false,
  },
  {
    key: "active_flows",
    label: "Active flows",
    tooltip: "Number of distinct flow definitions currently deployed and running.",
    getValue: (s) => s.operations?.active_flows,
    format: (n) => String(n),
    pct: false,
  },
];

const metrics = computed(() => {
  const s = stats.value;
  if (!s) return [];
  return METRIC_DEFS.map((m) => {
    const raw = m.getValue(s);
    const display = raw !== undefined && raw !== null ? m.format(raw) : "—";
    return { ...m, display };
  });
});

onMounted(async () => {
  const config = useRuntimeConfig();
  const base = (config.app?.baseURL ?? "/").replace(/\/$/, "") || "";
  const url = `${base}/prefect-stats.json`;
  try {
    const res = await fetch(url);
    if (!res.ok) {
      loadError.value = true;
      return;
    }
    const data = await res.json();
    stats.value = data;
    loadError.value = false;
  } catch {
    loadError.value = true;
    stats.value = null;
  }
});

function formatDate(iso?: string): string {
  if (!iso) return "—";
  try {
    const d = new Date(iso);
    return d.toLocaleDateString(undefined, { dateStyle: "medium" });
  } catch {
    return iso;
  }
}

function formatPct(n: number): string {
  return `${(n * 100).toFixed(1)}%`;
}

function formatRuns(n: number): string {
  return n > 0 ? `${n.toLocaleString()}+` : "0";
}
</script>

<style scoped>
.prefect-card {
  padding: 20px;
  width: 80%;
  max-width: 80%;
  margin: 0 auto;
  box-sizing: border-box;
  overflow: visible;
}

.prefect-card__title {
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
  margin: 0 0 14px;
}

.prefect-card__body {
  display: flex;
  flex-direction: column;
  gap: 20px;
  overflow: visible;
}

.prefect-card__updated {
  font-size: 0.8rem;
  color: var(--muted);
  margin: 0 0 12px;
}

.prefect-card__grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px 20px;
  overflow: visible;
}

.prefect-card__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  overflow: visible;
  min-width: 0;
  text-align: center;
}

.prefect-card__label-wrap {
  position: relative;
  cursor: help;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  max-width: 100%;
  min-width: 0;
}

.prefect-card__label {
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
  white-space: nowrap;
}

.prefect-card__label--with-tip {
  display: inline-flex;
  align-items: center;
  gap: 0;
}

.prefect-card__tip-icon {
  font-size: 0.7rem;
  opacity: 0.7;
  margin: 0;
  margin-left: 4px;
  flex-shrink: 0;
}

.prefect-card__tooltip {
  position: absolute;
  left: 50%;
  bottom: calc(100% + 6px);
  transform: translateX(-50%);
  width: 320px;
  max-width: min(360px, 90vw);
  padding: 8px 10px;
  font-size: 0.75rem;
  font-weight: 400;
  line-height: 1.35;
  text-transform: none;
  letter-spacing: normal;
  color: var(--bg);
  background: var(--text);
  border-radius: 6px;
  white-space: normal;
  visibility: hidden;
  opacity: 0;
  transition: visibility 0.15s, opacity 0.15s;
  z-index: 20;
  pointer-events: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.prefect-card__tooltip::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -4px;
  border: 4px solid transparent;
  border-top-color: var(--text);
}

.prefect-card__label-wrap:hover .prefect-card__tooltip {
  visibility: visible;
  opacity: 1;
}

.prefect-card__value {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text);
}

.prefect-card__value--pct {
  font-size: 1.4rem;
  color: var(--accent-2);
}

.prefect-card__error {
  color: var(--muted);
}

@media (max-width: 640px) {
  .prefect-card__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 380px) {
  .prefect-card__grid {
    grid-template-columns: 1fr;
  }
}
</style>
