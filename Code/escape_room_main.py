#Hauptklasse von der alle anderen aufgerufen und verwaltet werden

import tkinter as tk
import Zelle

# Startfenster erstellen
root = tk.Tk()
root.title("Prison-Escape")
root.geometry("800x800")
root.resizable(width=False, height=False)

#Startfenster Canvas erstellen
canvas = tk.Canvas(root, width=800, height=800, bg="black")
canvas.pack()

Img = tk.PhotoImage(file="../images/prison.png")
#text = tk.Text(text="Prison-Escape",  font='Helvetica 32 bold', fg="white")

prisonBg = canvas.create_image(0,0,image=Img, anchor='nw')
#prisonText = canvas.create_text(0,0,text=text, anchor='nw', fill="white")

#Button -> Geht zum ersten Raum
def start_cell():
    root.destroy()
    Zelle.run()
raum1 = tk.Button(root, text="Start", font='Helvetica 22', command=start_cell, height=2, width=12, bg="black", fg="white")
raum1.place(relx = 0.5, rely = 0.55, anchor = 'center')

# GUI starten
root.mainloop()