<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">HPC Orchestration Pipelines</h1>
        <p class="section__desc" style="max-width: 72ch; margin-top: 12px">
          Distributed workflow systems for large-scale scientific computation and simulation execution. Automated job scheduling, monitoring, and data generation across HPC environments, enabling reproducible research workflows and efficient resource utilization at scale.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Why This System Exists</h2>
        <p class="section__desc proj-desc">
          Large-scale scientific simulations generate enormous datasets and require thousands of compute hours. Manual job monitoring wastes researcher time and leads to failed or incomplete experiments.
        </p>
        <p class="section__desc proj-desc">
          High-performance computing environments introduce additional complexity:
        </p>
        <ul class="capability-list">
          <li>Distributed schedulers</li>
          <li>Unpredictable runtime durations</li>
          <li>Job timeouts</li>
          <li>Partial convergence failures</li>
          <li>Massive output files</li>
        </ul>
        <p class="section__desc proj-desc">
          This system exists to automate computational experimentation at scale, allowing researchers to focus on analysis instead of infrastructure management.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Create automated orchestration workflows that manage submission, monitoring, recovery, and data collection for large-scale simulation workloads across distributed supercomputing environments.
        </p>
        <p class="section__desc proj-desc">
          The objective is reproducible scientific computation at scale.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          Python orchestration scripts manage batches of simulation jobs across SLURM-based HPC systems. The system automatically:
        </p>
        <ul class="capability-list">
          <li>Submits simulation configurations</li>
          <li>Tracks execution states</li>
          <li>Detects timeouts or incomplete convergence</li>
          <li>Restarts jobs with preserved trajectories</li>
          <li>Transfers required outputs via SCP</li>
          <li>Logs experiment metadata for reproducibility</li>
        </ul>
        <p class="section__desc proj-desc">
          Structured datasets are generated from raw simulation outputs and used for downstream analysis, visualization, and publication workflows.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Architecture Concept</h2>
        <div class="arch-flow">
          Simulation Configurations → SLURM Job Submission → Runtime Monitoring & Validation → Automated Restart Logic → Data Extraction & Transfer → Structured Research Datasets
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Automation vs scientific oversight</h3>
          <p class="section__desc proj-desc">Simulations require physics-informed validation, preventing full autonomy.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Large data transfer vs selective extraction</h3>
          <p class="section__desc proj-desc">Moving full outputs is expensive; selective retrieval improves efficiency.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Flexible experiment design vs standardized pipelines</h3>
          <p class="section__desc proj-desc">Each configuration differs, requiring adaptable orchestration logic.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Automated SLURM job orchestration</li>
          <li>Failure detection and restart workflows</li>
          <li>Monitoring of long-running simulations</li>
          <li>Structured extraction from GB–TB scientific outputs</li>
          <li>Reproducible experiment tracking</li>
          <li>Large-scale parameter exploration</li>
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
  title: "HPC Orchestration Pipelines — Dave Austin",
  description: "Automated orchestration workflows for large-scale simulation workloads across distributed HPC environments.",
});

const technologies = [
  "Python",
  "SLURM",
  "Bash",
  "Linux",
  "SSH/SCP",
  "VASP",
  "Quantum ESPRESSO",
  "JSON/CSV Data Models",
  "HPC Clusters (Stampede, Perlmutter, Anvil)",
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
