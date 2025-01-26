// Get patient information from form
const patientNameInput = document.getElementById('patient-name');
const emergencyContactInput = document.getElementById('emergency-contact');

// Add event listener to form submission
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const patientName = patientNameInput.value;
    const emergencyContact = emergencyContactInput.value;
    // Send patient information to server or database
});
