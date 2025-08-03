from flask import Flask
from app.extensions import db
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(user_bp)

    return app
