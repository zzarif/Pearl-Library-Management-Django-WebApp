import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

var btnLogin = document.getElementById('btn_login');
btnLogin.addEventListener('click',function(event) {
    event.preventDefault();
    var api = urls.baseAPIUrl+urls.loginApiEndpoint;

    var username = document.getElementById('in_username').value;
    var password = document.getElementById('in_password').value;

    fetch(api, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            'id': username,
            'password': password,
            'role_is_borrower': false
        })
    })
    .then((response) => response.json())
    .then(function(response) {
        var responseCode = response.response_code;
        var responseMessage = response.response_message;

        if(responseCode==1) {
            sessionStorage.setItem(sessionKeys.userId,username);
            window.location = urls.baseUrl+urls.adminProfile;
        }
            
        else alert(responseMessage);
    });
});

window.onload = function() {
    sessionStorage.setItem(sessionKeys.userRole,'0');
}