"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200
@app.route('/members', methods=['POST'])
def handle_add():
    request_body= request.json
    members= jackson_family.add_member(request_body)
    response= jsonify(members)
    return response, 200

@app.route('/members/<int:member_id>', methods=['GET'])
def handle_one_member(member_id):
    member= jackson_family.get_member(member_id)
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
def member_delete(member_id):
    member= jackson_family.delete_member(member_id)
    if member == "Member Not Found":
        return jsonify(member), 400
    
    return jsonify(member), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
