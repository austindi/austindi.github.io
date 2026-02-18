<template>
  <article class="project card">
    <div class="project__header">
      <h3 class="project__title">
        <NuxtLink v-if="project.link" :to="project.link">{{ project.title }}</NuxtLink>
        <span v-else>{{ project.title }}</span>
      </h3>
      <span v-if="project.inProgress" class="project__status">In progress</span>
    </div>
    <p class="project__tagline">{{ project.tagline }}</p>
    <div v-if="project.stack?.length" class="project__tools">
      <span class="project__tools-label">Tools</span>
      <div class="stack">
        <span v-for="s in project.stack" :key="s" class="badge">{{ s }}</span>
      </div>
    </div>
    <div v-if="project.link" class="cta">
      <NuxtLink :to="project.link" class="btn">Learn more</NuxtLink>
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
    inProgress?: boolean
  }
}>()
</script>

<style scoped>
.project__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}
.project__title {
  margin: 0;
  flex: 1;
  min-width: 0;
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.3;
  color: var(--text);
}
.project__title a {
  color: inherit;
  text-decoration: none;
}
.project__status {
  flex-shrink: 0;
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--accent-2);
  background: color-mix(in lab, var(--accent) 18%, transparent);
  border: 1px solid color-mix(in lab, var(--accent) 40%, transparent);
  padding: 4px 8px;
  border-radius: 6px;
}
.project__tagline {
  line-height: 1.55;
}
.project__tools {
  margin-top: 4px;
}
.project__tools-label {
  display: block;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 8px;
}
.cta {
  margin-top: 14px;
}
</style>
