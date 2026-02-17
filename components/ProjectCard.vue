<template>
  <article class="project card">
    <h3 class="project__title">
      <NuxtLink v-if="project.link" :to="project.link">{{ project.title }}</NuxtLink>
      <span v-else>{{ project.title }}</span>
    </h3>
    <p class="project__tagline">{{ project.tagline }}</p>
    <div v-if="project.stack?.length" class="stack">
      <span v-for="s in project.stack" :key="s" class="badge">{{ s }}</span>
    </div>
    <div v-if="project.github" class="cta">
      <a :href="project.github" target="_blank" rel="noopener noreferrer" class="btn">GitHub</a>
    </div>
  </article>
</template>

<script setup lang="ts">
defineProps<{
  project: {
    title: string
    tagline?: string
    stack?: string[]
    link?: string
    github?: string
  }
}>()
</script>

<style scoped>
/* Uses global .project, .card, .project__tagline, .stack, .badge, .cta, .btn from main.css */
.project__title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 700;
}
.project__title a {
  color: inherit;
}
</style>
