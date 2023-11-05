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
        p = Canvas(new, width=sirka, height=vyska, bg="RoyalBlue3")
        p.pack()

        #court
        p.create_rectangle(50, 50, sirka-50, vyska-50, fill="white") #outline
        p.create_rectangle(60, 60, sirka-60, vyska-60, fill="RoyalBlue3") #core
        p.create_rectangle((sirka-100)/6*2+50-5, 55, (sirka-100)/6*2+50+5, vyska-55, fill="white", outline="white") #left line
        p.create_rectangle(sirka/2-5, 50, sirka/2+5, vyska-50, fill="white", outline="white") #central line
        p.create_rectangle((sirka-100)/6*4+50-5, 55, (sirka-100)/6*4+50+5, vyska-55, fill="white", outline="white") #right line

        #net
        stlpec = 0
        while stlpec < vyska+10:
            for riadok in range(0,50,10):
                p.create_rectangle((sirka-30)/2+riadok-10, stlpec, (sirka-30)/2+riadok, stlpec+10)
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