#Erster Raum - Gefängniszelle
import tkinter as tk  #Für GUI

def run_zelle():
    #Dictionary erstelllen
    inventar = {"key" : False,
                "code" : False
                }

    # Spielfenster erstellen
    cell = tk.Tk()
    cell.title("Zelle")
    cell.geometry("800x1200")
    cell.resizable(width=False, height=False)

    # Canvas erstellen
    canvas = tk.Canvas(cell, width=800, height=800)
    canvas.pack()

    # Bild laden und auf das Canvas zeichnen
    image_cell = tk.PhotoImage(file="../images/cell.png")
    canvas.create_image(0, 0, anchor="nw", image=image_cell)

    def key_action():
        if inventar["key"] == False:
            inventar["key"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\n\nEigentum: Schlüssel gefunden!\n")
            text_widget.see(tk.END)  # Automatisch den Text nach unten scrollen
            text_widget.configure(state="disabled")
    def chest_action():
        if inventar["code"] == False:
            if inventar["key"] == True:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,"\nDu findest in der Truhe einen Zettel auf dem steht:\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
                inventar["code"] = True
                #output = ("Eigentum: Code gefunden!")
            else:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,"\nDu kannst die Truhe nicht öffnen schaue dich nochmal um!\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")

    # Unsichtbare Rechtecke (als klickbarer Bereiche)
    rect_key = canvas.create_rectangle(370, 580, 470, 660, fill="", outline="")
    rect_chest = canvas.create_rectangle(220, 380, 250, 420, fill="", outline="")

    # Klick-Ereignisse binden
    canvas.tag_bind(rect_key, "<Button-1>", lambda event: key_action())
    canvas.tag_bind(rect_chest, "<Button-1>", lambda event: chest_action())

    # Funktion zur Überprüfung des Lösungsworts (Verarbeitung der Eingabe)
    def check_password():
        eingabe = user_input.get().lower()
        if eingabe == "freiheit":
            output = ("Glückwunsch! Die Tür öffnet sich.")
        else:
            output = ("Falsches Passwort!")
        # Text zur Ausgabe hinzufügen
        text_widget.configure(state="normal")
        text_widget.insert(tk.END,"\n"+output+"\n")
        text_widget.see(tk.END)
        text_widget.configure(state="disabled")

    # Ausgabefeld - Text Widget erstellen
    text_widget = tk.Text(cell, wrap="word", bg="white", fg="black", font=("Helvetica", 14), height=11)
    text_widget.pack(pady=5, padx=5, fill="x") #Text Widget platzieren
    anfang = ("Langsam öffnest du deine Augen und Findest dich alleine auf einem kargen Bett in einer kleinen Gefängniszelle wieder.\n"
    "Du bist noch ganz verwirrt und kannst dich nicht recht erinnern, wie du hierher gekommen bist.\n"
    "Langsam steht du auf und schaust dich erstmal um. In deiner Zelle befinden sich dein Bett, zwei kleine Lampe, ein kleiner Tisch, ein Teppich und eine große Truhe.\n"
    "Du gehst zur Zellentür und versuchst sie zu öffnen. Ohne Erfolg, die Tür ist wie zu erwarten verriegelt.\n"
    "Als nächstes versuchst du dein Glück bei der Truhe...\n"
    "Ebenfalls abgeschlossen. Du schaust dich nochmals im Raum um, auf der Suche nach etwas was dir helfen könnte die Truhe oder die Tür zu öffnen.") # Textinhalt setzen
    text_widget.insert("1.0", anfang)# Textinhalt dem Text-Widget hinzufügen
    # Buchstaben für "code" grün hervorheben
    highlight_positions = {
        'f': "1.35", #Indizes für die zu markierenden Buchstaben(Zeile und Stelle innerhalb der Zeile)
        'r': "1.78",
        'e1': "2.13",
        'i1': "2.43",
        'h': "5.25",
        'e2': "5.113",
        'i2': "6.19",
        't': "6.134",
    }
    """for char, pos in highlight_positions.items():
        text_widget.tag_add(char, pos, f"{pos}+1c")
        text_widget.tag_configure(char, foreground="green")"""
    text_widget.configure(state="disabled")# Text-Widget nicht bearbeitbar machen

    # Eingabefeld für den Code
    input_descibtion = tk.Label(cell,text="Eingabe: ", font='Helvetica 16')
    input_descibtion.place(x=50, y=1120)
    user_input = tk.Entry(cell)
    user_input.configure(font='Helvetica 16')
    user_input.place(x=170, y=1120)

    # Prüfen-Schaltfläche (verarbeitung)
    button_check = tk.Button(cell, text="BESTÄTIGEN", font='Helvetica 16', command=check_password, height=1, width=15, bg="green", fg="black")
    button_check.place(x=475, y=1115)

    # GUI starten
    cell.mainloop()
run_zelle()