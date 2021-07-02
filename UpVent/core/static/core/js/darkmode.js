// @license magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&dn=gpl-2.0.txt GPL-v2.0-or-Later
const toggle = document.querySelector("#toggledm");
toggle.addEventListener("click", modeSwitch);

let isLight = true;

function modeSwitch() {
  isLight = !isLight;
  isLight ? toggle.innerText = "🌞" : toggle.innerText = "🌚";
  var rootElement = document.body;
  /* Toggle dark body class in order to make body dark coloured */
  rootElement.classList.toggle("body-dark");
}



// @license-end
