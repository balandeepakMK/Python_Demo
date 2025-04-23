#Every comment in this file starts with capital letter
#Import statement on it's own line and very top of the file
#Swagger: Adds documentation UI at /apidocs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from models import db
from views import destination_bp


#Two blank lines to separate import and variables
#Initialize the app and Swagger
app = Flask(__name__)
#Connects to a MySQL database called travel (on localhost).
#For config keys as per PEP8 all are entered in Caps
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost:3306/travel"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
swagger = Swagger(app)


#Two blank lines to separate from class
#DB tables
with app.app_context():
    #4 spaces for every level of indentation
    db.create_all()

app.register_blueprint(destination_bp)


#Two blank lines above a top-level call
if __name__  == "__main__":
    #4 spaces for every level of indentation
    app.run(debug=True)
#Starts the Flask server in debug mode when you run the script