import tkinter as tk
from tkinter import *
import random

# player details
left_color_dress = "green"
left_num = 1
left_count = 0
left_num_list = []

right_color_dress = "red"
right_num = 1
right_count = 0
right_num_list = []

body_position = []

seconds = 0
is_running = False

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'white', 'black']

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
    global right_count, left_count
    global right_num_list, left_num_list
    global right_num, left_num

    x = action.x
    y = action.y

    free_place = overlay(x, y)

    if y - 15 > 90 and x - 30 > 60 and y + 45 < 540 and x + 30 < width / 2 - 25 and left_count < 6 and free_place == True:
        p.create_oval(x - 15, y - 15, x + 15, y - 45, fill="wheat")
        p.create_oval(x - 15, y + 15, x + 15, y + 45, fill="wheat")
        p.create_oval(x - 30, y - 30, x + 30, y + 30, fill=left_color_dress)

        while left_num in left_num_list:
            left_num = random.randint(1, 99)
        p.create_text(x, y, text=left_num, font=("Calibri", 22, "bold"))
        left_num_list.append(left_num)

        body_position.append(x)
        body_position.append(y)
        left_count += 1

    elif y - 15 > 90 and x - 30 > width / 2 + 25 and y + 45 < 540 and x + 30 < 940 and right_count < 6 and free_place == True:
        p.create_oval(x - 15, y - 15, x + 15, y - 45, fill="wheat")
        p.create_oval(x - 15, y + 15, x + 15, y + 45, fill="wheat")
        p.create_oval(x - 30, y - 30, x + 30, y + 30, fill=right_color_dress)

        while right_num in right_num_list:
            right_num = random.randint(1, 99)
        p.create_text(x, y, text=right_num, font=("Calibri", 22, "bold"))
        right_num_list.append(right_num)
        
        body_position.append(x)
        body_position.append(y)
        right_count += 1

    pass

def overlay(x, y):
    for i in range(0, len(body_position), 2):
        border = ((body_position[i]-x) ** 2 + (body_position[i+1]-y) ** 2) ** 0.5
        border1 = ((body_position[i]-x) ** 2 + (body_position[i+1]-y+60) ** 2) ** 0.5
        border2 = ((body_position[i]-x) ** 2 + (body_position[i+1]-y-60) ** 2) ** 0.5
        if border1 < 30 or border2 < 30 or border < 65:
            return False
    return True

def text():
    def submit1():
        global left_color_dress, right_color_dress
        global left_count
        global left_num

        current_color_dress = color1.get()
        if current_color_dress != right_color_dress and current_color_dress in colors and left_count == 0:
            left_color_dress = current_color_dress
        
        left_num = int(num1.get())

    def submit2():
        global right_color_dress, left_color_dress
        global right_count
        global right_num

        current_color_dress = color2.get()
        if current_color_dress != left_color_dress and current_color_dress in colors and right_count == 0:
            right_color_dress = current_color_dress

        right_num = int(num2.get())
    # adding space
    Label(o, text = "").pack()
    Label(o, text = "").pack()
    Label(o, text = "").pack()
    Label(o, text = "").pack()

    color1 = tk.StringVar()
    color2 = tk.StringVar()
    num1 = tk.StringVar()
    num2 = tk.StringVar()

    # left top text
    Label(o, text = "Farbu týmu na ľavo:").place(x = 100, 
                                                 y = height + 12)
    Entry(o,textvariable = color1, font=('calibre',10,'normal')).place(x = 100 + 120, 
                                                                       y = height + 14)
    # left bot text
    Label(o, text = "Číslo hráča na ľavo:").place(x = 100, 
                                                  y = height + 12 + 25)
    Entry(o,textvariable = num1, font=('calibre',10,'normal')).place(x = 100 + 120, 
                                                                     y = height + 14 + 25)
    # left button
    Button(text = 'OK', command = submit1).place(x = 100 + 120 + 170, 
                                                 y = height + 23)

    # right top text
    Label(o, text = "Farbu týmu na pravo:").place(x = width//2 + 100, 
                                                  y = height + 12)
    Entry(o,textvariable = color2, font=('calibre',10,'normal')).place(x = width//2 + 100 + 120, 
                                                                       y = height + 14)
    # right bot text
    Label(o, text = "Číslo hráča na pravo:").place(x = width//2 + 100, 
                                                   y = height + 12 + 25)
    Entry(o,textvariable = num2, font=('calibre',10,'normal')).place(x = width//2 + 100 + 120, 
                                                                     y = height + 14 + 25)
    #right
    Button(text = 'OK', command = submit2).place(x = width//2 + 100 + 120 + 170, 
                                                 y = height + 23)

def timer():
    def start_timer():
        global is_running
        if not is_running:
            is_running = True
            start_button.config(text="Stop")
            update_timer()
        else:
            is_running = False
            start_button.config(text="Start")

    def update_timer():
        global is_running, seconds
        if is_running:
            seconds += 1
            update_time()
            o.after(1000, update_timer)

    def update_time():
        minutes = seconds // 60
        seconds_display = seconds % 60
        time_label.config(text=f"{minutes}:{seconds_display:02}")

    global time_label
    time_label = Label(o, text="0:00", font=("Helvetica", 42))
    time_label.place(x=width // 2 - 55, y=height+2)

    start_button = Button(o, text="Start", command=start_timer)
    start_button.place(x=width//2-18, y=height+60)

def delete(action):
    p.delete("all")
    court()

    global left_color_dress, right_color_dress
    global left_num, right_num
    global left_count, right_count
    global left_num_list, right_num_list
    global body_position
    global seconds, is_running


    left_color_dress = "green"
    left_num = 1
    left_count = 0
    left_num_list = []

    right_color_dress = "red"
    right_num = 1
    right_count = 0
    right_num_list = []

    body_position = []

    seconds = 0
    is_running = False

o = Tk()
o.title('Volejbalové ihrisko')

width = 1000
height = 600

p = Canvas(height=height, width=width, bg='RoyalBlue3')
p.pack()

court()
text()
timer()

# button Pravidlá
Button(o, text = "Pravidlá", command=rules).place(x=width-58, y=10)

# player
p.bind_all("<Button-1>", player)
p.bind_all("<Button-3>", delete)

o.mainloop()