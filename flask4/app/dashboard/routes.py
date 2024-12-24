from flask import render_template
from app.dashboard import bp

@bp.route('/')
def dashboard():
    return render_template('dashboard/dashboard.html')

@bp.route('/stats')
def stats():
    # Add stats logic here
    return "Stats functionality will be implemented here"

@bp.route('/logs')
def logs():
    # Add logs logic here
    return "Logs functionality will be implemented here" 
