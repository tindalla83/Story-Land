// Story Homes Land — site behaviour
(function () {
  // Header: solid background once the page scrolls
  var header = document.querySelector('.site-header');
  if (header && !header.classList.contains('site-header--solid')) {
    var onScroll = function () { header.classList.toggle('is-solid', window.scrollY > 40); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mobile navigation
  var nav = document.querySelector('.nav');
  var toggle = document.querySelector('.nav__toggle');
  if (nav && toggle) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open);
    });
  }

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // Count-up statistics
  var counters = document.querySelectorAll('[data-count]');
  var animate = function (el) {
    var target = parseFloat(el.dataset.count);
    var suffix = el.dataset.suffix || '';
    var start = performance.now();
    var dur = 1600;
    var tick = function (now) {
      var p = Math.min((now - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('en-GB') + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animate(e.target); co.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { co.observe(el); });
  }

  // Testimonial slider
  document.querySelectorAll('.slider').forEach(function (slider) {
    var slides = slider.querySelectorAll('.slide');
    var dots = slider.querySelector('.slider__dots');
    if (!slides.length || !dots) return;
    var current = 0;
    var go = function (i) {
      slides[current].classList.remove('is-active');
      dots.children[current].classList.remove('is-active');
      current = i;
      slides[current].classList.add('is-active');
      dots.children[current].classList.add('is-active');
    };
    slides.forEach(function (_, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Show testimonial ' + (i + 1));
      b.addEventListener('click', function () { go(i); });
      dots.appendChild(b);
    });
    slides[0].classList.add('is-active');
    dots.children[0].classList.add('is-active');
    setInterval(function () { go((current + 1) % slides.length); }, 7000);
  });

  // Project filters
  var filters = document.querySelectorAll('.filter');
  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filters.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      var f = btn.dataset.filter;
      document.querySelectorAll('[data-region]').forEach(function (card) {
        card.hidden = f !== 'all' && card.dataset.region !== f;
      });
    });
  });

  // Enquiry forms (front-end only — wire to a backend/CRM to receive submissions)
  document.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      form.classList.add('is-sent');
    });
  });

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
