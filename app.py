from flask import Flask, request
from controller.authentication_controller import AuthenticationController
from config.db import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

auth_controller = AuthenticationController()


# configure the app with the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = Config.SQLALCHEMY_ECHO
app.config['SECRET_KEY'] = Config.SECRET_KEY

db = SQLAlchemy(app)


@app.post('/register')
def register_user():
    data = request.get_json()
    return auth_controller.register_user(data=data)


@app.post('/login')
def login_user():
    return auth_controller.login_user()


@app.post('/logout')
def logout_user():
    return auth_controller.logout_user()


if __name__ == '__main__':
    with app.app_context():
        try:
            # Explicitly test connection
            with db.engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                test_value = result.scalar()  # Get the value while connection is still open
                print("Database connection successful:", test_value)
                logging.info(
                    "✅ Database connection successful: %s", test_value)
        except Exception as e:
            logging.error("❌ Database connection failed: %s", e)
            raise

        # Now create tables if connection is fine
        db.create_all()
    app.run(debug=True)
