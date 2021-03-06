from flask import Blueprint, render_template
from flask_login.utils import login_required
from rpg_app.models import db, User, Character, character_schema, characters_schema

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')