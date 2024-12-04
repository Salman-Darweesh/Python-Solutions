

import random

class Humanoid:
    def __init__(self, height, weight, hairColor, eyeColor, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self._height = height
        self._weight = weight
        self._hairColor = hairColor
        self._eyeColor = eyeColor
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma
        
        # Setters and Getters for BAse stats
    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_hair_color(self):
        return self._hair_color

    def set_hair_color(self, hair_color):
        self._hair_color = hair_color

    def get_eye_color(self):
        return self._eye_color

    def set_eye_color(self, eye_color):
        self._eye_color = eye_color

        # Setters and Getters for other stats Stats
    def get_strength(self):
        return self._strength

    def set_strength(self, strength):
        self._strength = strength

    def get_dexterity(self):
        return self._dexterity

    def set_dexterity(self, dexterity):
        self._dexterity = dexterity

    def get_constitution(self):
        return self._constitution

    def set_constitution(self, constitution):
        self._constitution = constitution

    def get_intelligence(self):
        return self._intelligence

    def set_intelligence(self, intelligence):
        self._intelligence = intelligence

    def get_wisdom(self):
        return self._wisdom

    def set_wisdom(self, wisdom):
        self._wisdom = wisdom

    def get_charisma(self):
        return self._charisma

    def set_charisma(self, charisma):
        self._charisma = charisma
        

    def random_stats_generator(self):
        self._strength = random.randint(1, 18)
        self._dexterity = random.randint(1, 18)
        self._constitution = random.randint(1, 18)
        self._intelligence = random.randint(1, 18)
        self._wisdom = random.randint(1, 18)
        self._charisma = random.randint(1, 18)
    
    
    
    # make 
    
def character_Creation():
    print("\n Welcome \n")
    print("---------")
    print("1: Human\n2: Elf\n3: Dwarf")
    print("_________\n")
    character_Choice = input("Please pick a character (1, 2, 3): ")
    height = float(input("Please enter a Height for your character (3ft - 7ft): "))
    weight = float(input("Please enter a Weight for your character (60lbs - 300lbs): "))
    hairColor = input("Please enter a Hair Color for your character (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde): ")
    eyeColor = input("Please enter an Eye Color for your character (white, black, red, green, blue, brown, purple, amber): ")
    
    
    
if __name__ in "__main__":
    character_Creation()
    