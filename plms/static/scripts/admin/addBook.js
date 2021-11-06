import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

var addButton = document.getElementById('addButton');
addButton.addEventListener('click',function(event) {
    event.preventDefault();
    var api = urls.baseAPIUrl+urls.addBook;

    var id = document.getElementById('id').value;
    var title = document.getElementById('title').value;
    var author = document.getElementById('author').value;
    var publisher = document.getElementById('publisher').value;
    var category = document.getElementById('category').value;
    var description = document.getElementById('description').value;
    var copies = document.getElementById('copies').value;

    fetch(api, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            'id': id,
            'title': title,
            'author': author,
            'publisher': publisher,
            'category': category,
            'description': description,
            'number_of_copies_bought': copies
        })
    }).then(function (response) {
        var responseCode = response.response_code;
        var responseMessage = response.response_message;

        alert(responseMessage);
    });
});