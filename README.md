# comfort-airlines

Software Engineering capstone project

Example Commenting Below:

<em>/*  XYZ Function - will perform xyz task <br />
 &nbsp;&ast; Takes abc as input and transforms it into 123 <br />
&nbsp;*/ <br /></em>
int XYZ(string abc)<br />
{<br />
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return 123; //Single line comment explaining code if necessary<br />
}


## How to use the MariaDB Docker Container

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
