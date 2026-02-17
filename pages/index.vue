<template>
  <div>
    <!-- Hero -->
    <section class="hero">
      <div class="container hero__inner">
        <div>
          <div class="kicker">Data Engineer | AI Systems Builder | Scalable Data Platforms</div>
          <h1 class="h1">Hi, I’m Dr. Dave Austin,</h1>
          <div class="hero__sub">
            <p>
              I completed my PhD in Computational Physics at the University of Central Florida, where I built large-scale computational workflows and data pipelines to support high-performance simulations and analysis of complex materials systems. My work combined scientific modeling with automation, data engineering, and reproducible computing practices across HPC environments.
            </p>
            <p>
              I currently work as a Software Engineer and Data Engineer at Bear Cognition, where I design and maintain production data pipelines that transform diverse operational data into reliable, analytics-ready datasets. I develop cloud-based data systems with a focus on scalability, monitoring, and reliability, working with APIs, logistics data, and variable real-world inputs to build resilient ingestion and validation workflows.
            </p>
            <p>
              Across both research and industry, I apply a scientific approach to engineering — emphasizing measurable outcomes, systematic debugging, and systems built for long-term reliability.
            </p>
          </div>
          <div class="cta">
            <NuxtLink to="/phd-overview" class="btn btn--primary">Physics Career Overview</NuxtLink>
            <NuxtLink to="/blogs" class="btn">Blogs</NuxtLink>
            <a href="/Dave_Austin_Resume.pdf" class="btn">Download Resume</a>
          </div>
          <div class="pills">
            <span class="pill">⚡ Data Platforms & Automation</span>
            <span class="pill">☁ Cloud-Native Infrastructure</span>
            <span class="pill">📊 AI & Decision Systems</span>
            <span class="pill">🧩 End-to-End Data Engineering</span>
          </div>
          <div v-if="showPrefectStats" class="prefect-stats-block">
            <PrefectStatsCard />
          </div>
        </div>

        <div class="hero__photo" aria-label="Dave Austin portrait"></div>
      </div>
    </section>

    <!-- Experience -->
    <section id="experience" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Experience</h2>
        </div>
        <div class="timeline">
          <div class="timeline__item timeline__item--current">
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
        <div class="card skills-card">
          <div class="skills-row">
            <div class="skills-item">
              <strong>Cloud</strong>
              <p class="section__desc">AWS (Lambda, S3, EC2), GCP</p>
            </div>
            <div class="skills-item">
              <strong>Data</strong>
              <p class="section__desc">Pandas, Snowflake, Fivetran, DuckDB</p>
            </div>
            <div class="skills-item">
              <strong>Languages</strong>
              <p class="section__desc">Python, SQL, C++, Fortran, JavaScript</p>
            </div>
          </div>
          <div class="skills-row">
            <div class="skills-item">
              <strong>Orchestration</strong>
              <p class="section__desc">Prefect, Airflow</p>
            </div>
            <div class="skills-item">
              <strong>Infra</strong>
              <p class="section__desc">GitHub Actions, Docker, Terraform</p>
            </div>
            <div class="skills-item">
              <strong>Visualization</strong>
              <p class="section__desc">Power BI, Matplotlib</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Education -->
    <section id="education" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Education</h2>
        </div>
        <div class="timeline">
          <div v-for="edu in education" :key="edu.degree" class="timeline__item">
            <h3 style="margin: 0">{{ edu.degree }} — {{ edu.institution }}</h3>
            <p v-if="edu.field" class="section__desc">{{ edu.field }}</p>
            <p v-if="edu.dissertation" class="section__desc" style="font-size: 0.9rem; margin-top: 6px">
              <a v-if="edu.dissertation_link" :href="edu.dissertation_link" target="_blank" rel="noopener noreferrer">{{
                edu.dissertation }}</a>
              <span v-else>{{ edu.dissertation }}</span>
            </p>
            <p v-if="edu.date" class="section__desc" style="font-size: 0.9rem; margin-top: 4px">
              {{ edu.date }}
            </p>
            <p class="section__desc" style="font-size: 0.9rem; margin-top: 4px">
              <a v-if="edu.diploma_link" :href="edu.diploma_link" target="_blank" rel="noopener noreferrer">View
                Diploma</a>
              <span v-else class="diploma-placeholder">Diploma (add link)</span>
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Certifications -->
    <section id="certifications" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Certifications</h2>
          <p class="section__desc">
            Professional and technical certifications.
          </p>
        </div>
        <div class="timeline">
          <div v-for="cert in certifications" :key="cert.name" class="timeline__item">
            <h3 style="margin: 0">{{ cert.name }}</h3>
            <p v-if="cert.issuer" class="section__desc">{{ cert.issuer }}</p>
            <p v-if="cert.date || cert.link" class="section__desc" style="font-size: 0.9rem; margin-top: 4px">
              {{ cert.date }}{{ cert.date && cert.link ? " · " : "" }}
              <a v-if="cert.link" :href="cert.link" target="_blank" rel="noopener noreferrer">Verify</a>
            </p>
          </div>
          <p v-if="!certifications.length" class="section__desc">No certifications added yet.</p>
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
          <a href="mailto:austindi1133@gmail.com" class="btn btn--primary">Email Me</a>
          <NuxtLink to="/photos" class="btn">Photos of me</NuxtLink>
          <a href="https://www.linkedin.com/in/dave-austin-ph-d-616865a9" class="btn" target="_blank"
            rel="noopener noreferrer">LinkedIn</a>
          <a href="https://github.com/austindi" class="btn" target="_blank" rel="noopener noreferrer">GitHub</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Home — Dave Austin",
  description: "Data Engineer | AI Systems Builder | Scalable Data Platforms",
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
    github: "https://github.com/austindi/hpc-orch",
  },
  {
    title: "Simulated Scanning Tunneling Spectroscopy Data",
    tagline:
      "Bridged DFT simulations with experimental STS data to enable direct comparison between theory and scanning tunneling spectroscopy measurements.",
    stack: ["Python", "DFT", "VASP", "ASE"],
  },
];

const education = [
  { degree: "Ph.D. in Physics", institution: "University of Central Florida", field: "Computational physics, density functional theory", date: "Aug 2018 – Aug 2024", dissertation: "First Principles Studies of Nano-Scale Phenomena At Surfaces: From Characteristics of Single Atom Catalysts to Molecular Structure Formation", dissertation_link: "https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1500&context=etd2023", diploma_link: "" },
  { degree: "M.S. in Physics", institution: "University of Central Florida", field: "", date: "Aug 2018 – May 2020", diploma_link: "" },
  { degree: "B.S. in Physics", institution: "College of Charleston", field: "", date: "Aug 2014 – May 2018", diploma_link: "" },
];

const showPrefectStats = true; // Set false to hide Task Runs card

const certifications = [
  // Add your certifications, e.g.:
  // { name: "AWS Certified Solutions Architect", issuer: "Amazon Web Services", date: "2024", link: "https://..." },
];

</script>

<style scoped>
.diploma-placeholder {
  color: var(--muted);
  font-style: italic;
}

.skills-card {
  padding: 18px;
}

.skills-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px 24px;
}

.skills-row+.skills-row {
  margin-top: 20px;
}

.skills-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.prefect-stats-block {
  margin-top: 28px;
}
</style>
