# Software Engineering Capstone Project #

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

# Purpose
An airline software project created for Comfort Airlines by Cloud Nine. This program allows the user to perform operations on a time table of flights as well as run a simulation over a specified duration of time.

### Description
When this program is run it will give you key options for editing or viewing the timetable, running or configuring the simulation, as well as viewing or editing aircraft and airport tables. You can simply input the number corresponding to your choice or select 'back' to go back to the previous menu.

### How to run the program (Visual Studio Code)
1. Docker startup: 
Make sure you have the Docker daemon running. (Open the Docker Desktop app on your local machine)

2. Move to the docker directory: 
```bash
cd .\docker\
```

3. Compose the docker container: 
```bash
docker-compose up -d
```

4. Enter the database: 
```bash
docker exec -it mariadb-container mariadb -u admin -p cloudnine
```

5. Populate the database: 
To reset the schema, repopulate the airport table, and repopulate the aircraft table, run the following commands in the cloudnine database:
```bash
source /docker-entrypoint-initdb.d/schema.sql
source /docker-entrypoint-initdb.d/populate-airports-table.sql
source /docker-entrypoint-initdb.d/populate-aircraft-table.sql
source /docker-entrypoint-initdb.d/populate-flights-table.sql
```

6. Exit the database and install dependencies: 
To download these dependencies all at once first navigate to the /documents directory then run the following command in your terminal:
```bash
pip install -r dependencies.txt
```

7. Run the program: 
```bash
python3 comfort_airlines.py
```

# Other Guides (located in documents folder) ###

### Comfort Airlines
requirements.md - The requirements document is a list of features that we intend to implement/already have implemented for Comfort Airlines. Each feature also contains a breif description.

### Developers
functional-specification.md - The functional specification documents is a detailed introduction to the codebase highlighting the purpose and use of files, functions, schemas, and conditions involved in each. This file is intended to help acquaint new team members with our codebase.

test-plan.md - A detailed description of Cloud Nine's testing process. Our test plan is designed to reduce the overall number of bugs entered into the main codebase while maximizing time for developing new features.

defect-log.md - The defect log tracks bugs that our developers have encountered. Bugs are logged in hopes that if someone else has an error that has been logged already they will know how to handle it. This file also provides clarity for team members that are new to the codebase.