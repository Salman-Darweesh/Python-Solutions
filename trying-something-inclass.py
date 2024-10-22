



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
    
    
    
    
    

    


if __name__ == "__main__":
    morseCodeConverter()
    sub_dicton()