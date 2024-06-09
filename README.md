# Facebean
## A messaging service built with Python and Django

Facebean is the messaging service used by the citizens of Beanotown. 

## How it work

This was my first time working with Django so I followed various tutorials to reach MVP: a page that displayed all messages stored in a database.

As it was a small project I decided to use SQL Lite rather than MySQL or PostgreSQL. I used [DB Browser for SQLite](https://sqlitebrowser.org/) to open the database file generated. 

The app displays messages the five most recent messages sent by the inhabitants of [Beanotown](https://www.beano.com/categories/beanotown) to each other. The jokes were topical when I wrote them.

The project is structured as follows: first I created a local development environment. Within this I created a Django project called 'mysite' and within this I created the Facebean app. 

![image](https://github.com/aagb1884/python_framework_test/assets/113289014/57d7ec5b-7710-4b2d-ab57-69bdadc654c1)

The API was tested programmatically and via Postman:
![image](https://github.com/aagb1884/python_framework_test/assets/113289014/84d42321-f85b-4a8e-91d5-f488111e86d5)

I installed [Django REST framework](https://www.django-rest-framework.org/) using the terminal (though other options are available, see link for details).
```
pip install djangorestframework
```


## Get it working locally

1. Create a folder on your computer and move into it.
2. Using the Command Prompt/Terminal, check if you have Python installed with 'python -V'
   *NB. You may have to type 'python3' if 'python' isn't recognised as a command.
  
4. Create and then activate a virtual environment for your project [(click here for instructions)](https://docs.python.org/3/tutorial/venv.html).
  * When you have activated a virtual environment you will see the name you've given it appear on the left of the terminal.
    
4. Install Django in the project with the command:
    ```
    python -m pip install Django
    ```
5. Clone this repository into the Virtual Environment
   ```
   git clone git@github.com:aagb1884/python_framework_test.git
   cd python_framework_test
   ```
6. Move into the 'mysite' folder and then run
   ```
   python manage.py migrate
   ```
   * If you get the error "No module named 'rest_framework'" here try moving up a folder and then running
   ```
   pip3 install djangorestframework
   ```
7. Once you've successfully run migrate, you can run the server:
   ```
   python manage.py runserver
   ```
You will be able to find the main page at [http://localhost:8000/facebean/](http://localhost:8000/facebean/).

There will not be any messages there to begin with, but there is a file with suggested messages. You can add these or your own using:
* [The form on the API endpoint](http://localhost:8000/api/messages).
* [Postman](https://www.postman.com/)/[Insomnia](https://insomnia.rest/)
* SQL
* [Python Shell](https://docs.djangoproject.com/en/5.0/intro/tutorial02/#playing-with-the-api):
  ```
  python manage.py shell
  ``` 
NB. Cloning this repo will include images you can use for the user avatars.


Further advice on starting a Django project [can be found here](https://docs.djangoproject.com/en/5.0/intro/tutorial01/).
