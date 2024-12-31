

function toggleLoginButton() {
    var roleSelect = document.getElementById('role');
    var loginButton = document.getElementById('loginButton');
    
    // Enable the login button if a valid role is selected
    if (roleSelect.value !== "") {
        loginButton.disabled = false;
    } else {
        loginButton.disabled = true;
    }
}
