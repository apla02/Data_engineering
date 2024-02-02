
# Challenge

Starting...

1. Clone this repo in yout local machine

2. create a new local environment and activcate it

python -m g_env 

activate genv/bin/activate

3. install all of the requirements

pip install requirements.txt

4. Run the app
Python app.py

## Tasks

### Section 1: API

-  In the context of a DB migration with 3 different tables (departments, jobs, employees) , create
a local REST API that must:

1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request


Clarifications
- You decide the origin where the CSV files are located.
- You decide the destination database type, but it must be a SQL database.
- The CSV file is comma separated.

### Section 2: SQL
You need to explore the data that was inserted in the previous section. The stakeholders ask
for some specific metrics they need. You should create an end-point for each requirement.
Requirements

- Number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.


- List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).

### Bonus Track! Cloud, Testing & Containers
Add the following to your solution to make it more robust:
### Host your architecture in any public cloud (using the services you consider more
adequate)

### Add automated tests to the API
- You can use whichever library that you want

### Different tests types, if necessary, are welcome
- Containerize your application

Using Docker

- From #_g_challenge folder build the Docker file using this command
docker build -t myflaskapp .

- Run the application
docker run -p 5000:5000 myflaskapp


