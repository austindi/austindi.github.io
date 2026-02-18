<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">Automation for Messy Real-World Data</h1>
        <p class="section__desc proj-desc">
          A resilience-focused data ingestion and normalization system designed to make unreliable external data usable in production environments. The platform transforms inconsistent vendor inputs into validated, structured datasets while preserving observability and long-term pipeline stability.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Ensure business-critical data pipelines remain reliable despite inconsistent schemas, incomplete records, and unpredictable real-world data sources. The system prioritizes data trustworthiness by detecting issues early and preventing silent data corruption.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          This system provides a structured ingestion and validation layer for operational data coming from APIs, logistics feeds, spreadsheets, and third-party vendors. Instead of assuming clean inputs, pipelines are designed around failure tolerance — automatically detecting schema drift, malformed records, and missing data before downstream processing occurs.
        </p>
        <p class="section__desc proj-desc" style="margin-top: 12px">
          Validation rules, monitoring signals, and normalization logic convert heterogeneous inputs into consistent warehouse-ready datasets stored in Snowflake. Observability tooling enables rapid diagnosis when upstream systems change unexpectedly.
        </p>
        <p class="section__desc proj-desc" style="margin-top: 12px">
          The result is a stable interface between chaotic external systems and reliable internal analytics platforms.
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
          <li><strong>Strict Validation vs Data Availability</strong> — Rejecting bad data improves integrity but risks delayed reporting; selective quarantine pipelines were implemented instead.</li>
          <li><strong>Schema Flexibility vs Warehouse Stability</strong> — Flexible ingestion handles vendor variability while normalization enforces consistent downstream schemas.</li>
          <li><strong>Early Failure Detection vs Pipeline Throughput</strong> — Additional validation steps slightly increase runtime but significantly reduce downstream debugging cost.</li>
          <li><strong>Automation vs Manual Exception Handling</strong> — Automated detection handles most issues while allowing controlled human review for edge cases.</li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Handles schema drift and inconsistent vendor formats</li>
          <li>Normalizes structured and semi-structured datasets</li>
          <li>Performs automated validation and anomaly detection</li>
          <li>Prevents silent data loss through monitoring and alerts</li>
          <li>Produces analytics-ready Snowflake datasets</li>
          <li>Maintains observability across ingestion workflows</li>
          <li>Supports scalable storage and reprocessing via S3</li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Automation for Messy Real-World Data — Dave Austin",
  description: "Resilience-focused data ingestion and normalization system for unreliable external data sources.",
});

const technologies = [
  "Python",
  "SQL",
  "Snowflake",
  "Prefect",
  "AWS S3",
  "Data Validation Frameworks",
  "Structured Monitoring",
];
</script>

<style scoped>
.page-header {
  margin-bottom: 20px;
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
