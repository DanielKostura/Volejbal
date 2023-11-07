import tkinter as tk
from tkinter import *

# player details
left_color_dress = "blue"
left_num = "1"
left_count = 0

right_color_dress = "red"
right_num = "1"
right_count = 0

body_position = []
arms_position = []

def court():
    p.create_rectangle(50, 50, width - 50, height - 50, fill="white")  # outline
    p.create_rectangle(60, 60, width - 60, height - 60, fill="RoyalBlue3")  # core
    p.create_rectangle((width - 100) / 6 * 2 + 50 - 5, 55, (width - 100) / 6 * 2 + 50 + 5, height - 55, fill="white",
                   outline="white")  # left line
    p.create_rectangle(width / 2 - 5, 50, width / 2 + 5, height - 50, fill="white", outline="white")  # central line
    p.create_rectangle((width - 100) / 6 * 4 + 50 - 5, 55, (width - 100) / 6 * 4 + 50 + 5, height - 55, fill="white",
                   outline="white")  # right line
    
    net()

def net():
    column = 0
    while column < height + 10:
        for row in range(0, 50, 10):
            p.create_rectangle((width - 30) / 2 + row - 10, column, (width - 30) / 2 + row, column + 10)
        column += 10

def rules():
    new_okno = tk.Toplevel()  # Vytvořte nové okno
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
    global right_count
    global left_count

    x = action.x
    y = action.y

    free = overlay(x, y)

    if y - 15 > 90 and x - 30 > 60 and y + 45 < 540 and x + 30 < width / 2 - 25 and left_count < 6 and free == True:
        p.create_oval(x - 15, y - 15, x + 15, y - 45, fill="wheat")
        p.create_oval(x - 15, y + 15, x + 15, y + 45, fill="wheat")
        p.create_oval(x - 30, y - 30, x + 30, y + 30, fill=left_color_dress)
        p.create_text(x, y, text=left_num, font=("Calibri", 22, "bold"))

        body_position.append(x)
        body_position.append(y)
        arms_position.append(x)
        arms_position.append(y-30)
        arms_position.append(x)
        arms_position.append(y+30)
        left_count += 1

    elif y - 15 > 90 and x - 30 > width / 2 + 25 and y + 45 < 540 and x + 30 < 940 and right_count < 6 and free == True:
        p.create_oval(x - 15, y - 15, x + 15, y - 45, fill="wheat")
        p.create_oval(x - 15, y + 15, x + 15, y + 45, fill="wheat")
        p.create_oval(x - 30, y - 30, x + 30, y + 30, fill=right_color_dress)
        p.create_text(x, y, text=right_num, font=("Calibri", 22, "bold"))
        body_position.append(x)
        body_position.append(y)
        arms_position.append(x)
        arms_position.append(y-30)
        arms_position.append(x)
        arms_position.append(y+30)
        right_count += 1

def overlay(x, y):
    for i in range(0, len(body_position), 2):
        border = ((body_position[i]-x) ** 2 + (body_position[i+1]-y) ** 2) ** 0.5
        if border < 60:
            print("BBBBBBBBBBBBBBBBB")
            return False
    
    for i in range(0, len(arms_position), 4):
        border1 = ((arms_position[i]-x) ** 2 + (arms_position[i+1]-y) ** 2) ** 0.5
        border2 = ((arms_position[i+2]-x) ** 2 + (arms_position[i+3]-y) ** 2) ** 0.5
        if border1 < 30 or border2 < 30:
            print("AAAAAAAAAAAA")
            return False
    return True

def text():
    def submit1():
        global left_color_dress
        global left_num
        left_color_dress = color1.get()
        left_num = num1.get()
        
    def submit2():
        global right_color_dress
        global right_num
        right_color_dress = color2.get()
        right_num = num2.get()

    space = Label(o, text = "").pack()
    space = Label(o, text = "").pack()
    space = Label(o, text = "").pack()

    color1 = tk.StringVar()
    color2 = tk.StringVar()
    num1 = tk.StringVar()
    num2 = tk.StringVar()

    # left top text
    text1 = Label(o, text = "Farbu týmu na ľavo:").place(x = 100, y = height + 12)
    entry1 = Entry(o,textvariable = color1, font=('calibre',10,'normal')).place(x = 100 + 120,  y = height + 14)
    
    # left bot text
    text2 = Label(o, text = "Číslo hráča na ľavo:").place(x = 100, y = height + 12 + 25)
    entry2 = Entry(o,textvariable = num1, font=('calibre',10,'normal')).place(x = 100 + 120,  y = height + 14 + 25)


    button1 = Button(text = 'OK', command = submit1).place(x = 100 + 120 + 170, y = height + 23)
    
    # right top text
    text3 = Label(o, text = "Farbu týmu na pravo:").place(x = width//2 + 100, y = height + 12)
    entry3 = Entry(o,textvariable = color2, font=('calibre',10,'normal')).place(x = width//2 + 100 + 120, 
                                                                                  y = height + 14)
    
    # right bot text
    text4 = Label(o, text = "Číslo hráča na pravo:").place(x = width//2 + 100, y = height + 12 + 25)
    entry4 = Entry(o,textvariable = num2, font=('calibre',10,'normal')).place(x = width//2 + 100 + 120, y = height + 14 + 25)


    button2 = Button(text = 'OK', command = submit2).place(x = width//2 + 100 + 120 + 170, y = height + 23)

def delete(action):
    p.delete("all")
    court()
    global left_count
    global right_count
    left_count = 0
    right_count = 0
    body_position = []
    arms_position = []

o = tk.Tk()
o.title('Volejbalové ihrisko')

width = 1000
height = 600

p = tk.Canvas(height=height, width=width, bg='RoyalBlue3')
p.pack()

court()
text()

# button
b = Button(o, text = "Pravidlá", command=rules)
b.place(x=width-58, y=10)

# player
p.bind_all("<Button-1>", player)

p.bind_all("<Button-3>", delete)

o.mainloop()