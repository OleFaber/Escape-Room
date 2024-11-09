#Erster Raum - Gefängniszelle

import tkinter as tk
from tkinter import messagebox

output = ""

# Funktion zur Überprüfung des Lösungsworts
def check_password():
    if user_input == "CODE":
        return "Glückwunsch! Die Tür öffnet sich."
    else:
        return "Falsches Passwort!"

# Hauptfenster erstellen
root = tk.Tk()
root.title("Zelle")
root.geometry("400x400")
root.resizable(width=False, height=False)

# Begrüßungstext
label_text = tk.Label(root, text="Du erwachst in einer kalten, düsteren Gefängniszelle.\n" 
                                  "Die Luft ist feucht, und nur ein schwacher Lichtstrahl fällt durch ein kleines Fenster hoch oben an der Wand.\n"
                                  "An der Wand erkennst du eine Nachricht, die jemand eingeritzt hat:\n"
                                  "\n\"Der Weg in die Freiheit ist nahe, wenn du die Zeichen erkennst. COuragiert und aufmerksam, "
                                  "Damit du den SchlüssEl findest!\"\n", wraplength=400, justify="center")
label_text.pack(pady=10)

# Eingabefeld für das Lösungswort
user_input = tk.Entry(root)
user_input.pack(pady=10)

# Prüfen-Schaltfläche
button_check = tk.Button(root, text="Enter", command=check_password)
button_check.pack(pady=10)

#Ausgabefeld Schloss
label_output = tk.Label(root, text=output)
label_output.pack(pady=10)

# GUI starten
root.mainloop()