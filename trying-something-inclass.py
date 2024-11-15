
'''
def morseCodeConverter():
    
    morse_dictonary = {'a': '.-', 'b': '-...', 'c': '-.-.'}
    
    msg = input("Enter what you want to translte to morse code: ")
    for char in msg:
        if char in morse_dictonary:
                print(morse_dictonary[char])
 
 
 
 
def sub_dicton():
    lib_2 = {"Author": { "Tolkein": ["Lord of the Rings", "The Two Towers"], "R.L Stein": ["Goosebumps", "some book" ], "martin": ["Game of Thrones", "Fire and Ice"]
                                                                                       
        }, "publisher": { "Penguin": ["AuthorA", "AuthorB"], "MIT Press": "Book C"
                        }
            }
    
    print(lib_2["publisher"])

        if "Author" in lib_2:
            print(
                
morseCodeConverter()
sub_dicton()
    

  --------------------------------------------------------------------------------------------------
  

    # Building a program with multiple files 
    # vehcle class whch we will use as the superclass for inherited classes - car, plane, boat
class Vehicle:
    
    doors = 4 
    wheels = 4 
    engine = "V8"
    windows = 4 
    color = "Red"
    make = "Ford"
    model = "mustang"
    
    
    
    # Create a constructor for vehicle class objects 
    def __name__(self, doors, wheels, engine, windows, color, make, model ):
    
      self.doors = doors
      self.wheels = wheels
      self.engine = engine
      self.windows = windows
      self.color = color
      self.make = make
      self.model = model
        
    pass 

if __name__ == "__main__":

    myCar = Vehicle()
    print(myCar)
'''
    
    
    
    
# ----------------------------------recursive problems------------------------------------------
# greatest common denom if X can be eenly divided by Y then GCD of x and y is y 
# otherwise the GCD of x and y is equal to (GCD of y and GCD of the remainder of x/y)

#x == num    y == denom
def GCD(x, y):
    
    #Base Case
    if x % y == 0:
        return y
    
    else:
        return GCD(y, x % y )
    
    

if __name__ == "__main__":

        result = GCD(14, 7)
        print(result)

