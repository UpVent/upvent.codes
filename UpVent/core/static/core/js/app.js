import { h, render, Component } from './preact.min.js'
import htm from './htm.min.js'

const html = htm.bind(h);

function App (props) {
    return html`<h1>Hello ${props.name}!</h1>`;
  }

  render(html`<${App} name="World" />`, document.getElementById("coso"));
