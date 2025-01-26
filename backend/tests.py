


import pytest
from app import app, db
from models import User, Patient, Alert

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()
    yield app.test_client()
    db.session.remove()
    db.drop_all()

def test_get_ambulance_locations(client):
    response = client.get('/api/ambulance-locations')
    assert response.status_code == 200

def test_create_patient(client):
    data = {'id': 1, 'name': 'John Doe', 'age': 30, 'contact_number': '1234567890', 'address': '123 Main St'}
    response = client.post('/api/patients', json=data)
    assert response.status_code == 201

def test_get_patients(client):
    response = client.get('/api/patients')
    assert response.status_code == 200

def test_get_patient(client):
    data = {'id': 1, 'name': 'John Doe', 'age': 30, 'contact_number': '1234567890', 'address': '123 Main St'}
    client.post('/api/patients', json=data)
    response = client.get('/api/patients/1')
    assert response.status_code == 200

def test_update_patient(client):
    data = {'id': 1, 'name': 'John Doe', 'age': 30, 'contact_number': '1234567890', 'address': '123 Main St'}
    client.post('/api/patients', json=data)
    data = {'id': 1, 'name': 'Jane Doe', 'age': 31, 'contact_number': '1234567891', 'address': '456 Main St'}
    response = client.put('/api/patients/1', json=data)
    assert response.status_code == 200

def test_delete_patient(client):
    data = {'id': 1, 'name': 'John Doe', 'age': 30, 'contact_number': '1234567890', 'address': '123 Main St'}
    client.post('/api/patients', json=data)
    response = client.delete('/api/patients/1')
    assert response.status_code == 200

def test_create_alert(client):
    data = {'id': 1, 'message': 'Ambulance 1 is nearby', 'patient_id': 1, 'ambulance_id': 1}
    response = client.post('/api/alerts', json=data)
    assert response.status_code == 201

def test_get_alerts(client):
    response = client.get('/api/alerts')
    assert response.status_code == 200

def test_get_alert(client):
    data = {'id': 1, 'message': 'Ambulance 1 is nearby', 'patient_id': 1, 'ambulance_id': 1}
    client.post('/api/alerts', json=data)
    response = client.get('/api/alerts/1')
    assert response.status_code == 200


