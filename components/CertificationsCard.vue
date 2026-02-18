<template>
  <div class="certs">
    <!-- Have -->
    <div v-if="have.length" class="certs__group">
      <h4 class="certs__heading">Earned</h4>
      <div class="certs__grid">
        <a
          v-for="c in have"
          :key="c.name"
          :href="c.link"
          target="_blank"
          rel="noopener noreferrer"
          class="certs__badge certs__badge--have"
        >
          <img :src="imageUrl(c.image)" :alt="c.name" class="certs__img" />
          <span class="certs__name">{{ c.name }}</span>
          <span v-if="c.date" class="certs__meta">{{ c.date }}</span>
        </a>
      </div>
    </div>

    <!-- Next & Want (same line, greyed) -->
    <div v-if="nextAndWant.length" class="certs__group">
      <h4 class="certs__heading">Pursuing</h4>
      <div class="certs__grid">
        <div
          v-for="c in nextAndWant"
          :key="c.name"
          :class="['certs__badge', 'certs__badge--greyed', c.isNext && 'certs__badge--next']"
        >
          <span class="certs__img-wrap">
            <img :src="imageUrl(c.image)" :alt="c.name" class="certs__img" />
          </span>
          <span class="certs__name">{{ c.name }}</span>
          <span v-if="c.isNext" class="certs__next-pill">Next</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Cert {
  name: string;
  image: string;
  issuer?: string;
  date?: string;
  link?: string;
}

interface CertsData {
  have: Cert[];
  next: Cert[];
  want: Cert[];
}

const config = useRuntimeConfig();
const base = (config.app?.baseURL ?? "/").replace(/\/$/, "") || "";
const imageBase = `${base}/images`;

const certsData = ref<CertsData | null>(null);

function imageUrl(filename: string): string {
  return `${imageBase}/${filename}`;
}

const have = computed(() => certsData.value?.have ?? []);
const next = computed(() => certsData.value?.next ?? []);
const want = computed(() => certsData.value?.want ?? []);

const nextAndWant = computed(() => {
  const nextList = next.value;
  const wantList = want.value;
  const haveImages = new Set(have.value.map((c) => c.image));
  const nextImages = new Set(nextList.map((c) => c.image));
  const seen = new Set<string>();
  const out: Array<Cert & { isNext: boolean }> = [];
  for (const c of nextList) {
    if (!haveImages.has(c.image) && !seen.has(c.image)) {
      seen.add(c.image);
      out.push({ ...c, isNext: true });
    }
  }
  for (const c of wantList) {
    if (!haveImages.has(c.image) && !seen.has(c.image)) {
      seen.add(c.image);
      out.push({ ...c, isNext: nextImages.has(c.image) });
    }
  }
  return out;
});

onMounted(async () => {
  try {
    const res = await fetch(`${base}/images/certs.json`);
    if (res.ok) {
      certsData.value = await res.json();
    }
  } catch {
    certsData.value = null;
  }
});
</script>

<style scoped>
.certs {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.certs__heading {
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--muted);
  margin: 0 0 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.certs__next-pill {
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  background: var(--accent);
  color: var(--bg);
  padding: 2px 8px;
  border-radius: 999px;
}

.certs__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16px 20px;
}

.certs__badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 140px;
  text-decoration: none;
  color: inherit;
}

.certs__badge--have {
  padding: 10px;
  margin: -10px;
  border-radius: 10px;
  border: 1px solid transparent;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.certs__badge--have:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.12);
  border-color: var(--border-hover);
}

.certs__badge--greyed {
  opacity: 0.9;
  padding: 10px;
  margin: -10px;
  border-radius: 10px;
  border: 1px solid transparent;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.certs__badge--greyed:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.12);
  border-color: var(--border-hover);
}

.certs__badge--next {
  width: 115px;
  padding: 8px;
  margin: -8px;
  border-radius: 10px;
  background: transparent;
  border: 2px solid color-mix(in lab, var(--accent) 45%, transparent);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.certs__badge--next:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.12);
  border-color: var(--border-hover);
}

.certs__badge--next .certs__img-wrap,
.certs__badge--next .certs__img {
  width: 80px;
}

.certs__badge--next .certs__next-pill {
  margin-top: 2px;
}

.certs__badge--next .certs__name {
  font-size: 0.72rem;
  line-height: 1.15;
}

.certs__img-wrap {
  display: block;
  filter: grayscale(100%) brightness(0.65) saturate(0);
  -webkit-filter: grayscale(100%) brightness(0.65) saturate(0);
}

.certs__img {
  width: 100px;
  height: auto;
  object-fit: contain;
  border-radius: 8px;
  display: block;
}

.certs__name {
  font-size: 0.8rem;
  font-weight: 600;
  text-align: center;
  line-height: 1.2;
  color: var(--text);
}

.certs__meta {
  font-size: 0.7rem;
  color: var(--muted);
}
</style>
