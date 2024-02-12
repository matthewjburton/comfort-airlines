# comfort-airlines

## Softeware Engineering Capstone Project

### Comment Example for Methods  

```python
# XYZ Function - will perform xyz task 
# Takes `abc` as input and transforms it into `123`
def XYZ(abc):
    return 123 # Single line comment explaining code if necessary
```

### How to access the Docker container

1. Make sure you have the Docker daemon running. (You can make sure it's running by opening the Docker Desktop app on your local machine)
2. To open a new shell within the docker, run the following command in the terminal:

```bash
docker exec -it mariadb sh
```

3. To exit the Docker container, use the *exit* keyword

### How to access the Database

1. Execute the following command in the terminal to jump straight into the "cloudnine" database

```bash
#docker exec -it <container name> mariadb -u <username> -p <database name>
docker exec -it mariadb-container mariadb -u admin -p cloudnine
```

2. When prompted, enter the password: Cloud9

### How to reset the database

To execute a .sql file in the databse you first need to copy it from teh repository into the docker. The general process involved copying the file, entering the database and executing the .sql file which can be done as follows:

```bash
#docker cp <file to be copied> mariadb-container:/tmp/
#docker exec -it mariadb-container mariadb -u admin -p cloudnine
#source /tmp/<file name>
```

If you want to reset the schema, and repopulate both the airport and aircraft tables, run the following commands in the terminal while in the /comfort-airlines directory:

```bash
docker cp docker/schema.sql mariadb-container:/tmp/
docker cp populate-airports-table.sql mariadb-container:/tmp/
docker cp populate-aircraft-table.sql mariadb-container:/tmp/

docker exec -it mariadb-container mariadb -u admin -p cloudnine

source /tmp/schema.sql
source /tmp/populate-airports-table.sql
source /tmp/populate-aircraft-table.sql
```
