#Erster Raum - Gefängniszelle
def run():
    import tkinter as tk

    # Hauptfenster erstellen
    cell = tk.Tk()
    cell.title("Zelle")
    cell.geometry("800x800")
    cell.resizable(width=False, height=False)

    # Funktion zur Überprüfung des Lösungsworts
    def check_password():
        if user_input == "CODE":
            output = tk.StringVar(cell,"Glückwunsch! Die Tür öffnet sich.")
        else:
            output = tk.StringVar(cell,"")

        # Ausgabefeld Schloss
        label_output = tk.Label(cell, text=output)
        label_output.pack(pady=10)

    # Begrüßungstext

    label_text = tk.Label(cell, text="Du erwachst in einer kalten, düsteren Gefängniszelle.\n" 
                                      "Die Luft ist feucht, und nur ein schwacher Lichtstrahl fällt durch ein kleines Fenster hoch oben an der Wand.\n"
                                      "An der Wand erkennst du eine Nachricht, die jemand eingeritzt hat:\n"
                                      "\n\"Der Weg in die Freiheit ist nahe, wenn du die Zeichen erkennst. COuragiert und aufmerksam, "
                                      "Damit du den SchlüssEl findest!\"\n", wraplength=400, justify="center")
    label_text.pack(pady=10)

    # Eingabefeld für das Lösungswort
    user_input = tk.Entry(cell)
    user_input.pack(pady=10)
    print(user_input)

    # Prüfen-Schaltfläche
    button_check = tk.Button(cell, text="Enter", command=check_password)
    button_check.pack(pady=10)

    # GUI starten
    cell.mainloop()