<template>
  <nav class="site-nav">
    <div class="container bar">
      <NuxtLink to="/" class="brand">
        <span class="brand__dot" aria-hidden="true" />
        <span class="brand__name">Dave Austin</span>
      </NuxtLink>
      <div class="navlinks">
        <NuxtLink to="/">Home</NuxtLink>
        <a href="/#experience">Experience</a>
        <a href="/#projects">Projects</a>
        <a href="/#skills">Skills</a>
        <a href="/#education">Education</a>
        <a href="/#certifications">Certifications</a>
        <NuxtLink to="/blogs" active-class="active">Blogs</NuxtLink>
        <NuxtLink to="/phd-overview" active-class="active">Physics Career Overview</NuxtLink>
      </div>
    </div>
  </nav>
</template>

<style scoped>
/* Uses global .site-nav, .bar, .brand, .navlinks from main.css */
</style>
