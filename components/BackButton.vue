<template>
  <NuxtLink to="/" class="back-btn">
    ← Back to home
  </NuxtLink>
</template>

<script setup lang="ts">
</script>

<style scoped>
.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 18px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text);
  background: transparent;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  text-decoration: none;
  transition: background 0.15s ease, border-color 0.15s ease;
}

.back-btn:hover {
  background: color-mix(in lab, var(--accent) 15%, transparent);
  border-color: color-mix(in lab, var(--accent) 40%, transparent);
  text-decoration: none;
}
</style>
