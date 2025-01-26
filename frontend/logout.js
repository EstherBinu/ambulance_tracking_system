// logout.js
function logout() {
    // Clear local storage
    localStorage.clear();
    // Redirect to login page
    window.location.href = 'login.html';
  }
  
  // Get the logout button element
  const logoutButton = document.getElementById('logout-button');
  
  // Add an event listener to the logout button
  logoutButton.addEventListener('click', logout);
  
  