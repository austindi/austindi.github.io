<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">Prefect Workflow Ecosystem</h1>
        <span class="project-status">In progress</span>
        <p class="section__desc" style="max-width: 72ch; margin-top: 12px">
          Internal orchestration platform standardizing how data pipelines are created, deployed, and operated. Includes a custom CLI for initializing new pipelines, automated secret management through Doppler, CI/CD generation, and built-in testing frameworks. Centralizes execution, monitoring, and recovery across ingestion and transformation workflows, improving reliability and reducing operational overhead.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Why This System Exists</h2>
        <p class="section__desc proj-desc">
          As data pipelines grew, each new workflow introduced slightly different deployment patterns, secret handling, monitoring behavior, and failure recovery logic. Engineers were repeatedly solving the same operational problems — configuring orchestration, wiring credentials, setting up CI/CD, and building monitoring from scratch.
        </p>
        <p class="section__desc proj-desc">This created:</p>
        <ul class="capability-list">
          <li>Inconsistent reliability</li>
          <li>Difficult onboarding</li>
          <li>Hidden operational risk</li>
          <li>Slow delivery of new pipelines</li>
        </ul>
        <p class="section__desc proj-desc">
          The system exists to turn pipeline development from custom engineering into a standardized platform capability.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Provide a unified operational framework where pipelines can be created, deployed, and maintained using consistent patterns that enforce reliability, observability, and reproducibility by default.
        </p>
        <p class="section__desc proj-desc">
          The objective is not just orchestration — but reducing cognitive overhead for engineers while increasing system stability.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          The Prefect Workflow Ecosystem acts as an internal platform layer governing the full lifecycle of data workflows.
        </p>
        <p class="section__desc proj-desc">
          A custom developer CLI initializes pipelines using predefined templates that automatically include:
        </p>
        <ul class="capability-list">
          <li>Orchestration configuration</li>
          <li>Testing scaffolding</li>
          <li>Monitoring hooks</li>
          <li>Deployment workflows</li>
          <li>Secure secret injection through Doppler</li>
        </ul>
        <p class="section__desc proj-desc">
          Once deployed, Prefect manages execution scheduling, retries, dependency handling, and recovery behavior across ingestion and transformation pipelines. Operational telemetry is centralized, allowing failures and performance issues to be detected quickly.
        </p>
        <p class="section__desc proj-desc">
          This converts pipeline engineering from ad-hoc scripting into a repeatable platform process.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Architecture Concept</h2>
        <div class="arch-flow">
          Developer CLI → Standardized Repository Structure → Automated CI/CD Generation → Prefect Deployment → Centralized Monitoring & Recovery Layer
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Standardization vs Flexibility</h3>
          <p class="section__desc proj-desc">Enforcing templates reduces creativity but prevents fragile pipeline designs.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Centralized orchestration vs distributed autonomy</h3>
          <p class="section__desc proj-desc">Improves observability while introducing dependency on orchestration infrastructure.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Automation vs transparency</h3>
          <p class="section__desc proj-desc">Developers move faster, but deeper infrastructure knowledge becomes abstracted.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>One-command pipeline initialization</li>
          <li>Automatic secret provisioning</li>
          <li>Built-in testing and deployment workflows</li>
          <li>Consistent retry and recovery behavior</li>
          <li>Unified monitoring across all workflows</li>
          <li>Reduced onboarding time for new engineers</li>
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
  title: "Prefect Workflow Ecosystem — Dave Austin",
  description: "Internal orchestration platform standardizing how data pipelines are created, deployed, and operated.",
});

const technologies = [
  "Prefect",
  "Python",
  "Docker",
  "AWS",
  "Doppler",
  "GitHub Actions",
  "Snowflake",
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
