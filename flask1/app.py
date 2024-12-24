# Importing the Flask class from the flask module
from flask import Flask

# Creating a global instance of the Flask class
app = Flask(__name__)

# Defining a route for the root URL ("/")
@app.route("/")
def index():
    return "<p>Welcome to the home page</p>"

# Defining a route for the about page ("/about")
@app.route("/about")
def about():
    return "<p>All about us</p>"

# Running the Flask application
if __name__ == "__main__":
    app.run(debug=True)