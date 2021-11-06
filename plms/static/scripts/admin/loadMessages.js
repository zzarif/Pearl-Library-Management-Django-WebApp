import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

function loadMessages() {
    var api = urls.baseAPIUrl+urls.messageAll;
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
                        <td>${list[i].email_addresses}</td>
                        <td>${list[i].message}</td>
                        <td><a href="mailto:aaa@example.com"><button class="btn btn-success ">Reply</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

window.onload = function() {
    loadMessages();
}

