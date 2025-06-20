document.addEventListener('DOMContentLoaded', function() {
    // Animate timeline items on scroll
    const animateTimeline = function() {
        const timelineItems = document.querySelectorAll('.timeline-item');
        
        timelineItems.forEach(item => {
            const itemPosition = item.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;
            
            if (itemPosition < screenPosition) {
                item.querySelector('.timeline-content').classList.add('animated');
            }
        });
    };

    // Initial check
    animateTimeline();
    
    // Check on scroll
    window.addEventListener('scroll', animateTimeline);

    // Skill progress bars animation
    const animateSkills = function() {
        const skills = document.querySelectorAll('.skill-item');
        
        skills.forEach(skill => {
            const skillPosition = skill.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (skillPosition < screenPosition) {
                const progressBar = skill.querySelector('.progress-fill');
                const level = progressBar.getAttribute('data-level');
                progressBar.style.width = level;
                skill.classList.add('animated');
            }
        });
    };

    // Initial check
    animateSkills();
    
    // Check on scroll
    window.addEventListener('scroll', animateSkills);

    // Certification hover effects
    const certifications = document.querySelectorAll('.certification-card');
    certifications.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.certification-image img').style.transform = 'scale(1.05)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.certification-image img').style.transform = 'scale(1)';
        });
    });

    // Toggle view for experience details
    const experienceToggles = document.querySelectorAll('.experience-toggle');
    experienceToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const details = this.nextElementSibling;
            details.classList.toggle('show');
            this.querySelector('i').classList.toggle('fa-chevron-down');
            this.querySelector('i').classList.toggle('fa-chevron-up');
        });
    });
});