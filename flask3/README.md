# Flask 3

We use a Flask Blueprint to organize the application. 

The application exists in a package called ```app```.  
In Python, a subdirectory that includes a ```__init__.py``` file is considered a package.  

Instead of using a global Flask instance, we use an Application Factory to create the Flask app.

We also add a ```routes.py``` file to the ```app``` package to define the routes for the application.

## Running the app

Run the application with the following command:

```
python -m flask run
```

 Or

```
flask run
```

For more information, see the [Flask documentation](https://flask.palletsprojects.com/en/stable/quickstart/).