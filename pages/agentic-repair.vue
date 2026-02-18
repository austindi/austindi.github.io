<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">Agentic Repair & Pipeline Recovery</h1>
        <span class="project-status">In progress</span>
        <p class="section__desc proj-desc">
          An automated reliability system designed to detect pipeline failures, analyze execution context, and provide corrective recovery actions through an AI-assisted operations layer. The system transforms orchestration telemetry into structured diagnostic signals that can be consumed directly by LLM agents via MCP, enabling programmatic troubleshooting and semi-autonomous workflow recovery.
        </p>
        <p class="section__desc proj-desc" style="margin-top: 12px">
          Rather than relying on manual log inspection, the platform aggregates Prefect runtime events, warnings, and execution metadata into structured summaries. An LLM analyzes these signals to identify probable failure causes, highlight potential data gaps, and recommend recovery actions. These capabilities are exposed as tools within an MCP environment, allowing AI agents to investigate failures, propose fixes, and assist operators in maintaining data reliability.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Reduce operational downtime and manual debugging effort by enabling intelligent detection, diagnosis, and recovery of data pipeline failures. The system transforms orchestration telemetry into actionable insights, allowing engineers and AI agents to quickly understand failures and prevent silent data loss.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          Agentic Repair & Pipeline Recovery is an AI-assisted reliability layer built on top of production data workflows. The system continuously analyzes Prefect execution logs, warning messages, and runtime metadata, converting raw operational signals into structured diagnostics.
        </p>
        <p class="section__desc proj-desc" style="margin-top: 12px">
          These diagnostics are exposed through an MCP interface, allowing LLM agents to reason over pipeline behavior, summarize incidents, and recommend corrective actions. Instead of reacting to failures manually, engineers receive contextual explanations and recovery guidance automatically.
        </p>
        <p class="section__desc proj-desc" style="margin-top: 12px">
          The system acts as a bridge between traditional workflow orchestration and intelligent operational automation.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Technologies</h2>
        <div class="tech-list">
          <span v-for="t in technologies" :key="t" class="badge">{{ t }}</span>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <ul class="tradeoff-list">
          <li><strong>Automation vs Control</strong> — The system recommends and assists recovery rather than autonomously modifying production pipelines to avoid unintended side effects.</li>
          <li><strong>LLM Reasoning vs Deterministic Rules</strong> — Chosen to handle unpredictable real-world data failures that rule-based monitoring cannot anticipate.</li>
          <li><strong>Centralized Observability vs Complexity</strong> — Aggregating logs improves visibility but requires structured logging standards across pipelines.</li>
          <li><strong>Signal Quality vs Noise Reduction</strong> — Summarization layers were introduced to prevent alert fatigue caused by raw orchestration warnings.</li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Detects pipeline failures and anomalous execution patterns</li>
          <li>Aggregates Prefect warnings and runtime context into structured events</li>
          <li>Uses LLM analysis to identify probable root causes</li>
          <li>Highlights potential missed or partially processed data</li>
          <li>Generates daily operational summaries automatically</li>
          <li>Creates actionable recovery guidance for engineers</li>
          <li>Exposes diagnostics as MCP tools for AI agents</li>
          <li>Improves monitoring visibility across multi-customer workflows</li>
        </ul>
      </div>
    </section>

  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Agentic Repair & Pipeline Recovery — Dave Austin",
  description: "Automated reliability system for pipeline failure detection, diagnosis, and recovery through AI-assisted operations and MCP.",
});

const technologies = [
  "Prefect",
  "Python",
  "OpenAI API",
  "MCP",
  "Structured Logging",
  "Event-Driven Workflows",
  "Observability Systems",
];
</script>

<style scoped>
.page-header {
  margin-bottom: 20px;
}

.project-status {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--accent-2);
  background: color-mix(in lab, var(--accent) 18%, transparent);
  border: 1px solid color-mix(in lab, var(--accent) 40%, transparent);
  padding: 4px 8px;
  border-radius: 6px;
  margin-top: 8px;
}

.proj-desc {
  max-width: 72ch;
  line-height: 1.65;
}

.tech-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.badge {
  display: inline-block;
  font-size: 0.85rem;
  padding: 6px 12px;
  background: color-mix(in lab, var(--accent) 12%, transparent);
  border: 1px solid color-mix(in lab, var(--accent) 25%, transparent);
  border-radius: 8px;
  color: var(--accent-2);
  font-weight: 500;
}

.tradeoff-list,
.capability-list {
  max-width: 72ch;
  line-height: 1.65;
  margin: 0;
  padding-left: 1.5em;
}

.tradeoff-list li,
.capability-list li {
  margin-bottom: 12px;
}

.tradeoff-list li:last-child,
.capability-list li:last-child {
  margin-bottom: 0;
}
</style>
