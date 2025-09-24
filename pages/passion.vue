<template>
  <div>
    <header>
      <h1>About Me</h1>
    </header>
    <NavBar />
    <main>
      <section>
        <h2>Education</h2>
        <p>
          I earned my Ph.D. in Physics from the University of Central Florida
          (UCF) in August 2024. My doctoral research, under the guidance of Dr.
          Talat Rahman, focused on First Principles Studies of Nano-scale
          Phenomena at Surfaces: From Characteristics of Single Atom Catalysts
          to Molecular Structure Formation. Prior to this, I completed my M.S.
          in Physics at UCF in May 2022. I began my academic journey with a B.S.
          in Physics from the College of Charleston in May 2018
        </p>
      </section>

      <section>
        <h2>Research Experience</h2>
        <p>
          During my time as a graduate research assistant at UCF from 2018 to
          2024, I explored the theoretical underpinnings of surface phenomena,
          focusing on the unique electronic structures that emerge from the
          adsorption of atoms and molecules. My work included investigations
          into the physical and chemical properties of individually dispersed
          metal atom sites on oxide surfaces, with applications as
          cost-effective catalysts for critical chemical reactions. I also
          studied hybrid organic-inorganic interfaces to understand electron
          confinement and its implications for nanostructure engineering. Key
          projects involved elucidating water-gas shift reaction mechanisms,
          analyzing bi-stable molecular configurations, and uncovering a unique
          Kagome lattice pattern in molecular layers on Au(111). My research was
          generously supported by the National Science Foundation and supervised
          by Dr. Talat Rahman.
        </p>
        <p>
          As an undergraduate research assistant at the College of Charleston
          (2017–2018), I developed computational models to study phase response
          curves for neurons and networks, leveraging numerical solvers for the
          Hodgkin-Huxley model to simulate connections among thousands of
          neurons. This work explored phase locking and resetting of neural
          firing patterns and introduced generalized methods for multi-stimuli
          phase resetting. This research, funded by an NSF Career Award
          Fellowship, was conducted under the mentorship of Dr. Sorinel Oprisan.
        </p>
      </section>

      <section>
        <h2>Achievements</h2>
        <p>
          My academic journey is marked by numerous accolades and contributions.
          I was honored as the UCF Physics Department Student of the Year
          (2022–2023) and received the AVS NSTD Graduate Student Award in 2024.
          I also earned the Resolv Cluster International Research Fellowship,
          enabling me to conduct reseach in Germany in 2023, and was nominated
          for the UCF Order of the Pegasus in 2024. I have co-authored several
          peer-reviewed publications in journals such as Journal of Catalysis,
          ACS Nano, and Nature Communications. My published work spans topics
          including single-atom catalysts, molecular assembly on surfaces, and
          the electronic coupling at metal/organic interfaces. Additionally, I
          have delivered numerous oral and poster presentations at prestigious
          conferences, including the AVS International Symposium, the APS March
          Meeting, and the Gordon Research Conferences, showcasing my research
          findings to the scientific community.
        </p>
      </section>

      <section>
        <h2>Mentoring and Tutoring</h2>
        <p>
          I have a strong passion for mentoring and teaching, which has been
          evident throughout my academic career. I have mentored graduate
          students in research methodology, data analysis, and project
          execution, fostering their scientif ic and professional growth.
          Additionally, I guided high school students on science fair projects,
          sparking their in terest in STEM fields. As part of my mentorship
          responsibilities, I held bi-weekly meetings with first-year Ph.D.
          students to help them navigate academic challenges and manage the
          stresses of graduate school. As a teaching assistant at UCF, I led
          laboratory sessions for Introductory Physics, providing hands-on
          guidance to students and evaluating their performance. I also have
          extensive tutoring experience across various educational levels,
          ranging from middle school to graduate studies. Subjects I have
          tutored include mathematics (from algebra to a dvanced calculus and
          linear algebra), introductory and advanced physics, and other sciences
          such as chemistry and b iology. My ability to simplify complex
          concepts has been instrumental in helping students excel academically.
        </p>
      </section>

      <section>
        <h2>Passions</h2>
        <section>
          <h3>Basketball: A Lifelong Love</h3>

          <p>
            I have been passionate about basketball since I was 12 years old. I
            played AAU basketball for the Sp artanburg Bucks for five seasons
            and participated in local church leagues. In high school, I was a
            team manager for both varsity and JV basketball teams, as well as a
            member of the AV team, broadcasting games. I also played intram ural
            basketball in college for three years and continue to play at my
            local gym.
          </p>
        </section>

        <section>
          <h3>Music: A Harmonious Journey</h3>
          <p>
            Music has been a cornerstone of my life. I played the cello from 5th
            to 12th grade and performed in my high school’s symphony orchestra.
            I joined the marching band in 11th grade, playing the xylophone and
            marimba in the pit, and moved to the drumline as a bass drummer in
            12th grade. I also participated in the percussion ensemble, took
            piano lessons in college, and recently started drum lessons and
            self-teaching the guitar.
          </p>
        </section>

        <section>
          <h3>Billiards: Precision and Strategy</h3>
          <p>
            Since 2018, I’ve been passionate about billiards. As an APA member,
            I enjoy the challenge of strateg y and precision in pool. Although
            I’m an amateur, billiards has become a fulfilling part of my life,
            offering both relaxation and competition.
          </p>
        </section>
      </section>

      <div class="page-wrapper">
        <section class="image-slider">
          <img :src="currentImage" alt="My Passion Images" />
        </section>
        <div class="controls">
          <button @click="prevImage">Previous</button>
          <button @click="nextImage">Next</button>
        </div>
      </div>
    </main>

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
import { onMounted, ref } from "vue";

const images = ref([]);
const currentIndex = ref(0);
const currentImage = ref("placeholder.jpg");

const fetchImages = async () => {
  try {
    const res = await fetch("/passions.json");
    const data = await res.json();
    images.value = data.images;
    if (images.value.length > 0) {
      currentImage.value = images.value[currentIndex.value];
    }
  } catch (err) {
    console.error("Error loading images:", err);
  }
};

function nextImage() {
  if (images.value.length > 0) {
    currentIndex.value = (currentIndex.value + 1) % images.value.length;
    currentImage.value = images.value[currentIndex.value];
  }
}

function prevImage() {
  if (images.value.length > 0) {
    currentIndex.value =
      (currentIndex.value - 1 + images.value.length) % images.value.length;
    currentImage.value = images.value[currentIndex.value];
  }
}

onMounted(fetchImages);
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}
header {
  background: #333;
  color: #fff;
  padding: 1em 0;
  text-align: center;
}
/*        .button-bar {
            display: flex;
            justify-content: center;
            padding: 10px 0;
            background-color: #444;
        }
        .button-bar button {
            padding: 10px 15px;
            margin: 0 5px;
            font-size: 16px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .button-bar button:hover {
            background-color: #555;
        }*/
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #333;
  padding: 10px 0;
}

/* Footer Styles */
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

.navbar button {
  background-color: #0078d7;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.navbar button:hover {
  background-color: #005bb5;
}
main {
  padding: 20px;
}
/*.image-slider {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }*/

.image-slider {
  display: flex; /* Flexbox for centering */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  margin: 10px auto; /* Ensure the element is horizontally centered */
  width: 60%; /* Set the desired width */
  max-width: 500px; /* Optional maximum width */
  border: 2px solid #ccc; /* Optional: Visualize the container */
  padding: 10px; /* Adjust inner spacing if necessary */
  box-sizing: border-box; /* Include padding/border in width calculation */
}

.image-slider img {
  width: 100%; /* Make the image fill the container */
  max-height: 500px; /* Prevent the image from growing too tall */
  border: 2px solid #333; /* Optional border for the image */
  border-radius: 10px; /* Rounded corners */
}

.page-wrapper {
  flex-direction: column;
  display: flex; /* Flexbox for centering */
  justify-content: center; /* Horizontal centering */
  align-items: center; /* Vertical centering */
  height: 100vh; /* Full viewport height */
  gap: 5px;
}

.controls {
  gap: 10px; /* Space between buttons */
  display: flex; /* Flexbox for button alignment */
  justify-content: center;
}
.controls button {
  padding: 5px 15px;
  font-size: 16px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.controls button:hover {
  background-color: #555;
}
/* Responsive Adjustments */
@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
    justify-content: center;
  }

  .navbar button {
    margin: 5px;
  }

  .main-content {
    flex-direction: column;
  }
}
/* Responsive Adjustments */
@media (max-width: 768px) {
  .page-wrapper {
    gap: 8px; /* Reduce spacing between image and buttons */
  }

  .controls button {
    font-size: 14px; /* Reduce button text size */
    padding: 5px 10px; /* Adjust button padding */
  }
}

@media (max-width: 480px) {
  .page-wraper {
    gap: 5px; /* Further reduce spacing */
  }

  .controls button {
    font-size: 12px; /* Smaller button text */
    padding: 4px 8px; /* Adjust button size for smaller screens */
  }
}
</style>
