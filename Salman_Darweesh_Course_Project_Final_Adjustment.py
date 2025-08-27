import random

class Humanoid:
    # attributes, if given an attribute then it would be pointless to make the rest of the program
    strength = ''
    dexterity = '' 
    constitution = '' 
    intelligence = ''
    wisdom = ''
    charisma = ''
    
    def __init__(self, height, weight, hair_color, eye_color):#initializing all info for player
        self.height = height
        self.weight = weight
        self.haircolor = hair_color
        self.eyeColor = eye_color
        
        # Setters and Getters for BAse stats
    def get_height(self):   # This is where you access the info 
        return self.height

    def set_height(self, height):
        self.height = height        # Setting stat

    def get_weight(self):      # This is where you access the info 
        return self.weight      

    def set_weight(self, weight):
        self.weight = weight        # Setting stat

    def get_hair_color(self):   # This is where you access the info 
        return self.hair_color

    def set_hair_color(self, hair_color):
        self.hair_color = hair_color

    def get_eye_color(self):   # This is where you access the info 
        return self.eye_color        # Setting stat

    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

        # Setters and Getters for all the other stats
    def get_strength(self):   # This is where you access the info 
        return self.strength

    def set_strength(self, strength):
        self.strength = strength        # Setting stat

    def get_dexterity(self):   # This is where you access the info 
        return self.dexterity

    def set_dexterity(self, dexterity):
        self.dexterity = dexterity        # Setting stat

    def get_constitution(self):   # This is where you access the info 
        return self.constitution

    def set_constitution(self, constitution):
        self.constitution = constitution        # Setting stat

    def get_intelligence(self):   # This is where you access the info 
        return self.intelligence

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence        # Setting stat

    def get_wisdom(self):   # This is where you access the info 
        return self.wisdom

    def set_wisdom(self, wisdom):
        self.wisdom = wisdom        # Setting stat

    def get_charisma(self):   # This is where you access the info 
        return self.charisma

    def set_charisma(self, charisma):   # This is where you access the info 
        self.charisma = charisma        # Setting stat
    # Generate Random Stats
    def random_stats_generator(self):   # generating random values for the 6 base stats for all characters. also setting up the correct paremeters.
        self.strength = random.randint(1, 18)
        self.dexterity = random.randint(1, 18)
        self.constitution = random.randint(1, 18)
        self.intelligence = random.randint(1, 18)
        self.wisdom = random.randint(1, 18)
        self.charisma = random.randint(1, 18)

    # Humanoid Stat Bonus
    def choose_stat_bonus(self):
        user_stat = input("Please pick a stat you would like to get a +2 stat bonus (strength, dexterity, constitution, intelligence, wisdom, charisma): ").lower() # allowing the user to pick which stat they want to ge the bonus for, making sure its lower case.

        if user_stat == "strength":     # allowing the user to pick which stat they want to ge the bonus for
            self.strength += 2
        elif user_stat == "dexterity":
            self.dexterity += 2
        elif user_stat == "constitution":
            self.constitution += 2
        elif user_stat == "intelligence":
            self.intelligence += 2
        elif user_stat == "wisdom":
            self.wisdom += 2
        elif user_stat == "charisma":
            self.charisma += 2
        else:
            print("womp womp what you entered was wrong. :P ")      # error message.

    def display_stats(self):    # 1000% there could have been an easier way to do this but i stuck to this because somehow it worked? and i dont understand how lol 
        hair_color = self.hair_color
        eye_color = self.eye_color
        height = self.height
        weight = self.weight
        strength = self.strength
        dexterity = self.dexterity
        constitution = self.constitution
        intelligence = self.intelligence
        wisdom = self.wisdom
        charisma = self.charisma

        print("\nCharacter Stats for a Humanoid:")
        print(f"Hair Color: {hair_color} Eye Color: {eye_color} -- Height: {height}ft -- Weight: {weight}lbs")
        print(f"Strength: {strength} -- Dexterity: {dexterity} -- Constitution: {constitution} -- Intelligence: {intelligence}")
        print(f"Wisdom: {wisdom} -- Charisma: {charisma}")    # displaying the character stats


# Elf Class with Bonuses
class Elf(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color):    # inictializing the aesthetic parts of the character
        super().__init__(height, weight, hair_color, eye_color)
        self.resistance_to_sleep = "100% Resistance to Sleep, meaning that you cannot be put to sleep! :)"   # adding the bonus stat 

    def giving_user_a_bonus(self):
        self.dexterity += 2
        self.charisma += 2

    def display_stats(self):    # 1000% there could have been an easier way to do this but i stuck to this because somehow it worked? and i dont understand how lol 
        hair_color = self.hair_color
        eye_color = self.eye_color
        height = self.height
        weight = self.weight
        strength = self.strength
        dexterity = self.dexterity
        constitution = self.constitution
        intelligence = self.intelligence
        wisdom = self.wisdom
        charisma = self.charisma
        resistance_to_sleep = self.resistance_to_sleep

        print("\nCharacter Stats for an Elf:")
        print(f"Hair Color: {hair_color} Eye Color: {eye_color} -- Height: {height}ft -- Weight: {weight}lbs")
        print(f"Strength: {strength} -- Dexterity: {dexterity} -- Constitution: {constitution} -- Intelligence: {intelligence}")
        print(f"Wisdom: {wisdom} -- Charisma: {charisma}")
        print(f"Special Ability: {resistance_to_sleep}")    # displaying the character stats


#   creating a dwarf class while using the humanoid as the paremeter
class Dwarf(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color):    # inictializing the aesthetic parts of the character
        super().__init__(height, weight, hair_color, eye_color) 
        self.magic_resistance = "As a Dward you get 20% Resistance to Magic! :P (im a dwarf too)"   # adding the bonus stat 

    def giving_user_a_bonus(self):  # alsi addin the bonus stat that already exist
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2

    def display_stats(self):    # 1000% there could have been an easier way to do this but i stuck to this because somehow it worked? and i dont understand how lol 
        hair_color = self.hair_color
        eye_color = self.eye_color
        height = self.height
        weight = self.weight
        strength = self.strength
        dexterity = self.dexterity
        constitution = self.constitution
        intelligence = self.intelligence
        wisdom = self.wisdom
        charisma = self.charisma
        magic_resistance = self.magic_resistance

        print("\nCharacter Stats for a Dward:")
        print(f"Hair Color: {hair_color} Eye Color: {eye_color} -- Height: {height}ft -- Weight: {weight}lbs")
        print(f"Strength: {strength} -- Dexterity: {dexterity} -- Constitution: {constitution} -- Intelligence: {intelligence}")
        print(f"Wisdom: {wisdom} -- Charisma: {charisma}")
        print(f"Special Ability: {magic_resistance}")   # displaying the character stats


def character_Creation():   # character creation function
    print("\n Welcome \n")
    print("---------")
    print("1: Humanoid\n2: Elf\n3: Dwarf")  # character selection section
    print("_________\n")
    character_Choice = input("Please pick a character (1, 2, 3): ") #asking user for specific type of player.

    height = float(input("Please enter a Height for your character (3ft - 7ft): ")) #   asking user to stay withing certain perameters that were given in class 
    while height > 7.0 or height < 3.0:     # creating a while loop
        print("womp womp the hieght has to be between 3ft and 7ft.")
        height = float(input("Please enter a Height for your character (3ft - 7ft): "))

    weight = float(input("Please enter a Weight for your character (60lbs - 300lbs): "))
    while weight > 300.0 or weight < 60.0:     # creating a while loop
        print("womp womp the weight has to be between 60lbs and 300lbs.")
        weight = float(input("Please enter a Weight for your character (60lbs - 300lbs): "))#   asking user to stay withing certain perameters that were given in class 

    hair_color = input("Please enter a Hair Color for your character: ")    # making sure the variables stay the same.
    eye_color = input("Please enter an Eye Color for your character: ")

    if character_Choice == "2":
        character = Elf(height, weight, hair_color, eye_color)
        character.random_stats_generator() # Generating stats    # calling the function
        character.giving_user_a_bonus() #applying the bonus that was given to the user     # calling the function
        character.display_stats()#redisplaying the final stats    # calling the function

    elif character_Choice == "3":
        character = Dwarf(height, weight, hair_color, eye_color)
        character.random_stats_generator()# Generating stats    # calling the function
        character.giving_user_a_bonus()#applying the bonus that was given to the user     # calling the function
        character.display_stats() #redisplaying the final stats    # calling the function

    else: # having the first be humaanoid
        character = Humanoid(height, weight, hair_color, eye_color)
        character.random_stats_generator()# Generating stats    # calling the function
        character.choose_stat_bonus()#applying the bonus that was given to the user     # calling the function
        character.display_stats()#redisplaying the final stats    # calling the function


if __name__ == "__main__":
    character_Creation()# calling the function
    
    '''
    refrences:
    My Course Challenges from 5 - 12
    some videos as a refresher for how to init 'Python Tutorial for Beginners 25 - Python __init__ and self in class'
    textbook chapters 7-11

    '''