
import tkinter

class firstGUI():
    def __init__(self):
        
        # set the dimentions of the window
        self.main_window = tkinter.Tk()
        
        self.label = tkinter.Label(self.main_window, text="Hellow World!")
        
        self.label.pack()
        
        tkinter.mainloop()

if __name__ in "__main__":
    my_gui = firstGUI()