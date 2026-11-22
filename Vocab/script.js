// JavaScript for text fade-in effect on scroll
window.addEventListener('scroll', function() {
    const contentItems = document.querySelectorAll('.main-content p, .main-content h2, .main-content ul');
    contentItems.forEach(item => {
        const rect = item.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            item.classList.add('visible');
        } else {
            item.classList.remove('visible');
        }
    });
});
