<template>
  <div>
    <header>
      <h1>Home</h1>
      <NavBar />
    </header>
    <section class="main-content">
      <div class="about">
        <h2>About Me</h2>
        <p>
          Hi, I’m Dave Austin, Ph.D., a physicist specializing in computational
          materials science and passionate about exploring the intricate world
          of surface phenomena and catalytic reactions. My work combines
          theoretical insights and advanced modeling techniques to solve
          challenges in nanotechnology and sustainable energy. I’ve had the
          privilege of publishing in renowned journals such as Nature
          Communications and ACS Nano and presenting at international
          conferences like the APS March Meeting. My goal is to advance our
          understanding of material behaviors at the atomic scale and inspire
          others through science and education. Feel free to explore my website
          to learn more about my research, publications, and outreach
          initiatives. Let’s connect and create meaningful impact together!
        </p>
      </div>
      <div class="profile-picture">
        <img src="/images/Dave-Austin.jpeg" alt="Profile Picture" />
      </div>
    </section>

    <section class="publications-section">
      <h2>My Publications</h2>
      <div class="carousel">
        <button class="arrow left-arrow" @click="rotateLeft">&#8592;</button>
        <div class="carousel-wrapper">
          <TransitionGroup name="carousel" tag="div" class="carousel-slides">
            <div
              v-for="(pub, i) in visiblePublications"
              :key="`${pub.title}-${i}`"
              class="publication-card"
            >
              <img :src="pub.image_url" :alt="pub.title" />
              <h3>{{ pub.title }}</h3>
              <p>{{ pub.summary }}</p>
              <a :href="pub.link" target="_blank">Read More</a>
            </div>
          </TransitionGroup>
        </div>
        <button class="arrow right-arrow" @click="rotateRight">&#8594;</button>
      </div>
    </section>

    <footer>
      <p>
        Contact:
        <a href="mailto:austindi1133@gmail.com">austindi1133@gmail.com</a> |
        Phone: +1-(864)-384-9579 |
        <a href="https://github.com/austindi" target="_blank">GitHub</a> |
        <a
          href="https://www.linkedin.com/in/dave-austin-ph-d-616865a9"
          target="_blank"
          >LinkedIn</a
        >
      </p>
    </footer>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

const allPublications = ref([]);
const publications = ref([]); // currently rotated list
const visibleCount = ref(1);

const slideWidth = 300;
const gap = 20;

onMounted(async () => {
  const res = await fetch("/publications.json");
  allPublications.value = await res.json();
  publications.value = [...allPublications.value];
  calculateVisibleCount();
  window.addEventListener("resize", calculateVisibleCount);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", calculateVisibleCount);
});

function calculateVisibleCount() {
  const containerWidth = window.innerWidth;
  visibleCount.value = Math.floor((containerWidth + gap) / (slideWidth + gap));
}

function rotateLeft() {
  const last = publications.value.pop();
  if (last) publications.value.unshift(last);
}

function rotateRight() {
  const first = publications.value.shift();
  if (first) publications.value.push(first);
}

const visiblePublications = computed(() =>
  publications.value.slice(0, visibleCount.value)
);
</script>

<style scoped>
.main-content {
  display: flex;
  flex-wrap: wrap;
  padding: 20px;
  justify-content: center;
  align-items: center;
}

.about {
  flex: 1 1 300px;
  margin: 20px;
}

.about h2 {
  font-size: 24px;
  color: #333;
}

.about p {
  font-size: 16px;
  color: #555;
}

.profile-picture {
  flex: 1 1 300px;
  margin: 20px;
  display: flex;
  justify-content: center;
}

.profile-picture img {
  width: 100%;
  max-width: 300px;
  height: auto;
  display: block;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Publications Section */
.publications-section {
  text-align: center;
  padding: 20px;
  background-color: #f9f9f9;
}

.carousel {
  display: flex;
  align-items: center;
  overflow: hidden;
}

.carousel-wrapper {
  overflow: hidden;
  flex: 1;
}

.carousel-slides {
  display: flex;
  gap: 20px;
}

.carousel-move {
  transition: transform 0.5s ease;
}

.carousel-enter-active,
.carousel-leave-active,
.carousel-enter-from,
.carousel-leave-to {
  transition: none;
  opacity: 1;
  transform: none;
}
.publication-card {
  flex: 0 0 300px;
  background: white;
  padding: 10px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.publication-card img {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
}

.publication-card h3 {
  font-size: 18px;
  margin: 10px 0;
}

.publication-card p {
  font-size: 14px;
  color: #555;
}

.publication-card a {
  color: #0078d7;
  text-decoration: none;
  font-weight: bold;
}

.publication-card a:hover {
  text-decoration: underline;
}

.arrow {
  width: 40px;
  height: 40px;
  font-size: 20px;
  background: #0078d4;
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  z-index: 1;
}

.left-arrow {
  left: 10px;
}

.right-arrow {
  right: 10px;
}

.arrow:hover {
  background-color: #005bb5;
}
/* Responsive Adjustments */
@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
    justify-content: center;
  }

  .main-content {
    flex-direction: column;
  }
}
/* For small screens (e.g., mobile) */
@media (max-width: 600px) {
  .profile-picture img {
    max-width: 200px; /* Reduce the max width for smaller screens */
    max-height: 133px; /* Adjust height proportionally */
    height: auto; /* Ensure aspect ratio is maintained */
  }
}

@media (max-width: 400px) {
  .profile-picture img {
    max-width: 150px; /* Further reduce the max width for extra-small screens */
    max-height: 100px; /* Adjust height proportionally */
    height: auto; /* Ensure aspect ratio is maintained */
  }
}
</style>
