import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

function loadBookList() {
    var api = urls.baseAPIUrl+urls.detailsBookAPIEndPoint;
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
                        <td>${list[i].number_of_copies_bought}</td>
                        <td>${list[i].availability_status}</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

window.onload = function() {
    loadBookList();
}