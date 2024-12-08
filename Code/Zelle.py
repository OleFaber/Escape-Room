#Erster Raum - Gefängniszelle
import tkinter as tk  #Für GUI
import time

def run_zelle():
    #Dictionary erstelllen
    program_keys = {"key" : False,
                "chest" : False,
                "box" : False,
                "bed" : False,
                "desk" : False,
                "carpet" : False,
                "tool" : False,
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

    # Ausgabefeld - Text Widget erstellen
    text_widget = tk.Text(cell, wrap="word", bg="white", fg="black", font=("Helvetica", 12), height=13)
    text_widget.pack(pady=5, padx=10, fill="x")  # Text Widget platzieren
    anfang = (
        "Langsam öffnest du deine Augen und Findest dich alleine auf einem kargen Bett in einer kleinen Gefängniszelle wieder.\n"
        "Du bist noch ganz verwirrt und kannst dich nicht recht erinnern, wie du hierher gekommen bist.\n"
        "Du stehst auf und schaust dich erstmal um. In deiner Zelle befinden sich ein Bett, zwei kleine Lampe, ein kleiner Tisch, ein Teppich und eine große Truhe.\n"
        "Du gehst zur Zellentür und versuchst sie zu öffnen. Ohne Erfolg, die Tür ist verriegelt!\n"
        "Allerdings siehst du, dass sich neben der Tür ein Eingabefeld mit Zahlen befindet. Du musst irgendwie versuchen den passenden Code herauszufinden...\n\n"
        "Als nächstes versuchst du dein Glück bei der Truhe...\n"
        "Ebenfalls abgeschlossen. Du schaust dich nochmals im Raum um, auf der Suche nach etwas was dir helfen könnte die Truhe zu öffnen.\n")  # Textinhalt setzen
    text_widget.insert("1.0", anfang)  # Textinhalt dem Text-Widget hinzufügen

    # Eingabefeld für das Lösungswort
    input1_describtion = tk.Label(cell, text="Code-Box: ", font='Helvetica 14')
    input1_describtion.place(x=50, y=1115)
    user_input1 = tk.Entry(cell)
    user_input1.configure(font='Helvetica 14')
    user_input1.place(x=270, y=1115)

    # Eingabefeld für den Zahlencode
    input2_describtion = tk.Label(cell, text="Zahlencode-Tür: ", font='Helvetica 14')
    input2_describtion.place(x=50, y=1155)
    user_input2 = tk.Entry(cell)
    user_input2.configure(font='Helvetica 14')
    user_input2.place(x=270, y=1155)

    def key_action():
        if program_keys["key"] == False:
            program_keys["key"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nSchlüssel gefunden!\n")
            text_widget.see(tk.END)  # Automatisch den Text nach unten scrollen
            text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nDu hast den Schlüssel bereits aufgehoben!\n")
            text_widget.see(tk.END)  # Automatisch den Text nach unten scrollen
            text_widget.configure(state="disabled")
    def chest_action():
        if program_keys["chest"] == False:
            if program_keys["key"] == True:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,"\nMit dem Schlüssel lässt sich die Truhe erfolgreich öffnen.\n"
                                   "Du findest einen Schnipsel eines Zettels auf dem steht:\n"
                                   "\"Um 3 Uhr Nachmittags gehen jeden Tag die Wachen auf ihrem Kontrollgang durch den Korridor.\"\n"
                                    "Außerdem findest du eine kleine verschlossene Box. Sie scheint sich mit einem Passwort öffnen zu lassen.\n"
                                    "Weißt du das Passwort?\n"
                                   )
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
                program_keys["chest"] = True
                program_keys["box"] = True
            else:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,"\nDie Truhe ist verschlossen. Du kannst sie nicht öffnen schaue dich nochmal um!\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nDu hast den Zettel schon gesehen!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
    def bed_action():
        if program_keys["bed"] == False:
            program_keys["bed"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nDu findest unter der Matratze einen Schnipsel eines Zettels auf dem steht:\n"
                               "\"Jeden morgen stehe ich um 7 Uhr auf und die Sonne fällt durchs Fenster genau auf das Schloss der Tür\"\n")
            text_widget.see(tk.END)
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nDu hast dir das Bett bereits angesehen!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
    def desk_action():
        if program_keys["desk"] == False:
            program_keys["desk"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nDu findest in der Schublade im Tisch einen Zettel mit einem Rätsel drauf:\n"
                                "\"Ich kann weder gekauft noch verkauft werden,\n"
                                "doch jeder wünscht mich zu haben.\n"
                                "Manche kämpfen für mich,\n"
                                "andere verlieren mich.\n"
                                "Ohne mich fühlt man sich gefangen.\n\n"
                                "Was bin ich?\"\n"
                                "Vielleicht kann dir die Lösung des Rätsels anderswo behilflich sein...\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nDu hast dir den Tisch schon angesehen!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
    def secret_exit():
        if program_keys["carpet"] == False:
            program_keys["carpet"] = True
            program_keys["tool"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nGlückwunsch! Du hast ein Geheimnis gefunden!\n"
                               "Du rollst den Teppich zurück und findest erst einmal nichts. Doch bei genauerer Betrachtung fällt dir etwas auf:\n"
                               "Unter dem Teppich hat der Boden Risse und scheint an einer Stelle leicht erhöht zu sein.\n"
                               "Du nimmst an dieser Stelle einen losen Brocken Beton aus dem Boden und entdeckst etwas großartiges:\n\n"
                               "Eine FEILE!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,"\nDu hast das Geheimnis bereits entdeckt!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
    def window_action():
        try:
            if program_keys["tool"] == True:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END, "\nDu sägst mit der Feile die Gitterstäbe durch und entkommst durch das Fenster in die Freiheit!\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
                time.sleep(3)
                cell.destroy()
                print("Glückwunsch du hast Gewonnen!")
            else:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,
                                   "\nDu begutachtest die Gitterstäbe und stellst fest, dass sie sehr solide sind\n"
                                   "Hier kommst du vermutlich nicht raus, es sei denn du hast ein passendes Werkzeug\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
        except Exception as e:
            print("Ein Fehler ist aufgetreten:", e)

    # Unsichtbare Rechtecke (als klickbarer Bereiche)
    rect_key = canvas.create_rectangle(370, 580, 470, 660, fill="", outline="")
    rect_chest = canvas.create_rectangle(220, 380, 250, 420, fill="", outline="")
    rect_bed = canvas.create_rectangle(540, 300, 750, 470, fill="", outline="")
    rect_desk = canvas.create_rectangle(300, 340, 420, 380, fill="", outline="")
    rect_secret = canvas.create_rectangle(150, 755, 160, 765, fill="", outline="")
    rect_window = canvas.create_rectangle(250, 0, 460, 240, fill="", outline="")

    # Klick-Ereignisse binden
    canvas.tag_bind(rect_key, "<Button-1>", lambda event: key_action())
    canvas.tag_bind(rect_chest, "<Button-1>", lambda event: chest_action())
    canvas.tag_bind(rect_bed, "<Button-1>", lambda event: bed_action())
    canvas.tag_bind(rect_desk, "<Button-1>", lambda event: desk_action())
    canvas.tag_bind(rect_secret, "<Button-1>", lambda event: secret_exit())
    canvas.tag_bind(rect_window, "<Button-1>", lambda event: window_action())

    # Funktion zur Überprüfung des Lösungsworts (Verarbeitung der Eingabe)
    def check_password():
        eingabe_wort = user_input1.get().lower()
        if program_keys["box"] == True:
            if eingabe_wort == "freiheit":
                output = ("\nDie Box lässt sich nun öffnen. In ihr ist eine Notiz, auf der steht:\n\n"
                          "\"Es sind insgesamt 4 Wachen, die diesen Zellblock jeden Abend um 9 Uhr kontrollieren!\"")
            else:
                output = ("\nFalsches Passwort!\n")
        else:
            output = ("Ihr scheint die Box noch nicht gefunden zu haben!\n")
        # Text zur Ausgabe hinzufügen
        text_widget.configure(state="normal")
        text_widget.insert(tk.END,"\n"+output+"\n")
        text_widget.see(tk.END)
        text_widget.configure(state="disabled")

    # Funktion zur Überprüfung des Zahlencodes (Verarbeitung der Eingabe)
    def check_code():
        eingabe_code = user_input2.get().strip()
        if eingabe_code == "7349":
            output = ("\nHurra! Die Zellentür lässt sich öffnen und du kommst auf den Korridor vor den Zellen.\n"
                      "Anmerkung: Das Spiel geht nun in der Konsole weiter")
            #run_buero()
            cell.destroy()
        else:
            output = ("\nFalsches Passwort!\n")
        text_widget.configure(state="normal")
        text_widget.insert(tk.END, "\n" + output + "\n")
        text_widget.see(tk.END)
        text_widget.configure(state="disabled")

    # Prüfen-Schaltfläche für Lösungswort (verarbeitung)
    button_check1 = tk.Button(cell, text="BESTÄTIGEN", font='Helvetica 14', command=check_password, height=1, width=15, bg="green", fg="black")
    button_check1.place(x=575, y=1105)

    # Prüfen-Schaltfläche für Zahlencode (verarbeitung)
    button_check2 = tk.Button(cell, text="BESTÄTIGEN", font='Helvetica 14', command=check_code, height=1, width=15, bg="green", fg="black")
    button_check2.place(x=575, y=1150)

    # GUI starten
    cell.mainloop()
run_zelle()