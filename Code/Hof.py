#if uebergang == True:
import time

code = {}

def gefaengnishof_1():
    print("Du hast in der naechsten Stufe den Gefaengnishof erreicht und musst einen Weg finden, in den Wachturm zu gelangen.")
    time.sleep(5)
    print("Als du ueber den Hof gehst, siehst du mehrere einzelne Stationen.")
    time.sleep(5)
    print("Du kommst auf dem Weg zum Wachturm an einer Treppe, einem Tisch und einer Kiste vorbei.")
    time.sleep(5)
    print("Der Wachturm ist verschlossen und man benoetigt einen Schluessel, um hineinzukommen.")

    schluessel_gefunden = False
    teilcode_gefunden = False
    teilcode2_gefunden = False
    tuer_wachturm = False

    while True:
        print("Du siehst dir nochmals die Umgebung an.")
        kommando = input("Zu welcher Station moechtest du gehen? (Treppe/Kiste/Tisch/Wachturm): ").lower()
        time.sleep(3)

        if kommando == "treppe":  # Erster Teil zum entkommen
            if not schluessel_gefunden:
                print("Glueckwunsch! Unter der Treppe liegt ein Schluessel,den ein Wachmann dort verloren haben musss.")
                time.sleep(2)
                print("Du hebst den Schluesssel auf")
                schluessel_gefunden = True
                time.sleep(3)
            else:
                print("Die Treppe wurde bereits untersucht.")
                time.sleep(2)

        elif kommando == "kiste":  # Zweiter Teil (Hinweis 1)TREPPE
            if not teilcode_gefunden:
                print("In der Kiste ist ein Hinweis mit einem Code: 2357.")
                benutzer_code = input("Bitte notiere den Code, damit du ihn nicht vergisst: ")
                if benutzer_code == "2357":  # ueberpruefen, ob der eingegebene Code richtig ist
                    code["CODE_Teil1"] = benutzer_code
                    teilcode_gefunden = True
                    time.sleep(2)
                else:
                    print("Falscher Code!")
                    time.sleep(2)
            else:
                print("Die Kiste wurde bereits untersucht.")
                time.sleep(3)

        elif kommando == "tisch":  # Dritter Teil (Hinweis 2)
            if not teilcode2_gefunden:
                print("Unter dem Tisch ist ein Hinweis mit einem Code: 7685 den ein Informant fuer dich dort hinterlassen hat")
                benutzer_code = input("Bitte notiere den Code,damit du ihn nicht vergisst: ")
                if benutzer_code == "7685":  # ueberpruefen, ob der eingegebene Code richtig ist
                    code["CODE_Teil2"] = benutzer_code
                    teilcode2_gefunden = True
                    time.sleep(2)
                else:
                    print("Falscher Code!")
                    time.sleep(2)
            else:
                print("Die Bank wurde bereits untersucht.")
                time.sleep(2)

        elif kommando == "wachturm":  # Letzter Teil zum entkommen
            if not tuer_wachturm:
                if schluessel_gefunden and teilcode_gefunden and teilcode2_gefunden:
                    print(
                        "Du hast alle Hinweise in den Stationen sowie den Schluessel gefunden und kommst somit in die naechste Stufe.")
                    #tuer_wachturm = True
                    time.sleep(3)
                    break
                else:
                    print("Du musst erst alle Hinweise in dieser Stufe finden, um in den Wachturm zu gelangen")
                    time.sleep(3)
            else:
                print("Der Wachturm ist bereits betreten worden.")
                time.sleep(2)
        else:
            print("Unbekannter Befehl. Versuche eines der vier Befehle: Treppe, Kiste, Bank, Wachturm.")
            time.sleep(2)
#Aufruf der Funktion
gefaengnishof_1()

print("Herzlichen Glueckwunsch, du bist in der naechsten Stufe")

def gefaengnishof_2_wachturm():
    print("Du hast nun den Wachturm erreicht und bist nun vor der letzten Stufe unseres Spiels")
    time.sleep(2)
    print("Du gehst den Wachturm hinauf und ueberpruefst, ob irgendeine Tuer im Treppenhaus  offen ist.\n"
          "Es sind bis oben aber alle Tueren verschlossen und dir ist nur eine Abstellkammer des Hausmeisters in der dritten Etage aufgefallen, \n"
          "welcher mit einem digitalen Zahlenschloss versperrt ist.\n"
          "Ganz oben im Wachturm ist dir noch ein Fenster aufgefallen, welches nicht versperrt ist und aus dem Gefaengnis fuehrt")
    time.sleep(2)
    print("Du hast ohne Erfolg alle versperrten Tueren versucht mit dem gefundenen Schluessel aufzuschließen, \n"
          "also ist deine letzte Hoffnung die Abstellkammper ")
    time.sleep(2)
    print("Dein Informant, der die Hinweise sorgfaeltig versteckt hat, erklaerte, \n"
          "dass sich das Passwort aus dem einen Hinweis minus dem anderen Hinweis zusammensetzt. Er war sich aber unsicher wie herum")
    print("Hinweis aus der ersten Stufe", code.get("CODE_Teil1"),",", code.get("CODE_Teil2"))

    anzahl_versuche = 3
    while anzahl_versuche > 0:
        passwort = input("Bitte geben Sie das Passwort ein:")
        anzahl_versuche -= 1

        if passwort == "5328":
            print("Die Tuer laesst sich oeffnen")
            break
        else:
            print("Passwort falsch")
            print("Sie haben noch", anzahl_versuche, "versuche")
            if anzahl_versuche == 0:
                print("Das Nummernfeld geht aus und Sie kommen nicht weiter") # hier wieder nach ganz vorne?!
                # oder hier wieder an den anfang dieser Funktion
    #neue etappe im Code
    print("In der Abstellkammer findest du einen weiteren Schlüssel")
    time.sleep(2)
    print("Du testet ein weiteres mal mit diesem Schlüssel die Türen und es lässt sich eine Tür öffnen!")
    time.sleep(2)
    print("Der Raum ist dunkel und du siehst hinten in der Ecke nur einen Umriss von einem Schreibtisch. \n"
          "In der andern Ecke steht eine Truhe und rechts von dir steht eine kleiner Werkzeugkoffer")
    time.sleep(2)
    print("Die Truhe ist wieder mit einem Zahlenschloss versperrt")

    seil_gefunden = False
    code_gefunden = False

    while seil_gefunden == False:
        kommando = input("Was möchtest du dir ansehen? Schreibtisch / Truhe / Werkzeugkoffer:").lower()

        if kommando == "schreibtisch":
            if code_gefunden == False:
                print("Auf dem Schreibtisch liegt nur ein Stift und ein Block")
                time.sleep(2)
                print("In der Schreibtischschublade ist ein kleines Notizbuch, indem auf der ersten Seite ein weiterer Code notiert ist")
                time.sleep(2)
                print("Der Code ist 1234")

                benutzer_code = input("Bitte notiere den Code damit du ihn nicht vergisst:")
                if benutzer_code == "1234":
                    code_gefunden = True
                    code["CODE_Teil3"] = benutzer_code
                    print("richtiger Code!")
                    time.sleep(2)

                else:
                    print("Falscher Code!")
            else:
                print("Der Schreibtisch wurde bereits untersucht")
        elif kommando == "werkzeugkoffer":
            print("Der Werkzeugkoffer ist leer")
        elif kommando == "truhe":
            if seil_gefunden == False:
                if code_gefunden == True:
                    print("Die Truhe ist wie schon erwäht mit einem Zahlenschloss verschlossen")
                    time.sleep(2)
                    print("Villeicht bringt dich der Code, den du gerade notiert hast, weiter", code.get("CODE_Teil3"))
                    while True:
                        try:
                            zahlencode_truhe = int(input("Bitte gib den Code ein"))
                            if zahlencode_truhe == 1234:
                                print("richtiger Code!")
                                time.sleep(2)
                                break
                            else:
                                print("Falscher Code!")

                        except ValueError as e:
                            print("Sie dürfen keinen String eingeben", e)
                    print("In der Truhe liegt ein Seil")
                    seil_gefunden = True

                else:
                    print("Du musst erst einen anderen Hinweis finden")
            else:
                print("Die Truhe wurde bereits geöffnet")
                time.sleep(2)
        else:
            print("Unbekannter Befehl, probiere Schreibtisch / Truhe / Werkzeugkoffer")
    print("Mit dem Seil könntest du versuchen aus dem Fenster im oberen Stockwerk zu klettern")
    time.sleep(2)
    print("oben angekommen öffnest du das Fenster, kletterst runter und flüchtest")

#Aufruf der zweiten Funktion
gefaengnishof_2_wachturm()