(() => {
  const header = document.querySelector('.tech-header');
  const revealTargets = document.querySelectorAll('.ai-intro,.assistant-card,.skill-panel,.skill-detail,.work-card,.timeline-item,.journal-card,.live-card,.tech-section-head,.tech-actions');

  const onScroll = () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 18);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if ('IntersectionObserver' in window) {
    revealTargets.forEach((el) => el.classList.add('reveal-v11'));
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px' });
    revealTargets.forEach((el) => observer.observe(el));
  }
})();
