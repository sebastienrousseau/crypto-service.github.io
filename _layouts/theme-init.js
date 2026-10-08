/*!
 * Runs before first paint so a stored choice or system preference applies
 * without a flash of the wrong palette.
 *
 * Evaluates the active palette and stamps data-theme ("dark" | "light")
 * and data-theme-mode ("system" | "light" | "dark") onto <html> so all CSS
 * selectors and theme variables resolve with 100% consistency.
 */
(function () {
  var root = document.documentElement;
  root.classList.remove("no-js");
  try {
    var saved = localStorage.getItem("theme");
    var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    var mode = (saved === "dark" || saved === "light") ? saved : "system";
    var effective = (saved === "dark" || saved === "light") ? saved : (prefersDark ? "dark" : "light");
    root.setAttribute("data-theme", effective);
    root.setAttribute("data-theme-mode", mode);
  } catch (e) {
    var prefersDarkFallback = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    root.setAttribute("data-theme", prefersDarkFallback ? "dark" : "light");
    root.setAttribute("data-theme-mode", "system");
  }
})();
