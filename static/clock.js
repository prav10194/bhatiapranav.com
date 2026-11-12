/* clock.js — the time where pranav is, not where you are. */
(function clock() {
  const nodes = document.querySelectorAll("[data-clock]");
  if (!nodes.length) return;

  const fmt = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Chicago",
    hour: "numeric",
    minute: "2-digit",
    hour12: true,
  });

  function tick() {
    const now = new Date();
    // some engines use a narrow no-break space before am/pm
    const text = fmt.format(now).replace(/ /g, " ").toLowerCase();
    nodes.forEach(function (node) {
      node.textContent = text;
      node.setAttribute("datetime", now.toISOString());
    });
  }

  tick();
  // land on the top of the next minute, then tick once a minute
  window.setTimeout(function () {
    tick();
    window.setInterval(tick, 60000);
  }, (60 - new Date().getSeconds()) * 1000);
})();
