import os
import pandas as pd
from app.models import Department, Job, Employee
from app import db 
from multiprocessing import Value

global_record_count = Value('i', 0)


def create_tables():
    """
    This functions creates the local database using SQLite and SqlAlquemy ORM
    """
    db.create_all()

#def process_csv(file_path):
    #return pd.read_csv(file_path)

def upload_data_to_db(file_path, batch_size=1000):
    
    global global_record_count

    dict_atributtes = {
        'department' : ['id', 'department'],
        'job': ['id', 'job'],
        'employee' : ['id', 'name', 'datetime', 'department_id', 'job_id']
    }
    
    file_name =  os.path.basename(file_path)
    if file_name in ['departments.csv', 'jobs.csv', 'hired_employees.csv']:
        table_name = file_name.split('.')[0].split('_')[-1][:-1]
        print(table_name)
        
        chunks = pd.read_csv(file_path, names = dict_atributtes[table_name], chunksize=batch_size)
        try:
            #chunk.to_sql(table_name, db.engine, if_exists= 'append', index=False)
            
            for chunk in chunks:
                chunk.to_sql(table_name, db.engine, if_exists= 'append', index=False)
                with global_record_count.get_lock():
                    global_record_count.value += len(chunk)
            
            
            db.session.commit()
            print('Data was uploaded into the database')
        except Exception as e:
            print(f"Error uploading data to the database: {str(e)}")
            db.session.rollback()

 

def insert_batch_transactions(df):
    pass






