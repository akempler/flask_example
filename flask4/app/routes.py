from flask import Blueprint, render_template

bp = Blueprint("routes", __name__)

@bp.route('/')
def index():
    return render_template('welcome.html') 

@bp.route('/about')
def about():
    return render_template('about.html')
