from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints here
    from app.routes import routes
    app.register_blueprint(routes)

    return app