from flask import request, jsonify, render_template
from werkzeug.utils import secure_filename
from app import app, db
from app.utils import create_tables, upload_data_to_db
import os


UPLOAD_FOLDER = './uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'], strict_slashes=False)
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


