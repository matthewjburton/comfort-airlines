# comfort-airlines

## Softeware Engineering Capstone Project

### Comment Example for Methods  

```cpp
/* XYZ Function - will perform xyz task*  
 * Takes `abc` as input and transforms it into `123`
 */
int XYZ(string abc)
{
    return 123; // Single line comment explaining code if necessary
}
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
