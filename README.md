# Hirate
This is simple rest service developed using Django Rest framework.

### Installation
- Prerequisite: Python 3.x (3.8.10)
- All the required python libraries are listed in requirements.txt file. Run the following to install them
    ```
    pip install -r requirements.txt
    ```
- Run the migrations and start server. Before that review and rewrite (if required) the DB details in `hirate\settings.py` file 
    ```
    python manage.py migrate
    python manage.py runserver
    ```
- Create a super user for admin login and create an Application object (the client_id and client_secert of this application object will be required in oauth token)

### API
All the api endpoints and the formatted responses are present `Hirate API.postman_collection.json` file. All apis requires oauth token except SignUp api and token api.
