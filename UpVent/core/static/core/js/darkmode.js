// @license magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&dn=gpl-2.0.txt GPL-v2.0-or-Later
const toggle = document.querySelector("#toggledm");
toggle.addEventListener("click", modeSwitch);

let isLight = true;

function modeSwitch() {
  isLight = !isLight;

  if (!isLight) {
    alert("El modo oscuro es experimental y puede contener errores");
  }

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


function KeyHandler(cb) {
  var input = '';
  var key = '38384040373937396665';
  document.addEventListener('keydown', function (e) {
    input += ("" + e.keyCode);
    if (input === key) {
      return cb();
    }
    if (!key.indexOf(input)) return;
    input = ("" + e.keyCode);
  });
}

KeyHandler(function () {alert('42')})
// @license-end
