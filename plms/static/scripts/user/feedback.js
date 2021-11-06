import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

var addfeedback = document.getElementById('addfeedback');
addfeedback.addEventListener('click',function(event) {
    event.preventDefault();
    var api = urls.baseAPIUrl+urls.addFeedback;

    var feedback = document.getElementById('in_feedback').value;

    fetch(api, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            'feedback': feedback,
            'user_id': sessionStorage.getItem(sessionKeys.userId),
        })
    })
    .then((response) => response.json())
    .then(function(response) {
        var responseCode = response.response_code;
        var responseMessage = response.response_message;

        if(responseCode==1) location.reload();
        else alert(responseMessage);
    });
});

function loadFeedbacks() {
    var api = urls.baseAPIUrl+urls.feedback+sessionStorage.getItem(sessionKeys.userId);
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
                        <td>${list[i].feedback}</td>
                    </tr>
                `;

            tableContent.innerHTML += newRow;
        }
    });
};

window.onload = function() {
    loadFeedbacks();
}