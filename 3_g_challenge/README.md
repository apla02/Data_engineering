
# Challenge

## Section 1: API

1. Clone this repo in yout local machine

2. create a new local environment and activcate it

python -m g_env 

activate genv/bin/activate

3. install all of the requirements

pip install requirements.txt


4. Run the sqlite database
./init.sh


5. Run the app
Python app.py


-  In the context of a DB migration with 3 different tables (departments, jobs, employees) , create
a local REST API that must:

1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request

You need to publish your code in GitHub. It will be taken into account if frequent updates are
made to the repository that allow analyzing the development process. Ideally, create a
markdown file for the Readme.md

Clarifications
● You decide the origin where the CSV files are located.
● You decide the destination database type, but it must be a SQL database.
● The CSV file is comma separated.

## Section 2: SQL
You need to explore the data that was inserted in the previous section. The stakeholders ask
for some specific metrics they need. You should create an end-point for each requirement.
Requirements

● Number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.
Output example:
department job Q1 Q2 Q3 Q4
Staff Recruiter 3 0 7 11
Staff Manager 2 1 0 2
Supply Chain Manager 0 1 3 0

● List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).
Output example:
id department hired
7 Staff 45
9 Supply Chain 12

Bonus Track! Cloud, Testing & Containers
Add the following to your solution to make it more robust:
● Host your architecture in any public cloud (using the services you consider more
adequate)
● Add automated tests to the API
○ You can use whichever library that you want

○ Different tests types, if necessary, are welcome
● Containerize your application
○ Create a Dockerfile to deploy the package

Csv files structures
hired_employees.csv:
id INTEGER Id of the employee
name STRING Name and surname of the employee
datetime STRING Hire datetime in ISO format
department_id INTEGER Id of the department which the employee was hired for
job_id INTEGER Id of the job which the employee was hired for

4535,Marcelo Gonzalez,2021-07-27T16:02:08Z,1,2
4572,Lidia Mendez,2021-07-27T19:04:09Z,1,2
File hired_employees.csv should be attached by recruiter
departments.csv
id INTEGER Id of the department
department STRING Name of the department

1, Supply Chain
2, Maintenance
3, Staff
File departments.csv should be attached by recruiter
jobs.csv:
id INTEGER Id of the job
job STRING Name of the job

1, Recruiter
2, Manager
3, Analyst
File jobs.csv should be attached by recruiter  