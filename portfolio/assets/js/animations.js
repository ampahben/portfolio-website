document.addEventListener('DOMContentLoaded', function() {
    // Animate elements when they come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animated-text, [data-aos]');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (elementPosition < screenPosition) {
                element.classList.add('aos-animate');
            }
        });
    };

    // Initial check
    animateOnScroll();
    
    // Check on scroll
    window.addEventListener('scroll', animateOnScroll);

    // Hero section text animation
    const heroTexts = document.querySelectorAll('.hero h1, .hero h2, .hero p, .hero-buttons');
    heroTexts.forEach((text, index) => {
        text.style.animationDelay = `${index * 0.2 + 0.2}s`;
    });

    // Pulse animation for call-to-action elements
    const pulseElements = document.querySelectorAll('.btn-primary, .hero-image');
    pulseElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            el.style.animation = 'pulse 1.5s infinite';
        });
        
        el.addEventListener('mouseleave', () => {
            el.style.animation = '';
        });
    });

    // Parallax effect for hero image
    const heroImage = document.querySelector('.hero-image img');
    if (heroImage) {
        window.addEventListener('scroll', function() {
            const scrollPosition = window.pageYOffset;
            heroImage.style.transform = `translateY(${scrollPosition * 0.2}px)`;
        });
    }
});