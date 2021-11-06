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
                        <td id="book-id">${list[i].id}</td>
                        <td>${list[i].title}</td>
                        <td>${list[i].author}</td>
                        <td>${list[i].category}</td>
                        <td>${list[i].availability_status}</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

var requestButton = document.getElementById('requestButton')
requestButton.addEventListener('click',function(event) {
    event.preventDefault();
    var api = urls.baseAPIUrl+urls.requestBook;

    var bookId = document.getElementById('book-id-given').value;

    fetch(api, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            'book_id': bookId,
            'user_id': sessionStorage.getItem(sessionKeys.userId),
        })
    })
    .then((response) => response.json())
    .then(function(response) {
        var responseCode = response.response_code;
        var responseMessage = response.response_message;

        alert(responseMessage);
    });
});

window.onload = function() {
    loadBookList();
}

