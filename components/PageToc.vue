<template>
  <aside class="toc" aria-label="Table of contents">
    <nav class="toc__nav">
      <div class="toc__title">On this page</div>
      <ul class="toc__list">
        <li v-for="item in items" :key="item.id" class="toc__item">
          <a
            :href="`#${item.id}`"
            class="toc__link"
            :class="{ 'toc__link--active': activeId === item.id }"
          >
            {{ item.label }}
          </a>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script setup lang="ts">
const props = defineProps<{
  items: { id: string; label: string }[];
}>();

const activeId = ref<string | null>(null);
let observer: IntersectionObserver | null = null;

onMounted(() => {
  if (typeof window === "undefined") return;
  const ids = props.items.map((i) => i.id);
  observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          activeId.value = entry.target.id;
        }
      }
    },
    {
      rootMargin: "-80px 0px -55% 0px",
      threshold: 0,
    }
  );
  ids.forEach((id) => {
    const el = document.getElementById(id);
    if (el) observer?.observe(el);
  });
});

onBeforeUnmount(() => {
  observer?.disconnect();
});
</script>

<style scoped>
.toc {
  position: sticky;
  top: 88px;
  align-self: start;
  display: flex;
  justify-content: center;
  width: 100%;
}

.toc__nav {
  border-left: 4px solid var(--border);
  padding: 28px 0 28px 28px;
  min-width: 260px;
}

.toc__title {
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 20px;
}

.toc__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.toc__item {
  margin-bottom: 16px;
}

.toc__item:last-child {
  margin-bottom: 0;
}

.toc__link {
  font-size: 1.05rem;
  line-height: 1.35;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.15s ease;
  display: block;
}

.toc__link:hover {
  color: var(--accent);
}

.toc__link--active {
  color: var(--accent);
  font-weight: 600;
}

@media (max-width: 1020px) {
  .toc {
    display: none;
  }
}
</style>
