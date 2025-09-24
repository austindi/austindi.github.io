<template>
  <nav class="navbar">
    <NuxtLink to="/" class="nav-button">Home</NuxtLink>
    <NuxtLink to="/passion" class="nav-button">About Me</NuxtLink>
    <NuxtLink to="/projects" class="nav-button">Projects</NuxtLink>
    <NuxtLink to="/presentations" class="nav-button">Presentations</NuxtLink>
    <NuxtLink to="/skills" class="nav-button">Skills</NuxtLink>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #2d2d2d; /* dark background */
  padding: 1.5rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.nav-button {
  background-color: #0d6efd; /* Bootstrap-like blue */
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: background-color 0.3s ease;
  margin: 5px;
}

.nav-button:hover {
  background-color: #0b5ed7;
}
@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
