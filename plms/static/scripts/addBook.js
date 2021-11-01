
var addButton = document.getElementById('addBook');
addButton.addEventListener('click',function(event) {
    event.preventDefault();
    var api = 'http://localhost:8000/apis/addBook/';

    var title = document.getElementById('title').value;
    var author = document.getElementById('author').value;
    var publisher = document.getElementById('publisher').value;
    var category = document.getElementById('category').value;
    var description = document.getElementById('description').value;
    var rating = document.getElementById('rating').value;
    var copies = document.getElementById('copies').value;

    fetch(api, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            'title': title,
            'author': author,
            'publisher': publisher,
            'category': category,
            'description': description,
            'rating': rating,
            'number_of_copies': copies
        })
    }).then(function (response) {
        alert(response)
    });
});