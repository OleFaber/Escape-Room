from itertools import filterfalse

#if übergang == True:
import time

code = {}

def gefängnishof_1():
    print("Du hast in der nächsten Stufe den Gefängnishof erreicht und musst einen Weg finden, in den Wachturm zu gelangen.")
    time.sleep(5)
    print("Als du über den Hof gehst, siehst du mehrere einzelne Stationen.")
    time.sleep(5)
    print("Du kommst auf dem Weg zum Wachturm an einer Treppe, einem Tisch und einer Kiste vorbei.")
    time.sleep(5)
    print("Der Wachturm ist verschlossen und man benötigt einen Schlüssel, um hineinzukommen.")

    schlüssel_gefunden = False
    teilcode_gefunden = False
    teilcode2_gefunden = False
    tür_wachturm = False

    while True:
        print("Du siehst dir nochmals die Umgebung an.")
        kommando = input("Zu welcher Station möchtest du gehen? (Treppe/Kiste/Tisch/Wachturm): ").lower()

        if kommando == "treppe":  # Erster Teil zum entkommen
            if not schlüssel_gefunden:
                print("Glückwunsch! Unter der Treppe liegt ein Schlüssel,den ein Wachmann dort verloren haben musss.")
                time.sleep(2)
                print("Du hebst den Schlüsssel auf")
                schlüssel_gefunden = True
                time.sleep(3)
            else:
                print("Die Treppe wurde bereits untersucht.")
                time.sleep(2)

        elif kommando == "kiste":  # Zweiter Teil (Hinweis 1)
            if not teilcode_gefunden:
                print("In der Kiste ist ein Hinweis mit einem Code: 2357.")
                benutzer_code = input("Bitte notiere den Code, damit du ihn nicht vergisst: ")
                if benutzer_code == "2357":  # Überprüfen, ob der eingegebene Code richtig ist
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
                print("Unter dem Tisch ist ein Hinweis mit einem Code: 7685 den ein Informant für dich dort hinterlassen hat")
                benutzer_code = input("Bitte notiere den Code,damit du ihn nicht vergisst: ")
                if benutzer_code == "7685":  # Überprüfen, ob der eingegebene Code richtig ist
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
            if not tür_wachturm:
                if schlüssel_gefunden and teilcode_gefunden and teilcode2_gefunden:
                    print(
                        "Du hast alle Hinweise in den Stationen sowie den Schlüssel gefunden und kommst somit in die nächste Stufe.")
                    tür_wachturm = True
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


# Aufruf der Funktion
gefängnishof_1()
print("Herzlichen Glückwunsch, du bist in der nächsten Stufe")
print("Hinweis aus der ersten Stufe", code.get("CODE_Teil1"),",", code.get("CODE_Teil2"))
def gefängnishof_2_Wachturm():
    print("Du hast nun den Wachturm erreicht und bist nun vor der letzten Stufe unseres Spiels")
    time.sleep(2)
    print("Du gehst den Wachturm hinauf und überprüfst, ob irgendeine Tür im Treppenhaus  offen ist.\n "
          "Es sind bis oben aber alle Türen verschlossen und dir ist nur eine Abstellkammer des Hausmeisters in der dritten Etage aufgefallen, welcher mit einem digitalen Zahlenschloss versperrt ist.\n"
          "Ganz oben im Wachturm ist dir noch ein Fenster aufgefallen, welches nicht versperrt ist und aus dem Gefängnis führt"
    time.sleep(2)
    print("Du hast alle versperrten Türen versucht mit dem gefundenen Schlüssel aufzuschließen, also ist deine letzte Hoffnung die Abstellkammper ")


anzahl_versuche = 3
while anzahl_versuche > 0
    passwort ==




