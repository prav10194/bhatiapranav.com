/* presence.js — the tab icon: a white dot with a slow pulse, like a status light. */
(function presence() {
  const link = document.getElementById("favicon");
  if (!link) return;

  const canvas = document.createElement("canvas");
  canvas.width = 32;
  canvas.height = 32;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const PERIOD = 2400;
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function draw(t) {
    // 0 at rest, 1 at full stretch
    const phase = (Math.sin((t / PERIOD) * Math.PI * 2) + 1) / 2;
    ctx.clearRect(0, 0, 32, 32);

    // the halo breathes outwards and fades as it goes
    ctx.beginPath();
    ctx.arc(16, 16, 7.5 + phase * 7.5, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255, 255, 255, ${0.32 * (1 - phase)})`;
    ctx.fill();

    ctx.beginPath();
    ctx.arc(16, 16, 6.5, 0, Math.PI * 2);
    ctx.fillStyle = "#ffffff";
    ctx.fill();

    link.href = canvas.toDataURL("image/png");
  }

  if (reduced) {
    draw(PERIOD / 4); // a plain, still dot
    return;
  }

  let timer = null;
  function start() {
    if (timer === null) timer = window.setInterval(function () { draw(performance.now()); }, 90);
  }
  function stop() {
    if (timer !== null) { window.clearInterval(timer); timer = null; }
  }

  draw(0);
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop(); else start();
  });
  start();
})();
