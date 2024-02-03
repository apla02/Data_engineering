import os
import pytest
from flask import Flask
from app import app, db
from app.routes import allowed_file, upload_data_to_db
from app.routes import  get_employees_by_department_and_job_2021
from app.routes import  departments_with_more_employees_hired_than_avg


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_allowed_file():
    assert allowed_file("example.csv")
    assert not allowed_file("example.txt")

def test_upload_file_route(client):
    data = {'file': (open('./tests/test.csv', 'rb'), './tests/test.csv')}
    
    response = client.post('/uploads', data=data)
    assert response.status_code == 200
