#if uebergang == True:
import time # Importieren des Zeit Moduls, um Pausen zwischen den print-Befehlen zu erzeugen

code = {} # leeres Dictionary, um Codes zu speichern, die der Spieler während des Spiels sammelt

# Diese Funktion simuliert die erste Stufe des Spiels, in der der Spieler Hinweise und einen Schlüssel finden muss,
# um in den Wachturm zu gelangen.
def gefaengnishof_1():
    print("Du hast in der naechsten Stufe den Gefaengnishof erreicht und musst einen Weg finden, in den Wachturm zu gelangen.")
    time.sleep(2)
    print("Als du ueber den Hof gehst, siehst du mehrere einzelne Stationen.")
    time.sleep(2)
    print("Du kommst auf dem Weg zum Wachturm an einer Treppe, einem Tisch und einer Kiste vorbei.")
    time.sleep(2)
    print("Der Wachturm ist verschlossen und man benoetigt einen Schluessel, um hineinzukommen.") # Einleitung in das Thema des Raumes

    #Variablen, die den Fortschritt des Spielers speichern
    schluessel_gefunden = False # Gibt an, ob der Schlüssel gefunden wurde
    teilcode_gefunden = False   # Gibt an, ob der erste Code gefunden wurde
    teilcode2_gefunden = False  # Gibt an, ob der zweite Code gefunden wurde
    tuer_wachturm = False       # Gibt an, ob die Wachturm-Tür bereits geöffnet wurde

    # Schleife, damit alle Stationen wiederholt werden, bis Wachturm erreicht wurde
    while True:
        print("Du siehst dir nochmals die Umgebung an.")
        kommando = input("Zu welcher Station moechtest du gehen? (Treppe/Kiste/Tisch/Wachturm): ").lower() # Spieler wählt Station
        time.sleep(2)

        # Überprüfen der Eingabe (Station)
        if kommando == "treppe":
            if not schluessel_gefunden: # Überprüfen, ob Schlüssel bereits gefunden
                print("Glueckwunsch! Unter der Treppe liegt ein Schluessel,den ein Wachmann dort verloren haben musss.")
                time.sleep(2)
                print("Du hebst den Schluesssel auf")
                schluessel_gefunden = True # Variable wird auf True gesetzt, da Schlüssel gefunden wurde
                time.sleep(2)
            else:
                print("Die Treppe wurde bereits untersucht.")
                time.sleep(2)

        elif kommando == "kiste":
            if not teilcode_gefunden: # Überprüfen, ob Teilcode aus Kiste bereits gefunden
                print("In der Kiste ist ein Hinweis mit einem Code: 2357.")
                benutzer_code = input("Bitte notiere den Code, damit du ihn nicht vergisst: ") # Aufforderung den Code zu notieren, für spätere Spielschritte
                if benutzer_code == "2357":  # Überpruefen, ob der eingegebene Code richtig ist
                    code["CODE_Teil1"] = benutzer_code
                    print("Richtiger Code!")
                    teilcode_gefunden = True # Variable wird auf True gesetzt, wenn Teilcode "Kiste" gefunden
                    time.sleep(2)
                else:
                    print("Falscher Code!")
                    time.sleep(2)
            else:
                print("Die Kiste wurde bereits untersucht.")
                time.sleep(2)

        elif kommando == "tisch":
            if not teilcode2_gefunden: # Überprüfen, ob Teilcode vom Tisch bereits gefunden
                print("Unter dem Tisch ist ein Hinweis mit einem Code: 7685 den ein Informant fuer dich dort hinterlassen hat")
                benutzer_code = input("Bitte notiere den Code,damit du ihn nicht vergisst: ") # Aufforderung den Code zu notieren, für spätere Spielschritte
                if benutzer_code == "7685":  # Überpruefen, ob der eingegebene Code richtig ist
                    code["CODE_Teil2"] = benutzer_code
                    print("Richtiger Code!")
                    teilcode2_gefunden = True # Variable wird auf True gesetzt, wenn Teilcode "Tisch" gefunden
                    time.sleep(2)
                else:
                    print("Falscher Code!")
                    time.sleep(2)
            else:
                print("Die Bank wurde bereits untersucht.")
                time.sleep(2)

        elif kommando == "wachturm":
            if not tuer_wachturm: # Überprüfen, ob Wachturm bereits betreten wurde
                # Überprüfe, ob der Spieler alle notwendigen Hinweise gefunden hat, um in diese Station zu gelangen
                if schluessel_gefunden and teilcode_gefunden and teilcode2_gefunden:
                    print("Du hast alle Hinweise in den Stationen sowie den Schluessel gefunden und kommst somit in die naechste Stufe.")
                    tuer_wachturm = True # Variable wird auf True gesetzt, wenn Wachturm betreten wird
                    time.sleep(2)
                    break # Schleife wird beendet und nächste Station wird erreicht
                else:
                    print("Du musst erst alle Hinweise in dieser Stufe finden, um in den Wachturm zu gelangen")
                    time.sleep(2)
            else:
                print("Der Wachturm ist bereits betreten worden.")
                time.sleep(2)
        else: # Fehlermeldungen für die Eingabe falscher Kommandos
            print("Unbekannter Befehl. Versuche eines der vier Befehle: Treppe, Kiste, Bank, Wachturm.")
            time.sleep(2)

# Aufruf der Funktion um die erste Station
gefaengnishof_1()

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
          "also ist deine letzte Hoffnung die Abstellkammper ") # Einleitung in den Wachturm und zur neuen Herausforderung
    time.sleep(2)
    print("Dein Informant, der die Hinweise sorgfaeltig versteckt hat, erklaerte, \n"
          "dass sich das Passwort aus dem einen Hinweis minus dem anderen Hinweis zusammensetzt. Er war sich aber unsicher wie herum")
    print("Hinweis aus der ersten Stufe", code.get("CODE_Teil1"),",", code.get("CODE_Teil2")) # Hinweise zum digitalen Zahlenschloss

    # Eingabe des Codes
    anzahl_versuche = 3 # Der Spieler hat drei Versuche das richtige Passwort einzugeben
    while anzahl_versuche > 0: # Schleife die solange läuft, bis keine Versuche
        passwort = input("Bitte geben Sie das Passwort ein:") # Spieler gibt Passwort ein
        anzahl_versuche -= 1 # Reduziert verbleibenden Versuche um 1

        if passwort == "5328": # Richtige Kombnation aus Code 1 - Code 2 (Differenz zwischen 7685 und 2357)
            print("Die Tuer laesst sich oeffnen")
            break # beendet Schleife da richtige Eingabe
        else: # falsche Eingabe, informiert Spieler über verbleibende Versuche
            print("Passwort falsch")
            print("Sie haben noch", anzahl_versuche, "versuche")
            if anzahl_versuche == 0: # Wenn keine Versuche mehr übrig sind muss als Strafe der vorherige Raum gespielt werden, sodass man weiter kommt
                print("Das Nummernfeld geht aus und Sie kommen nicht weiter")
                time.sleep(2)
                print("Du wirst eine Station nach hinten versetzt")
                time.sleep(2)
                gefaengnishof_1() # startet erste Funktion neu

    print("In der Abstellkammer findest du einen weiteren Schlüssel") # Belohnung für das Öffnen der Tür
    time.sleep(2)
    print("Du testet ein weiteres mal mit diesem Schlüssel die Türen und es lässt sich eine Tür öffnen!")
    time.sleep(2)
    print("Der Raum ist dunkel und du siehst hinten in der Ecke nur einen Umriss von einem Schreibtisch. \n"
          "In der andern Ecke steht eine Truhe und rechts von dir steht eine kleiner Werkzeugkoffer")
    time.sleep(2)
    print("Die Truhe ist wieder mit einem Zahlenschloss versperrt") # neue Herausforderung

    # Variablen, die den Fortschritt des Spielers speichern
    seil_gefunden = False # Gibt an, ob das Seil bereits gefunden wurde.
    code_gefunden = False # Gibt an, ob der neue Code gefunden wurde.
    werkzeugkoffer_durchsucht = False

    while seil_gefunden == False: # Schleife, die läuft, bis das Seil gefunden wurde.
        kommando = input("Was möchtest du dir ansehen? Schreibtisch / Truhe / Werkzeugkoffer:").lower()

        if kommando == "schreibtisch": # Spieler untersucht den Schreibtisch.
            if code_gefunden == False: # Code wurde noch nicht gefunden.
                print("Auf dem Schreibtisch liegt nur ein Stift und ein Block")
                time.sleep(2)
                print("In der Schreibtischschublade ist ein kleines Notizbuch, indem auf der ersten Seite ein weiterer Code notiert ist.\n"
                      "Außerdem liegen ein paar Büroklammern in der Schublade")
                time.sleep(2)
                print("Der Code ist 1234")
                # Spieler muss den Code korrekt eingeben.
                benutzer_code = input("Bitte notiere den Code damit du ihn nicht vergisst:")
                if benutzer_code == "1234": # Richtiger Code.
                    code_gefunden = True # Speichert, dass der Code gefunden wurde.
                    code["CODE_Teil3"] = benutzer_code # Fügt den Code zum Dictionary hinzu.
                    print("richtiger Code!")
                    time.sleep(2)

                else:
                    print("Falscher Code!")
            else:
                print("Der Schreibtisch wurde bereits untersucht")
        elif kommando == "werkzeugkoffer": # Spieler untersucht den Werkzeugkoffer.
            if werkzeugkoffer_durchsucht == False: # Werkzeugkoffer wurde noch nicht durchsucht
                print("Im Wekzeugkoffer sind ein paar Maulschlüssel, sowie ein paar kleinere Bügelschellen, ansonsten ist er leer")
                werkzeugkoffer_durchsucht = True # speichert das Werzeugkoffer durchsucht
            else:
                print("Der Werkzeugkoffer wurde bereits untersucht!")
        elif kommando == "truhe": # Spieler untersucht die Truhe.
            if seil_gefunden == False:
                if code_gefunden == True and werkzeugkoffer_durchsucht == True: # Überprüft, ob alle Hinweise gefunden wurden
                    print("Die Truhe ist wie schon erwäht mit einem Zahlenschloss verschlossen")
                    time.sleep(2)
                    print("Villeicht bringt dich der Code, den du gerade notiert hast, weiter", code.get("CODE_Teil3"))
                    # Spieler gibt den Code für die Truhe ein.
                    while True: # Ausnahmebehandlung für den Valueerror
                        try:
                            zahlencode_truhe = int(input("Bitte gib den Code ein"))
                            if zahlencode_truhe == 1234: # richtiger Code
                                print("richtiger Code!")
                                time.sleep(2)
                                break # beendet Eingabeschleife, nachdem der code korrekr eingegeben wurde
                            else:
                                print("Falscher Code!")

                        except ValueError as e: # Fehlermeldung falls ien String eingegeben wurde
                            print("Sie dürfen keinen String eingeben", e)
                    print("In der Truhe liegt ein Seil") # Belohnung für das Lösen des Rätsels.
                    seil_gefunden = True  # Fortschritt wird aktualisiert.

                else:
                    print("Du musst erst einen anderen Hinweis finden") # Code fehlt noch
            else:
                print("Die Truhe wurde bereits geöffnet")
                time.sleep(2)
        else: # Fehlermeldung bei falscher eingabe
            print("Unbekannter Befehl, probiere Schreibtisch / Truhe / Werkzeugkoffer")
    print("Mit dem Seil könntest du versuchen aus dem Fenster im oberen Stockwerk zu klettern")
    time.sleep(2)

    print("oben angekommen öffnest du das Fenster und siehst dich um wie du das Seil am besten befestigst \n"
          "Du könntest das Seil an das Geländer knoten, wobei du dir aber nicht sicher mit welchem Knoten das \n"
          "relativ dicke Seil zuverlässig hält")
    time.sleep(2)
    print("Du hast unten in dem Werkzeugkoffer Bügelschellen gesehen, die du für die Seilverbindung ähnlich wie Seilklemmen nutzen könntest")
    time.sleep(2)
    print("Mit dem Seil aus dem Fenster zu klettern ist mit einem großen Risiko verbunden\n"
          "Du könntest auch nach einer Altenative suchen, um nich dein Leben zu riskieren") # Erklärung der weiteren Geschichte

    while True: # Der Spieler trifft eine Entscheidung um aus dem Gefängnis zu fliehen
        vorgehen = input("Möchtest du die Bügelschellen holen, das Seil anknoten oder dir eine Alternative suchen? Knoten / Schelle / Altenative").lower()
        if vorgehen == "knoten":
            print("Du knotest das Seil an kletterst aus dem Fester und während des Abseilens löst sich das Seil vom Geländer und du fällst in die Teife und stirbst")
            time.sleep(2)
            print("Der Ausbruch ist fehlgeschlagen") # Verloren
            break
        elif vorgehen == "schelle":
            print("Du gehst hinunter holst die Schellen, sowie den richtigen Schlüssel für diese und befestigst das Seil sicher an dem Geländer")
            time.sleep(2)
            print("Du kletterst aus dem Fenster, seilst dich ab und unten angekommen fliehst du in die Freiheit")
            time.sleep(2)
            print("Glückwunsch, du bist erfolgreich aus dem Gefängnis ausgebrochen") # Gewonnen
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
            print("Glückwunsch, du bist erfolgreich aus dem Gefängnis ausgebrochen") # Gewonnen
            break
        else: # Fehlermeldung bei falscher Eingabe
            print("Unbekannter Befehl, probiere Knoten / Schelle / Altenative")
#Aufruf der zweiten Funktion
gefaengnishof_2_wachturm()

