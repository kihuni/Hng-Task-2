from flask import request, jsonify
from app import app, db
from app.models import Person
from sqlalchemy.exc import IntegrityError



@app.route('/')
def index():
    return "Welcome to my first API!"


@app.route('/api', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        new_person = Person(name=data['name'])
        db.session.add(new_person)
        db.session.commit()
        return jsonify({'message': 'New person added!'}), 201
    except IntegrityError:
        return jsonify({'message': 'Name already exists!'}), 400

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)
    if person:
        return jsonify({'name': person.name}), 200
    else:
        return jsonify({'message': 'Person not found!'}), 404

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get(user_id)
    if person:
        data = request.get_json()
        person.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Person updated!'}), 200
    else:
        return jsonify({'message': 'Person not found!'}), 404


@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted!'}), 200
    else:
        return jsonify({'message': 'Person not found!'}), 404

        