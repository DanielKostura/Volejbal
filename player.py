import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Player Character")

# Create a Canvas widget within the window
platno = tk.Canvas(root, width=400, height=400)
platno.pack()

def player():
    x1, x2, y1, y2 = 200, 300, 200, 300
    platno.create_oval(x1 + 35, y1 - 15, x2 - 35, y2 - 85, fill="wheat")
    platno.create_oval(x1 + 35, y1 + 85, x2 - 35, y2 + 15, fill="wheat")
    platno.create_oval(x1, y1, x2, y2, fill="blue")

player()