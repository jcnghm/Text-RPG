# Random Fantasy Character Generator

import random
from rpg_app.class_race_data import RACES, CLASSES, NAMES, DWARF_ABILITIES, DWARF_WEAPONS, HUMAN_ABILITIES, HUMAN_WEAPONS, ELF_ABILITIES, ELF_WEAPONS, DRAGONBORN_ABILITIES, DRAGONBORN_WEAPONS, TAUREN_ABILITES, TAUREN_WEAPONS, ORC_ABILITIES, ORC_WEAPONS 
from rpg_app.class_abilities import BARD_ABILITIES, DRUID_ABILITIES, PALADIN_ABILITIES, MAGUS_ABILITIES, RANGER_ABILITIES, WARRIOR_ABILITIES
    
class newCharacter():

    def __init__(self, name, race):
        self.name = name
        self.race = race

    def createWarrior(self):
        self.strength = random.randint(70, 90)
        self.dexterity = random.randint(40, 60)
        self.intelligence = random.randint(20, 40)
        self.vitality = random.randint(70, 90)
        self.primary_ability = random.choice(WARRIOR_ABILITIES) 
        return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}'   

    def createBard(self):
        self.strength = random.randint(50, 70)
        self.dexterity = random.randint(40, 60)
        self.intelligence = random.randint(40, 60)
        self.vitality = random.randint(50, 60) 
        self.primary_ability = random.choice(BARD_ABILITIES) 
        return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}'  

    def createDruid(self):
        self.strength = random.randint(70, 85)
        self.dexterity = random.randint(40, 60)
        self.intelligence = random.randint(60, 80)
        self.vitality = random.randint(70, 90) 
        self.primary_ability = random.choice(DRUID_ABILITIES) 
        return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}' 

    def createMagus(self):
        self.strength = random.randint(20, 30)
        self.dexterity = random.randint(20, 30)
        self.intelligence = random.randint(80, 100)
        self.vitality = random.randint(40, 50)  
        self.primary_ability = random.choice(MAGUS_ABILITIES)
        return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}' 

    def createPaladin(self):
        self.strength = random.randint(50, 70)
        self.dexterity = random.randint(40, 50)
        self.intelligence = random.randint(60, 80)
        self.vitality = random.randint(50, 70)  
        self.primary_ability = random.choice(PALADIN_ABILITIES)
        return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}' 

    def createRanger(self):
        self.strength = random.randint(40, 60)
        self.dexterity = random.randint(80, 100)
        self.intelligence = random.randint(40, 60)
        self.vitality = random.randint(50, 70) 
        self.primary_ability = random.choice(RANGER_ABILITIES) 
        return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nVitality: {self.vitality}\nPrimary Ability: {self.primary_ability}'

def createCharacter():

        random_race = random.choice(RACES)
        random_class = random.choice(CLASSES)
        random_name = random.choice(NAMES)

        # Dwarf Generation
        if random_race.lower() == "dwarf":
            racial_ability = random.choice(DWARF_ABILITIES)
            racial_weapon = random.choice(DWARF_WEAPONS)   

            # Warrior Class
            if random_class.lower() == "warrior":
                warrior = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(warrior.createWarrior())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Bard Class
            elif random_class.lower() == "bard":
                bard = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(bard.createBard())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Druid Class
            elif random_class.lower() == "druid":
                druid = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(druid.createDruid())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Magus Class
            elif random_class.lower() == "magus":
                magus = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(magus.createMagus())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Paladin Class
            elif random_class.lower() == "paladin":
                paladin = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(paladin.createPaladin())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Ranger Class
            elif random_class.lower() == "ranger":
                ranger = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(ranger.createRanger())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}') 
        
        # Elf Generation
        if random_race.lower() == "elf":
            racial_ability = random.choice(ELF_ABILITIES)
            racial_weapon = random.choice(ELF_WEAPONS)  

            # Warrior Class
            if random_class.lower() == "warrior":
                warrior = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(warrior.createWarrior())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Bard Class
            elif random_class.lower() == "bard":
                bard = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(bard.createBard())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Druid Class
            elif random_class.lower() == "druid":
                druid = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(druid.createDruid())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Magus Class
            elif random_class.lower() == "magus":
                magus = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(magus.createMagus())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Paladin Class
            elif random_class.lower() == "paladin":
                paladin = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(paladin.createPaladin())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Ranger Class
            elif random_class.lower() == "ranger":
                ranger = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(ranger.createRanger())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}') 

        # Human Generation
        if random_race.lower() == "human":
            racial_ability = random.choice(HUMAN_ABILITIES)
            racial_weapon = random.choice(HUMAN_WEAPONS)  

            # Warrior Class
            if random_class.lower() == "warrior":
                warrior = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(warrior.createWarrior())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Bard Class
            elif random_class.lower() == "bard":
                bard = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(bard.createBard())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Druid Class
            elif random_class.lower() == "druid":
                druid = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(druid.createDruid())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Magus Class
            elif random_class.lower() == "magus":
                magus = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(magus.createMagus())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Paladin Class
            elif random_class.lower() == "paladin":
                paladin = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(paladin.createPaladin())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Ranger Class
            elif random_class.lower() == "ranger":
                ranger = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(ranger.createRanger())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}') 

        # Dragonborn Generation
        if random_race.lower() == "dragonborn":
            racial_ability = random.choice(DRAGONBORN_ABILITIES)
            racial_weapon = random.choice(DRAGONBORN_WEAPONS)  

            # Warrior Class
            if random_class.lower() == "warrior":
                warrior = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(warrior.createWarrior())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Bard Class
            elif random_class.lower() == "bard":
                bard = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(bard.createBard())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Druid Class
            elif random_class.lower() == "druid":
                druid = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(druid.createDruid())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Magus Class
            elif random_class.lower() == "magus":
                magus = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(magus.createMagus())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Paladin Class
            elif random_class.lower() == "paladin":
                paladin = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(paladin.createPaladin())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Ranger Class
            elif random_class.lower() == "ranger":
                ranger = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(ranger.createRanger())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}') 

        # Orc Generation
        if random_race.lower() == "orc":
            racial_ability = random.choice(ORC_ABILITIES)
            racial_weapon = random.choice(ORC_WEAPONS)  

            # Warrior Class
            if random_class.lower() == "warrior":
                warrior = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(warrior.createWarrior())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Bard Class
            elif random_class.lower() == "bard":
                bard = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(bard.createBard())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Druid Class
            elif random_class.lower() == "druid":
                druid = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(druid.createDruid())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Magus Class
            elif random_class.lower() == "magus":
                magus = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(magus.createMagus())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Paladin Class
            elif random_class.lower() == "paladin":
                paladin = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(paladin.createPaladin())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Ranger Class
            elif random_class.lower() == "ranger":
                ranger = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(ranger.createRanger())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}') 

        # Tauren Generation
        if random_race.lower() == "tauren":
            racial_ability = random.choice(TAUREN_ABILITES)
            racial_weapon = random.choice(TAUREN_WEAPONS)  

            # Warrior Class
            if random_class.lower() == "warrior":
                warrior = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(warrior.createWarrior())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Bard Class
            elif random_class.lower() == "bard":
                bard = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(bard.createBard())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Druid Class
            elif random_class.lower() == "druid":
                druid = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(druid.createDruid())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Magus Class
            elif random_class.lower() == "magus":
                magus = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(magus.createMagus())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Paladin Class
            elif random_class.lower() == "paladin":
                paladin = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(paladin.createPaladin())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}')
            # Ranger Class
            elif random_class.lower() == "ranger":
                ranger = newCharacter(random_name, random_race)
                print(f'New {random_race.title()} {random_class.title()} created, named {random_name.title()}')
                print("With Character Stats: ")
                print(ranger.createRanger())
                print(f'Special Racial Ability: {racial_ability}')
                print(f'Special {random_race} Weaponry: {racial_weapon}') 
               
character_list = {}

createCharacter()

    