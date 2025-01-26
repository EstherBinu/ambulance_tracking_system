

from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client['gps_ambulance_tracker']

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def save_to_db(self):
        db['users'].insert_one({
            'username': self.username,
            'password': self.password,
            'role': self.role
        })

    @staticmethod
    def find_by_username(username):
        user_data = db['users'].find_one({'username': username})
        if user_data:
            return User(user_data['username'], user_data['password'], user_data['role'])
        return None

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Patient:
    def __init__(self, id, name, age, contact_number, address):
        self.id = id
        self.name = name
        self.age = age
        self.contact_number = contact_number
        self.address = address

    def save_to_db(self):
        db['patients'].insert_one({
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'contact_number': self.contact_number,
            'address': self.address
        })

    @staticmethod
    def find_by_id(id):
        patient_data = db['patients'].find_one({'id': id})
        if patient_data:
            return Patient(patient_data['id'], patient_data['name'], patient_data['age'], patient_data['contact_number'], patient_data['address'])
        return None

class Alert:
    def __init__(self, id, message, patient_id, ambulance_id):
        self.id = id
        self.message = message
        self.patient_id = patient_id
        self.ambulance_id = ambulance_id

    def save_to_db(self):
        db['alerts'].insert_one({
            'id': self.id,
            'message': self.message,
            'patient_id': self.patient_id,
            'ambulance_id': self.ambulance_id
        })

    @staticmethod
    def find_by_id(id):
        alert_data = db['alerts'].find_one({'id': id})
        if alert_data:
            return Alert(alert_data['id'], alert_data['message'], alert_data['patient_id'], alert_data['ambulance_id'])
        return None

