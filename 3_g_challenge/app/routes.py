from flask import request, jsonify, render_template
from werkzeug.utils import secure_filename
from app import app, db
from app.utils import upload_data_to_db
from sqlalchemy import text, func
from app.models import Department, Job, Employee


UPLOAD_FOLDER = './uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return 'Index Page'


@app.route("/uploads", methods=['GET', 'POST'], strict_slashes=False)
def upload_file():

    """
    Receive historical data from CSV files
    """
    
    if request.method == 'POST':

        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files.get('file')

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if filename in ['departments.csv', 'jobs.csv', 'hired_employees.csv']:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                upload_data_to_db(file_path)
                return jsonify({'message': 'file was saved'}), 200
            else:
                return jsonify({'error': 'file name is not valid, please select a new file'})

        return jsonify({'error': 'invalid file format'}), 400
        
    return render_template('upload_file.html')

    

@app.route('/employees_departments_jobs', methods=['GET'])
def get_employees_by_department_and_job_2021():

    """
    Get the number of employees hired for each job and department in 2021 divided by quarter.
    The table must be ordered alphabetically by department and job.

    """

    try:
        query = text("""
            SELECT
                d.department,
                j.job,
                COUNT(CASE WHEN strftime('%m', e.datetime) BETWEEN '01' AND '03' THEN e.id END) AS 'Q1',
                COUNT(CASE WHEN strftime('%m', e.datetime) BETWEEN '04' AND '06' THEN e.id END) AS 'Q2',
                COUNT(CASE WHEN strftime('%m', e.datetime) BETWEEN '07' AND '09' THEN e.id END) AS 'Q3',
                COUNT(CASE WHEN strftime('%m', e.datetime) BETWEEN '10' AND '12' THEN e.id END) AS 'Q4'
            FROM
                employee as e
            INNER JOIN job as j ON e.job_id = j.id
            INNER JOIN department d ON e.department_id = d.id
            WHERE strftime('%Y', e.datetime) = '2021'
            GROUP BY d.department, j.job
            ORDER BY d.department, j.job
        """)

        with db.engine.connect() as connection:
            result = connection.execute(query)

        employees_by_department_and_job_2021 = [
            {
                'department': row.department,
                'job': row.job,
                'Q1': row.Q1,
                'Q2': row.Q2,
                'Q3': row.Q3,
                'Q4': row.Q4
            }
            for row in result
        ]

        response = {'employees_by_department_and_job_2021': employees_by_department_and_job_2021}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/departments', methods=['GET'])
def departments_with_more_employees_hired_than_avg():

    """List of ids, name and number of employees hired of each department that hired more
    employees than the mean of employees hired in 2021 for all the departments, ordered
    by the number of employees hired (descending).
    """
    
    # departments with more employees hired than mean  in 2021
    query = text("""WITH AVG_DPTS AS (
        SELECT d.id, d.department, count(e.id) as hired, e.datetime FROM employee as e
        INNER JOIN department as d
        ON e.department_id = d.id
        INNER JOIN job as j
        on j.id = e.job_id
        WHERE strftime("%Y", e.datetime) = '2021'
        GROUP BY d.id, d.department)

        SELECT id, department,  hired FROM AVG_DPTS
        WHERE hired > (SELECT AVG(hired) FROM AVG_DPTS)
        ORDER BY hired DESC
        LIMIT 3
    """)

    with db.engine.connect() as connection:
            result = connection.execute(query)

    departments_with_more_employees_hired_than_avg = [
        {   'id': row.id,
            'department': row.department,
            'hired': row.hired,
        }
        for row in result
    ]

    response = {'employees_by_department_and_job_2021': departments_with_more_employees_hired_than_avg}
    return jsonify(response) 
