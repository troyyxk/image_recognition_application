# Image Recognition Server Backend

## How to run?
1. Install the required libraries. See `requirements.txt` for details.
   Note currently `celery` is not added to `requirements.txt`. Celery is available on Linux systems ONLY.
2. Initialize the database.
    ```bash
    $ python manage.py migrate
    ```
3. Create a superuser.
    ```bash
    $ python manage.py createsuperuser
    ```
   Follow the instructions in the console to create a superuser.
4. Run development server.
    ```bash
    $ python manage.py runserver 0.0.0.0:8000
    ```
   
Now you can access the website at [http://127.0.0.1:8000](http://127.0.0.1:8000). You should see a 404 Not Found message.

## APIs
There are two functions defined in `recognition.views`. They are linked to 2 url paths defined in `back_end.urls`. These two functions have not been implement yet. Read both files for details.

The documentation of APIs is HERE.

## If you need to add / delete / alter a field in `models.py`
After you make your changes to that file, execute the following commands to apply your changes.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

If something goes wrong when migrating, follow the instructions in the console.
