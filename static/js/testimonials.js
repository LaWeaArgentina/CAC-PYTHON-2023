const testimonialContainer = document.querySelector('.testimonial-slider');
const testimonialText = document.querySelector('#testimonial-text');
const testimonialAuthor = document.querySelector('#testimonial-author');

const apiUrl = 'https://raw.githubusercontent.com/annituss/fake-testimonials/main/es/testimonials.json'; // Updated API URL

let currentIndex = 0;
let testimonials = [];

// Fetch testimonials from the API
function fetchTestimonials() {
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      testimonials = data;
      displayTestimonial(currentIndex);
      // Start autoplay after fetching testimonials
      startAutoplay();
    })
    .catch((error) => console.error('Error fetching testimonials: ', error));
}

// Display the current testimonial
function displayTestimonial(index) {
  if (testimonials.length > 0) {
    const testimonial = testimonials[index];
    testimonialText.textContent = testimonial.comment;
    testimonialAuthor.textContent = testimonial.name + ' - ' + testimonial.company;
    testimonialContainer.style.display = 'block';
  } else {
    testimonialText.textContent = 'No testimonials available.';
    testimonialAuthor.textContent = '';
  }
}

// Autoplay variables
let intervalId;
const autoplayInterval = 7000; // 7 seconds

// Start autoplay
function startAutoplay() {
  intervalId = setInterval(() => {
    currentIndex = (currentIndex + 1) % testimonials.length;
    displayTestimonial(currentIndex);
  }, autoplayInterval);
}

// Initialize the slider
fetchTestimonials();
