from app import app

"""
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = 'company_db'

@app.route("/")
def hello():
    return " hello. World"

def init_database():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    commands = ('''

        CREATE TABLE IF NOT EXISTS department(
            id INT PRIMARY KEY,
            department VARCHAR(26),
        '''
        ,
        '''
        CREATE TABLE IF NOT EXISTS jobs(
            id INT PRIMARY KEY,
            job VARCHAR(26)
        )
        '''
        ,
        '''
        CREATE TABLE IF NOT EXISTS employees(
            id INT PRIMARY KEY,
            name VARCHAR(26),
            datetime DATETIME
            department_id INT,
            FOREIGN KEY (department_id) REFERENCES departments (id)
            job_id INT,
            FOREIGN KEY (job_id) REFERENCES jobs (id)
        )
        ''')

    for command in commands:
         cursor.execute(command)
    
    conn.commit()
    conn.close()



"""
"""from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})"""


with app.app_context():
    db.create_all()

@app.errorhandler(404)
def not_found(error):
    """handle error 404: Not found"""
    return make_response(jsonify({"error": "Not found"}), 404)



if __name__ == '__main__':

    app.run(debug=True)
