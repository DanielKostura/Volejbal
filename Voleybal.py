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

        sirka = 900
        vyska = 400
        p = Canvas(new, width=sirka, height=vyska)
        p.pack()

        p.create_text(sirka//2, 15, text="Pravidlá Volejbalu", font=("Cooper Black",25, "bold"))
        p.create_text(60, 40, text="Tímy a hráči:", font=("Calibri", 15, "bold"))
        p.create_text(395, 60, text="Volejbal sa obvykle hraje medzi dvoma tímami, pričom každý tím pozostáva z 6 hráčov na ihrisku. Existujú aj varianty s iným počtom hráčov.", font=("Calibri", 10,))
        p.create_text(40, 80, text="Cieľ hry:", font=("Calibri", 15, "bold"))
        p.create_text(315, 100, text="Cieľom hry je získať bod tým, že pošleš loptu na stranu súpera a donútiš ju dopadnúť na zem v ich časti ihriska.", font=("Calibri", 10,))
        p.create_text(82, 120, text="Zakladné pravidlá:", font=("Calibri", 15, "bold"))
        p.create_text(185, 140, text="Hra sa začína podaním, ktoré vykoná hráč z označeného miesta.", font=("Calibri", 10,))
        p.create_text(165, 160, text="Po podaní hra pokračuje, kým jeden z tímov nezíska bod.", font=("Calibri", 10,))
        p.create_text(168, 180, text="Tím, ktorý získa bod, získa právo na nasledujúce podanie.", font=("Calibri", 10,))
        p.create_text(57, 200, text="Body a sety:", font=("Calibri", 15, "bold"))
        p.create_text(63, 220, text="Tím získa bod, keď:", font=("Calibri", 10,))
        p.create_text(132, 240, text="Lopta dopadne na zem v časti súpera.", font=("Calibri", 10,))
        p.create_text(155, 260, text="Súper urobí chybu (napríklad sa dotkne siete).", font=("Calibri", 10,))
        p.create_text(170, 280, text="Set sa obvykle hrá na 25 bodov (treba vyhrať o dva body).", font=("Calibri", 10,))
        p.create_text(127, 300, text="Tím, ktorý vyhrá tri sety, vyhrá celý zápas.", font=("Calibri", 10,))
        p.create_text(40, 320, text="Rotácia:", font=("Calibri", 15, "bold"))
        p.create_text(315, 340, text="Hráči sa pohybujú po ihrisku v určenom poradí (rotujú) a menia svoje pozície v závislosti na tom, kto podáva.", font=("Calibri", 10,))
        p.create_text(33, 360, text="Libero:", font=("Calibri", 15, "bold"))
        p.create_text(418, 380, text="Tímy môžu mať jedného hráča označeného ako libero, ktorý má obmedzené možnosti útoku, ale môže byť vymenený za ľubovoľného hráča pri podaní.", font=("Calibri", 10,))


def main(): 
    menu().mainloop()

if __name__ == '__main__':
    main()