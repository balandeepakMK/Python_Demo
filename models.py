#Every comment in this file starts with capital letter
#Import statement on it's own line and very top of the file
#SQLAlchemy: ORM to handle database models and queries
from flask_sqlalchemy import SQLAlchemy

#One blank line to separate variables and database
#SQLAlchemy is initialized to manage models and queries.
db = SQLAlchemy()


#Two blank lines to separate database and class
#PascalCase used for class name and no underscore used 
#This defines a Destination table with 4 fields:
#id: Primary key
#destination: Name of the destination (e.g. Paris)
#country: Country name
#rating: Rating (e.g. 5 stars)
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