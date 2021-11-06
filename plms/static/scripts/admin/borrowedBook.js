import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

function loadBorrowerBooks() {
    var api = urls.baseAPIUrl+urls.borrowedBookAPIEndPoint;
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
                        <td>${list[i].trans_id}</td>
                        <td>${list[i].title}</td>
                        <td>${list[i].author}</td>
                        <td>${list[i].name}</td>
                        <td>${list[i].returning_date}</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

window.onload = function() {
    loadBorrowerBooks();
}