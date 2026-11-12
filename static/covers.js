/* covers.js — a jacket that will not load is replaced by a blank block,
   rather than the browser's broken-image mark. */
(function covers() {
  function blank(img) {
    var div = document.createElement("div");
    div.className = "cover cover-blank";
    div.setAttribute("aria-hidden", "true");
    if (img.parentNode) img.replaceWith(div);
  }

  document.querySelectorAll("img.cover").forEach(function (img) {
    // the load may already have failed before this script ran
    if (img.complete && img.naturalWidth === 0) {
      blank(img);
      return;
    }
    img.addEventListener("error", function () { blank(img); });
  });
})();
