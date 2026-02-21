<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">STM/STS Simulation & Analysis Platform</h1>
        <p class="section__desc" style="max-width: 72ch; margin-top: 12px">
          Developed a computational pipeline to simulate scanning tunneling microscopy (STM) and spectroscopy (STS) measurements directly from density functional theory (DFT) calculations. The system automated post-processing, visualization, and comparison between theoretical models and experimental data, enabling reproducible analysis of nanoscale electronic structure.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Why This System Exists</h2>
        <p class="section__desc proj-desc">
          Electronic structure simulations produce raw quantum mechanical data that is difficult to interpret directly. Experimental researchers rely on scanning tunneling microscopy (STM) and spectroscopy (STS) measurements, but theoretical results must be translated into comparable observable signals.
        </p>
        <p class="section__desc proj-desc">
          Manual processing of simulation outputs is slow, error-prone, and difficult to reproduce.
        </p>
        <p class="section__desc proj-desc">
          This platform exists to bridge theoretical physics and experimental measurement through automated data transformation and simulation.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Goal</h2>
        <p class="section__desc proj-desc">
          Convert density functional theory (DFT) outputs into reproducible simulated STM and STS measurements that enable direct comparison between theoretical predictions and experimental observations.
        </p>
        <p class="section__desc proj-desc">
          The objective is reproducible scientific interpretation.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">System Overview</h2>
        <p class="section__desc proj-desc">
          The platform ingests electronic structure outputs from DFT calculations and extracts physical quantities such as charge density, wavefunctions, energies, and electron localization.
        </p>
        <p class="section__desc proj-desc">
          Custom Python tooling processes these datasets to generate simulated STM images and STS spectra. Results are automatically visualized and regenerated using tracked configuration metadata, ensuring full reproducibility of published figures.
        </p>
        <p class="section__desc proj-desc">
          The system enables rapid exploration of atomic-scale structures and electronic behavior without repeated manual analysis.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Architecture Concept</h2>
        <div class="arch-flow">
          DFT Outputs (VASP / QE) → Data Parsing & Feature Extraction → Physical Modeling Layer → STM/STS Simulation → Visualization & Reproducible Outputs
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Engineering Tradeoffs</h2>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Physical accuracy vs computational cost</h3>
          <p class="section__desc proj-desc">Higher fidelity simulations increase runtime significantly.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">Automation vs scientific interpretation</h3>
          <p class="section__desc proj-desc">Physics-informed validation remains necessary to avoid nonphysical results.</p>
        </div>
        <div class="tradeoff-block">
          <h3 class="capability-heading">General tooling vs experiment-specific workflows</h3>
          <p class="section__desc proj-desc">Flexibility was prioritized to support diverse material systems.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section__title">Key Capabilities</h2>
        <ul class="capability-list">
          <li>Automated parsing of electronic structure outputs</li>
          <li>Simulation of STM images and STS spectra</li>
          <li>Reproducible regeneration of analysis artifacts</li>
          <li>Feature extraction from large quantum datasets</li>
          <li>Direct comparison between theory and experiment</li>
          <li>Support for peer-reviewed publication workflows</li>
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
  title: "STM/STS Simulation & Analysis Platform — Dave Austin",
  description: "Computational pipeline for simulating STM and STS measurements from DFT outputs with reproducible analysis.",
});

const technologies = [
  "Python",
  "ASE",
  "NumPy",
  "Matplotlib",
  "VASP",
  "Quantum ESPRESSO",
  "HPC (SLURM)",
  "Scientific Data Pipelines",
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
