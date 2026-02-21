<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">AI-Driven Pipeline Observability</h1>
        <span class="project-status">In progress</span>
        <p class="section__desc" style="max-width: 72ch; margin-top: 12px">
          Automated monitoring system that analyzes Prefect workflow logs to detect warnings and incomplete processing events. An LLM summarizes operational issues, identifies potential data gaps, and delivers daily diagnostic reports, improving visibility and reducing unnoticed pipeline failures.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Why This System Exists</h2>
        <p class="section__desc proj-desc">
          Traditional monitoring systems surface failures but do not explain them. Engineers are left parsing logs manually, correlating warnings across services, and determining whether missing data represents a true failure or a recoverable condition.
        </p>
        <p class="section__desc proj-desc">
          As pipeline complexity grows, operational awareness becomes the bottleneck rather than computation.
        </p>
        <p class="section__desc proj-desc">
          This system exists to convert raw operational telemetry into actionable understanding, reducing cognitive load and enabling faster decision-making.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Transform workflow logs and warning signals into structured operational intelligence that identifies risk, summarizes failures, and highlights potential downstream data impact automatically.
        </p>
        <p class="section__desc proj-desc">
          The objective is to move from monitoring systems to diagnostic systems.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          Prefect workflows continuously collect runtime logs, warnings, and execution metadata across production pipelines. A scheduled analysis flow aggregates these signals and submits structured context to an LLM.
        </p>
        <p class="section__desc proj-desc">
          The LLM evaluates:
        </p>
        <ul class="capability-list">
          <li>Warning patterns</li>
          <li>Skipped or delayed data</li>
          <li>Abnormal execution behavior</li>
          <li>Potential business impact</li>
        </ul>
        <p class="section__desc proj-desc">
          The system generates daily operational summaries and sends automated reports outlining detected risks, likely causes, and recommended follow-up actions.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Architecture Concept</h2>
        <div class="arch-flow">
          Pipeline Runs → Log & Warning Aggregation → Context Structuring Layer → LLM Analysis → Diagnostic Summaries → Automated Reporting
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Signal richness vs noise</h3>
          <p class="section__desc proj-desc">Too many logs overwhelm analysis; aggregation requires intelligent filtering.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">LLM reasoning vs deterministic alerts</h3>
          <p class="section__desc proj-desc">AI improves interpretation but must remain advisory rather than authoritative.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Automation vs operator trust</h3>
          <p class="section__desc proj-desc">Outputs emphasize explanations to maintain human confidence in decisions.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Aggregate warnings across distributed workflows</li>
          <li>Detect potential missed or incomplete data processing</li>
          <li>Produce human-readable operational summaries</li>
          <li>Identify recurring failure patterns</li>
          <li>Reduce manual log investigation</li>
          <li>Improve visibility into system health over time</li>
        </ul>
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
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "AI-Driven Pipeline Observability — Dave Austin",
  description: "Transforms workflow logs into structured operational intelligence through LLM analysis.",
});

const technologies = [
  "Prefect",
  "Python",
  "Structured Logging",
  "OpenAI API",
  "MCP Integration",
  "Email Automation",
  "Event Scheduling",
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

.tradeoff-block {
  margin-bottom: 24px;
}

.tradeoff-block:last-child {
  margin-bottom: 0;
}

.capability-heading {
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0 0 8px;
  color: var(--text);
}

.capability-list {
  max-width: 72ch;
  line-height: 1.65;
  margin: 0 0 16px;
  padding-left: 1.5em;
}

.capability-list li {
  margin-bottom: 8px;
}

.capability-list li:last-child {
  margin-bottom: 0;
}

.arch-flow {
  max-width: 72ch;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--muted);
  padding: 16px;
  background: var(--hover-bg);
  border: 1px solid var(--border);
  border-radius: 10px;
}
</style>
