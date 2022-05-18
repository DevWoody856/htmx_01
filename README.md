<img src="https://res.cloudinary.com/dfqctp7bq/image/upload/v1652626899/htmx_vnpb2w.gif">


This repository is for <a href="https://rx-36.life/post/create-a-modal-window-with-django-htmx-and-hyperscript/" target="_blank"><span class="link">this blog post</span></a>.<br> I made a small experimental modal window application with HTMX and Django.

## How to setup this app

Here is how to download this repo locally and running the application.  

This description assumes the use of docker and windows11.  
And I use pycharm for my IDE.


1. Enter following command from the command line.
```
git clone https://github.com/DevWoody856/htmx_01
```

2. Create an `.env` file in the root of the project.

3. In the .env file you created, write the following.

```python
DEBUG_VALUE=TRUE

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db_htmxui_01_220503
DB_PORT=5432

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

As a reminder, DB_HOST is the service name of the database in docker-compose.yaml.  
In this docker configuration, it is `db_htmx_02_220501`.  
Also, this time the secret key is written directly in `settings.py`.

4. From the project root, enter the following command.

```python
docker-compose up --build
```

5. If you success `docker-compose up -build`, you can see the message "starting development server at http://0.0.0.0:8000/".   
Once it is up and running, please **open another terminal** while docker running, enter the following command.
This is the command that enters the dokcer side and launches the command line.

```python
docker-compose exec backend sh
```

6. When you are ready to enter a command, type the following command.
```python
python manage.py makemigrations
```

7. Then, after that
```python
python manage.py migrate
```

8. Database set is finished.
Enter the following command and the application should start.
```python
python manage.py runserver
```

9. If  you get the following message, it is working.
```python
Starting development server at http://127.0.0.1:8000/
```


 

