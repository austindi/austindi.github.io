 // Publications Carousel
 let currentIndex = 0;

 async function loadPublications() {
     try {
         const response = await fetch('publications.json');
         const publications = await response.json();

         const container = document.getElementById('publications-container');
         container.innerHTML = ''; // Clear previous content

         publications.forEach(pub => {
             const publicationCard = `
                 <div class="publication-card">
                     <img src="${pub.image_url}" alt="${pub.title}">
                     <h3>${pub.title}</h3>
                     <p>${pub.summary}</p>
                     <a href="${pub.link}" target="_blank">Read More</a>
                 </div>
             `;
             container.innerHTML += publicationCard;
         });

         updateCarousel();
     } catch (error) {
         console.error('Error loading publications:', error);
     }
 }

 function updateCarousel() {
     const container = document.getElementById('publications-container');
     const totalSlides = document.querySelectorAll('.publication-card').length;
     const offset = -currentIndex * 320; // Adjust based on card width + gap
     container.style.transform = `translateX(${offset}px)`;

     document.querySelector('.left-arrow').disabled = currentIndex === 0;
     document.querySelector('.right-arrow').disabled = currentIndex === totalSlides - 1;
 }

 function nextSlide() {
     const totalSlides = document.querySelectorAll('.publication-card').length;
     if (currentIndex < totalSlides - 1) {
         currentIndex++;
         updateCarousel();
     }
 }

 function prevSlide() {
     if (currentIndex > 0) {
         currentIndex--;
         updateCarousel();
     }
 }
