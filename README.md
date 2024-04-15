## Software Engineering Capstone Project

- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

# Purpose
An airline software project created for Comfort Airlines by Cloud Nine. This program allows the user to perform operations on a time table of flights as well as run a simulation over a specified duration of time.

# Description
When this program is run it will give you key options for editing or viewing the timetable, running or configuring the simulation, as well as viewing or editing aircraft and airport tables. You can simply input the number corresponding to your choice or select 'back' to go back to the previous menu.

# How to use


### Comment Example for Methods  

```python
# XYZ Function - will perform xyz task 
# Takes `abc` as input and transforms it into `123`
def XYZ(abc):
    return 123 # Single line comment explaining code if necessary
```

## Docker

Make sure you have the Docker daemon running. (Open the Docker Desktop app on your local machine)

### Create a shell in the Docker

To open a new shell within the docker, run the following command in the terminal:

```bash
#docker exec -it <container name> <shell>
docker exec -it mariadb-container sh
```

To exit the Docker container, use the *exit* keyword

### How to enter the MariaDB container

Make sure you are already within the docker by creating a shell as described above. To enter the MariaDB container, execute the following command:

```bash
# mariadb -u <username> -p
mariadb -u admin -p
```

### How to enter the cloudnine database

Make sure you are already within the MariaDB container as described above. To enter the cloudnine database, execute the following sql command:

```bash
# USE <database name>;
USE cloudnine;
```

### How to directly enter the Database

To jump straight into the "cloudnine" database, execute the following command:

```bash
#docker exec -it <container name> mariadb -u <username> -p <database name>
docker exec -it mariadb-container mariadb -u admin -p cloudnine
```

### How to execute .sql files

.sql files are linked to the database using a docker volume. The /docker/sql-files directory is the volume designated for .sql files that will be run when the docker is initialized. Any .sql files in this folder are also accessible within the docker through the /docker-entrypoint-initdb.d directory. You can execute .sql files using the source command and the file path as follows:

```bash
#source /docker-entrypoint-initdb.d/<file_name.sql>
```

If you want to reset the schema, repopulate the airport table, or the aircraft table, run the following command(s) in the cloudnine database:

```bash
source /docker-entrypoint-initdb.d/schema.sql
source /docker-entrypoint-initdb.d/populate-airports-table.sql
source /docker-entrypoint-initdb.d/populate-aircraft-table.sql
source /docker-entrypoint-initdb.d/populate-flights-table.sql
```

### Dependencies

This project relies on certain dependencies to be installed on your local machine to execute the programs involved.  
To download these dependencies all at once first navigate to the /documents directory then run the following command in your terminal:

```bash
pip install -r dependencies.txt
```
