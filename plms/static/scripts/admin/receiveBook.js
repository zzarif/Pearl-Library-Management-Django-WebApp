import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

var receive = document.getElementById('receive');
receive.addEventListener('click',function(event) {
    event.preventDefault();
    var trans_id = document.getElementById('trans_id').value;

    var api = urls.baseAPIUrl+urls.receiveBook+trans_id+'/';


    fetch(api, {
        method: 'GET',
    })
    .then((response) => response.json())
    .then(function(response) {
        var responseCode = response.response_code;
        var responseMessage = response.response_message;

        if(responseCode==1) window.location = urls.baseUrl+urls.adminProfile+urls.borrowedBook
            
        else alert(responseMessage);
    });
});

window.onload = function() {
    sessionStorage.setItem(sessionKeys.userRole,'0');
}