import { h, render, Component } from './preact.min.js'
import htm from './htm.min.js'

const html = htm.bind(h);

/**
 * This is the main App class for our index.html file
 * */
class App extends Component {

    /**
     * Render this component into readable HTML
     * @returns {html} The readable html elements for this page.
     * */
    render() {
        return html `<h1>Hello, world!</h1>`;
    }
}

render(html`<${App}/>`, document.getElementById("coso"));
