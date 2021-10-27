from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow




db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# User Creation

class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    new_character = db.relationship('Character', backref = 'owner', lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify


    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database.'



# Character Creation Storage

class Character(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150))
    race = db.Column(db.String(150))
    class_type = db.Column(db.String(150))
    strength = db.Column(db.String(4))
    dexterity = db.Column(db.String(4))
    intelligence = db.Column(db.String(4))
    vitality = db.Column(db.String(4))
    primary_ability = db.Column(db.String(150))
    racial_ability = db.Column(db.String(150))
    racial_weapon = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, race, class_type, strength, dexterity, intelligence, vitality, primary_ability, racial_ability, racial_weapon, user_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.race = race
        self.class_type = class_type
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.vitality = vitality
        self.primary_ability = primary_ability
        self.racial_ability = racial_ability
        self.racial_weapon = racial_weapon
        self.user_token = user_token

    def __repr__(self):
        return f'New {self.race} {self.class_type} created, named {self.name}!\nWith Character Stats:\nStrength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}\nRacial Ability: {self.racial_ability}\nSpecial {self.race} Weaponry: {self.racial_weapon}'
        
    def set_id(self):
        return secrets.token_urlsafe()


class CharacterSchema(ma.Schema):
    class Meta:
        fields = ['id','name', 'race', 'class_type', 'strength', 'dexterity', 'intelligence', 'vitality','primary_ability', 'racial_ability', 'racial_weapon']

character_schema = CharacterSchema()

characters_schema = CharacterSchema(many=True)