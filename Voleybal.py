import tkinter as tk
from tkinter import *
from tkinter import ttk

class menu( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Menu")

        self.button1 = Button( self, text = "Hracia plocha", width = 25,
                               command = self.voleyball )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.button2 = Button( self, text = "Pravidla", width = 25,
                               command = self.roles )
        self.button2.grid( row = 1, column = 2, columnspan = 2, sticky = W+E+N+S )

    def voleyball(self):
        self.newWindow = volleyball_court()
    
    def roles(self):
        self.newWindow = roles()
    

class volleyball_court(Frame):     
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Volejbalové ihrisko")


class roles(Frame):    
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Pravidla")


def main(): 
    menu().mainloop()

if __name__ == '__main__':
    main()