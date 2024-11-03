

# attributes, if given an attribute then it would be pointless to make the rest of the program
health = "" 
armor_rating = ""
attack_power = ""

class PlayerCharacter:  # creating a class for the player

    def __init__(self,health,armor_rating,attack_power):    #initializing all stats as private (safety reasons)
        self._health = health
        self._armor_rating = armor_rating
        self._attack_power = attack_power
        
                
    def set_health(self,_health):
        self.health = _health   #Setting stat

    def set_armor_rating(self,_armor_rating):
        self.armour_rating = _armor_rating      #Setting stat
        

    def set_attack_power(self,_attack_power):
        self.attack_power = _attack_power       #Setting stat

    def get_health(self):   #creating a function for the stat
        return self.health      # returning stat value

    def get_armor_rating(self):   #creating a function for the stat
        return self.armour_rating    # returning stat value

    def get_attack_power(self):   #creating a function for the stat
        return self.attack_power    # returning stat value

    def __str__(self):
        # shows user all details of the character with the values they choose
        return f"The Wizard has {self._health} health, power {self._attack_power}, and armour {self._armor_rating}"


def main():
    
    charac_Health = int(input("Enter a value for what you would like your player health to be (1-100): "))  #asking user to give us a value
    while charac_Health not in range(1, 101):   # creating a range loop that allows user to only enter a vlaue in a given rnage
        
        print("The value you have chosen is out of the required range, try again.")     # the error message given if the value is wrong 
        charac_Health = int(input("Enter a value for what you would like your player health to be (1-100): "))
    
    print(f"Char health of: {charac_Health}")     #reitterates whats the chosen value for the stat
    
    
            
    charac_Armor = int(input("Enter a value for what you would like your player health to be (1-20): "))  #asking user to give us a value
    while charac_Armor not in range(1, 21):   # creating a range loop that allows user to only enter a vlaue in a given rnage
        
        print("The value you have chosen is out of the required range, try again.")     # the error message given if the value is wrong 
        charac_Armor = int(input("Enter a value for what you would like your player health to be (1-20): "))
    
    print(f"Char armor of: {charac_Armor}")     #reitterates whats the chosen value for the stat
    
    
            
    charac_Power = int(input("Enter a value for what you would like your player armor to be (1-20): "))  #asking user to give us a value
    while charac_Power not in range(1, 21):   # creating a range loop that allows user to only enter a vlaue in a given rnage
        
        print("The value you have chosen is out of the required range, try again.")     # the error message given if the value is wrong 
        charac_Power = int(input("Enter a value for what you would like your player power to be (1-21): "))
        
    print(f"Char power of: {charac_Power}")     #reitterates whats the chosen value for the stat
    
    Wizard = PlayerCharacter(charac_Health, charac_Armor, charac_Power)     #where all values are taken to consideration for the class
        
    print(Wizard)   #printing output fo for all the values

if __name__ == "__main__":  # where the program starts
        main()     # calling the specific fuction to start
        
        
'''
Refrences: 
Class Lecture, and question asked after class
Module 7 
MOdule 9
ch10 book
''' 