// Keyboard nav: each nav link declares its own letter via data-key.
// Ignores keystrokes while typing, and anything with a modifier held.
(function () {
  var links = {};
  document.querySelectorAll(".nav-link[data-key]").forEach(function (a) {
    links[a.dataset.key] = a.getAttribute("href");
  });

  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var el = document.activeElement;
    if (el && (el.isContentEditable || /^(input|textarea|select)$/i.test(el.tagName))) return;

    var href = links[e.key.toLowerCase()];
    if (href && href !== window.location.pathname) {
      window.location.href = href;
    }
  });
})();
