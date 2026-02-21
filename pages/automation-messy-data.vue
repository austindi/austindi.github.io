<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">Automation for Messy Real-World Data</h1>
        <p class="section__desc" style="max-width: 72ch; margin-top: 12px">
          Resilient ingestion pipelines designed for inconsistent APIs, logistics feeds, and spreadsheet data. Standardizes heterogeneous inputs into structured, analytics-ready datasets, enabling reliable downstream reporting and decision-making.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Why This System Exists</h2>
        <p class="section__desc proj-desc">
          Most real operational data is not clean, stable, or well-defined. Vendor feeds change formats, APIs return incomplete records, spreadsheets contain hidden assumptions, and schemas evolve without notice.
        </p>
        <p class="section__desc proj-desc">
          Traditional pipelines assume structured inputs. Real businesses operate on inconsistent data sources that break deterministic systems.
        </p>
        <p class="section__desc proj-desc">
          This platform exists to transform unreliable inputs into trustworthy, analytics-ready datasets without constant manual intervention.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Build resilient ingestion and validation infrastructure capable of continuously normalizing inconsistent operational data while preserving correctness, traceability, and long-term maintainability.
        </p>
        <p class="section__desc proj-desc">
          The objective is reliability under uncertainty, not perfect upstream data.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          The system ingests data from APIs, logistics platforms, spreadsheets, and third-party integrations. Incoming data passes through layered validation and normalization stages that:
        </p>
        <ul class="capability-list">
          <li>Detect schema drift</li>
          <li>Validate required business constraints</li>
          <li>Standardize naming and structure</li>
          <li>Flag ambiguous or incomplete records</li>
        </ul>
        <p class="section__desc proj-desc">
          LLM-assisted normalization is used selectively where deterministic rules fail — particularly for semi-structured or human-generated inputs.
        </p>
        <p class="section__desc proj-desc">
          Processed data is stored in Snowflake as standardized models supporting reporting, analytics, and downstream automation.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Architecture Concept</h2>
        <div class="arch-flow">
          External Sources (APIs, files, vendors) → Ingestion Pipelines → Validation & Schema Detection → Normalization Layer → Structured Data Models → Analytics & Reporting Systems
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Strict validation vs ingestion continuity</h3>
          <p class="section__desc proj-desc">Rejecting bad data protects quality but risks blocking operations.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Rule-based logic vs adaptive interpretation</h3>
          <p class="section__desc proj-desc">LLM assistance improves flexibility but requires guardrails.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Early normalization vs downstream flexibility</h3>
          <p class="section__desc proj-desc">Standardizing early simplifies analytics but increases pipeline complexity.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Handle schema drift and inconsistent vendor formats</li>
          <li>Normalize semi-structured operational inputs</li>
          <li>Validate business-critical fields automatically</li>
          <li>Detect missing or ambiguous data conditions</li>
          <li>Maintain analytics-ready datasets despite unstable upstream systems</li>
          <li>Enable scalable ingestion without manual cleanup</li>
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
  title: "Automation for Messy Real-World Data — Dave Austin",
  description: "Resilient data ingestion and normalization for inconsistent operational data sources.",
});

const technologies = [
  "Python",
  "Pandas/Polars",
  "Snowflake",
  "SQL",
  "REST APIs",
  "AWS S3",
  "Prefect Monitoring",
  "OpenAI API (LLM-assisted normalization)",
  "Parquet",
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
