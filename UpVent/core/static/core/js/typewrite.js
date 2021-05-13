// @license [magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&dn=gpl-2.0.txt] [GPLv2.0]

let i = 0;

let txt = 'Para Negocios Inteligentes.';
let speed = 50;

function typewrite() {
    if (i < txt.length) {
        document.getElementById("smart").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typewrite, speed);
    }
}


// @license-end
