<template>
  <div class="photos-page">
    <div class="container">
      <header class="photos-page__head">
        <BackButton />
        <h1 class="photos-page__title">Gallery</h1>
        <p class="section__desc">A few pictures from work, travel, and life.</p>
      </header>
      <div v-if="images.length" class="photos-grid">
        <div
          v-for="(src, i) in images"
          :key="i"
          class="photos-grid__item"
        >
          <img
            :src="src"
            :alt="`Photo ${i + 1}`"
            class="photos-grid__img"
            loading="lazy"
          />
        </div>
      </div>
      <p v-else class="section__desc">Loading…</p>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Photos — Dave Austin",
  description: "Photos of Dave Austin.",
});

const config = useRuntimeConfig();
const base = (config.app?.baseURL ?? "/").replace(/\/$/, "") || "";
const images = ref<string[]>([]);

onMounted(async () => {
  try {
    const res = await fetch(`${base}/images/list.json`);
    if (!res.ok) return;
    const list: string[] = await res.json();
    images.value = list.map((name) => `${base}/images/${encodeURIComponent(name)}`);
  } catch {
    images.value = [];
  }
});
</script>

<style scoped>
.photos-page {
  padding: 32px 0 48px;
}

.photos-page__head {
  margin-bottom: 32px;
}

.photos-page__title {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 8px;
}

.photos-page__head :deep(.back-btn) {
  margin-bottom: 20px;
  display: inline-block;
}

.photos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
}

.photos-grid__item {
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--panel);
  border: 1px solid var(--border);
}

.photos-grid__img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  display: block;
}
</style>
