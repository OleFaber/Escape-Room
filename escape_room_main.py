#Hauptklasse von der alle anderen aufgerufen und verwaltet werden

import tkinter as tk
import Zelle

# Hauptfenster erstellen
root = tk.Tk()
root.title("Prison-Escape")
root.geometry("800x800")
root.resizable(width=False, height=False)

#Starttext
text = tk.Label(root, text="Prison-Escape",  font='Helvetica 26 bold')
text.place(relx = 0.5, rely = 0.4, anchor = 'center')

#Geht zum ersten Raum
def start_cell():
    root.destroy()
    Zelle.run()
raum1 = tk.Button(root, text="Start", font='Helvetica 22', command=start_cell, height=2, width=12)
raum1.place(relx = 0.5, rely = 0.55, anchor = 'center')

# GUI starten
root.mainloop()