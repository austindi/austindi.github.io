<template>
  <div class="error-page">
    <div class="error-page__inner">
      <h1 class="error-page__title">{{ is404 ? 'Page not found' : 'Something went wrong' }}</h1>
      <p class="error-page__message">
        {{ is404
          ? "The page you're looking for doesn't exist or has been moved."
          : error?.message || 'An unexpected error occurred.' }}
      </p>
      <button type="button" class="btn btn--primary" @click="handleError">Go home</button>
    </div>
  </div>
</template>

<script setup lang="ts">
const error = useError()

const is404 = computed(() => error.value?.statusCode === 404 || error.value?.status === 404)

function handleError() {
  clearError({ redirect: '/' })
}
</script>

<style scoped>
.error-page {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.error-page__inner {
  text-align: center;
  max-width: 420px;
}

.error-page__title {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 12px;
}

.error-page__message {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  margin: 0 0 24px;
}
</style>
