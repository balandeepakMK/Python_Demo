#Absolute imports used in this project to make it clear where things are coming from
#Flask: Main web framework
#jsonify: Converts Python dicts/lists to JSON responses
#request: Accesses incoming request data
from flask import Blueprint, jsonify, request 


from controllers import (
    get_all_destinations,
    get_destination_by_id,
    create_destination,
    update_destination,
    delete_destination
)

destination_bp = Blueprint("destination", __name__)


@destination_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message":"Welcome to the Travel API"})
#Returns a welcome message.


@destination_bp.route("/destinations", methods=["GET"])
def get_destinations_view():
        return jsonify(get_all_destinations())


#Two blank lines to separate from above GET method
@destination_bp.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination_view(destination_id):
      dest = get_destination_by_id(destination_id)
      if dest:
        #4 spaces for every level of indentation
        return jsonify(dest.to_dict())
      else:
        return jsonify(("error:Destination not found!")), 404
#Takes an ID from the URL
#Returns that destination or a 404 if not found.


@destination_bp.route("/destinations", methods=["POST"])
def add_destination_view():
    data = request.get_json()
    new_destionation = create_destination(data)
    return jsonify(new_destionation.to_dict()), 201


@destination_bp.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination_view(destination_id):
    data = request.get_json()
    updated = update_destination(destination_id, data)
    if updated:
        return jsonify(updated.to_dict())
    return jsonify({"error": "Destination not found"}), 404

@destination_bp.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination_view(destination_id):
    deleted = delete_destination(destination_id)
    if deleted:
        return jsonify({"message": "Destination was deleted"})
    return jsonify({"error": "Destination not found"}), 404