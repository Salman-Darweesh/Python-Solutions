

import random

    
class Humanoid:
    strength = ''
    dexterity = '' 
    constitution = '' 
    intelligence = ''
    wisdom = ''
    charisma = ''
    
    
    def __init__(self, height, weight, hairColor, eyeColor, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        
        # Setters and Getters for BAse stats
    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_hair_color(self):
        return self.hair_color

    def set_hair_color(self, hair_color):
        self.hair_color = hair_color

    def get_eye_color(self):
        return self.eye_color

    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

        # Setters and Getters for other stats Stats
    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_dexterity(self):
        return self.dexterity

    def set_dexterity(self, dexterity):
        self.dexterity = dexterity

    def get_constitution(self):
        return self.constitution

    def set_constitution(self, constitution):
        self.constitution = constitution

    def get_intelligence(self):
        return self.intelligence

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence

    def get_wisdom(self):
        return self.wisdom

    def set_wisdom(self, wisdom):
        self.wisdom = wisdom

    def get_charisma(self):
        return self.charisma

    def set_charisma(self, charisma):
        self.charisma = charisma
        

    def random_stats_generator(self):
        self._strength = random.randint(1, 18)
        self._dexterity = random.randint(1, 18)
        self._constitution = random.randint(1, 18)
        self._intelligence = random.randint(1, 18)
        self._wisdom = random.randint(1, 18)
        self._charisma = random.randint(1, 18)
        
    def showing_stats(self):
        print(f"Here are the stats for your character: ")
    
    
    
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
    