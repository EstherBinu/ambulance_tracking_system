

// Get alerts and notifications container
const alertsContainer = document.getElementById('alerts-container');

// Define a function to display alerts and notifications
function displayAlerts(alerts) {
  // Clear the alerts container
  alertsContainer.innerHTML = '';

  // Loop through the alerts and display them
  alerts.forEach((alert) => {
    const alertElement = document.createElement('div');
    alertElement.classList.add('alert');
    alertElement.innerHTML = `
      <h2>${alert.title}</h2>
      <p>${alert.message}</p>
      <p>Time: ${alert.time}</p>
    `;
    alertsContainer.appendChild(alertElement);
  });
}

// Define a function to simulate getting alerts from a server
function getAlerts() {
  // Simulate a server response with some alerts
  const alerts = [
    {
      title: 'Ambulance Delayed',
      message: 'The ambulance is delayed due to traffic.',
      time: '10:00 AM',
    },
    {
      title: 'Patient Update',
      message: 'The patient is stable and en route to the hospital.',
      time: '10:15 AM',
    },
    {
      title: 'ETA Update',
      message: 'The estimated time of arrival at the hospital is 10:30 AM.',
      time: '10:20 AM',
    },
  ];

  // Display the alerts
  displayAlerts(alerts);
}

// Call the getAlerts function to simulate getting alerts from a server
getAlerts();

// Set an interval to simulate getting new alerts every minute
setInterval(getAlerts, 60000);