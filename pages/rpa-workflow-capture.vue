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
          A browser-based automation platform designed to convert human operational workflows into executable software processes. The system captures user interactions directly from the browser, transforms those actions into structured workflow events, and persists them into a semi-structured data model that supports execution, monitoring, and long-term evolution of automated workflows.
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
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          The goal of the system is to bridge manual business operations and programmable data infrastructure, enabling automation of legacy systems and repetitive workflows that lack APIs or structured integrations.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          The platform records user actions through a Chrome extension and translates them into normalized workflow steps. These steps are stored in a semi-structured database rather than static scripts, allowing workflows to be queried, modified, versioned, and executed programmatically.
        </p>
        <p class="section__desc proj-desc">
          Execution is handled by Python services orchestrated with Prefect, enabling retries, monitoring, scheduling, and operational visibility. When workflows fail due to UI or structural changes, an LLM-assisted repair layer analyzes failures and proposes corrective adjustments, improving resilience in unstable real-world environments.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <ul class="tradeoff-list">
          <li><strong>Flexible capture vs rigid schema</strong> — workflows are initially stored with flexible structure to support unknown user behaviors, accepting later normalization complexity.</li>
          <li><strong>JSON as interchange layer</strong> — JSON enables rapid recording and portability, while long-term persistence uses structured storage for scalability and querying.</li>
          <li><strong>Adaptive recovery vs deterministic automation</strong> — LLM-assisted repair improves robustness when external systems change, trading strict determinism for operational resilience.</li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Capture browser interactions as structured workflow events</li>
          <li>Normalize recorded actions into reusable execution models</li>
          <li>Persist workflows in a semi-structured database for querying and version control</li>
          <li>Execute automation pipelines through orchestrated backend services</li>
          <li>Integrate legacy web systems into modern data workflows</li>
          <li>Automatically detect and diagnose workflow failures using LLM analysis</li>
          <li>Enable scalable automation without requiring direct API access</li>
        </ul>
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
  "Semi-Structured Data Modeling",
  "OpenAI API",
  "Workflow Orchestration",
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
