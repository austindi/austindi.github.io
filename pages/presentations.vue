<template>
  <div>
    <header>
      <h1>Presentation</h1>
    </header>

    <nav class="navbar">
      <NuxtLink to="/">Home</NuxtLink>
      <NuxtLink to="/passion">About Me</NuxtLink>
      <NuxtLink to="/projects">Projects</NuxtLink>
      <NuxtLink to="/presentations">Presentations</NuxtLink>
      <NuxtLink to="/skills">Skills</NuxtLink>
    </nav>

    <main>
      <section>
        <h1>My Presentations</h1>

        <div class="presentation-section">
          <h2>Oral Presentations</h2>
          <div class="presentation-list">
            <div
              class="presentation-item"
              v-for="(presentation, i) in oralPresentations"
              :key="`oral-${i}`"
            >
              <h3>{{ presentation.title }}</h3>
              <p>Event: {{ presentation.event }}</p>
              <p>Date: {{ presentation.date }}</p>
              <span>Location: {{ presentation.location }}</span>
              <p>Authors: {{ presentation.authors }}</p>
            </div>
          </div>
        </div>

        <div class="presentation-section">
          <h2>Poster Presentations</h2>
          <div class="presentation-list">
            <div
              class="presentation-item"
              v-for="(presentation, i) in posterPresentations"
              :key="`poster-${i}`"
            >
              <h3>{{ presentation.title }}</h3>
              <p>Event: {{ presentation.event }}</p>
              <p>Date: {{ presentation.date }}</p>
              <span>Location: {{ presentation.location }}</span>
              <p>Authors: {{ presentation.authors }}</p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <footer>
      <p>
        Contact: <a href="mailto:austindi1133@gmail.com">austindi1133@gmail.com</a> |
        Phone: +1-(864)-384-9579 |
        <a href="https://github.com/austindi" target="_blank">GitHub</a> |
        <a href="https://www.linkedin.com/in/dave-austin-ph-d-616865a9" target="_blank">LinkedIn</a>
      </p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const oralPresentations = ref([])
const posterPresentations = ref([])

onMounted(async () => {
  try {
    const res = await fetch('/presentations.json')
    const data = await res.json()
    oralPresentations.value = data.oral
    posterPresentations.value = data.poster
  } catch (err) {
    console.error('Error loading presentations:', err)
  }
})
</script>

<style scoped>
header {
  background: #333;
  color: #fff;
  padding: 1em 0;
  text-align: center;
}
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #333;
  padding: 10px 0;
}
.navbar a {
  background-color: #0078d7;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  font-size: 16px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}
.navbar a:hover {
  background-color: #005bb5;
}
footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 10px 0;
  font-size: 14px;
}
footer a {
  color: #0078d7;
  text-decoration: none;
  margin: 0 10px;
}
footer a:hover {
  text-decoration: underline;
}
.presentation-section {
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f9f9f9;
}
.presentation-section h2 {
  font-size: 24px;
  color: #333;
  margin-bottom: 15px;
}
.presentation-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.presentation-item {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  background-color: #fff;
}
.presentation-item h3 {
  margin: 0;
  font-size: 20px;
  color: #0078d7;
}
.presentation-item p {
  margin: 5px 0;
  font-size: 16px;
  color: #555;
}
.presentation-item span {
  font-size: 14px;
  color: #0078d7;
  font-weight: bold;
}
@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
    justify-content: center;
  }
  .navbar a {
    margin: 5px;
  }
}
</style>
