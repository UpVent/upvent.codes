let searchForm = document.getElementById('search-form');
let csrfToken = searchForm.querySelector('input[name=csrfmiddlewaretoken]').value;

let searchResults = document.getElementById('search-results');

if (window.screen.width > 800 ) {
    searchResults.style.width = searchForm.clientWidth*.6 + 'px';
    searchResults.style.marginLeft = searchForm.clientWidth*.2 + 'px';
} else {
    searchResults.style.width = searchForm.clientWidth + 'px';
}

document.getElementById('search-input').addEventListener("input", (e) => {
    if (e.target.value !== '') {
        searchResults.style.display = 'table';
        searchResults.innerHTML = '<div class="lds-ring"><div></div><div></div><div></div><div></div></div>';

        let data = new FormData();
        data.append('query', e.target.value);
        data.append('csrfmiddlewaretoken', csrfToken);
        fetch(`${searchForm.action}`, {
            method: 'POST',
            body: data,
            credentials: 'same-origin',
        })
            .then(response => response.json())
            .then(data => {
                if (data.data.length !== 0) {
                    searchResults.innerHTML = '<ul></ul>'
                    let results = '';
                    data.data.forEach(result => {
                        results += `<li><img class="img-fluid" src="${result.image}"><span><b>${result.title}</b> ${result.description}</span><a href="${result.url}">Ir</a></li>`;
                    });
                    searchResults.firstElementChild.innerHTML = results;
                } else {
                    searchResults.innerHTML = '<p>Sin resultados</p>'
                }
            });

    } else {
        searchResults.style.display = 'none';
    }
});
