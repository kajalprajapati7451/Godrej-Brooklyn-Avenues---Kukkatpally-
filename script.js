// ==========================================
// GODREJ BROOKLYN AVENUES - MAIN SCRIPT
// ==========================================

document.addEventListener('DOMContentLoaded', () => {

    // 1. Update Footer Year
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // 2. Navbar Scroll Effect
    const navbar = document.querySelector('.premium-nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Scroll to Top Button Visibility
    const scrollToTopBtn = document.getElementById('scrollToTop');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollToTopBtn.classList.add('show');
        } else {
            scrollToTopBtn.classList.remove('show');
        }
    });

    // 4. Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Close mobile menu if open
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                    if (bsCollapse) {
                        bsCollapse.hide();
                    }
                }
            }
        });
    });

    // 5. Reveal Animations on Scroll
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const elementVisible = 100;

        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('active');
            }
        });
    };

    // Initial check
    revealOnScroll();
    
    // Add scroll listener for animations
    window.addEventListener('scroll', revealOnScroll);

    // 6. Form Submissions (Mock handling)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Mock success message
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.textContent;
            
            btn.textContent = 'Request Received!';
            btn.classList.replace('btn-gradient', 'btn-success');
            btn.disabled = true;
            
            setTimeout(() => {
                btn.textContent = originalText;
                btn.classList.replace('btn-success', 'btn-gradient');
                btn.disabled = false;
                form.reset();
            }, 3000);
        });
    });

});
