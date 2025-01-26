

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_socketio import SocketIO, emit
from models import User, Patient, Alert, Ambulance

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a random secret key
app.config['SECRET_KEY'] = 'secret!'  # Change this to a random secret key
CORS(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins='*')

# Sample data for ambulance locations
ambulance_locations = [
    {"id": 1, "latitude": -27.464844976322492, "longitude": 153.00695627531488},
    {"id": 2, "latitude": -27.465844976322492, "longitude": 153.00795627531488},
]

# Sample data for patients
patients = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Doe", "age": 25},
]

# Sample data for alerts and notifications
alerts = [
    {"id": 1, "message": "Ambulance 1 is nearby"},
    {"id": 2, "message": "Patient 1 needs attention"},
]

# API endpoint to get ambulance locations
@app.route("/api/ambulance-locations", methods=["GET"])
@jwt_required
def get_ambulance_locations():
    return jsonify(ambulance_locations)

# API endpoint to create a new patient
@app.route('/api/patients', methods=['POST'])
@jwt_required
def create_patient():
    data = request.json
    patient = Patient(data['id'], data['name'], data['age'], data['contact_number'], data['address'])
    patient.save_to_db()
    return jsonify({'message': 'Patient created successfully'}), 201

# API endpoint to get all patients
@app.route('/api/patients', methods=['GET'])
@jwt_required
def get_patients():
    patients = Patient.find_all()
    return jsonify([patient.__dict__ for patient in patients]), 200

# API endpoint to get a patient by ID
@app.route('/api/patients/<id>', methods=['GET'])
@jwt_required
def get_patient(id):
    patient = Patient.find_by_id(id)
    if patient:
        return jsonify(patient.__dict__), 200
    return jsonify({'message': 'Patient not found'}), 404

# API endpoint to update a patient
@app.route('/api/patients/<id>', methods=['PUT'])
@jwt_required
def update_patient(id):
    patient = Patient.find_by_id(id)
    if patient:
        data = request.json
        patient.name = data['name']
        patient.age = data['age']
        patient.contact_number = data['contact_number']
        patient.address = data['address']
        patient.save_to_db()
        return jsonify({'message': 'Patient updated successfully'}), 200
    return jsonify({'message': 'Patient not found'}), 404

# API endpoint to delete a patient
@app.route('/api/patients/<id>', methods=['DELETE'])
@jwt_required
def delete_patient(id):
    patient = Patient.find_by_id(id)
    if patient:
        patient.delete_from_db()
        return jsonify({'message': 'Patient deleted successfully'}), 200
    return jsonify({'message': 'Patient not found'}), 404

# API endpoint to create a new alert
@app.route('/api/alerts', methods=['POST'])
@jwt_required
def create_alert():
    data = request.json
    alert = Alert(data['id'], data['message'], data['patient_id'], data['ambulance_id'])
    alert.save_to_db()
    return jsonify({'message': 'Alert created successfully'}), 201

# API endpoint to get all alerts
@app.route('/api/alerts', methods=['GET'])
@jwt_required
def get_alerts():
    alerts = Alert.find_all()
    return jsonify([alert.__dict__ for alert in alerts]), 200

# API endpoint to get an alert by ID
@app.route('/api/alerts/<id>', methods=['GET'])
@jwt_required
def get_alert(id):
    alert = Alert.find_by_id(id)
    if alert:
        return jsonify(alert.__dict__), 200
    return jsonify({'message': 'Alert not found'}), 404

# Real-time location tracking
@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

@socketio.on('update_location')
def update_location(data):
    ambulance_id = data['ambulance_id']
