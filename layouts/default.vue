<template>
  <div>
    <SiteNav />
    <slot />
    <footer class="footer container">
      <p>
        Contact: <a href="mailto:austindi1133@gmail.com">austindi1133@gmail.com</a>
        | Phone: +1-(864)-384-9579
        | <a href="https://github.com/austindi" target="_blank" rel="noopener noreferrer">GitHub</a>
        | <a href="https://www.linkedin.com/in/dave-austin-ph-d-616865a9" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      </p>
      <p>© {{ new Date().getFullYear() }} Dave Austin • Built with Nuxt</p>
    </footer>
  </div>
</template>

<script setup lang="ts">
// Default layout: nav + page slot + footer. All pages use this unless they set a different layout.
</script>
