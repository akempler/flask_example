# Importing the Flask class from the flask module
from flask import Flask, render_template

# Creating an instance of the Flask class
app = Flask(__name__)

# Defining a route for the root URL ("/")
@app.route("/")
def index():
    # Because this is just a module, the template file is in the root of the templates folder.
    # SEE: https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates 
    return render_template("welcome.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Running the Flask application
if __name__ == "__main__":
    app.run(debug=True)