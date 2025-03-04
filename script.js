// Scroll Animations
const elements = document.querySelectorAll('.fade-in, .slide-in');
const options = {
  threshold: 0.5
};

const handleIntersection = (entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add(entry.target.classList.contains('fade-in') ? 'fade-in' : 'slide-in');
      observer.unobserve(entry.target);
    }
  });
};

const observer = new IntersectionObserver(handleIntersection, options);
elements.forEach(element => {
  observer.observe(element);
});

// Initialize Vanilla Tilt
VanillaTilt.init(document.querySelectorAll('.tilt'), {
  max: 15,
  speed: 400
});


window.onload = function() {
    // Add the fade-in class to the header
    document.querySelector('header').classList.add('fade-in');
    
    // Fade-in content after header fade
    setTimeout(function() {
      document.querySelector('.hero h1').classList.add('fade-in');
      document.querySelector('.hero p').classList.add('fade-in');
      document.querySelector('.cta-btn').classList.add('slide-in');
    }, 1000); // Wait a bit before fading in content
  };
  