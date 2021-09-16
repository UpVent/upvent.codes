function addDarkmodeWidget() {

    const options = {
        time: '0.5s',
        label: '🌞',
        saveInCookies: false,
        autoMatchOsTheme: true
    }

    new Darkmode(options).showWidget();
}

window.addEventListener('load', addDarkmodeWidget);
