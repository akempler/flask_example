# Flask 4

This one uses a ```run.py``` file to run the application. 

This example follows the [Flask documentation](https://flask.palletsprojects.com/en/stable/quickstart/)

We break out the app into a separate packages for the main functionality and the admin functionality. 

A base template is used to define the layout of the app. The other templates extend this base template. 

## Running the app

Run the application with the following command:

```
python run.py
```

Or run the application using the Flask application factory pattern:  
[Flask documentation](https://flask.palletsprojects.com/en/stable/patterns/appfactories/)
 

```
python -m flask run
```

 Or

```
flask run
```
Note, if you use a different name for the app (other than app.py), you need to specify the name of the app:

```
flask --app hello run
```

This will run the application and display "Hello, World!" when you visit the root URL.
It runs on port 5000 by default:  
http://127.0.0.1:5000 

To run the application on a different port, you can use the following command:

```
flask --app hello run --port 5001
```

For more information, see the [Flask documentation](https://flask.palletsprojects.com/en/stable/quickstart/).