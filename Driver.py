'''

Driver program

'''

import Vehicle, Car

def menu():
    pass

def main():
    
    myVehicle = Vehicle()
    myVehicle.color = "Pink"
    
    myCar = Car()
    myCar.color = "Red"
    #myCar.set_color("Green")    # you dont need to do it this way
    print(myCar.color)