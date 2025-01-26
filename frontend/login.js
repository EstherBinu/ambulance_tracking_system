const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Authenticate user
    authenticateUser(username, password).then((response) => {
        if (response.success) {
            // Login successful, redirect to dashboard
            window.location.href = 'dashboard.html';
        } else {
            // Login failed, display error message
            alert('Invalid username or password');
        }
    });
});

// Authenticate user function
function authenticateUser(username, password) {
    // Simulate authentication with a fake API
    return new Promise((resolve) => {
        setTimeout(() => {
            if (username === 'admin' && password === 'password') {
                resolve({ success: true });
            } else {
                resolve({ success: false });
            }
        }, 1000);
    });
}
