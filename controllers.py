#Every comment in this file starts with capital letter
#Import statement on it's own line and very top of the file
from models import Destination, db

def get_all_destinations():
    #4 spaces for every level of indentation
    return (destination.to_dict() for destination in Destination.query.all())
#Queries all rows in the Destination table
#Returns a list of destination dictionaries

def get_destination_by_id(destination_id):
    #4 spaces for every level of indentation
    return Destination.query.get(destination_id)

def create_destination(data):
    new_destination = Destination(
        destination=data["destination"],
        country=data["country"],
        rating=data['rating']
    )

    #One blank line to separate from variable
    #4 spaces for every level of indentation
    db.session.add(new_destination)
    db.session.commit()
    return new_destination

def update_destination(destination_id, data):
    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)
        db.session.commit()
    return destination

def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
    return destination
