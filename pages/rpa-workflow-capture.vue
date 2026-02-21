<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">RPA Workflow Capture & Execution System</h1>
        <span class="project-status">In progress</span>
        <p class="section__desc" style="max-width: 72ch; margin-top: 12px">
          Browser-based automation platform designed to convert human operational workflows into executable software processes. Captures user interactions from the browser, transforms them into structured workflow events, and persists them in a semi-structured data model for execution, monitoring, and evolution.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Why This System Exists</h2>
        <p class="section__desc proj-desc">
          Many business-critical workflows live inside legacy web systems with no APIs. Operations teams perform repetitive manual actions daily — copying data between systems, navigating dashboards, downloading reports, and triggering processes by hand.
        </p>
        <p class="section__desc proj-desc">Traditional automation fails because:</p>
        <ul class="capability-list">
          <li>APIs don't exist</li>
          <li>Interfaces change frequently</li>
          <li>Workflows vary between users</li>
          <li>Rigid scripts break easily</li>
        </ul>
        <p class="section__desc proj-desc">
          This system exists to convert human operational knowledge into executable infrastructure.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Bridge the gap between manual business operations and programmable automation by allowing workflows to be captured directly from user behavior and executed as resilient backend processes.
        </p>
        <p class="section__desc proj-desc">
          The long-term aim is to transform undocumented human procedures into structured, scalable automation assets.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          A Chrome extension records user interactions inside the browser — clicks, inputs, navigation, and contextual events. These actions are normalized into workflow events and stored in a semi-structured database rather than static scripts.
        </p>
        <p class="section__desc proj-desc">
          Execution services written in Python replay workflows through orchestrated automation pipelines managed by Prefect. Because real-world interfaces change, an LLM-assisted repair layer analyzes failures and proposes adjustments when workflows break.
        </p>
        <p class="section__desc proj-desc">
          This allows automation to adapt instead of failing catastrophically.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Architecture Concept</h2>
        <div class="arch-flow">
          Browser Interaction Capture → Event Normalization Layer → Semi-Structured Workflow Store → Prefect Execution Engine → LLM Repair & Adaptation
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Flexible capture vs schema stability</h3>
          <p class="section__desc proj-desc">Capturing unknown workflows requires loose structure initially.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Adaptive AI repair vs deterministic automation</h3>
          <p class="section__desc proj-desc">Resilience improves, but behavior becomes probabilistic.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Rapid recording vs long-term maintainability</h3>
          <p class="section__desc proj-desc">Easy onboarding introduces later normalization complexity.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Record workflows directly from user behavior</li>
          <li>Convert manual processes into executable pipelines</li>
          <li>Store workflows as queryable data models</li>
          <li>Execute automation with retries and monitoring</li>
          <li>Adapt to UI changes using AI-assisted repair</li>
          <li>Integrate legacy systems without APIs</li>
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
  title: "RPA Workflow Capture & Execution System — Dave Austin",
  description: "Browser-based automation platform that converts human workflows into executable software processes.",
});

const technologies = [
  "TypeScript",
  "Chrome Extension APIs",
  "Nuxt",
  "Python",
  "Prefect",
  "REST APIs",
  "OpenAI API",
  "Semi-Structured Data Modeling",
  "GitHub",
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
