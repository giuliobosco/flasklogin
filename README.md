# flasklogin

Small test project for learn to use `Flask-Login`, following this tutorial, [https://hackersandslackers.com/configure-flask-applications/](https://hackersandslackers.com/configure-flask-applications/).

## start

Befor start the project be sure to have a mysql server available, create an empty database for the project:

```
create schema flasklogin;
```

then create a copy of the file `.env.example`, in `.env` and edit the line of the database connection.

```
SQLALCHEMY_DATABASE_URI=mysql+pymysql://myuser:mypassword@host.example.com:1234/mydatabase
```

then build the docker image:

```
docker build -t flasklogin .
```

for start the project there are two ways, via his entrypoint or via interractive mode (manually)

```
# entrypoint
docker run -it -v $PWD/:/app -p 5000:5000 flasklogin /app/start.sh
# manually
docker run -it -v %PWD/:/app -p 5000:5000 flasklogin /bin/bash
./start.sh
```
