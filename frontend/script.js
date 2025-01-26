

// script.js
let ambulanceLocation = { lat: -27.464844976322492, lng: 153.00695627531488 };
let patientLocation = { lat: -27.474844976322492, lng: 153.01695627531488 };

function addMarkers() {
  const iframe = document.querySelector('iframe');
  const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

  // Create ambulance marker
  const ambulanceMarker = iframeDoc.createElement('div');
  ambulanceMarker.className = 'ambulance-marker';
  ambulanceMarker.style.top = `${ambulanceLocation.lat}px`;
  ambulanceMarker.style.left = `${ambulanceLocation.lng}px`;
  iframeDoc.body.appendChild(ambulanceMarker);

  // Create patient marker
  const patientMarker = iframeDoc.createElement('div');
  patientMarker.className = 'patient-marker';
  patientMarker.style.top = `${patientLocation.lat}px`;
  patientMarker.style.left = `${patientLocation.lng}px`;
  iframeDoc.body.appendChild(patientMarker);
}

function updateAmbulanceLocation() {
  // Simulate new location data
  ambulanceLocation.lat += Math.random() * 0.001;
  ambulanceLocation.lng += Math.random() * 0.001;

  // Update ambulance marker position
  const iframe = document.querySelector('iframe');
  const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
  const ambulanceMarker = iframeDoc.querySelector('.ambulance-marker');
  ambulanceMarker.style.top = `${ambulanceLocation.lat}px`;
  ambulanceMarker.style.left = `${ambulanceLocation.lng}px`;
}

function updatePatientLocation() {
  // Simulate new location data
  patientLocation.lat += Math.random() * 0.001;
  patientLocation.lng += Math.random() * 0.001;

  // Update patient marker position
  const iframe = document.querySelector('iframe');
  const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
  const patientMarker = iframeDoc.querySelector('.patient-marker');
  patientMarker.style.top = `${patientLocation.lat}px`;
  patientMarker.style.left = `${patientLocation.lng}px`;
}

// Add markers initially
addMarkers();

// Update marker positions every second
setInterval(updateAmbulanceLocation, 1000);
setInterval(updatePatientLocation, 1000);