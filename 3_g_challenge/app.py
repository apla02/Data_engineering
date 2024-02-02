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


    @app.post("/upload")
    def upload_csv_file():
        if request.method == 'POST':
            f= request.files.get('file')


"""
if __name__ == '__main__':

    app.run(debug=True)
