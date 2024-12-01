#Erster Raum - Gefängniszelle
import tkinter as tk

def run():
    # Hauptfenster erstellen
    cell = tk.Tk()
    cell.title("Zelle")
    cell.geometry("800x800")
    cell.resizable(width=False, height=False)

    # Funktion zur Überprüfung des Lösungsworts (Verarbeitung der Eingabe)
    def check_password():
        eingabe = user_input.get().lower()
        if eingabe == "freiheit":
            output = ("Glückwunsch! Die Tür öffnet sich.")
        else:
            output = ("Falsches Passwort")
        # Text zur Ausgabe hinzufügen
        text_output.delete("1.0", tk.END)
        text_output.insert("1.0", output)

    # Text Widget erstellen
    text_widget = tk.Text(cell, wrap="word", bg="black", fg="white", font=("Helvetica", 12, 'bold'))
    #Text Widget platzieren
    text_widget.pack(pady=10, fill="both", expand=False)
    # Textinhalt setzen
    content = ("Langsam öffnest du deine Augen und Findest dich alleine in einer kalten, düsteRen Gefängniszelle wieder.\n"
    "Die AtmosphärE ist erdrückend, und die massIven Steinwände verstärken das Gefühl der Einsamkeit.\n"
    "Du bemerkst, dass jemand eine Botschaft in die kahle Betonwand eingeritzt hat:\n\n"
    "\"In der Stunde der DunkelHeit liegt der Schlüssel zum Entkommen verborgen. Ein mutiger Schritt kann den ersten "
    "StEin ins Rollen bringen. Öffne deine Augen und suche nach den verborgenen Hinweisen.\n"
    "Vertraue auf deine Instinkte, und sei stets wachsam. Die Wahrheit liegt nicht immer offensichtlich vor dir. "
    "Beginne mit einem tiefen ATemzug, lausche dem Klang der Stille und folge dem Flüstern der Hoffnung.\"\n\n"
    "An der Zellentür findest du ein Eingabefeld, bei dem du ein Password eingeben musst.")
    # Textinhalt dem Text-Widget hinzufügen
    text_widget.insert("1.0", content)
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
    for char, pos in highlight_positions.items():
        text_widget.tag_add(char, pos, f"{pos}+1c")
        text_widget.tag_configure(char, foreground="green")
    # Text-Widget nicht bearbeitbar machen
    text_widget.configure(state="disabled")

    # Eingabefeld für das Lösungswort
    user_input = tk.Entry(cell)
    user_input.pack(pady=10)

    # Prüfen-Schaltfläche (verarbeitung)
    button_check = tk.Button(cell, text="PRÜFEN", font='Helvetica 20', command=check_password, height=1, width=15, bg="black", fg="white")
    button_check.pack(pady=10)

    # Ausgabefeld Schloss
    text_output = tk.Text(cell, wrap="word", bg="white", fg="black", font=("Helvetica", 12, 'bold'))
    text_output.pack(pady=10)

    # GUI starten
    cell.mainloop()
run()