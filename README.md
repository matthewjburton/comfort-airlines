# comfort-airlines

## Software Engineering Capstone Project

### Comment Example for Methods  

*XYZ Function - will perform xyz task*  
*Takes `abc` as input and transforms it into `123`*

```cpp
int XYZ(string abc)
{
    return 123; // Single line comment explaining code if necessary
}
```

### How to access the MariaDB Docker container

1. Make sure you have the Docker daemon running. (You can make sure it's running by opening the Docker Desktop app on your local machine)
2. To open a new shell within the docker, run the following command in the terminal:

```bash
docker exec -it mariadb sh
```

3. Once inside the docker, open the MariaDB contianer using the following command:

```bash
mariadb -p
```

4. To gain access, enter the password as defined in the .env file.
5. To view the current databases run the following command:

```bash
show databases
```

6. To exit the MariaDB container, use the *exit* keyword
7. To exit the docker, also use the *exit* keyword
