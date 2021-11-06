import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

function loadBorrowers() {
    var api = urls.baseAPIUrl+urls.borrowersApiEndPoint;
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
                        <td>${list[i].name}</td>
                        <td>${list[i].phone_number}</td>
                        <td>${list[i].email_address}</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

window.onload = function() {
    loadBorrowers();
}