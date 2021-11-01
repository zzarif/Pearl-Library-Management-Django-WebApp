

function loadBookList() {
    var api = 'http://localhost:8000/apis/bookList';
    fetch(api, {
        method: 'GET'
    })
    .then((response) => response.json())
    .then(function (list) {
        var tableContent = document.getElementById('tableContent');
        tableContent.innerHTML = '';

        for (var i in list) {

            var newRow = `
                    <tr>
                        <td>${list[i].id}</td>
                        <td>${list[i].title}</td>
                        <td>${list[i].author}</td>
                        <td>${list[i].publisher}</td>
                        <td>${list[i].category}</td>
                        <td>${list[i].description}</td>
                        <td>${list[i].rating}</td>
                        <td>${list[i].number_of_copies}</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

window.onload = function() {
    loadBookList();
}