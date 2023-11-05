import tkinter as tk
from tkinter import *

def rules():
    new_okno = tk.Toplevel() 
    new_okno.title('Pravidlá Volejbalu')

    width = 900
    height = 400
    new_p = tk.Canvas(new_okno, width=width, height=height)
    new_p.pack()

    new_p.create_text(width//2, 15, text="Pravidlá Volejbalu", font=("Cooper Black",25, "bold"))
    new_p.create_text(60, 40, text="Tímy a hráči:", font=("Calibri", 15, "bold"))
    new_p.create_text(395, 60, text="Volejbal sa obvykle hraje medzi dvoma tímami, pričom každý tím pozostáva z 6 hráčov na ihrisku. Existujú aj varianty s iným počtom hráčov.", font=("Calibri", 10,))
    new_p.create_text(40, 80, text="Cieľ hry:", font=("Calibri", 15, "bold"))
    new_p.create_text(315, 100, text="Cieľom hry je získať bod tým, že pošleš loptu na stranu súpera a donútiš ju dopadnúť na zem v ich časti ihriska.", font=("Calibri", 10,))
    new_p.create_text(82, 120, text="Zakladné pravidlá:", font=("Calibri", 15, "bold"))
    new_p.create_text(185, 140, text="Hra sa začína podaním, ktoré vykoná hráč z označeného miesta.", font=("Calibri", 10,))
    new_p.create_text(165, 160, text="Po podaní hra pokračuje, kým jeden z tímov nezíska bod.", font=("Calibri", 10,))
    new_p.create_text(168, 180, text="Tím, ktorý získa bod, získa právo na nasledujúce podanie.", font=("Calibri", 10,))
    new_p.create_text(57, 200, text="Body a sety:", font=("Calibri", 15, "bold"))
    new_p.create_text(63, 220, text="Tím získa bod, keď:", font=("Calibri", 10,))
    new_p.create_text(132, 240, text="Lopta dopadne na zem v časti súpera.", font=("Calibri", 10,))
    new_p.create_text(155, 260, text="Súper urobí chybu (napríklad sa dotkne siete).", font=("Calibri", 10,))
    new_p.create_text(170, 280, text="Set sa obvykle hrá na 25 bodov (treba vyhrať o dva body).", font=("Calibri", 10,))
    new_p.create_text(127, 300, text="Tím, ktorý vyhrá tri sety, vyhrá celý zápas.", font=("Calibri", 10,))
    new_p.create_text(40, 320, text="Rotácia:", font=("Calibri", 15, "bold"))
    new_p.create_text(315, 340, text="Hráči sa pohybujú po ihrisku v určenom poradí (rotujú) a menia svoje pozície v závislosti na tom, kto podáva.", font=("Calibri", 10,))
    new_p.create_text(33, 360, text="Libero:", font=("Calibri", 15, "bold"))
    new_p.create_text(418, 380, text="Tímy môžu mať jedného hráča označeného ako libero, ktorý má obmedzené možnosti útoku, ale môže byť vymenený za ľubovoľného hráča pri podaní.", font=("Calibri", 10,))

def player(action):
    x = action.x
    y = action.y
    p.create_oval(x - 15, y - 15, x + 15, y - 45, fill="wheat")
    p.create_oval(x - 15, y + 15, x + 15, y + 45, fill="wheat")
    p.create_oval(x - 30, y - 30, x + 30, y + 30, fill=farba_dresu)
    p.create_text(x, y, text=cislo, font=("Calibri", 22, "bold"))

okno = tk.Tk()
okno.title('Volejbalové ihrisko')

width = 1000
height = 600

p = tk.Canvas(height=height, width=width, bg='RoyalBlue3')
p.pack()

# court
p.create_rectangle(50, 50, width - 50, height - 50, fill="white")  # outline
p.create_rectangle(60, 60, width - 60, height - 60, fill="RoyalBlue3")  # core
p.create_rectangle((width - 100) / 6 * 2 + 50 - 5, 55, (width - 100) / 6 * 2 + 50 + 5, height - 55, fill="white",
                   outline="white")  # left line
p.create_rectangle(width / 2 - 5, 50, width / 2 + 5, height - 50, fill="white", outline="white")  # central line
p.create_rectangle((width - 100) / 6 * 4 + 50 - 5, 55, (width - 100) / 6 * 4 + 50 + 5, height - 55, fill="white",
                   outline="white")  # right line

# net
column = 0
while column < height + 10:
    for row in range(0, 50, 10):
        p.create_rectangle((width - 30) / 2 + row - 10, column, (width - 30) / 2 + row, column + 10)
    column += 10

# button
b = Button(okno, text = "Pravidlá", command=rules)
b.place(x=width-60, y=10)

# player
farba_dresu = "blue"
cislo = "1"
p.bind_all("<Button-1>", player)

# lables


okno.mainloop()
