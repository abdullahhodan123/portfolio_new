document.addEventListener("DOMContentLoaded", function () {
  var sidebar = document.querySelector(".sidebar");
  var toggle = document.querySelector(".sidebar-toggle");

  if (toggle && sidebar) {
    toggle.addEventListener("click", function () {
      sidebar.classList.toggle("is-open");
    });
  }

  /* close mobile menu + smooth-scroll on nav click */
  document.querySelectorAll(".sidebar-nav a").forEach(function (link) {
    link.addEventListener("click", function () {
      if (sidebar) sidebar.classList.remove("is-open");
    });
  });

  /* scroll-spy: highlight active section in sidebar nav */
  var navLinks = document.querySelectorAll(".sidebar-nav a");
  var sections = Array.from(navLinks)
    .map(function (link) {
      var id = link.getAttribute("href").replace("#", "");
      return document.getElementById(id);
    })
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var link = document.querySelector('.sidebar-nav a[href="#' + entry.target.id + '"]');
          if (!link) return;
          if (entry.isIntersecting) {
            navLinks.forEach(function (l) { l.classList.remove("is-active"); });
            link.classList.add("is-active");
          }
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    sections.forEach(function (section) { observer.observe(section); });
  }

  /* skill meters: animate the fill in once visible */
  var meters = document.querySelectorAll(".meter-fill");
  if ("IntersectionObserver" in window && meters.length) {
    var meterObserver = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var target = entry.target.getAttribute("data-value") + "%";
            entry.target.style.width = target;
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    meters.forEach(function (m) {
      m.style.width = "0%";
      meterObserver.observe(m);
    });
  }
});