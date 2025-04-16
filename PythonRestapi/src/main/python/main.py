#Every comment in this file starts with capital letter
#Import statement on it's own line and very top of the file
#Absolute imports used in this project to make it clear where things are coming from
from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy


#Two blank lines to separate import and variables
app = Flask(__name__)
#For config keys as per PEP8 all are entered in Caps
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

#One blank line to separate variables and database
db = SQLAlchemy(app)


#Two blank lines to separate database and class
#PascalCase used for class name and no underscore used 
class Destination(db.Model):
    #4 spaces for every level of indentation
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating =  db.Column(db.String(50), nullable=False)

    #Used one blank line to separate method definitions inside a class.
    def to_dict(self):
        return{
            #4 spaces for every level of indentation
            #For class attributes id, destination, country, rating snake_case is used
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating":self.rating
        }


#Two blank lines to separate from class
#DB tables
with app.app_context():
    #4 spaces for every level of indentation
    db.create_all()

#Two blank lines to separate from DB tables
#Routes
@app.route("/")
def home():
    #4 spaces for every level of indentation
    return jsonify({"message":"Welcome to the Travel API"})


#Two blank lines to separate from routes
@app.route("/destinations", methods=["GET"])
def get_destinations():
    #4 spaces for every level of indentation
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])


#Two blank lines to separate from above GET method
@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    #4 spaces for every level of indentation
    destination = Destination.query.get(destination_id)
    if destination:
        #4 spaces for every level of indentation
        return jsonify(destination.to_dict())
    else:
        #4 spaces for every level of indentation
        return jsonify(("error:Destination not found!")), 404


#Two blank lines to separate from above GET method
@app.route("/destinations", methods=["POST"])
def add_destination():
    #4 spaces for every level of indentation
    data = request.get_json()

    #One blank line to separate from variable
    #4 spaces for every level of indentation
    #Line of code is too long so hanging indent used 
    new_destination = Destination(
        destination=data["destination"],
        country=data["country"],
        rating=data['rating']
        )
    
    #One blank line to separate from variable
    #4 spaces for every level of indentation
    db.session.add(new_destination)
    db.session.commit()

    #One blank line to separate from variable
    #4 spaces for every level of indentation
    return jsonify(new_destination.to_dict()), 201


#Two blank lines to separate from above POST method
@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    #4 spaces for every level of indentation
    data = request.get_json()
    destination = Destination.query.get(destination_id)

    #One blank line to separate from variables
    #4 spaces for every level of indentation
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)
        #4 spaces for every level of indentation
        db.session.commit()
        return jsonify(destination.to_dict())
    else:
        #4 spaces for every level of indentation
        return jsonify({"error":"Destination not found"}), 404


#Two blank lines to separate from above PUT method
@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        # 4 spaces for every level of indentation
        db.session.delete(destination)
        db.session.commit()
        # 4 spaces for every level of indentation
        return jsonify({"message": "destination was deleted"})
    else:
        #4 spaces for every level of indentation
        return jsonify({"error":"Destination not found"}), 404


#Two blank lines above a top-level call
if __name__  == "__main__":
    #4 spaces for every level of indentation
    app.run(debug=True)
