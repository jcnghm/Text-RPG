from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from rpg_app.forms import UserLoginForm, characterCreationForm
from rpg_app.models import User,db, Character
from rpg_app.character_creator import createCharacter

#  Imports for Flask Login
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)
            user = User(email, password = password)
            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'user-created')

            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please Check Your Form')

    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET','POST'])
def signin():

    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            print(email,password)

            logged_user = User.query.filter(User.email==email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successfully logged in', 'auth-success')
                return redirect(url_for('site.profile'))

            else:
                flash('Your Email/Password is incorrect', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form')
    return render_template('signin.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))

@auth.route('/ownedCharacters', methods = ['GET', 'POST'])
@login_required
def owned():
    owner = current_user.token
    characters = Character.query.filter_by(user_token = owner).all()

    # Create a random character for db
    # character_form = characterCreationForm()

    # try:
    #     if request.method == 'POST' and character_form.validate_on_submit():
    #         new_character = createCharacter()
    #         name = new_character.random_name.data
    #         race = new_character.random_race.data
    #         class_type = new_character.random_class.data
    #         strength = new_character.strength.data
    #         dexterity = new_character.dexterity.data
    #         intelligence = new_character.intelligence.data
    #         vitality = new_character.vitality.data
    #         primary_ability = new_character.primary_ability.data
    #         racial_ability = new_character.racial_ability.data
    #         racial_weapon = new_character.racial_weapon.data


    #         character = Character(name, race, class_type, strength, dexterity, intelligence, vitality, primary_ability, racial_ability, racial_weapon)
    #         db.session.add(character)
    #         db.session.commit()

    #         return redirect(url_for('auth.ownedCharacters'))
    
    # except:
    #     raise Exception('Invalid Form Data: Please Check Your Form')


    return render_template('ownedCharacters.html', characters = characters, owner = owner)


