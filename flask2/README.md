# Flask 2

Separate out the content into templates. 

## Running the app

Run the application by running the following command:

```
python app.py
```

Or

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