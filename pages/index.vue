<template>
  <div>
    <SiteNav />

    <!-- Hero -->
    <section class="hero">
      <div class="container hero__inner">
        <div>
          <div class="kicker">Software & Data Engineer • Physicist</div>
          <h1 class="h1">Hi, I’m Dr. Dave Austin,</h1>
          <p class="hero__sub">
            I completed my PhD in computational physics at the University of
            Central Florida, where I used high-performance computing and
            advanced simulation methods to study 2D materials and their
            electronic properties. My research combined density functional
            theory, data analysis, and experimental collaboration to uncover
            insights into nanoscale phenomena. I am currently working as a
            Software Engineer/Data Engineer at Bear Cognition, where I design
            and optimize data pipelines, build scalable cloud-based solutions,
            and apply my analytical background to solve complex business
            problems.
          </p>
          <div class="cta">
            <a href="#projects" class="btn btn--primary">View My Projects</a>
            <a href="/Dave_Austin_Resume.pdf" class="btn">Download Resume</a>
          </div>
          <div class="pills">
            <span class="pill">⚡ Fast Data Pipelines</span>
            <span class="pill">☁ Cloud Architecture</span>
            <span class="pill">📊 ML Analytics</span>
          </div>
        </div>

        <div class="hero__photo" aria-label="Dave Austin portrait"></div>
      </div>
    </section>

    <!-- About -->
    <section id="about" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">About Me</h2>
        </div>
        <div class="card" style="padding: 18px">
          <p style="color: var(--muted); max-width: 75ch; margin: 8px 0">
            With a PhD in Physics and years working in high-performance
            computing, I now specialize in building robust data systems and
            scalable software solutions. I’ve engineered ETL pipelines on AWS,
            orchestrated workflows with Prefect, integrated Snowflake &
            Fivetran, and shipped ML features that reduce manual effort.
          </p>
        </div>
      </div>
    </section>

    <!-- Projects -->
    <section id="projects" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Projects</h2>
          <p class="section__desc">
            Selected work in data engineering, automation, and ML.
          </p>
        </div>
        <div class="projects">
          <ProjectCard v-for="p in projects" :key="p.title" :project="p" />
        </div>
      </div>
    </section>

    <!-- Skills -->
    <section id="skills" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Skills</h2>
        </div>
        <div class="card" style="padding: 18px">
          <div
            style="
              display: grid;
              grid-template-columns: repeat(3, 1fr);
              gap: 10px;
            "
          >
            <div>
              <strong>Languages</strong>
              <p class="section__desc">Python, SQL, C++, Fortran, JavaScript</p>
            </div>
            <div>
              <strong>Data</strong>
              <p class="section__desc">Pandas, Snowflake, Fivetran, DuckDB</p>
            </div>
            <div>
              <strong>Cloud</strong>
              <p class="section__desc">AWS (Lambda, S3, EC2), GCP</p>
            </div>
            <div>
              <strong>Orchestration</strong>
              <p class="section__desc">Prefect, Airflow</p>
            </div>
            <div>
              <strong>CI/CD & Infra</strong>
              <p class="section__desc">GitHub Actions, Docker, Terraform</p>
            </div>
            <div>
              <strong>Viz</strong>
              <p class="section__desc">Power BI, Matplotlib</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Experience -->
    <section id="experience" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Experience</h2>
        </div>
        <div class="timeline">
          <div class="timeline__item">
            <h3 style="margin: 0">Data Engineer — Bear Cognition</h3>
            <p class="section__desc">
              Designed and deployed production-grade data pipelines integrating
              Snowflake, Prefect, and Fivetran. Built ML-assisted automation for
              bid classification and commissions.
            </p>
          </div>
          <div class="timeline__item">
            <h3 style="margin: 0">Computational Physics — UCF</h3>
            <p class="section__desc">
              Orchestrated HPC workflows (SLURM); authored tooling in Python;
              collaborated internationally on large datasets and publications.
            </p>
          </div>
          <div class="timeline__item">
            <h3 style="margin: 0">Postdoc — Quantum Devices</h3>
            <p class="section__desc">
              Modeled Josephson devices; automated analysis and experiment
              pipelines; introduced data standards across the team.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact -->
    <section id="contact" class="section">
      <div class="container card" style="padding: 18px">
        <div class="section__head" style="margin: 0 0 6px">
          <h2 class="section__title" style="margin: 0">Contact</h2>
        </div>
        <p class="section__desc">Open to roles and collaborations.</p>
        <div class="cta">
          <a href="mailto:dave@example.com" class="btn btn--primary"
            >Email Me</a
          >
          <a
            href="https://www.linkedin.com/in/your-handle"
            class="btn"
            target="_blank"
            >LinkedIn</a
          >
          <a href="https://github.com/your-handle" class="btn" target="_blank"
            >GitHub</a
          >
        </div>
      </div>
    </section>

    <footer class="footer container">
      © {{ new Date().getFullYear() }} Dave Austin • Built with Nuxt
    </footer>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Home — Dave Austin",
  description: "Software & Data Engineer portfolio",
});

const projects = [
  {
    title: "2PL Data Pipeline",
    tagline:
      "Scalable logistics ETL using Python, Prefect, AWS Lambda, and Snowflake. Automated shipment ingestion and reduced processing time by 80%.",
    stack: ["Python", "Prefect", "AWS Lambda", "Snowflake", "S3"],
    link: "/projects/2pl",
    github: "https://github.com/your-handle/2pl",
  },
  {
    title: "Automated Bid Classification",
    tagline:
      "ML classifier integrated into ETL to label shipping bids in real time, cutting manual review by 70%.",
    stack: ["Python", "sklearn", "Pandas", "ETL"],
    link: "/projects/bid-classifier",
    github: "https://github.com/your-handle/bid-classifier",
  },
  {
    title: "HPC Simulation Orchestration",
    tagline:
      "Multi-step orchestration of DFT workloads with SLURM; thousand-job campaigns with robust restart and lineage.",
    stack: ["Python", "SLURM", "HPC", "ASE"],
    link: "/projects/hpc-orch",
    github: "https://github.com/your-handle/hpc-orch",
  },
];
</script>

<style scoped>
/* page-scoped tweaks can live here if needed */
</style>
