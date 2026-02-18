<template>
  <div class="section blogs-page">
    <div class="container">
      <BackButton />
      <h1 class="h1">404</h1>
      <p class="section__desc">Blogs coming soon.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: "Blogs — Dave Austin",
  description: "Blog posts",
});
</script>

<style scoped>
.blogs-page :deep(.back-btn) {
  margin-bottom: 20px;
  display: inline-block;
}
</style>
