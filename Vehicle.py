
    
class Vehicle:
    
    #doors = 4 
    #wheels = 4 
    #engine = "V8"
    #windows = 4 
    #color = "Red"
    #make = "Ford"
    #model = "mustang"
    
    
    
    # Create a constructor for vehicle class objects 
    def __name__(self, doors, wheels, engine, windows, __color, make, model ):
    
      self.doors = doors
      self.wheels = wheels
      self.engine = engine
      self.windows = windows
      self.color = __color
      self.make = make
      self.model = model
      
    def set_color(self,color):
        self.color = color
        
    def getColor(self):
        return self.color
        
  