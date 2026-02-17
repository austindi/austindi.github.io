<template>
  <div>
    <section class="section hero">
      <div class="container">
        <h1 class="h1">Physics Career Overview</h1>
        <p class="section__desc" style="max-width: 60ch">
          Peer-reviewed publications, oral presentations, and poster presentations from my doctoral research in computational physics.
        </p>
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
                <p class="publication-card__summary">{{ pub.summary }}</p>
                <a :href="pub.link" target="_blank" rel="noopener noreferrer" class="btn">Read More</a>
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
            v-for="(p, i) in oralPresentations"
            :key="`oral-${i}`"
            class="presentation-card card"
          >
            <h4 class="presentation-card__title">{{ p.title }}</h4>
            <p class="presentation-card__meta">{{ p.event }} · {{ p.date }}</p>
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
            v-for="(p, i) in posterPresentations"
            :key="`poster-${i}`"
            class="presentation-card card"
          >
            <h4 class="presentation-card__title">{{ p.title }}</h4>
            <p class="presentation-card__meta">{{ p.event }} · {{ p.date }}</p>
            <p class="presentation-card__location">{{ p.location }}</p>
            <p class="presentation-card__authors">{{ p.authors }}</p>
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
  image_url: string;
  summary: string;
  link: string;
}

const oralPresentations = ref<Presentation[]>([]);
const posterPresentations = ref<Presentation[]>([]);
const publications = ref<Publication[]>([]);
const visibleCount = ref(1);
const slideWidth = 300;
const gap = 20;

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
    publications.value = Array.isArray(pubData) ? pubData : [];
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
.presentation-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px;
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

.carousel__arrow:hover {
  filter: brightness(1.1);
}

.publication-card {
  flex: 0 0 300px;
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

.publication-card__summary {
  margin: 0;
  font-size: 0.875rem;
  color: var(--muted);
  line-height: 1.5;
  -webkit-line-clamp: 3;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
