<template>
  <div class="page-with-toc">
    <main class="page-with-toc__main">
      <div class="container main-content">
      <!-- Hero -->
      <section id="introduction" class="hero">
        <div class="hero__inner">
          <div>
            <div class="kicker">Building reliable data platforms, intelligent workflows, and AI-driven systems</div>
            <h1 class="h1">Hi, I’m Dave Austin, Ph.D.,</h1>
            <div class="hero__sub">
              <p>
                I design systems that turn messy, unreliable data and complex workflows into reliable, decision-ready infrastructure. My work sits at the intersection of data engineering, AI-assisted automation, and scientific computing, focused on building systems that continue to operate correctly under real-world uncertainty.
              </p>
              <p>I build:</p>
              <ul class="hero__sub-list">
                <li>Reliable data platforms that tolerate inconsistent operational inputs and evolving schemas</li>
                <li>AI-assisted systems that monitor workflows, detect failures, and guide recovery decisions</li>
                <li>Automated pipelines that scale from research environments to production cloud systems</li>
              </ul>
              <p>
                These systems have been developed across HPC supercomputers, cloud platforms, and production business environments where correctness, observability, and long-term reliability matter.
              </p>
              <p>
                I currently work as a Software Engineer and Data Engineer at Bear Cognition, designing and operating production data pipelines that transform diverse operational data into trusted, analytics-ready datasets. My work focuses on scalability, monitoring, and validation, enabling teams to make decisions from data they can rely on.
              </p>
              <p>
                Across both research and industry, I apply a scientific approach to engineering: measure outcomes, isolate failure modes, and build systems designed to remain stable as complexity grows.
              </p>
              <p>
                My background in computational physics shaped how I approach engineering problems, treating systems as experiments that must be observable, reproducible, and continuously improved.
              </p>
            </div>
            <div class="cta cta--centered">
              <NuxtLink to="/phd-overview" class="btn btn--primary">Scientific Background & Research Foundations</NuxtLink>
              <NuxtLink to="/blogs" class="btn">Blogs</NuxtLink>
              <div ref="resumeDropdownRef" class="resume-dropdown">
                <button
                  type="button"
                  class="btn"
                  :class="{ 'resume-dropdown__trigger--open': resumeDropdownOpen }"
                  :aria-expanded="resumeDropdownOpen"
                  aria-haspopup="true"
                  @click="resumeDropdownOpen = !resumeDropdownOpen"
                >
                  Download Resume <span class="resume-dropdown__caret">▾</span>
                </button>
                <div v-show="resumeDropdownOpen" class="resume-dropdown__menu" role="menu">
                  <a
                    v-for="opt in resumeOptions"
                    :key="opt.label"
                    :href="opt.path"
                    class="resume-dropdown__item"
                    role="menuitem"
                    download
                    @click="resumeDropdownOpen = false"
                  >
                    {{ opt.label }}
                  </a>
                </div>
              </div>
            </div>
            <div class="pills">
              <span class="pill">⚡ Reliable Data Systems</span>
              <span class="pill">🤖 AI-Assisted Automation</span>
              <span class="pill">📊 Decision & Analytics Infrastructure</span>
              <span class="pill">🔄 Workflow Orchestration at Scale</span>
            </div>
            <div v-if="showPrefectStats" class="prefect-stats-block">
              <PrefectStatsCard />
            </div>
          </div>
        </div>
      </section>

      <!-- Representative Systems -->
      <section id="projects" class="section">
        <div>
          <div class="section__head">
            <h2 class="section__title">Representative Systems</h2>
          </div>
          <p class="section__desc" style="margin-top: -8px; margin-bottom: 18px">
            These systems were developed across research computing, production data engineering, and applied AI environments. While independent, they share a common goal: transforming unreliable processes, messy inputs, and complex workflows into stable, observable, and reproducible systems.
          </p>
          <div class="projects">
            <ProjectCard v-for="p in visibleProjects" :key="p.title" :project="p" />
          </div>
          <div v-if="projects.length > 3" class="projects-toggle">
            <button type="button" class="btn" @click="showAllProjects = !showAllProjects">
              {{ showAllProjects ? 'Show less' : 'Show more' }}
            </button>
          </div>
        </div>
      </section>

      </div>

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
                <li>Architect and operate production data pipelines integrating APIs, partner systems, and event-driven sources into Snowflake using Prefect orchestration and automated ingestion frameworks.</li>
                <li>Designed normalization and validation systems to stabilize highly inconsistent operational data, enabling reliable analytics and reporting across logistics, finance, and operations teams.</li>
                <li>Built AI-assisted automation workflows for bid classification and commission processing, reducing manual review and increasing processing throughput.</li>
                <li>Implemented observability, retry strategies, and failure diagnostics that surfaced actionable pipeline issues and improved overall workflow reliability.</li>
                <li>Partner with engineering and business stakeholders to translate manual processes into scalable data systems supporting decision-making and operational execution.</li>
              </ul>
            </div>
            <div class="timeline__item">
              <h3 style="margin: 0">Data Engineering / Scientific Computing — University of Central Florida</h3>
              <p class="section__desc" style="font-size: 0.9rem; margin-top: 4px">Aug 2018 – Apr 2025</p>
              <ul class="timeline__bullets">
                <li>Designed and operated large-scale HPC workflow systems using SLURM to orchestrate distributed simulation workloads across national supercomputing environments.</li>
                <li>Developed Python automation tooling for ingestion, validation, and post-processing of multi-stage computational outputs, transforming raw simulation artifacts into structured, analysis-ready datasets.</li>
                <li>Built reproducible data pipelines that tracked configuration metadata, enabled automated regeneration of results, and supported reliable scientific analysis at scale.</li>
                <li>Implemented monitoring, logging, and restart logic to detect failures, recover long-running jobs, and eliminate manual intervention across thousands of simulations.</li>
                <li>Optimized compute utilization and data movement strategies, improving throughput and reducing delays in large experimental parameter studies.</li>
                <li>Collaborated with international experimental and computational teams to translate complex scientific outputs into usable datasets supporting multiple peer-reviewed publications.</li>
              </ul>
              <div style="margin-top: 12px; text-align: center">
                <NuxtLink to="/phd-overview" class="btn">Learn more about the science — click here</NuxtLink>
              </div>
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
                <strong>Languages</strong>
                <p class="section__desc">Python, SQL, TypeScript, JavaScript, C++, Fortran, MATLAB, Mathematica, Bash / Shell Scripting</p>
              </div>
              <div class="skills-item">
                <strong>Data Platforms & Processing</strong>
                <p class="section__desc">Snowflake, Databricks, DuckDB, Pandas, NumPy, Parquet, REST APIs, Fivetran, MongoDB, Firestore, Linear API</p>
              </div>
              <div class="skills-item">
                <strong>AI & Intelligent Systems</strong>
                <p class="section__desc">LLM integration (OpenAI API), RAG concepts, LLM-assisted automation, workflow diagnostics, agentic monitoring systems, structured prompt pipelines</p>
              </div>
            </div>
            <div class="skills-row">
              <div class="skills-item">
                <strong>Cloud & Infrastructure</strong>
                <p class="section__desc">AWS (Lambda, S3, EC2), GCP, Docker, Linux, GitHub Actions, Doppler</p>
              </div>
              <div class="skills-item">
                <strong>Orchestration & Distributed Systems</strong>
                <p class="section__desc">Prefect, SLURM, workflow orchestration, event-driven pipelines, distributed compute workflows</p>
              </div>
              <div class="skills-item">
                <strong>Data Engineering & Reliability</strong>
                <p class="section__desc">ETL/ELT pipelines, ingestion & normalization, schema evolution, observability, structured logging, automated recovery systems</p>
              </div>
            </div>
            <div class="skills-row">
              <div class="skills-item">
                <strong>Visualization & Application Frameworks</strong>
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
    <aside class="page-with-toc__sidebar index-sidebar">
      <div class="index-sidebar__inner">
        <div class="hero__photo" aria-label="Dave Austin portrait"></div>
        <div class="index-sidebar__toc-wrap">
          <PageToc :items="tocItems" />
        </div>
      </div>
    </aside>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Home — Dave Austin",
  description: "Data Engineer | AI Systems Builder | Scalable Data Platforms",
});

const projects = [
  {
    title: "Prefect Workflow Ecosystem",
    tagline:
      "Internal orchestration platform standardizing how data pipelines are created, deployed, and operated. Includes a custom CLI for initializing new pipelines, automated secret management through Doppler, CI/CD generation, and built-in testing frameworks. Centralizes execution, monitoring, and recovery across ingestion and transformation workflows, improving reliability and reducing operational overhead.",
    stack: ["Prefect", "Python", "Docker", "AWS", "Doppler", "GitHub Actions", "Snowflake"],
    link: "/prefect-workflow-ecosystem",
    inProgress: true,
  },
  {
    title: "RPA Workflow Capture & Execution System",
    link: "/rpa-workflow-capture",
    tagline:
      "Browser-based automation platform designed to convert human operational workflows into executable software processes. Captures user interactions from the browser, transforms them into structured workflow events, and persists them in a semi-structured data model for execution, monitoring, and evolution.",
    stack: ["TypeScript", "Chrome Extension APIs", "Nuxt", "Python", "Prefect", "REST APIs", "OpenAI API", "Semi-Structured Data Modeling"],
    inProgress: true,
  },
  {
    title: "Agentic Repair & Pipeline Recovery",
    link: "/agentic-repair",
    tagline:
      "Automated reliability system that detects pipeline failures, analyzes execution context, and provides corrective recovery actions through an AI-assisted operations layer. Transforms orchestration telemetry into structured diagnostic signals consumable by LLM agents via MCP.",
    stack: ["Prefect", "Python", "OpenAI API", "MCP", "Structured Logging", "Event-Driven Workflows", "Observability Systems"],
    inProgress: true,
  },
  {
    title: "AI-Driven Pipeline Observability",
    tagline:
      "Automated monitoring system that analyzes Prefect workflow logs to detect warnings and incomplete processing events. An LLM summarizes operational issues, identifies potential data gaps, and delivers daily diagnostic reports, improving visibility and reducing unnoticed pipeline failures.",
    stack: ["Prefect", "Python", "OpenAI API", "MCP", "Structured Logging", "Email Automation"],
    link: "/ai-driven-pipeline-observability",
    inProgress: true,
  },
  {
    title: "Workflow Observability & Incident Automation",
    tagline:
      "Operational monitoring system that detects workflow failures and automatically generates Linear tickets with execution context, reducing manual triage and improving response time. Tracks per-customer flow runtime and resource usage to provide visibility into operational cost and performance across data pipelines.",
    stack: ["Prefect", "Python", "OpenAI API", "MCP", "Linear API", "Structured Logging", "AWS", "Snowflake"],
    link: "/workflow-observability-incident-automation",
  },
  {
    title: "Automation for Messy Real-World Data",
    tagline:
      "Resilient ingestion pipelines designed for inconsistent APIs, logistics feeds, and spreadsheet data. Standardizes heterogeneous inputs into structured, analytics-ready datasets, enabling reliable downstream reporting and decision-making.",
    stack: ["Python", "Pandas/Polars", "Snowflake", "SQL", "REST APIs", "AWS S3", "OpenAI API (LLM-assisted normalization)", "Parquet"],
    link: "/automation-messy-data",
  },
  {
    title: "HPC Orchestration Pipelines",
    tagline:
      "Distributed workflow systems for large-scale scientific computation and simulation execution. Automated job scheduling, monitoring, and data generation across HPC environments, enabling reproducible research workflows and efficient resource utilization at scale.",
    stack: ["Python", "SLURM", "Bash", "Linux", "VASP", "Quantum ESPRESSO", "SSH/SCP"],
    link: "/hpc-orchestration-pipelines",
  },
  {
    title: "STM/STS Simulation & Analysis Platform",
    tagline:
      "Developed a computational pipeline to simulate scanning tunneling microscopy (STM) and spectroscopy (STS) measurements directly from density functional theory (DFT) calculations. The system automated post-processing, visualization, and comparison between theoretical models and experimental data, enabling reproducible analysis of nanoscale electronic structure.",
    stack: ["Python", "ASE", "VASP", "Quantum ESPRESSO", "HPC (SLURM)", "NumPy", "Matplotlib"],
    link: "/stm-sts-simulation-analysis-platform",
  },
];

const showAllProjects = ref(false);
const visibleProjects = computed(() =>
  showAllProjects.value ? projects : projects.slice(0, 3)
);

const education = [
  { degree: "Ph.D. in Physics", institution: "University of Central Florida", field: "Computational physics, density functional theory", date: "Aug 2018 – Aug 2024", dissertation: "First Principles Studies of Nano-Scale Phenomena At Surfaces: From Characteristics of Single Atom Catalysts to Molecular Structure Formation", dissertation_link: "https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1500&context=etd2023", diploma_link: "" },
  { degree: "M.S. in Physics", institution: "University of Central Florida", field: "", date: "Aug 2018 – May 2020", diploma_link: "" },
  { degree: "B.S. in Physics", institution: "College of Charleston", field: "", date: "Aug 2014 – May 2018", diploma_link: "" },
];

const showPrefectStats = true; // Set false to hide Task Runs card

const resumeOptions = [
  { label: "Data Engineering", path: "/Data_Engineering_Resume.pdf" },
  { label: "Data Science / Analytics", path: "/Data_Science_Resume.pdf" },
  { label: "AI / Solution Engineering", path: "/AI_Engineering_Resume.pdf" },
];

const resumeDropdownOpen = ref(false);
const resumeDropdownRef = ref<HTMLElement | null>(null);

function handleClickOutside(e: MouseEvent) {
  if (resumeDropdownRef.value && !resumeDropdownRef.value.contains(e.target as Node)) {
    resumeDropdownOpen.value = false;
  }
}

onMounted(() => {
  document.addEventListener("click", handleClickOutside);
});
onBeforeUnmount(() => {
  document.removeEventListener("click", handleClickOutside);
});

const tocItems = [
  { id: "introduction", label: "Introduction" },
  { id: "projects", label: "Representative Systems" },
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

.projects-toggle {
  margin-top: 20px;
}

.resume-dropdown {
  position: relative;
  display: inline-block;
}

.resume-dropdown__caret {
  display: inline-block;
  margin-left: 4px;
  opacity: 0.8;
  transition: transform 0.2s ease;
}

.resume-dropdown__trigger--open .resume-dropdown__caret {
  transform: rotate(180deg);
}

.resume-dropdown__menu {
  position: absolute;
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  min-width: 220px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 10px;
  box-shadow: 0 8px 24px rgb(0 0 0 / 25%);
  padding: 8px 0;
  z-index: 100;
}

.resume-dropdown__item {
  display: block;
  padding: 10px 16px;
  color: var(--text);
  text-decoration: none;
  font-weight: 500;
  transition: background 0.15s ease, color 0.15s ease;
}

.resume-dropdown__item:hover {
  background: var(--hover-bg);
  color: var(--accent);
  text-decoration: none;
}

.page-with-toc {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 48px;
  align-items: start;
}

@media (max-width: 1020px) {
  .page-with-toc {
    grid-template-columns: 1fr;
  }

  .page-with-toc__sidebar {
    order: -1;
    position: static;
    max-height: none;
  }
}
</style>
