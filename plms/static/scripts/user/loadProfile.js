import { urls } from "../urls.js";
import { sessionKeys } from "../sessionKeys.js"

function loadProfile() {
    var api = urls.baseAPIUrl+urls.userInfoId+sessionStorage.getItem(sessionKeys.userId)+'/';
    fetch(api, {
        method: 'GET'
    })
    .then((response) => response.json())
    .then(function (response) {
        document.getElementById('name').innerHTML = response.name;
        document.getElementById('email_address').innerHTML = 'Mail: '+response.email_address;
        document.getElementById('phone_number').innerHTML = 'Contact: '+response.phone_number;
        document.getElementById('home_address').innerHTML = response.home_address;
    });
};

window.onload = function() {
    loadProfile();
}

