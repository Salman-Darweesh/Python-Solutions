

# attributes
health = "" 
armor_rating = ""
attack_power = ""

class PlayerCharacter: 

    def __init__(self,health,armor_rating,attack_power):
        self._health = health
        self._armor_rating = armor_rating
        self._attack_power = attack_power
        
                
    def set_health(self,_health):
        self.health = _health

    def set_armor_rating(self,_armor_rating):
        self.armour_rating = _armor_rating
        

    def set_attack_power(self,_attack_power):
        self.attack_power = _attack_power

    def get_health(self):
        return self.health

    def get_armor_rating(self):
        return self.armour_rating

    def get_attack_power(self):
        return self.attack_power

    def __str__(self):
        
        return f"The Wizard has {self._health} health, power {self._attack_power}, and armour {self._armor_rating}"


def main():
    
    charac_Health = int(input("Enter a value for what you would like your player health to be (1-100): "))
    while charac_Health not in range(1, 101):
        
        print("The value you have chosen is out of the required range, try again.")
        charac_Health = int(input("Enter a value for what you would like your player health to be (1-100): "))
    
    print(f"Char health of: {charac_Health}")
    
    
            
    charac_Armor = int(input("Enter a value for what you would like your player health to be (1-20): "))
    while charac_Armor not in range(1, 21):
        
        print("The value you have chosen is out of the required range, try again.")
        charac_Armor = int(input("Enter a value for what you would like your player health to be (1-20): "))
    
    print(f"Char armor of: {charac_Armor}")
    
    
            
    charac_Power = int(input("Enter a value for what you would like your player armor to be (1-20): "))
    while charac_Power not in range(1, 21):
        
        print("The value you have chosen is out of the required range, try again.")
        charac_Power = int(input("Enter a value for what you would like your player power to be (1-100): "))
        
    print(f"Char power of: {charac_Power}")
    
    Wizard = PlayerCharacter(charac_Health, charac_Armor, charac_Power)
        
    print(Wizard)

if __name__ == "__main__":
        main()
        