<template>
  <div class="page-with-toc">
    <main class="page-with-toc__main">
      <!-- Hero -->
      <section id="introduction" class="hero">
        <div class="container hero__inner">
          <div>
            <div class="kicker">Data Engineer | AI Systems Builder | Scalable Data Platforms</div>
            <h1 class="h1">Hi, I’m Dave Austin, Ph.D.,</h1>
            <div class="hero__sub">
              <p>
                I build data systems that turn unreliable operational data into trusted, decision-ready infrastructure.
                I completed my PhD in Computational Physics at the University of Central Florida, where I built
                large-scale computational workflows and data pipelines to support high-performance simulations and
                analysis of complex materials systems. My work combined scientific modeling with automation, data
                engineering, and reproducible computing practices across HPC environments.
              </p>
              <p>
                I currently work as a Software Engineer and Data Engineer at Bear Cognition, where I design and maintain
                production data pipelines that transform diverse operational data into reliable, analytics-ready
                datasets.
                I develop cloud-based data systems with a focus on scalability, monitoring, and reliability, working
                with
                APIs, logistics data, and variable real-world inputs to build resilient ingestion and validation
                workflows.
              </p>
              <p>
                Across both research and industry, I apply a scientific approach to engineering — emphasizing measurable
                outcomes, systematic debugging, and systems built for long-term reliability.
              </p>
              <p>
                My background in computational physics shaped how I design reliable, measurable data systems.
              </p>
            </div>
            <div class="cta">
              <NuxtLink to="/phd-overview" class="btn btn--primary">Scientific Background & Research Foundations
              </NuxtLink>
              <div class="cta__row">
                <NuxtLink to="/blogs" class="btn">Blogs</NuxtLink>
                <a href="/Resume.pdf" class="btn" download="dave_austin_resume.pdf">Download Resume</a>
              </div>
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

      <!-- Systems I've Built -->
      <section id="projects" class="section">
        <div class="container">
          <div class="section__head">
            <h2 class="section__title">Systems I've Built</h2>
            <p class="section__desc">
              Selected work in data engineering, automation, and ML.
            </p>
          </div>
          <div class="projects">
            <ProjectCard v-for="p in projects" :key="p.title" :project="p" />
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
            <div class="timeline__item timeline__item--current">
              <h3 style="margin: 0">Data Engineer — Bear Cognition</h3>
              <p class="section__desc" style="font-size: 0.9rem; margin-top: 4px">April 2025 – Present</p>
              <ul class="timeline__bullets">
                <li>Designed and deployed production data pipelines integrating APIs, databases, and event-driven
                  sources into Snowflake using Prefect orchestration and Fivetran ingestion.</li>
                <li>Built resilient transformation workflows handling inconsistent operational data, enabling reliable
                  analytics and reporting across business teams.</li>
                <li>Developed ML-assisted automation workflows for bid classification and commission processing,
                  reducing manual review and improving processing throughput.</li>
                <li>Implemented monitoring, retry logic, and failure diagnostics to improve pipeline reliability and
                  surface actionable operational alerts.</li>
                <li>Collaborated with engineering and operations stakeholders to translate business processes into
                  scalable, automated data systems.</li>
              </ul>
            </div>
            <div class="timeline__item">
              <h3 style="margin: 0">Data Engineering/Computational Physics — University of Central Florida</h3>
              <p class="section__desc" style="font-size: 0.9rem; margin-top: 4px">Aug 2018 – April 2025</p>
              <ul class="timeline__bullets">
                <li>Designed and orchestrated large-scale HPC workflows using SLURM to manage distributed simulation
                  workloads and high-volume computational datasets.</li>
                <li>Developed Python tooling for automated data ingestion, validation, and post-processing of simulation
                  outputs across multi-step research pipelines.</li>
                <li>Built reproducible data workflows enabling reliable tracking, transformation, and analysis of large
                  scientific datasets generated across compute clusters.</li>
                <li>Optimized data movement and resource utilization to reduce runtime and improve throughput for
                  thousands of simulation jobs.</li>
                <li>Collaborated with international experimental and computational teams to translate raw simulation
                  data into structured, analysis-ready datasets supporting peer-reviewed publications.</li>
              </ul>
              <NuxtLink to="/phd-overview" class="btn" style="margin-top: 12px; display: inline-block">Learn more about
                the science — click here</NuxtLink>
            </div>
            <div class="timeline__item">
              <h3 style="margin: 0">Technical Instruction & Communication — University of Central Florida</h3>
              <p class="section__desc" style="font-size: 0.9rem; margin-top: 4px">Aug 2018 – May 2020</p>
              <p class="section__desc" style="margin-top: 8px">
                Early in my career, I taught undergraduate physics laboratories at the University of Central Florida,
                guiding groups of 20–30 students through experimental design, data analysis, and scientific reasoning.
              </p>
              <ul class="timeline__bullets">
                <li>Led hands-on technical sessions focused on measurement, data interpretation, and analytical problem
                  solving.</li>
                <li>Designed structured lab workflows that helped students move from raw data to validated conclusions.
                </li>
                <li>Translated complex physical concepts into clear, practical explanations for learners with diverse
                  technical backgrounds.</li>
                <li>Developed evaluation frameworks and feedback processes to improve analytical thinking and
                  reproducibility.</li>
              </ul>
            </div>
            <div class="timeline__item">
              <h3 style="margin: 0">Technical Mentorship & Leadership</h3>
              <p class="section__desc" style="font-size: 0.9rem; margin-top: 4px">Aug 2014 – Present</p>
              <p class="section__desc" style="margin-top: 8px">
                I have regularly worked in environments where complex technical systems needed to be understood,
                adopted, and used by others. Across research and industry roles, I have mentored collaborators and
                junior engineers on computational workflows, data practices, and reproducible engineering methods.
              </p>
              <ul class="timeline__bullets">
                <li>Mentored undergraduate and graduate researchers on high-performance computing workflows and
                  large-scale data analysis.</li>
                <li>Guided collaborators in designing reproducible data pipelines and validation strategies for
                  scientific and operational datasets.</li>
                <li>Developed tooling, documentation, and onboarding practices to help teams reliably run simulations
                  and data workflows.</li>
                <li>Provided long-term technical tutoring across physics, mathematics, and computational topics,
                  strengthening my ability to explain complex systems clearly and help others become independent
                  problem-solvers.</li>
                <li>Supported cross-disciplinary teams by translating complex computational results into actionable
                  insights.</li>
              </ul>
            </div>
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
                <p class="section__desc">Pandas, NumPy, Snowflake, Databricks, Fivetran, DuckDB, MongoDB, Firestore,
                  Parquet, REST APIs, OpenAI API, Linear API</p>
              </div>
              <div class="skills-item">
                <strong>Languages</strong>
                <p class="section__desc">Python, SQL, C++, Fortran, JavaScript, TypeScript, MATLAB, Mathematica, Shell
                  scripting, Bash</p>
              </div>
            </div>
            <div class="skills-row">
              <div class="skills-item">
                <strong>Orchestration</strong>
                <p class="section__desc">Prefect, SLURM</p>
              </div>
              <div class="skills-item">
                <strong>Infra</strong>
                <p class="section__desc">GitHub Actions, Docker, Doppler, Linux</p>
              </div>
              <div class="skills-item">
                <strong>Visualization & frameworks</strong>
                <p class="section__desc">Plotly, Matplotlib, Nuxt</p>
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
                <a v-if="edu.dissertation_link" :href="edu.dissertation_link" target="_blank"
                  rel="noopener noreferrer">{{
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
          <CertificationsCard />
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
            <NuxtLink to="/photos" class="btn">Gallery</NuxtLink>
            <a href="https://www.linkedin.com/in/dave-austin-ph-d-616865a9" class="btn" target="_blank"
              rel="noopener noreferrer">LinkedIn</a>
            <a href="https://github.com/austindi" class="btn" target="_blank" rel="noopener noreferrer">GitHub</a>
          </div>
        </div>
      </section>
    </main>
    <PageToc :items="tocItems" />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Home — Dave Austin",
  description: "Data Engineer | AI Systems Builder | Scalable Data Platforms",
});

const projects = [
  {
    title: "RPA Workflow Capture & Execution System",
    tagline:
      "Browser-based automation platform that records human workflows and converts them into executable processes. Enables scalable automation of legacy systems and manual operations, bridging human actions with programmable data pipelines.",
    stack: ["TypeScript", "Chrome Extension APIs", "Nuxt", "Python", "Prefect", "JSON workflow models", "REST APIs", "OpenAI API (LLM-assisted workflow repair)"],
    github: "https://github.com/austindi",
    inProgress: true,
  },
  {
    title: "Agentic Repair & Pipeline Recovery",
    tagline:
      "Automated monitoring systems that detect pipeline failures, analyze runtime context, and generate corrective recovery actions. Reduces manual intervention by enabling self-healing workflows and faster operational recovery.",
    stack: ["Prefect", "Python", "OpenAI API", "MCP", "Structured logging", "Event-driven workflows"],
    github: "https://github.com/austindi",
    inProgress: true,
  },
  {
    title: "Automation for Messy Real-World Data",
    tagline:
      "Engineering solutions built to handle unreliable operational inputs, schema drift, and inconsistent vendor formats. Emphasizes validation, observability, and long-term stability to maintain trustworthy data pipelines under real production conditions.",
    stack: ["Python", "Data validation frameworks", "Prefect monitoring", "SQL", "Snowflake", "Cloud storage (AWS S3)"],
    github: "https://github.com/austindi",
  },
  {
    title: "Prefect Workflow Ecosystem",
    tagline:
      "Internal orchestration platform standardizing how data pipelines are created, deployed, and operated. Includes a custom CLI for initializing new pipelines, automated secret management through Doppler, CI/CD generation, and built-in testing frameworks. Centralizes execution, monitoring, and recovery across ingestion and transformation workflows, improving reliability and reducing operational overhead.",
    stack: ["Prefect", "Python", "Docker", "AWS", "Doppler", "GitHub Actions", "Snowflake"],
    github: "https://github.com/austindi",
    inProgress: true,
  },
  {
    title: "AI-Driven Pipeline Observability",
    tagline:
      "Automated monitoring system that analyzes Prefect workflow logs to detect warnings and incomplete processing events. An LLM summarizes operational issues, identifies potential data gaps, and delivers daily diagnostic reports, improving visibility and reducing unnoticed pipeline failures.",
    stack: ["Prefect", "Python", "OpenAI API", "MCP", "Structured Logging", "Email Automation"],
    github: "https://github.com/austindi",
    inProgress: true,
  },
  {
    title: "Workflow Observability & Incident Automation",
    tagline:
      "Operational monitoring system that detects workflow failures and automatically generates Linear tickets with execution context, reducing manual triage and improving response time. Tracks per-customer flow runtime and resource usage to provide visibility into operational cost and performance across data pipelines.",
    stack: ["Prefect", "Python", "OpenAI API", "MCP", "Linear API", "Structured Logging", "AWS", "Snowflake"],
    github: "https://github.com/austindi",
  },
  {
    title: "Data Ingestion & Normalization Platform",
    tagline:
      "Resilient ingestion pipelines designed for inconsistent APIs, logistics feeds, and spreadsheet data. Standardizes heterogeneous inputs into structured, analytics-ready datasets, enabling reliable downstream reporting and decision-making.",
    stack: ["Python", "Pandas", "Databricks", "SQL", "Snowflake", "REST APIs", "OpenAI API (LLM-assisted normalization)", "Parquet"],
    github: "https://github.com/austindi",
  },
  {
    title: "HPC Orchestration Pipelines",
    tagline:
      "Distributed workflow systems for large-scale scientific computation and simulation execution. Automated job scheduling, monitoring, and data generation across HPC environments, enabling reproducible research workflows and efficient resource utilization at scale.",
    stack: ["Python", "SLURM", "Bash", "Linux", "VASP", "Quantum ESPRESSO", "SSH/SCP"],
    github: "https://github.com/austindi",
  },
  {
    title: "STM/STS Simulation & Analysis Platform",
    tagline:
      "Developed a computational pipeline to simulate scanning tunneling microscopy (STM) and spectroscopy (STS) measurements directly from density functional theory (DFT) calculations. The system automated post-processing, visualization, and comparison between theoretical models and experimental data, enabling reproducible analysis of nanoscale electronic structure.",
    stack: ["Python", "ASE", "VASP", "Quantum ESPRESSO", "HPC (SLURM)", "NumPy", "Matplotlib"],
    github: "https://github.com/austindi",
  },
];

const education = [
  { degree: "Ph.D. in Physics", institution: "University of Central Florida", field: "Computational physics, density functional theory", date: "Aug 2018 – Aug 2024", dissertation: "First Principles Studies of Nano-Scale Phenomena At Surfaces: From Characteristics of Single Atom Catalysts to Molecular Structure Formation", dissertation_link: "https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1500&context=etd2023", diploma_link: "" },
  { degree: "M.S. in Physics", institution: "University of Central Florida", field: "", date: "Aug 2018 – May 2020", diploma_link: "" },
  { degree: "B.S. in Physics", institution: "College of Charleston", field: "", date: "Aug 2014 – May 2018", diploma_link: "" },
];

const showPrefectStats = true; // Set false to hide Task Runs card

const tocItems = [
  { id: "introduction", label: "Introduction" },
  { id: "projects", label: "Systems I've Built" },
  { id: "experience", label: "Experience" },
  { id: "skills", label: "Skills" },
  { id: "education", label: "Education" },
  { id: "certifications", label: "Certifications" },
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

.page-with-toc {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 48px;
  align-items: start;
}

@media (max-width: 1020px) {
  .page-with-toc {
    grid-template-columns: 1fr;
  }
}
</style>
