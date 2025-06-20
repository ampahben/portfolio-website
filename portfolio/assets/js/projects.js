document.addEventListener('DOMContentLoaded', function() {
    // Initialize all Swiper sliders
    const initSwipers = function() {
        // Cloud Projects Slider
        const cloudSwiper = new Swiper('.cloud-projects-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                },
                1024: {
                    slidesPerView: 3,
                }
            }
        });

        // Cybersecurity Projects Slider
        const cyberSwiper = new Swiper('.cyber-projects-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                }
            }
        });

        // Web Projects Slider
        const webSwiper = new Swiper('.web-projects-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                }
            }
        });
    };

    // Initialize Swiper only if elements exist
    if (document.querySelector('.swiper')) {
        // Load Swiper library dynamically if not already loaded
        if (typeof Swiper === 'undefined') {
            const swiperScript = document.createElement('script');
            swiperScript.src = 'https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.js';
            swiperScript.onload = initSwipers;
            document.head.appendChild(swiperScript);
        } else {
            initSwipers();
        }
    }

    // Project filtering functionality
    const filterButtons = document.querySelectorAll('.project-filter button');
    if (filterButtons.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                
                // Add active class to clicked button
                this.classList.add('active');
                
                // Get filter value
                const filterValue = this.getAttribute('data-filter');
                
                // Filter projects
                const projects = document.querySelectorAll('.project-card');
                projects.forEach(project => {
                    if (filterValue === 'all' || project.getAttribute('data-category') === filterValue) {
                        project.style.display = 'block';
                    } else {
                        project.style.display = 'none';
                    }
                });
            });
        });
    }

    // Project card hover effects
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.project-info').style.transform = 'translateY(0)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.project-info').style.transform = 'translateY(100%)';
        });
    });
});