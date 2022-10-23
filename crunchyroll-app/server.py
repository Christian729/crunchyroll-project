# This is the launch point for our app to be displayed online
# this is just a small edit
from flask_app.controllers import users
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)