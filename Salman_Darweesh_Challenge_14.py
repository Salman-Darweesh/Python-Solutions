    
'''
class firstGUI():
    def __init__(self):
        
        # set the dimentions of the window
        self.main_window = tkinter.Tk()
        
        self.label = tkinter.Label(self.main_window, text="Hellow World!")
        
        self.label.pack()
        
        tkinter.mainloop()

ifmain :
    my_gui = firstGUI()
'''


import tkinter
import tkinter.messagebox

class holywood_star():
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text= 'Salman Darweesh', command=self.do_something_invert)


        self.my_button.pack()
        tkinter.mainloop()
        
    def do_something_invert():
        tkinter.messagebox.showinfo("Salman Darweesh")

if __name__ in "__main__":
    star = holywood_star()