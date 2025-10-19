// Image Slider for Passions
let images = [];
let currentImageIndex = 0;
const sliderImage = document.getElementById('slider-image');

fetch('passions.json')
    .then(response => response.json())
    .then(data => {
        images = data.images; // Assume the JSON contains an array of image URLs
        if (images.length > 0) {
            sliderImage.src = images[currentImageIndex]; // Load the first image
        }
    })
    .catch(error => console.error('Error loading images:', error));

document.getElementById('prev-btn').addEventListener('click', () => {
    if (images.length > 0) {
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        sliderImage.src = images[currentImageIndex];
    }
});

document.getElementById('next-btn').addEventListener('click', () => {
    if (images.length > 0) {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        sliderImage.src = images[currentImageIndex];
    }
});

