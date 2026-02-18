<template>
  <div>
    <section class="section hero">
      <div class="container">
        <div class="page-header">
          <BackButton />
        </div>
        <h1 class="h1">Physics Career Overview</h1>
        <p class="section__desc" style="max-width: 60ch">
          Peer-reviewed publications, oral and poster presentations, and leadership roles from my doctoral research in computational physics.
        </p>
      </div>
    </section>

    <!-- Research Experience -->
    <section id="research" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Research Experience</h2>
          <p class="section__desc">
            Computational physics and simulation from graduate, postdoctoral, and undergraduate work.
          </p>
        </div>
        <div class="research-experience">
          <article class="research-card card">
            <div class="research-card__label">
              <div class="research-card__row">
                <h3 class="research-card__heading">Postdoctoral Research</h3>
                <p class="research-card__period">Aug 2024 – Mar 2025</p>
              </div>
              <div class="research-card__row">
                <h3 class="research-card__heading">Graduate Research</h3>
                <p class="research-card__period">Aug 2018 – Aug 2024</p>
              </div>
            </div>
            <p class="research-card__text">
              During my graduate and postdoc research at the University of Central Florida, I studied atomic-scale surface phenomena using high-performance computing and advanced simulation methods. My work focused on modeling electronic structure, catalytic behavior, and nanoscale material interactions, including single-atom catalysts, hybrid organic–inorganic interfaces, and molecular systems on metal surfaces. This research required designing large computational workflows, analyzing complex simulation datasets, and developing reproducible tools to understand and predict material behavior. The work was supported by the National Science Foundation under Professor Talat Rahman.
            </p>
          </article>
          <article class="research-card card">
            <div class="research-card__label">
              <h3 class="research-card__heading">Undergraduate Research</h3>
              <p class="research-card__period">Aug 2014 – July 2018</p>
            </div>
            <p class="research-card__text">
              As an undergraduate researcher at the College of Charleston, I developed computational models of neural systems, building numerical solvers for the Hodgkin–Huxley equations and simulating large neural networks to study synchronization and phase stability. This work combined mathematical modeling, numerical methods, and large-scale simulation to investigate complex dynamical behavior in biological systems, supported by an NSF CAREER Award under Professor Sorinel Oprisan.
            </p>
          </article>
        </div>
      </div>
    </section>

    <!-- Peer-reviewed papers -->
    <section id="publications" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Peer-reviewed Papers</h2>
          <p class="section__desc">
            Selected publications in catalysis, surface science, and computational physics.
          </p>
        </div>
        <div class="carousel">
          <button
            type="button"
            class="carousel__arrow"
            aria-label="Previous"
            @click="rotateLeft"
          >
            &#8592;
          </button>
          <div class="carousel__wrapper">
            <div class="carousel__slides">
              <article
                v-for="(pub, i) in visiblePublications"
                :key="`${pub.title}-${i}`"
                class="publication-card card"
              >
                <img :src="`/${pub.image_url}`" :alt="pub.title" />
                <h4 class="publication-card__title">{{ pub.title }}</h4>
                <p v-if="pub.journal" class="publication-card__journal">{{ pub.journal }}</p>
                <p v-if="pub.date" class="publication-card__date">{{ pub.date }}</p>
                <p class="publication-card__summary">{{ pub.summary }}</p>
                <div class="publication-card__action">
                  <a :href="pub.link" target="_blank" rel="noopener noreferrer" class="btn">Read More</a>
                </div>
              </article>
            </div>
          </div>
          <button
            type="button"
            class="carousel__arrow"
            aria-label="Next"
            @click="rotateRight"
          >
            &#8594;
          </button>
        </div>
      </div>
    </section>

    <!-- Grants and Awards -->
    <section id="grants-awards" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Grants and Awards</h2>
          <p class="section__desc">
            Fellowships, travel grants, and recognition from UCF, APS, AVS, and NSF.
          </p>
        </div>
        <div class="awards-list">
          <article
            v-for="(item, i) in grantsAndAwards"
            :key="`award-${i}`"
            class="award-card card"
          >
            <h4 class="award-card__name">{{ item.name }}</h4>
            <p class="award-card__period">{{ item.period }}</p>
            <p v-if="item.organization" class="award-card__org">{{ item.organization }}</p>
            <p v-if="item.details" class="award-card__details">{{ item.details }}</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Oral presentations -->
    <section id="oral" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Oral Presentations</h2>
          <p class="section__desc">
            Invited and contributed talks at conferences and symposia.
          </p>
        </div>
        <div class="presentation-list">
          <article
            v-for="(p, i) in visibleOral"
            :key="`oral-${i}`"
            class="presentation-card card"
          >
            <h4 class="presentation-card__title">{{ p.title }}</h4>
            <p class="presentation-card__meta">{{ p.event }}</p>
            <p class="presentation-card__date">{{ p.date }}</p>
            <p class="presentation-card__location">{{ p.location }}</p>
            <p class="presentation-card__authors">{{ p.authors }}</p>
          </article>
        </div>
        <div v-if="oralRest.length > 0" class="presentation-toggle">
          <button
            type="button"
            class="btn"
            @click="showMoreOral = !showMoreOral"
          >
            {{ showMoreOral ? "Show less" : "Show more" }}
          </button>
        </div>
        <div v-if="showMoreOral && oralRest.length" class="presentation-list presentation-list--extra">
          <article
            v-for="(p, i) in oralRest"
            :key="`oral-extra-${i}`"
            class="presentation-card card"
          >
            <h4 class="presentation-card__title">{{ p.title }}</h4>
            <p class="presentation-card__meta">{{ p.event }}</p>
            <p class="presentation-card__date">{{ p.date }}</p>
            <p class="presentation-card__location">{{ p.location }}</p>
            <p class="presentation-card__authors">{{ p.authors }}</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Poster presentations -->
    <section id="posters" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Poster Presentations</h2>
          <p class="section__desc">
            Poster presentations at conferences and symposia.
          </p>
        </div>
        <div class="presentation-list">
          <article
            v-for="(p, i) in visiblePoster"
            :key="`poster-${i}`"
            class="presentation-card card"
          >
            <h4 class="presentation-card__title">{{ p.title }}</h4>
            <p class="presentation-card__meta">{{ p.event }}</p>
            <p class="presentation-card__date">{{ p.date }}</p>
            <p class="presentation-card__location">{{ p.location }}</p>
            <p class="presentation-card__authors">{{ p.authors }}</p>
          </article>
        </div>
        <div v-if="posterRest.length > 0" class="presentation-toggle">
          <button
            type="button"
            class="btn"
            @click="showMorePoster = !showMorePoster"
          >
            {{ showMorePoster ? "Show less" : "Show more" }}
          </button>
        </div>
        <div v-if="showMorePoster && posterRest.length" class="presentation-list presentation-list--extra">
          <article
            v-for="(p, i) in posterRest"
            :key="`poster-extra-${i}`"
            class="presentation-card card"
          >
            <h4 class="presentation-card__title">{{ p.title }}</h4>
            <p class="presentation-card__meta">{{ p.event }}</p>
            <p class="presentation-card__date">{{ p.date }}</p>
            <p class="presentation-card__location">{{ p.location }}</p>
            <p class="presentation-card__authors">{{ p.authors }}</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Leadership Experience -->
    <section id="leadership" class="section">
      <div class="container">
        <div class="section__head">
          <h2 class="section__title">Leadership Experience</h2>
          <p class="section__desc">
            Roles in professional and departmental organizations at UCF.
          </p>
        </div>
        <div class="leadership-list">
          <article
            v-for="(item, i) in leadershipExperience"
            :key="`leadership-${i}`"
            class="leadership-card card"
          >
            <h4 class="leadership-card__role">{{ item.role }}</h4>
            <p class="leadership-card__period">{{ item.period }}</p>
            <p class="leadership-card__org">{{ item.organization }}</p>
            <p v-if="item.details" class="leadership-card__details">{{ item.details }}</p>
          </article>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Physics Career Overview — Dave Austin",
  description: "Peer-reviewed publications, oral and poster presentations",
});

interface Presentation {
  title: string;
  event: string;
  date: string;
  location: string;
  authors: string;
}

interface Publication {
  title: string;
  journal?: string;
  date?: string;
  image_url: string;
  summary: string;
  link: string;
}

interface LeadershipItem {
  role: string;
  period: string;
  organization: string;
  details?: string;
}

interface GrantOrAward {
  name: string;
  period: string;
  organization?: string;
  details?: string;
}

const grantsAndAwards: GrantOrAward[] = [
  { name: "UCF Order of the Pegasus", period: "2025" },
  { name: "AVS NSTD Graduate Student", period: "2024" },
  { name: "UCF Order of the Pegasus Nomination", period: "2024" },
  { name: "AVS Dorothy M. and Earl S. Hoffman Travel Grant", period: "2024" },
  {
    name: "Resolv Cluster International Research Fellowship",
    period: "August 2023 – December 2023",
    organization: "Bochum, Germany",
  },
  { name: "UCF Physics Department Student of the Year Award", period: "2022–2023" },
  { name: "American Physical Society Leadership Summit", period: "2023, 2024" },
  { name: "UCF College of Graduate Studies Presentation Fellowship", period: "2022, 2023, 2024" },
  { name: "UCF Student Government Association Travel Grant", period: "2022, 2023, 2024" },
  {
    name: "Alliance for Graduate Education and the Professoriate",
    period: "2020 – 2024",
    organization: "National Science Foundation",
  },
  {
    name: "Outstanding Undergraduate Research",
    period: "2018",
    organization: "Department of Physics and Astronomy, College of Charleston",
  },
  {
    name: "Best Poster Presentation",
    period: "Fall 2016",
    details: "A Generalized Phase Resetting Method for Phase-Locked Modes Prediction",
    organization: "Southern Atlantic Coast Section of the American Association of Physics Teachers (SACS-AAPT)",
  },
];

const leadershipExperience: LeadershipItem[] = [
  { role: "Vice Chair", period: "2023–2024", organization: "APS Chapter at the University of Central Florida" },
  { role: "Founding Treasurer", period: "2020–2023", organization: "APS Chapter at the University of Central Florida" },
  { role: "Treasurer", period: "2019–2020", organization: "Graduate Society of Physics Students, UCF" },
  { role: "Committee Member", period: "2020–2022", organization: "APS IDEALS Committee" },
  {
    role: "Committee Member",
    period: "2018–2021",
    organization: "Outreach Committee, UCF Department of Physics",
    details: "STEM Day, Physics Career Day, Florida Prison Education Project",
  },
];

const oralPresentations = ref<Presentation[]>([]);
const posterPresentations = ref<Presentation[]>([]);
const publications = ref<Publication[]>([]);
const visibleCount = ref(1);
const slideWidth = 300;
const gap = 20;
const showMoreOral = ref(false);
const showMorePoster = ref(false);

const INITIAL_COUNT = 6;

function parseDate(p: Presentation): number {
  const d = new Date(p.date);
  return Number.isNaN(d.getTime()) ? 0 : d.getTime();
}

function isImportantOral(p: Presentation): boolean {
  const e = (p.event || "").toLowerCase();
  const loc = (p.location || "").toLowerCase();
  return (
    e.includes("avs") ||
    e.includes("american physical society") ||
    e.includes("aps") ||
    e.includes("american chemical society") ||
    e.includes("acs")
  );
}

function isImportantPoster(p: Presentation): boolean {
  const e = (p.event || "").toLowerCase();
  const loc = (p.location || "").toLowerCase();
  return (
    loc.includes("germany") ||
    e.includes("gordon") ||
    e.includes("cns") ||
    e.includes("organization for computational neurosciences") ||
    e.includes("aapt") ||
    (e.includes("science") && e.includes("emerging")) ||
    (e.includes("technology") && e.includes("emerging")) ||
    e.includes("emerging materials")
  );
}

const sortedOral = computed(() => {
  const list = [...oralPresentations.value];
  list.sort((a, b) => parseDate(b) - parseDate(a));
  const important = list.filter(isImportantOral);
  const rest = list.filter((p) => !isImportantOral(p));
  return [...important, ...rest];
});

const sortedPoster = computed(() => {
  const list = [...posterPresentations.value];
  list.sort((a, b) => parseDate(b) - parseDate(a));
  const important = list.filter(isImportantPoster);
  const rest = list.filter((p) => !isImportantPoster(p));
  return [...important, ...rest];
});

const visibleOral = computed(() => sortedOral.value.slice(0, INITIAL_COUNT));
const oralRest = computed(() => {
  const rest = sortedOral.value.slice(INITIAL_COUNT);
  return [...rest].sort((a, b) => parseDate(b) - parseDate(a));
});
const visiblePoster = computed(() => sortedPoster.value.slice(0, INITIAL_COUNT));
const posterRest = computed(() => {
  const rest = sortedPoster.value.slice(INITIAL_COUNT);
  return [...rest].sort((a, b) => parseDate(b) - parseDate(a));
});

const visiblePublications = computed(() =>
  publications.value.slice(0, Math.max(1, visibleCount.value))
);

function calculateVisibleCount() {
  const containerWidth = typeof window !== "undefined" ? window.innerWidth : 1100;
  visibleCount.value = Math.max(1, Math.floor((containerWidth + gap) / (slideWidth + gap)));
}

function rotateLeft() {
  const last = publications.value.pop();
  if (last) publications.value.unshift(last);
}

function rotateRight() {
  const first = publications.value.shift();
  if (first) publications.value.push(first);
}

onMounted(async () => {
  try {
    const [presRes, pubRes] = await Promise.all([
      fetch("/presentations.json"),
      fetch("/publications.json"),
    ]);
    const presData = await presRes.json();
    oralPresentations.value = presData.oral ?? [];
    posterPresentations.value = presData.poster ?? [];

    const pubData = await pubRes.json();
    const list = Array.isArray(pubData) ? pubData : [];
    list.sort((a, b) => {
      const yearA = parseInt(String(a.date || "0"), 10) || 0;
      const yearB = parseInt(String(b.date || "0"), 10) || 0;
      return yearB - yearA;
    });
    publications.value = list;
    calculateVisibleCount();
    window.addEventListener("resize", calculateVisibleCount);
  } catch {
    oralPresentations.value = [];
    posterPresentations.value = [];
    publications.value = [];
  }
});

onBeforeUnmount(() => {
  if (typeof window !== "undefined") {
    window.removeEventListener("resize", calculateVisibleCount);
  }
});
</script>

<style scoped>
/* Hover pop for cards and interactive elements */
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.12);
}

.btn {
  transition: transform 0.2s ease;
}

.btn:hover {
  transform: scale(1.03);
}

.carousel__arrow {
  transition: transform 0.2s ease, filter 0.15s ease;
}

.carousel__arrow:hover {
  transform: scale(1.08);
  filter: brightness(1.1);
}

.presentation-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px;
}

.presentation-list--extra {
  margin-top: 14px;
}

.presentation-toggle {
  margin-top: 16px;
}

.presentation-card {
  padding: 16px;
}

.presentation-card__title {
  margin: 0 0 8px;
  font-size: 1rem;
  font-weight: 600;
}

.presentation-card__meta {
  margin: 0 0 4px;
  font-size: 0.9rem;
  color: var(--muted);
}

.presentation-card__date {
  margin: 0 0 4px;
  font-size: 0.875rem;
  color: var(--muted);
}

.presentation-card__location {
  margin: 0 0 4px;
  font-size: 0.85rem;
  color: var(--muted);
}

.presentation-card__authors {
  margin: 0;
  font-size: 0.85rem;
  color: var(--muted);
}

.research-experience {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.research-card {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 24px;
  padding: 20px 24px;
}

.research-card__label {
  flex-shrink: 0;
  width: 160px;
}

.research-card__row {
  margin-bottom: 12px;
}

.research-card__row:last-child {
  margin-bottom: 0;
}

.research-card__heading {
  margin: 0 0 4px;
  font-size: 1.125rem;
  font-weight: 600;
}

.research-card__period {
  margin: 0;
  font-size: 0.875rem;
  color: var(--muted);
}

@media (max-width: 520px) {
  .research-card {
    flex-direction: column;
    gap: 10px;
  }
  .research-card__label {
    width: auto;
  }
}

.research-card__text {
  margin: 0;
  flex: 1;
  min-width: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
}

.awards-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 14px;
}

.award-card {
  padding: 16px;
}

.award-card__name {
  margin: 0 0 4px;
  font-size: 1rem;
  font-weight: 600;
}

.award-card__period {
  margin: 0 0 6px;
  font-size: 0.9rem;
  color: var(--muted);
}

.award-card__org {
  margin: 0 0 4px;
  font-size: 0.9rem;
  color: var(--muted);
}

.award-card__details {
  margin: 0;
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.4;
}

.leadership-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 14px;
}

.leadership-card {
  padding: 16px;
}

.leadership-card__role {
  margin: 0 0 4px;
  font-size: 1rem;
  font-weight: 600;
}

.leadership-card__period {
  margin: 0 0 6px;
  font-size: 0.9rem;
  color: var(--muted);
}

.leadership-card__org {
  margin: 0 0 4px;
  font-size: 0.9rem;
  color: var(--muted);
}

.leadership-card__details {
  margin: 0;
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.4;
}

.carousel {
  display: flex;
  align-items: center;
  gap: 12px;
  overflow: hidden;
}

.carousel__wrapper {
  overflow: hidden;
  flex: 1;
}

.carousel__slides {
  display: flex;
  gap: 20px;
  flex-wrap: nowrap;
}

.carousel__arrow {
  flex-shrink: 0;
  width: 44px;
  height: 44px;
  font-size: 20px;
  background: var(--accent);
  color: #042423;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  font-weight: 700;
  transition: filter 0.15s ease;
}


.publication-card {
  flex: 0 0 300px;
  min-height: 420px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-align: center;
}

.publication-card img {
  width: 100%;
  max-height: 180px;
  object-fit: cover;
  border-radius: 8px;
}

.publication-card__title {
  margin: 0;
  font-size: 1rem;
  font-weight: 700;
  line-height: 1.3;
}

.publication-card__journal {
  margin: 0 0 4px;
  font-size: 0.875rem;
  color: var(--muted);
}

.publication-card__date {
  margin: 0 0 8px;
  font-size: 0.8125rem;
  color: var(--muted);
}

.publication-card__summary {
  margin: 0;
  flex: 1 1 auto;
  font-size: 0.875rem;
  color: var(--muted);
  line-height: 1.5;
  -webkit-line-clamp: 5;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.publication-card__action {
  margin-top: auto;
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
}

.page-header {
  margin-bottom: 20px;
}
</style>
