#Startbildschirm
import tkinter as tk
import time

# Startfenster erstellen
root = tk.Tk()
root.title("Prison-Escape")
root.geometry("800x800")
root.resizable(width=False, height=False)

#Startfenster Canvas erstellen
canvas = tk.Canvas(root, width=800, height=800, bg="black")
canvas.pack()

#Foto in Canvas packen
Img = tk.PhotoImage(file="../images/prison.png")
prisonBg = canvas.create_image(0,0,image=Img, anchor='nw')

#Titeltext erstellen
label = tk.Label(root, text="Prison-Escape", bg="black", fg="white", font=("Helvetica", 30, "bold"))
label.place(relx=0.5, rely=0.2, anchor = 'center')

#Erster Raum - Gefängniszelle
#------------start zelle----------------
def run_zelle():
    # Spielfenster erstellen
    cell = tk.Tk()
    cell.title("Zelle")
    cell.geometry("800x800")
    cell.resizable(width=False, height=False)

    # Funktion zur Überprüfung des Lösungsworts (Verarbeitung der Eingabe)
    def check_password():
        eingabe = user_input.get().lower()
        print(eingabe)
        if eingabe == "freiheit":
            output = "Glückwunsch! Die Tür öffnet sich."
        else:
            output = "Fehler!"

    # Text Widget erstellen
    text_widget = tk.Text(cell, wrap="word", bg="black", fg="white", font=("Helvetica", 10, "bold"))
    #Text Widget platzieren
    text_widget.pack(pady=10, fill="both", expand=False)
    # Textinhalt setzen
    content = ("Langsam öffnest du deine Augen und Findest dich alleine in einer kalten, düsteRen Gefängniszelle wieder.\n"
    "Die AtmosphärE ist erdrückend, und die massIven Steinwände verstärken das Gefühl der Einsamkeit.\n"
    "Du bemerkst, dass jemand eine Botschaft in die kahle Betonwand eingeritzt hat:\n\n"
    "\"In der Stunde der Dunkelheit liegt der Schlüssel zum Entkommen verborgen. Ein mutiger SchRitt kann den ersten "
    "Stein ins Rollen bringen. Öffne deine Augen und suche nach den verBorgenen Hinweisen.\n"
    "Vertraue auf dEine Instinkte, und sei stets wachsam. Die WahRheit liegt nicht immer offensichtlich vor dir. "
    "Beginne mit einem tiefen Atemzug, lausche dem Klang der Stille und folge dem Flüstern der Hoffnung.\"\n")
    # Textinhalt dem Text-Widget hinzufügen
    text_widget.insert("1.0", content)
    # Buchstaben für "code" grün hervorheben
    highlight_positions = {
        'f': "1.35", #Indizes für die zu markierenden Buchstaben(Zeile und Stelle innerhalb der Zeile)
        'r': "1.78",
        'e1': "2.12",
        'i1': "2.41",
        'h': "3.42",
        'e2': "4.8",
        'i2': "4.99",
        't': "5.33",
    }
    for char, pos in highlight_positions.items():
        text_widget.tag_add(char, pos, f"{pos}+1c")
        text_widget.tag_configure(char, foreground="green")
    # Text-Widget nicht bearbeitbar machen
    text_widget.configure(state="disabled")

    # Eingabefeld für das Lösungswort
    user_input = tk.Entry(cell)
    user_input.pack(pady=10)

    # Prüfen-Schaltfläche
    button_check = tk.Button(cell, text="PRÜFEN", command=check_password)
    button_check.pack(pady=10)

    # Ausgabefeld Schloss
    #label_output = tk.Label(cell, text=output)
    #label_output.pack(pady=10)

    # GUI starten
    cell.mainloop()
#------------ende zelle-------------

#Funktion -> Geht zum ersten Raum
def start_zelle():
    root.destroy()
    run_zelle()
# Funktion -> Geht zum zweiten Raum
def start_buero():
    root.destroy()
    #run_buero()
# Funktion -> Geht zum dritten Raum
def start_hof():
    root.destroy()
    #run_hof()
def spielende():
    root.destroy()
#Buttons zum Starten in verschiedenen Räumen
zelle = tk.Button(root, text="Start Zelle", font='Helvetica 22', command=start_zelle, height=1, width=15, bg="black", fg="white")
zelle.place(relx = 0.5, rely = 0.4, anchor = 'center')
buero = tk.Button(root, text="Start Wärterbüro", font='Helvetica 22', command=start_buero, height=1, width=15, bg="black", fg="white")
buero.place(relx = 0.5, rely = 0.5, anchor = 'center')
hof = tk.Button(root, text="Start Hof", font='Helvetica 22', command=start_hof, height=1, width=15, bg="black", fg="white")
hof.place(relx = 0.5, rely = 0.6, anchor = 'center')
beenden = tk.Button(root, text="Beenden", font='Helvetica 22', command=spielende, height=1, width=15, bg="black", fg="white")
beenden.place(relx = 0.5, rely = 0.75, anchor = 'center')

#GUI starten
root.mainloop()