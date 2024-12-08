import tkinter as tk  #Importieren des tkinter Moduls, für die grafische Benutzeroberfläche
import time # Importieren des Zeit Moduls, um Pausen zwischen den print-Befehlen zu erzeugen

# Startfenster erstellen
root = tk.Tk()
root.title("Prison-Escape")
root.geometry("800x800")
root.resizable(width=False, height=False)

#Startfenster Canvas erstellen
canvas = tk.Canvas(root, width=800, height=800, bg="black")
canvas.pack()

#Foto in Canvas packen
image_prison = tk.PhotoImage(file="../images/prison.png")
prisonBg = canvas.create_image(0,0,image=image_prison, anchor='nw')

#Titeltext erstellen
offsets = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
for offset in offsets:
    canvas.create_text(400 + offset[0], 180 + offset[1], text="Prison-Escape",
                       font=("Helvetica", 32, "bold"), fill="white")
canvas.create_text(400, 180, text="Prison-Escape", font=("Helvetica", 32, "bold"), fill="black")

#Dritter Raum - Gefängnishof
#------------start hof----------------
def run_hof():
    code = {}  # leeres Dictionary, um Codes zu speichern, die der Spieler während des Spiels sammelt

    # Diese Funktion simuliert die erste Stufe des Spiels, in der der Spieler Hinweise und einen Schlüssel finden muss,
    # um in den Wachturm zu gelangen.
    def gefaengnishof_1():
        print(
            "Du hast in der naechsten Stufe den Gefaengnishof erreicht und musst einen Weg finden, in den Wachturm zu gelangen.")
        time.sleep(2)
        print("Als du ueber den Hof gehst, siehst du mehrere einzelne Stationen.")
        time.sleep(2)
        print("Du kommst auf dem Weg zum Wachturm an einer Treppe, einem Tisch und einer Kiste vorbei.")
        time.sleep(2)
        print(
            "Der Wachturm ist verschlossen und man benoetigt einen Schluessel, um hineinzukommen.")  # Einleitung in das Thema des Raumes

        # Variablen, die den Fortschritt des Spielers speichern
        schluessel_gefunden = False  # Gibt an, ob der Schlüssel gefunden wurde
        teilcode_gefunden = False  # Gibt an, ob der erste Code gefunden wurde
        teilcode2_gefunden = False  # Gibt an, ob der zweite Code gefunden wurde
        tuer_wachturm = False  # Gibt an, ob die Wachturm-Tür bereits geöffnet wurde

        # Schleife, damit alle Stationen wiederholt werden, bis Wachturm erreicht wurde
        while True:
            print("Du siehst dir nochmals die Umgebung an.")
            kommando = input(
                "Zu welcher Station moechtest du gehen? (Treppe/Kiste/Tisch/Wachturm): ").lower()  # Spieler wählt Station
            time.sleep(2)

            # Überprüfen der Eingabe (Station)
            if kommando == "treppe":
                if not schluessel_gefunden:  # Überprüfen, ob Schlüssel bereits gefunden
                    print(
                        "Glueckwunsch! Unter der Treppe liegt ein Schluessel,den ein Wachmann dort verloren haben musss.")
                    time.sleep(2)
                    print("Du hebst den Schluesssel auf")
                    schluessel_gefunden = True  # Variable wird auf True gesetzt, da Schlüssel gefunden wurde
                    time.sleep(2)
                else:
                    print("Die Treppe wurde bereits untersucht.")
                    time.sleep(2)

            elif kommando == "kiste":
                if not teilcode_gefunden:  # Überprüfen, ob Teilcode aus Kiste bereits gefunden
                    print("In der Kiste ist ein Hinweis mit einem Code: 2357.")
                    benutzer_code = input(
                        "Bitte notiere den Code, damit du ihn nicht vergisst: ")  # Aufforderung den Code zu notieren, für spätere Spielschritte
                    if benutzer_code == "2357":  # Überpruefen, ob der eingegebene Code richtig ist
                        code["CODE_Teil1"] = benutzer_code
                        teilcode_gefunden = True  # Variable wird auf True gesetzt, wenn Teilcode "Kiste" gefunden
                        time.sleep(2)
                    else:
                        print("Falscher Code!")
                        time.sleep(2)
                else:
                    print("Die Kiste wurde bereits untersucht.")
                    time.sleep(2)

            elif kommando == "tisch":
                if not teilcode2_gefunden:  # Überprüfen, ob Teilcode vom Tisch bereits gefunden
                    print(
                        "Unter dem Tisch ist ein Hinweis mit einem Code: 7685 den ein Informant fuer dich dort hinterlassen hat")
                    benutzer_code = input(
                        "Bitte notiere den Code,damit du ihn nicht vergisst: ")  # Aufforderung den Code zu notieren, für spätere Spielschritte
                    if benutzer_code == "7685":  # Überpruefen, ob der eingegebene Code richtig ist
                        code["CODE_Teil2"] = benutzer_code
                        teilcode2_gefunden = True  # Variable wird auf True gesetzt, wenn Teilcode "Tisch" gefunden
                        time.sleep(2)
                    else:
                        print("Falscher Code!")
                        time.sleep(2)
                else:
                    print("Die Bank wurde bereits untersucht.")
                    time.sleep(2)

            elif kommando == "wachturm":
                if not tuer_wachturm:  # Überprüfen, ob Wachturm bereits betreten wurde
                    # Überprüfe, ob der Spieler alle notwendigen Hinweise gefunden hat, um in diese Station zu gelangen
                    if schluessel_gefunden and teilcode_gefunden and teilcode2_gefunden:
                        print(
                            "Du hast alle Hinweise in den Stationen sowie den Schluessel gefunden und kommst somit in die naechste Stufe.")
                        tuer_wachturm = True  # Variable wird auf True gesetzt, wenn Wachturm betreten wird
                        time.sleep(2)
                        break  # Schleife wird beendet und nächste Station wird erreicht
                    else:
                        print("Du musst erst alle Hinweise in dieser Stufe finden, um in den Wachturm zu gelangen")
                        time.sleep(2)
                else:
                    print("Der Wachturm ist bereits betreten worden.")
                    time.sleep(2)
            else:  # Fehlermeldungen für die Eingabe falscher Kommandos
                print("Unbekannter Befehl. Versuche eines der vier Befehle: Treppe, Kiste, Bank, Wachturm.")
                time.sleep(2)

    # Aufruf der Funktion um die erste Station
    # gefaengnishof_1()

    print("Herzlichen Glueckwunsch, du bist in der naechsten Stufe")

    # Diese Funktion simuliert die zweite Stufe des Spiels, in der der Spieler einen weiteren Code und ein Seil finden muss,
    # um aus dem Wachturm zu entkommen.
    def gefaengnishof_2_wachturm():
        print("Du hast nun den Wachturm erreicht und bist nun vor der letzten Stufe unseres Spiels")
        time.sleep(2)
        print("Du gehst den Wachturm hinauf und ueberpruefst, ob irgendeine Tuer im Treppenhaus  offen ist.\n"
              "Es sind bis oben aber alle Tueren verschlossen und dir ist nur eine Abstellkammer des Hausmeisters in der dritten Etage aufgefallen, \n"
              "welcher mit einem digitalen Zahlenschloss versperrt ist.\n"
              "Ganz oben im Wachturm ist dir noch ein Fenster aufgefallen, welches nicht versperrt ist und aus dem Gefaengnis fuehrt")
        time.sleep(2)
        print("Du hast ohne Erfolg alle versperrten Tueren versucht mit dem gefundenen Schluessel aufzuschließen, \n"
              "also ist deine letzte Hoffnung die Abstellkammper ")  # Einleitung in den Wachturm und zur neuen Herausforderung
        time.sleep(2)
        print("Dein Informant, der die Hinweise sorgfaeltig versteckt hat, erklaerte, \n"
              "dass sich das Passwort aus dem einen Hinweis minus dem anderen Hinweis zusammensetzt. Er war sich aber unsicher wie herum")
        print("Hinweis aus der ersten Stufe", code.get("CODE_Teil1"), ",",
              code.get("CODE_Teil2"))  # Hinweise zum digitalen Zahlenschloss

        # Eingabe des Codes
        anzahl_versuche = 3  # Der Spieler hat drei Versuche das richtige Passwort einzugeben
        while anzahl_versuche > 0:  # Schleife die solange läuft, bis keine Versuche
            passwort = input("Bitte geben Sie das Passwort ein:")  # Spieler gibt Passwort ein
            anzahl_versuche -= 1  # Reduziert verbleibenden Versuche um 1

            if passwort == "5328":  # Richtige Kombnation aus Code 1 - Code 2 (Differenz zwischen 7685 und 2357)
                print("Die Tuer laesst sich oeffnen")
                break  # beendet Schleife da richtige Eingabe
            else:  # falsche Eingabe, informiert Spieler über verbleibende Versuche
                print("Passwort falsch")
                print("Sie haben noch", anzahl_versuche, "versuche")
                if anzahl_versuche == 0:  # Wenn keine Versuche mehr übrig sind muss als Strafe der vorherige Raum gespielt werden, sodass man weiter kommt
                    print("Das Nummernfeld geht aus und Sie kommen nicht weiter")
                    time.sleep(2)
                    print("Du wirst eine Station nach hinten versetzt")
                    time.sleep(2)
                    gefaengnishof_1()  # startet erste Funktion neu

        print("In der Abstellkammer findest du einen weiteren Schlüssel")  # Belohnung für das Öffnen der Tür
        time.sleep(2)
        print("Du testet ein weiteres mal mit diesem Schlüssel die Türen und es lässt sich eine Tür öffnen!")
        time.sleep(2)
        print("Der Raum ist dunkel und du siehst hinten in der Ecke nur einen Umriss von einem Schreibtisch. \n"
              "In der andern Ecke steht eine Truhe und rechts von dir steht eine kleiner Werkzeugkoffer")
        time.sleep(2)
        print("Die Truhe ist wieder mit einem Zahlenschloss versperrt")  # neue Herausforderung

        # Variablen, die den Fortschritt des Spielers speichern
        seil_gefunden = False  # Gibt an, ob das Seil bereits gefunden wurde.
        code_gefunden = False  # Gibt an, ob der neue Code gefunden wurde.
        werkzeugkoffer_durchsucht = False

        while seil_gefunden == False:  # Schleife, die läuft, bis das Seil gefunden wurde.
            kommando = input("Was möchtest du dir ansehen? Schreibtisch / Truhe / Werkzeugkoffer:").lower()

            if kommando == "schreibtisch":  # Spieler untersucht den Schreibtisch.
                if code_gefunden == False:  # Code wurde noch nicht gefunden.
                    print("Auf dem Schreibtisch liegt nur ein Stift und ein Block")
                    time.sleep(2)
                    print(
                        "In der Schreibtischschublade ist ein kleines Notizbuch, indem auf der ersten Seite ein weiterer Code notiert ist.\n"
                        "Außerdem liegen ein paar Büroklammern in der Schublade")
                    time.sleep(2)
                    print("Der Code ist 1234")
                    # Spieler muss den Code korrekt eingeben.
                    benutzer_code = input("Bitte notiere den Code damit du ihn nicht vergisst:")
                    if benutzer_code == "1234":  # Richtiger Code.
                        code_gefunden = True  # Speichert, dass der Code gefunden wurde.
                        code["CODE_Teil3"] = benutzer_code  # Fügt den Code zum Dictionary hinzu.
                        print("richtiger Code!")
                        time.sleep(2)

                    else:
                        print("Falscher Code!")
                else:
                    print("Der Schreibtisch wurde bereits untersucht")
            elif kommando == "werkzeugkoffer":  # Spieler untersucht den Werkzeugkoffer.
                print(
                    "Im Wekzeugkoffer sind ein paar Maulschlüssel, sowie ein paar kleinere Bügelschellen, ansonsten ist er leer")
                werkzeugkoffer_durchsucht = True
            elif kommando == "truhe":  # Spieler untersucht die Truhe.
                if seil_gefunden == False:
                    if code_gefunden == True and werkzeugkoffer_durchsucht == True:  # Überprüft, ob alle Hinweise gefunden wurden
                        print("Die Truhe ist wie schon erwäht mit einem Zahlenschloss verschlossen")
                        time.sleep(2)
                        print("Villeicht bringt dich der Code, den du gerade notiert hast, weiter",
                              code.get("CODE_Teil3"))
                        # Spieler gibt den Code für die Truhe ein.
                        while True:  # Ausnahmebehandlung für den Valueerror
                            try:
                                zahlencode_truhe = int(input("Bitte gib den Code ein"))
                                if zahlencode_truhe == 1234:  # richtiger Code
                                    print("richtiger Code!")
                                    time.sleep(2)
                                    break  # beendet Eingabeschleife, nachdem der code korrekr eingegeben wurde
                                else:
                                    print("Falscher Code!")

                            except ValueError as e:  # Fehlermeldung falls ien String eingegeben wurde
                                print("Sie dürfen keinen String eingeben", e)
                        print("In der Truhe liegt ein Seil")  # Belohnung für das Lösen des Rätsels.
                        seil_gefunden = True  # Fortschritt wird aktualisiert.

                    else:
                        print("Du musst erst einen anderen Hinweis finden")  # Code fehlt noch
                else:
                    print("Die Truhe wurde bereits geöffnet")
                    time.sleep(2)
            else:  # Fehlermeldung bei falscher eingabe
                print("Unbekannter Befehl, probiere Schreibtisch / Truhe / Werkzeugkoffer")
        print("Mit dem Seil könntest du versuchen aus dem Fenster im oberen Stockwerk zu klettern")
        time.sleep(2)

        print("oben angekommen öffnest du das Fenster und siehst dich um wie du das Seil am besten befestigst \n"
              "Du könntest das Seil an das Geländer knoten, wobei du dir aber nicht sicher mit welchem Knoten das \n"
              "relativ dicke Seil zuverlässig hält")
        time.sleep(2)
        print(
            "Du hast unten in dem Werkzeugkoffer Bügelschellen gesehen, die du für die Seilverbindung ähnlich wie Seilklemmen nutzen könntest")
        time.sleep(2)
        print("Mit dem Seil aus dem Fenster zu klettern ist mit einem großen Risiko verbunden\n"
              "Du könntest auch nach einer Altenative suchen, um nich dein Leben zu riskieren")  # Erklärung der weiteren Geschichte

        while True:  # Der Spieler trifft eine Entscheidung um aus dem Gefängnis zu fliehen
            vorgehen = input(
                "Möchtest du die Bügelschellen holen, das Seil anknoten oder dir eine Alternative suchen? Knoten / Schelle / Altenative").lower()
            if vorgehen == "knoten":
                print(
                    "Du knotest das Seil an kletterst aus dem Fester und während des Abseilens löst sich das Seil vom Geländer und du fällst in die Teife und stirbst")
                time.sleep(2)
                print("Der Ausbruch ist fehlgeschlagen")  # Verloren
                break
            elif vorgehen == "schellen":
                print(
                    "Du gehst hinunter holst die Schellen, sowie den richtigen Schlüssel für diese und befestigst das Seil sicher an dem Geländer")
                time.sleep(2)
                print("Du kletterst aus dem Fenster, seilst dich ab und unten angekommen fliehst du in die Freiheit")
                time.sleep(2)
                print("Glückwunsch, du bist erfolgreich aus dem Gefängnis ausgebrochen")  # Gewonnen
                break
            elif vorgehen == "alternative":
                print("Du schaust dir nochmal alles in dem Wachturm an und überlegst wie du noch entkommen kannst\n"
                      "Du sitzt verzweifelt längere Zeit im Wachturm und überlegst, ob du doch die Flucht durchs Fenster wagst")
                time.sleep(2)
                print("Dir fällt ein, dass in der Schublade Büroklammern liegen")
                time.sleep(2)
                print("Du holst die Büroklammern und versuchst mit diesen das Schloss der Tür zu knacken")
                time.sleep(2)
                print("nach langem Probieren geligt es dir und du entkommst")
                print("Glückwunsch, du bist erfolgreich aus dem Gefängnis ausgebrochen")  # Gewonnen
                break
            else:  # Fehlermeldung bei falscher Eingabe
                print("Unbekannter Befehl, probiere Knoten / Schelle / Altenative")

    # Aufruf der zweiten Funktion
    gefaengnishof_2_wachturm()
#------------ende hof-----------------

#Zweiter Raum - Wärterbüro
#------------start büro----------------
def run_buero():
    zellennummern = {}  # Dictionarie für die Zellennummern erstellt

    def flur():  # Funktion für die Informationen aus dem Flur
        print("Du schleichst den Flur in Richtung Wärterbüro entlang und kommst dabei an drei Zellen vorbei!")
        print("Zelle 151")
        time.sleep(7)
        print("Zelle 24")
        time.sleep(4)
        print("Zelle 2")
        print("Um dir die Nummern zu merken, schreibst du sie dir auf den Arm!")
        zellennummern["zelle_1"] = input("Nummer der ersten Zelle:")  # Eingabe wird im Dictionary gespeichert
        zellennummern["zelle_2"] = input("Nummer der zweiten Zelle:")  # Eingabe wird im Dictionary gespeichert
        zellennummern["zelle_3"] = input("Nummer der dritten Zelle:")  # Eingabe wird im Dictionary gespeichert

    flur()  # Starten der Flur-Funktion

    def tuer_waerterbuero():
        print("An der Tür ist ein PIN-Pad angebracht. Es wird eine vierstellige PIN benötigt")
        print("____")
        print("Vor ein paar Tagen konntest du die Wärter über eine Änderung des Codes belauschen.\n"
              "Du kannst dich leider nur noch an wenig erinnern.\n"
              "Die erste Stelle des Codes war die Quersumme der ersten Zellennummer.")
        i = 5
        while i >= 0:  # While-Schleife für die Eingabe und Verarbeitung der ersten Ziffer des Pin-Codes
            while True:  # Ausnahmebehandlung für den Value Error
                try:
                    pin_1 = int(input("1.Zahl:"))  # Eingabe der ersten Zahl des Pin-Codes
                    break
                except ValueError:
                    print("Bitte gib eine Ganzzahl ein!")
            if pin_1 == 7:  # Vergleich der eingegebenen Zahl und der Lösung
                print(pin_1, "___")  # Ausgabe des Zahlenfeldes
                break
            else:  # Wenn die Zahl falsch ist wird der folgende Codeblock abgearbeitet
                print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
                if i == 0:
                    print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                    flur()  # Rückschritt in erste Funktion
                i -= 1
        print(
            "Für die zweite Ziffer haben die Wachleute irgendwas von Modulo Zelle 1 durch Zelle 3 gefaselt")  # Aufgabe für die zweite Ziffer
        zahl_1 = int(zellennummern.get("zelle_1"))  # Variable erstellen und Zahl aus Dictionary holen
        zahl_2 = int(zellennummern.get("zelle_3"))  # Variable erstellen und Zahl aus Dictionary holen
        ergebniss_2 = zahl_1 % zahl_2  # Berechnung mit den beiden Zahlen durchführen und in der Variable speichern
        j = 5
        while j >= 0:  # Schleife zur Eingabe und Verarbeitung der zweiten Ziffer des Pin-Codes
            while True:  # Ausnahmebehandlung für den Value Error
                try:
                    pin_2 = int(input("2.Zahl:"))  # Eingabe der zweiten Ziffer des Pin-Codes
                    break
                except ValueError:
                    print("Bitte gib eine Ganzzahl ein!")
            if pin_2 == ergebniss_2:  # Vergleich der beiden Variablen ob die Zahlen übereinstimmen
                print(pin_1, pin_2, "__")
                break
            else:
                print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
                if j == 0:
                    print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                    flur()  # Rückschritt in erste Funktion
                j -= 1
        print("Die letzen beiden Ziffern der PIN sind die Ziffern der zweiten Zelle umgekehrt!")
        zahl_3 = int(zellennummern.get("zelle_2"))  # Zahlenwert aus dem Dictionary holen
        ergebniss_34 = str(zahl_3)[::-1]  # Zahlenwert umdrehen und in der variable speichern
        ergebniss_34 = int(ergebniss_34)  # Str in Int umwandeln um damit weiterarbeiten zu können
        k = 5
        while k >= 0:  # Schleife zur Eingabe und Verarbeitung der dritten und vierten Ziffer des Pin-Codes
            while True:  # Ausnahmebehandlung für den Value Error
                try:
                    pin_34 = int(input("Dritte und vierte Ziffer:"))  # Eingabe der letzen beiden Ziffern des Pin-Codes
                    break
                except ValueError:
                    print("Bitte gib eine Ganzzahl ein!")
            if pin_34 == ergebniss_34:  # Vergleich von Eingabe und Ergebnis
                print(pin_1, pin_2, pin_34)
                break
            else:
                print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
                if k == 0:
                    print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                    flur()  # Rückschritt in erste Funktion
                k -= 1
        print("Die Tür zum Wächterbüro öffnet sich und du gehst hinein!")

    tuer_waerterbuero()  # Starten der Wärterbürotür-Funktion

    def waerterbuero():  # Erstellen des nächsten Raumes über eine Funktion
        print("Im Wärterbüro angekommen, schaust du dich um und entdeckst die Steuerung der\n"
              "Überwachungskameras. Diese musst du für deine Flucht unbedingt deaktivieren!\n"
              "Du gehst zum Terminal und siehst, dass du einen USB-Stick zum Entriegeln brauchst.\n"
              "Du schaust dich um und siehst in dem Raum einen Schrank, einen Schreibtisch, eine kleine Schachtel und einen Stuhl.")
        found = False
        schere = False  # Variable auf False gesetzt, Schere noch nicht gefunden
        while found == False:  # While-Schleife für die Auswahl von Orten zum suchen
            kommando = input(
                "Was möchtest du dir als erstes Ansehen? Schrank / Schreibtisch / Stuhl / Schachtel").lower()  # Variable in denen die Auswahl gespeicchert wird
            if kommando == "stuhl" and schere == True:  # Stuhl ausgewählt
                print("Der Stuhl quietscht als du dich drauf setzt.\n"
                      "Du merkst, wie dir etwas in den Rücken sticht.\n"
                      "Du beginnst die Stelle mit deiner Schere aufzuschneiden und findest den USB-Stick!")
                found = True
                break
            if kommando == "stuhl" and schere == False:  # Stuhl ausgewählt und Schere gefunden
                print("Du siehst in dem Stuhl einen USB-Stick-förmigen Abdruck.\n"
                      "Hättest du nur eine Schere um den Stuhl aufzuschneiden")
            if kommando == "schrank":  # Schrank ausgewählt
                print("Du öffnest die Schranktüren und es fallen dir lauter Ordner entgegen.\n"
                      "Hier hat wohl seit Jahren keiner mehr aufgeräumt!\n"
                      "Du durchsuchst die Ordner, aber findest leider keinen USB-Stick!")
                found = False
            if kommando == "schreibtisch":  # Schreitisch ausgewählt
                print("Du gehst zum Schreibtisch und öffnest die Schubladen, leider findest du keinen USB-Stick!")
                found = False
            if kommando == "schachtel":  # Schachtel ausgewählt
                print("Du hebst die Schachtel auf und versuchst sie zu öffnen. Der Verschluss klemmt. \n"
                      "Mit ein bisschen Kraft lässt sich die Schachtel dennoch öffnen und du findest eine Schere!")
                schere = True  # Variable Schere wird auf True gesetzt
            if kommando != "schrank" and kommando != "schreibtisch" and kommando != "stuhl" and kommando != "schachtel":  # Ausnahmebehandlung von falscher Eingabe
                print("Bitte gib einen der angegebenen Gegenstände ein!")
        if found == True:  # USB-Stick wurde gefunden und das Programm läuft weiter
            print("Mit dem USB-Stick kannst du endlich die Kameras deaktivieren.")
            time.sleep(1)
            print("Das Display der Kamerasteuerung blinkt rot auf, als du den USB-Stick einsteckst!\n"
                  "Die Kameras sind deaktiviert!\n"
                  "Nun kannst du dich endlich um die Tür zum Hof kümmern.\n"
                  "Du verlässt das Büro und gehst Richtung Hoftür.")
            time.sleep(2)
            run_hof()

    waerterbuero()  # Starten der Wärterbüro-Funktion

    def flur_2():  # Erstellen der Funktion flur_2
        print("Auf dem Weg zur Hoftür musst du durch eine weitere Tür.\n"
              "Während du zu der Tür läufst, gehst du an drei Spinden vorbei.\n"
              "An der Tür angekommen, siehts du, dass die Tür durch eine Nutmutter verschlossen ist.\n"
              "Um diese zu lösen benötigst du ein passendes Werkzeug!")
        while True:  # While-Schleife für die Auswahlmöglichkeiten der Schränke
            wahl = input(
                "Welchen Schrank möchtest du durchsuchen? 1, 2 oder 3?")  # Erstellen der Variable für die Auswahl
            if wahl == "1":  # Anwahl 1 wird verarbeitet
                print("Du öffnest den Schrank 1 und findest die Gefängniskleidung!")
            if wahl == "2":  # Anwahl 2 wird verarbeitet
                print("Du öffnest den Schrank 2 und findest Geschirr für die Kantine")
            if wahl == "3":  # Anwahl 3 wird verarbeitet
                print("Du öffnest den Schrank 3 und findest drei Werkzeuge!\n"
                      "einen Maulschlüssel, einen Hakenschlüssel und einen Schraubendreher!")
                break  # Schleife wird abgebrochen
        print("Wieder an der Tür angekommen, musst du dich entscheiden welches Werkzeug du verwenden möchtest!")
        while True:
            auswahl = input(
                "Welches Werkzeug möchtest du ausprobieren? Maulschlüssel / Hakenschlüssel / Schraubendreher").lower()
            if auswahl == "maulschlüssel":
                print("Der Maulschlüssel rutscht über die Nutmutter und löst diese nicht!")
            if auswahl == "hakenschlüssel":
                print("Der Hakenschlüssel passt einwandfrei! Die Nutmutter löst sich und die Tür lässt sich öffnen!")
                break
            if auswahl == "schraubendreher":
                print("Du setzt den Schraubendreher an und rutscht ab! Die Nutmutter lässt sich nicht lösen!")
        print("Die Tür hat sich geöffnet und du kannst weiter in Richtung Hoftür gehen!")

    flur_2()

    def hoftuer():
        print("Das Display leuchtet ROT auf!")
        time.sleep(2)
        print("Das Display leuchtet GELB auf!")
        time.sleep(2)
        while True:  # While Schleife zum Auswerten der Eingabe des Spielers
            farbe_1 = input("Welche Farbe ergibt diese Kombination?").lower()  # Eingabe der Lösung des Spielers
            if farbe_1 == "orange":
                print("Das war richtig!")
                break
            else:
                print("Falsch! Bitte probier es erneut! Achte auch auf die Rechtschreibung!")
        print("Das Display leuchtet BLAU auf!")
        time.sleep(2)
        print("Das Display leuchtet GELB auf!")
        time.sleep(2)
        while True:  # While Schleife zum Auswerten der Eingabe des Spielers
            farbe_2 = input("Welche Farbe ergibt die Kombination?").lower()  # Eingabe der Lösung des Spielers
            if farbe_2 == "grün":
                print("Das war richtig!")
                break
            else:
                print("Falsch! Bitte probier es erneut! Achte auch auf die Rechtschreibung!")
        print("Das Display leuchtet LILA auf!")
        time.sleep(2)
        farbe_3 = input("Was ist die Komplementärfarbe von Lila?").lower()  # Eingabe der Lösung des Spielers
        while True:  # While Schleife zum Auswerten der Eingabe des Spielers
            if farbe_3 == "gelb":
                print("Das war richtig!")
                break
            else:
                print("Falsch! Bitte probier es erneut! Kleiner Tipp: Die Farbe der Sonnenblume!")
        print("Das Display leuchtet MAGENTA auf!")
        time.sleep(2)
        while True:  # While Schleife zum Auswerten der Eingabe des Spielers
            antwort = input(
                "Welches Unternehmen verbindest du mit der Farbe?").lower()  # Eingabe der Lösung des Spielers
            if antwort == "telekom":  # Vergleich von Antwort mit Lösung
                print("Das war richtig!")
                break
            else:
                print("Falsch! Bitte probier es erneut! Kleiner Tipp: Sie kümmern sich um Internet!")
        print("Das Display leuchtet WEIß auf!")
        while True:  # While Schleife zum Auswerten der Eingabe des Spielers
            antwort = input("Welchen Kontinent verbindest du mit der Farbe?").lower()  # Eingabe der Lösung des Spielers
            if antwort == "antarktis":  # Vergleich von Antwort mit Lösung
                print("Das war richtig!")
                break
            else:
                print("Falsch! Bitte probier es erneut! Kleiner Tipp: Dort leben Pinguine!")
        print("Das Display leuchtet GRÜN auf und die Hoftür entriegelt sich!")

    hoftuer()  # Starten der Hoftür-Funktion
#------------ende büro-----------------

#Erster Raum - Gefängniszelle
#------------start zelle----------------
def run_zelle():
    # Dictionary erstelllen
    program_keys = {"key": False,
                    "chest": False,
                    "box": False,
                    "bed": False,
                    "desk": False,
                    "carpet": False,
                    "tool": False,
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
    text = (
        "Langsam öffnest du deine Augen und Findest dich alleine auf einem kargen Bett in einer kleinen Gefängniszelle wieder.\n"
        "Du bist noch ganz verwirrt und kannst dich nicht recht erinnern, wie du hierher gekommen bist.\n"
        "Du stehst auf und schaust dich erstmal um. In deiner Zelle befinden sich ein Bett, zwei kleine Lampe, ein kleiner Tisch, ein Teppich und eine große Truhe.\n"
        "Du gehst zur Zellentür und versuchst sie zu öffnen. Ohne Erfolg, die Tür ist verriegelt!\n"
        "Allerdings siehst du, dass sich neben der Tür ein Eingabefeld mit Zahlen befindet. Du musst irgendwie versuchen den passenden Code herauszufinden...\n\n"
        "Als nächstes versuchst du dein Glück bei der Truhe...\n"
        "Ebenfalls abgeschlossen. Du schaust dich nochmals im Raum um, auf der Suche nach etwas was dir helfen könnte die Truhe zu öffnen.\n")  # Textinhalt setzen
    text_widget.insert("1.0", text)  # Textinhalt dem Text-Widget hinzufügen

    # Eingabefeld für das Lösungswort
    input1_describtion = tk.Label(cell)
    input1_describtion.configure(text="Code-Box: ", font='Helvetica 14')
    user_input1 = tk.Entry(cell)
    user_input1.configure(font='Helvetica 14')

    # Eingabefeld für den Zahlencode
    input2_describtion = tk.Label(cell)
    input2_describtion.configure(text="Zahlencode-Tür: ", font='Helvetica 14')
    user_input2 = tk.Entry(cell)
    user_input2.configure(font='Helvetica 14')

    # Funktion fürs Verfärben von Zahlen
    def color_numbers(text_widget):
        color_numbers = ['7', '3', '4', '9']  # Zahlen die hervorgehoben werden sollen
        for number in color_numbers:
            start_index = "1.0"
            while True:
                # Nach der aktuellen Zahl im Text suchen
                start_index = text_widget.search(number, start_index, tk.END)
                if not start_index:
                    break
                # Berechnen des Endindex für die Tag-Anwendung
                end_index = f"{start_index} + 1 chars"
                # Tag für die gefundenen Zahlen anwenden
                text_widget.tag_add("color", start_index, end_index)
                text_widget.tag_configure("color", foreground="green", font='bold')
                # Startindex aktualisieren
                start_index = end_index

    # Funktionen fürs Anklicken verschiedener Stellen im Bild
    def key_action():
        if program_keys["key"] == False:
            program_keys["key"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nDu hast einen Schlüssel gefunden!\n")
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
                text_widget.insert(tk.END, "\nMit dem Schlüssel lässt sich die Truhe erfolgreich öffnen.\n"
                                           "Du findest das zweite drittel eines Zettels auf dem steht:\n"
                                           "\"Um 3 Uhr Nachmittags gehen jeden Tag die Wachen auf ihrem Kontrollgang durch den Korridor.\"\n"
                                           "Außerdem findest du eine kleine verschlossene Box. Sie scheint sich mit einem Passwort öffnen zu lassen.\n"
                                           "Weißt du das Passwort?\n"
                                   )
                color_numbers(text_widget)
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
                program_keys["chest"] = True
                program_keys["box"] = True
                input1_describtion.place(x=50, y=1115)
                user_input1.place(x=270, y=1115)
                button_check1.place(x=575, y=1105)
            else:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,
                                   "\nDie Truhe ist verschlossen.\nDu kannst sie nicht öffnen schaue dich nochmal um!\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nDu hast den Zettel schon gesehen!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")

    def bed_action():
        if program_keys["bed"] == False:
            program_keys["bed"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,
                               "\nDu findest unter der Matratze das erste drittel eines Zettels auf dem steht:\n"
                               "\"Jeden morgen stehe ich um 7 Uhr auf und die Sonne fällt durchs Fenster genau auf das Schloss der Tür\"\n")
            color_numbers(text_widget)
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nDu hast dir das Bett bereits angesehen!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")

    def desk_action():
        if program_keys["desk"] == False:
            program_keys["desk"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END,
                               "\nDu findest in der Schublade des Tisches einen Zettel mit einem Rätsel drauf:\n"
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
            text_widget.insert(tk.END, "\nDu hast dir den Tisch schon angesehen!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")

    def secret_exit():
        if program_keys["carpet"] == False:
            program_keys["carpet"] = True
            program_keys["tool"] = True
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nGlückwunsch! Du hast ein Geheimnis gefunden!\n"
                                       "Du rollst den Teppich zurück und findest erst einmal nichts. Doch bei genauerer Betrachtung fällt dir etwas auf:\n"
                                       "Unter dem Teppich hat der Boden Risse und scheint an einer Stelle leicht erhöht zu sein.\n"
                                       "Du nimmst an dieser Stelle einen losen Brocken Beton aus dem Boden und entdeckst etwas großartiges:\n\n"
                                       "Eine FEILE!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")
        else:
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, "\nDu hast das Geheimnis bereits entdeckt!\n")
            text_widget.see(tk.END)
            text_widget.configure(state="disabled")

    def window_action():
        try:
            if program_keys["tool"] == True:
                text_widget.configure(state="normal")
                text_widget.insert(tk.END,
                                   "\nDu sägst mit der Feile die Gitterstäbe durch und entkommst durch das Fenster in die Freiheit!\n")
                text_widget.see(tk.END)
                text_widget.configure(state="disabled")
                cell.after(4000, cell.destroy)
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

    def door_action():
        input2_describtion.place(x=50, y=1155)
        user_input2.place(x=270, y=1155)
        button_check2.place(x=575, y=1150)

    # Unsichtbare Rechtecke (als klickbarer Bereiche) erstellen
    rect_key = canvas.create_rectangle(370, 580, 470, 660, fill="", outline="")
    rect_chest = canvas.create_rectangle(220, 380, 250, 420, fill="", outline="")
    rect_bed = canvas.create_rectangle(540, 300, 750, 470, fill="", outline="")
    rect_desk = canvas.create_rectangle(300, 340, 420, 380, fill="", outline="")
    rect_secret = canvas.create_rectangle(150, 755, 160, 765, fill="", outline="")
    rect_window = canvas.create_rectangle(250, 0, 460, 240, fill="", outline="")
    # Text (als klickbaren Bereich) erstellen
    text_door = canvas.create_text(360, 770, text="▽ Zellentür betrachten ▽", font=("Arial", 16), fill="grey", )

    # Klick-Ereignisse zu den jeweiligen Rechtecken hinzufügen
    canvas.tag_bind(rect_key, "<Button-1>", lambda event: key_action())
    canvas.tag_bind(rect_chest, "<Button-1>", lambda event: chest_action())
    canvas.tag_bind(rect_bed, "<Button-1>", lambda event: bed_action())
    canvas.tag_bind(rect_desk, "<Button-1>", lambda event: desk_action())
    canvas.tag_bind(rect_secret, "<Button-1>", lambda event: secret_exit())
    canvas.tag_bind(rect_window, "<Button-1>", lambda event: window_action())
    canvas.tag_bind(text_door, "<Button-1>", lambda event: door_action())

    # Funktion zur Überprüfung des Lösungsworts (Verarbeitung der Eingabe des oberen Eingabefeld)
    def check_password():
        eingabe_wort = user_input1.get().lower()
        if program_keys["box"] == True:
            if eingabe_wort == "freiheit":
                output = (
                    "\nDie Box lässt sich nun öffnen. In ihr ist das letzte drittel eines Zettels, auf dem steht:\n\n"
                    "\"Es sind insgesamt 4 Wachen, die diesen Zellblock jeden Abend um 9 Uhr kontrollieren!\"")
            else:
                output = ("\nFalsches Passwort!\n")
        else:
            output = ("Ihr scheint die Box noch nicht gefunden zu haben!\n")
        # Text zur Ausgabe hinzufügen
        text_widget.configure(state="normal")
        text_widget.insert(tk.END, "\n" + output + "\n")
        color_numbers(text_widget)
        text_widget.see(tk.END)
        text_widget.configure(state="disabled")

    # Funktion zur Überprüfung des Zahlencodes (Verarbeitung der Eingabe des unteren Eingabefeld)
    def check_code():
        eingabe_code = user_input2.get().strip()
        if eingabe_code == "7349":
            output = ("\nHurra! Die Zellentür lässt sich öffnen und du kommst auf den Korridor vor den Zellen.\n\n"
                      "Anmerkung: Das Spiel geht von nun an in der Konsole weiter")
            cell.after(5000, cell.destroy)
            run_buero()
        else:
            output = ("\nDas Passwort ist falsch!\n")
        text_widget.configure(state="normal")
        text_widget.insert(tk.END, "\n" + output + "\n")
        text_widget.see(tk.END)
        text_widget.configure(state="disabled")

    # Prüfen-Schaltfläche für Lösungswort (verarbeitung)
    button_check1 = tk.Button(cell, text="BESTÄTIGEN", font='Helvetica 14', command=check_password, height=1, width=15,
                              bg="lightgreen", fg="black")
    # Button wird erst angezeigt, wenn die Truhe geöffnet wurde

    # Prüfen-Schaltfläche für Zahlencode (verarbeitung)
    button_check2 = tk.Button(cell, text="BESTÄTIGEN", font='Helvetica 14', command=check_code, height=1, width=15,
                              bg="lightgreen", fg="black")
    # Button wird erst angezeigt, wenn 'Zellentür betrachten' ausgewählt wird

    # GUI starten
    cell.mainloop()
#------------ende zelle-----------------

#Funktion -> Zeigt Auswahlmöglichkeiten der Räume
def show_buttons():
    start.place_forget()
    wahl.place_forget()
    beenden.place_forget()
    zurueck.place(relx=0.5, rely=0.35, anchor='center')
    zelle.place(relx=0.5, rely=0.45, anchor='center')
    buero.place(relx=0.5, rely=0.54, anchor='center')
    hof.place(relx=0.5, rely=0.63, anchor='center')
# Funktion -> Kehrt zum Hauptmenü zurück
def hide_buttons():
    zurueck.place_forget()
    zelle.place_forget()
    buero.place_forget()
    hof.place_forget()
    start.place(relx=0.5, rely=0.35, anchor='center')
    wahl.place(relx=0.5, rely=0.45, anchor='center')
    beenden.place(relx=0.5, rely=0.55, anchor='center')

#Funktion -> Geht zum ersten Raum
def start_spiel():
    root.destroy()
    run_zelle()
#Funktion -> Geht zum zweiten Raum
def start_buero():
    root.destroy()
    run_buero()
#Funktion -> Geht zum dritten Raum
def start_hof():
    root.destroy()
    run_hof()
#Funktion -> Beendet Startfenster
def spielende():
    root.destroy()

#Buttons zum Starten des Spiels
start = tk.Button(root, text="Starte das Spiel", font='Helvetica 20', command=start_spiel, height=1, width=15, bg="black", fg="white")
start.place(relx = 0.5, rely = 0.35, anchor = 'center')
wahl = tk.Button(root, text="Wähle einen Raum", font='Helvetica 20', command=show_buttons, height=1, width=15, bg="black", fg="white")
wahl.place(relx = 0.5, rely = 0.45, anchor = 'center')
zurueck = tk.Button(root, text="Zurück", font='Helvetica 20', command=hide_buttons, height=1, width=15, bg="black", fg="white")
zelle = tk.Button(root, text="Starte in Zelle", font='Helvetica 20', command=start_spiel, height=1, width=15, bg="black", fg="white")
buero = tk.Button(root, text="Starte in Wärterbüro", font='Helvetica 20', command=start_buero, height=1, width=15, bg="black", fg="white")
hof = tk.Button(root, text="Starte in Hof", font='Helvetica 20', command=start_hof, height=1, width=15, bg="black", fg="white")
beenden = tk.Button(root, text="Beenden", font='Helvetica 20', command=spielende, height=1, width=15, bg="black", fg="white")
beenden.place(relx = 0.5, rely = 0.55, anchor = 'center')

#GUI starten
root.mainloop()