from flask import Blueprint, request, jsonify, render_template
from rpg_app.helpers import token_required
from rpg_app.models import db, User, Character, character_schema, characters_schema



api = Blueprint('api', __name__, url_prefix = '/api')


@api.route('/characters', methods = ['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    race = request.json['race']
    class_type = request.json['class_type']
    strength = request.json['strength']
    dexterity = request.json['dexterity']
    intelligence= request.json['intelligence']
    vitality = request.json['vitality']
    primary_ability = request.json['primary_ability']
    racial_ability = request.json['racial_ability']
    racial_weapon = request.json['racial_weapon']
    user_token = current_user_token.token
    character = Character(name, race, class_type, strength, dexterity, intelligence, vitality, primary_ability, racial_ability, racial_weapon, user_token)
    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)


@api.route('/characters', methods = ['GET'])
@token_required
def get_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)




@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)