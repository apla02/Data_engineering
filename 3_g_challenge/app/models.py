from flask import url_for
from app import db


class Department(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    department = db.Column(db.String(256), nullable=False)
    # jobs = relationship('Job', back_populates ='department')
    # employees = relationship('Employee', back_populates = 'department')


    def __repr__(self):
        return f'<Department {self.name}>'

class Job(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    job =  db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'<Job {self.job}>'


class Employee(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(256)) 
    datetime = db.Column(db.DateTime(timezone=True))
    department_id= db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref='employees')
    job_id= db.Column(db.Integer, db.ForeignKey('job.id'))
    department = db.relationship('Job', backref='employees')


    def __repr__(self):
        return f'<Employee { self.name}>'




