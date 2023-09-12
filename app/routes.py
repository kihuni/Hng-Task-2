from flask import request, jsonify
from app import app, db
from app.models import Person


@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    name = data.get('name')
    if not isinstance(name, str):
        return jsonify({"error": "Invalid input"}), 400
    
    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return jsonify({"message": "Person added", "person_id": person.id}), 201

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get_or_404(user_id)
    return jsonify({"id": person.id, "name": person.name}), 200

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get_or_404(user_id)
    data = request.json
    new_name = data.get('name')
    if not isinstance(new_name, str):
        return jsonify({"error": "Invalid input"}), 400
    
    person.name = new_name
    db.session.commit()
    return jsonify({"message": "Person updated", "new_name": new_name}), 200

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get_or_404(user_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted"}), 200

        