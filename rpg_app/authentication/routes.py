from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from rpg_app.forms import UserLoginForm
from rpg_app.models import User,db, Character, character_schema
import random
from rpg_app.class_race_data import RACES, CLASSES, NAMES, DWARF_ABILITIES, DWARF_WEAPONS, HUMAN_ABILITIES, HUMAN_WEAPONS, ELF_ABILITIES, ELF_WEAPONS, DRAGONBORN_ABILITIES, DRAGONBORN_WEAPONS, TAUREN_ABILITES, TAUREN_WEAPONS, ORC_ABILITIES, ORC_WEAPONS 
from rpg_app.class_abilities import BARD_ABILITIES, DRUID_ABILITIES, PALADIN_ABILITIES, MAGUS_ABILITIES, RANGER_ABILITIES, WARRIOR_ABILITIES

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

    return render_template('ownedCharacters.html', characters = characters, owner = owner)

@auth.route("/delete/<id>", methods = ['GET', 'DELETE'])
@login_required
def delete(id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for("auth.owned"))


@auth.route("/add", methods=["POST"])
@login_required
def add():
    owner = current_user.token
    random_race = random.choice(RACES)
    random_class = random.choice(CLASSES)
    random_name = random.choice(NAMES)

    # Dwarf Creation
    if random_race.lower() == "dwarf":
        class_racial_ability = random.choice(DWARF_ABILITIES)
        class_racial_weapon = random.choice(DWARF_WEAPONS)
        # Warrior Class
        if random_class.lower() == "warrior":
            class_strength = random.randint(70, 90)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(20, 40)
            class_vitality = random.randint(70, 90)
            class_ability = random.choice(WARRIOR_ABILITIES) 
        # Bard Class
        elif random_class.lower() == "bard":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 60) 
            class_ability = random.choice(BARD_ABILITIES)
        # Druid Class
        elif random_class.lower() == "druid":
            class_strength = random.randint(70, 85)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(70, 90) 
            class_ability = random.choice(DRUID_ABILITIES)
        # Magus Class
        elif random_class.lower() == "magus":
            class_strength = random.randint(20, 30)
            class_dexterity = random.randint(20, 30)
            class_intelligence = random.randint(80, 100)
            class_vitality = random.randint(40, 50)  
            class_ability = random.choice(MAGUS_ABILITIES)
        # Paladin Class
        elif random_class.lower() == "paladin":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 50)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(50, 70)  
            class_ability = random.choice(PALADIN_ABILITIES)
        # Ranger Class
        elif random_class.lower() == "ranger":
            class_strength = random.randint(40, 60)
            class_dexterity = random.randint(80, 100)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 70) 
            class_ability = random.choice(RANGER_ABILITIES) 

    # Elf Creation        
    if random_race.lower() == "elf":
        class_racial_ability = random.choice(ELF_ABILITIES)
        class_racial_weapon = random.choice(ELF_WEAPONS)

        # Warrior Class
        if random_class.lower() == "warrior":
            class_strength = random.randint(70, 90)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(20, 40)
            class_vitality = random.randint(70, 90)
            class_ability = random.choice(WARRIOR_ABILITIES) 
        # Bard Class
        elif random_class.lower() == "bard":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 60) 
            class_ability = random.choice(BARD_ABILITIES)
        # Druid Class
        elif random_class.lower() == "druid":
            class_strength = random.randint(70, 85)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(70, 90) 
            class_ability = random.choice(DRUID_ABILITIES)
        # Magus Class
        elif random_class.lower() == "magus":
            class_strength = random.randint(20, 30)
            class_dexterity = random.randint(20, 30)
            class_intelligence = random.randint(80, 100)
            class_vitality = random.randint(40, 50)  
            class_ability = random.choice(MAGUS_ABILITIES)
        # Paladin Class
        elif random_class.lower() == "paladin":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 50)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(50, 70)  
            class_ability = random.choice(PALADIN_ABILITIES)
        # Ranger Class
        elif random_class.lower() == "ranger":
            class_strength = random.randint(40, 60)
            class_dexterity = random.randint(80, 100)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 70) 
            class_ability = random.choice(RANGER_ABILITIES) 

    # Human Generation
    if random_race.lower() == "human":
        class_racial_ability = random.choice(HUMAN_ABILITIES)
        class_racial_weapon = random.choice(HUMAN_WEAPONS)
        # Warrior Class
        if random_class.lower() == "warrior":
            class_strength = random.randint(70, 90)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(20, 40)
            class_vitality = random.randint(70, 90)
            class_ability = random.choice(WARRIOR_ABILITIES) 
        # Bard Class
        elif random_class.lower() == "bard":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 60) 
            class_ability = random.choice(BARD_ABILITIES)
        # Druid Class
        elif random_class.lower() == "druid":
            class_strength = random.randint(70, 85)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(70, 90) 
            class_ability = random.choice(DRUID_ABILITIES)
        # Magus Class
        elif random_class.lower() == "magus":
            class_strength = random.randint(20, 30)
            class_dexterity = random.randint(20, 30)
            class_intelligence = random.randint(80, 100)
            class_vitality = random.randint(40, 50)  
            class_ability = random.choice(MAGUS_ABILITIES)
        # Paladin Class
        elif random_class.lower() == "paladin":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 50)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(50, 70)  
            class_ability = random.choice(PALADIN_ABILITIES)
        # Ranger Class
        elif random_class.lower() == "ranger":
            class_strength = random.randint(40, 60)
            class_dexterity = random.randint(80, 100)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 70) 
            class_ability = random.choice(RANGER_ABILITIES) 

    # Dragonborn Generation
    if random_race.lower() == "dragonborn":
        class_racial_ability = random.choice(DRAGONBORN_ABILITIES)
        class_racial_weapon = random.choice(DRAGONBORN_WEAPONS) 
        # Warrior Class
        if random_class.lower() == "warrior":
            class_strength = random.randint(70, 90)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(20, 40)
            class_vitality = random.randint(70, 90)
            class_ability = random.choice(WARRIOR_ABILITIES) 
        # Bard Class
        elif random_class.lower() == "bard":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 60) 
            class_ability = random.choice(BARD_ABILITIES)
        # Druid Class
        elif random_class.lower() == "druid":
            class_strength = random.randint(70, 85)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(70, 90) 
            class_ability = random.choice(DRUID_ABILITIES)
        # Magus Class
        elif random_class.lower() == "magus":
            class_strength = random.randint(20, 30)
            class_dexterity = random.randint(20, 30)
            class_intelligence = random.randint(80, 100)
            class_vitality = random.randint(40, 50)  
            class_ability = random.choice(MAGUS_ABILITIES)
        # Paladin Class
        elif random_class.lower() == "paladin":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 50)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(50, 70)  
            class_ability = random.choice(PALADIN_ABILITIES)
        # Ranger Class
        elif random_class.lower() == "ranger":
            class_strength = random.randint(40, 60)
            class_dexterity = random.randint(80, 100)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 70) 
            class_ability = random.choice(RANGER_ABILITIES) 

    # Orc Generation
    if random_race.lower() == "orc":
        class_racial_ability = random.choice(ORC_ABILITIES)
        class_racial_weapon = random.choice(ORC_WEAPONS) 
        # Warrior Class
        if random_class.lower() == "warrior":
            class_strength = random.randint(70, 90)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(20, 40)
            class_vitality = random.randint(70, 90)
            class_ability = random.choice(WARRIOR_ABILITIES) 
        # Bard Class
        elif random_class.lower() == "bard":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 60) 
            class_ability = random.choice(BARD_ABILITIES)
        # Druid Class
        elif random_class.lower() == "druid":
            class_strength = random.randint(70, 85)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(70, 90) 
            class_ability = random.choice(DRUID_ABILITIES)
        # Magus Class
        elif random_class.lower() == "magus":
            class_strength = random.randint(20, 30)
            class_dexterity = random.randint(20, 30)
            class_intelligence = random.randint(80, 100)
            class_vitality = random.randint(40, 50)  
            class_ability = random.choice(MAGUS_ABILITIES)
        # Paladin Class
        elif random_class.lower() == "paladin":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 50)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(50, 70)  
            class_ability = random.choice(PALADIN_ABILITIES)
        # Ranger Class
        elif random_class.lower() == "ranger":
            class_strength = random.randint(40, 60)
            class_dexterity = random.randint(80, 100)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 70) 
            class_ability = random.choice(RANGER_ABILITIES) 

    # Tauren Generation
    if random_race.lower() == "tauren":
        class_racial_ability = random.choice(TAUREN_ABILITES)
        class_racial_weapon = random.choice(TAUREN_WEAPONS)  
        # Warrior Class
        if random_class.lower() == "warrior":
            class_strength = random.randint(70, 90)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(20, 40)
            class_vitality = random.randint(70, 90)
            class_ability = random.choice(WARRIOR_ABILITIES) 
        # Bard Class
        elif random_class.lower() == "bard":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 60) 
            class_ability = random.choice(BARD_ABILITIES)
        # Druid Class
        elif random_class.lower() == "druid":
            class_strength = random.randint(70, 85)
            class_dexterity = random.randint(40, 60)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(70, 90) 
            class_ability = random.choice(DRUID_ABILITIES)
        # Magus Class
        elif random_class.lower() == "magus":
            class_strength = random.randint(20, 30)
            class_dexterity = random.randint(20, 30)
            class_intelligence = random.randint(80, 100)
            class_vitality = random.randint(40, 50)  
            class_ability = random.choice(MAGUS_ABILITIES)
        # Paladin Class
        elif random_class.lower() == "paladin":
            class_strength = random.randint(50, 70)
            class_dexterity = random.randint(40, 50)
            class_intelligence = random.randint(60, 80)
            class_vitality = random.randint(50, 70)  
            class_ability = random.choice(PALADIN_ABILITIES)
        # Ranger Class
        elif random_class.lower() == "ranger":
            class_strength = random.randint(40, 60)
            class_dexterity = random.randint(80, 100)
            class_intelligence = random.randint(40, 60)
            class_vitality = random.randint(50, 70) 
            class_ability = random.choice(RANGER_ABILITIES) 


    name = random_name.title()
    race = random_race.title()
    class_type = random_class.title()
    strength = class_strength
    dexterity = class_dexterity
    intelligence = class_intelligence
    vitality = class_vitality
    primary_ability = class_ability
    racial_ability = class_racial_ability
    racial_weapon = class_racial_weapon

    new_character = Character(name, race, class_type, strength, dexterity, intelligence, vitality, primary_ability, racial_ability, racial_weapon, owner)
    db.session.add(new_character)
    db.session.commit()
    flash("New Character Created")

    return redirect(url_for('auth.owned'))


