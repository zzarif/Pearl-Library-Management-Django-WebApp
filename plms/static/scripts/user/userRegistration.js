import { urls } from "../urls.js";

var btnRegister = document.getElementById('btn_register');
btnRegister.addEventListener('click',function(event) {
    event.preventDefault();
    var api = urls.baseAPIUrl+urls.registerApiEndpoint;

    var username = document.getElementById('in_username').value;
    var name = document.getElementById('in_name').value;
    var email_address = document.getElementById('in_email_address').value;
    var phone_number = document.getElementById('in_phone_number').value;
    var home_address = document.getElementById('in_home_address').value;
    var role_is_borrower = document.getElementById('in_role_is_borrower').value;
    var password = document.getElementById('in_password').value;
    var conf_password = document.getElementById('in_conf_password').value;
    

    fetch(api, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            'id': username,
            'name': name,
            'role_is_borrower': role_is_borrower,
            'phone_number': phone_number,
            'home_address': home_address,
            'email_address': email_address,
            'password': password
        })
    })
    .then((response) => response.json())
    .then(function(response) {
        var responseCode = response.response_code;
        var responseMessage = response.response_message;

        if(responseCode==1) 
            window.location = urls.baseUrl+urls.home;
        else alert(responseMessage);
    });
});