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
        
        sirka = 1000
        vyska = 600
        p = Canvas(new, width=sirka, height=vyska, bg="wheat")
        p.pack()

        p.create_rectangle(50, 50, sirka-50, vyska-50, fill="white")
        p.create_rectangle(60, 60, sirka-60, vyska-60, fill="wheat")

        stlpec = 0
        while stlpec < vyska+10:
            for riadok in range(0,50,10):
                p.create_rectangle((sirka-30)/2+riadok, stlpec, (sirka-30)/2+riadok+10, stlpec+10)
            stlpec += 10


class roles(Frame):    
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Pravidla")

        p = Canvas(new, width=500, height=400)
        p.pack()

        p.create_text(0, 0, text="kakakaka")


def main(): 
    menu().mainloop()

if __name__ == '__main__':
    main()