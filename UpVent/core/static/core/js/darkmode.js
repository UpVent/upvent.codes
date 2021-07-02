// @license magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&dn=gpl-2.0.txt GPL-v2.0-or-Later
const toggle = document.querySelector("#toggledm");
toggle.addEventListener("click", modeSwitch);

let isLight = true;

function modeSwitch() {
  isLight = !isLight;
  isLight ? toggle.innerText = "🌞" : toggle.innerText = "🌚";
  var rootElement = document.body;

  /* ==== Dark Mode Actions ==== */

  /* Remove dark-text class */
  rootElement.classList.remove("text-dark");
  /* Toggle dark body class in order to make body dark coloured */
  rootElement.classList.toggle("body-dark");
  /* Untoggle opposite text classes */
  rootElement.classList.toggle("text-light");

  /* CARD class change */
  document.querySelectorAll('.card').forEach(item => {
    item.classList.add('card-dark');
  });
}
// @license-end
