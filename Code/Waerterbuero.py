import time
import Hof

#if übergang == True:#Abfrage ob der Zellenabschnitt abgeschlossen wurde
zellennummern = {}#Dictionarie für die Zellennummern
def flur():#Funktion für die Informationen aus dem Flur
    print("Du schleichst den Flur in Richtung Wärterbüro entlang und kommst dabei an drei Zellen vorbei!")
    print("Zelle 151")
    time.sleep(7)
    print("Zelle 24")
    time.sleep(4)
    print("Zelle 2")
    print("Um dir die Nummern zu merken, schreibst du sie dir auf den Arm!")
    zellennummern ["zelle_1"] = input("Nummer der ersten Zelle:")
    zellennummern ["zelle_2"] = input("Nummer der zweiten Zelle:")
    zellennummern ["zelle_3"] = input("Nummer der dritten Zelle:")
flur()


def tuer_waerterbuero():
    #Aufgabe für die erste Ziffer
    print("An der Tür ist ein PIN-Pad angebracht. Es wird eine vierstellige PIN benötigt")
    print("____")
    print("Vor ein paar Tagen konntest du die Wärter über eine Änderung des Codes belauschen.\n"
          "Du kannst dich leider nur noch an wenig erinnern.\n"
          "Die erste Stelle des Codes war die Quersumme der ersten Zellennummer.")

    i=5
    while i>=0:
        pin_1 = int(input("1.Zahl:"))
        if pin_1 == 7:
            print(pin_1,"___")
            break
        else:
            print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch",i,"Versuche")
            if i == 0:
                print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                start_cell()
            i-=1
    #Aufgabe für die zweite Ziffer
    print("Für die zweite Ziffer haben die Wachleute irgendwas von Modulo Zelle 1 durch Zelle 3 gefaselt")
    zahl_1 = int(zellennummern.get("zelle_1"))
    zahl_2 = int(zellennummern.get("zelle_3"))
    ergebniss_2 = zahl_1 % zahl_2

    i = 5
    while i >= 0:
        pin_2 = int(input("2.Zahl:"))
        if pin_2 == ergebniss_2:
            print(pin_1, pin_2,"__")
            break
        else:
            print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
            if i == 0:
                print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                # Raum1 wieder aufrufen
    #letzten beiden Ziffern eingeben
    print("Die letzen beiden Ziffern der PIN sind die Ziffern der zweiten Zelle umgekehrt!")
    zahl_3 = int(zellennummern.get("zelle_2"))
    ergebniss_34 = str(zahl_3)[::-1]

    i = 5
    while i >= 0:
        pin_34 = int(input("Dritte und vierte Ziffer:"))
        if pin_34 == ergebniss_34:
            print(pin_1,pin_2,pin_34)
            break
        else:
            print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
            if i == 0:
                print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                # Raum1 wieder aufrufen
    print("Die Tür zum Wächterbüro öffnet sich und du gehst hinein!")
tuer_waerterbuero()

def waerterbuero():
    print("Im Wärterbüro angekommen, schaust du dich um und entdeckst die Steuerung der\n"
    "Überwachungskameras. Diese musst du für deine Flucht unbedingt deaktivieren!\n"
    "Du gehst zum Terminal und siehst, dass du einen USB-Stick zum Entriegeln brauchst.\n"
    "Du schaust dich um und siehst in dem Raum einen Schrank, einen Schreibtisch und einen Stuhl.")

    kommando = input("Was möchtest du dir als erstes Ansehen? Schrank / Schreibtisch / Stuhl").lower()
    gefunden = False
    while gefunden == False:
        if kommando == "stuhl":
            print("Der Stuhl quietscht als du dich drauf setzt.\n"
                  "Du merkst, wie dir etwas in den Rücken sticht.\n"
                  "Du beginnst die Stelle mit einer Schere aufzuschneiden und findest den USB-Stick!")
            gefunden = True

        if kommando == "schrank":
            print("Du öffnest die Schranktüren und es fallen dir lauter Ordner entgegen.\n"
                  "Hier hat wohl seit Jahren keiner mehr aufgeräumt!\n"
                  "Du durchsuchst die Ordner, aber findest leider keinen USB-Stick!")
            gefunden = False

        if kommando == "schreibtisch":
            print("Du gehst zum Schreibtisch und öffnest die Schubladen, leider findest du keinen USB-Stick!")
            gefunden = False

    if gefunden == True:
        print("Mit dem USB-Stick kannst du endlich die Kameras deaktivieren.")

    print("Das Display der Kamerasteuerung blinkt rot auf, als du den USB-Stick einstecks!\n"
          "Die Kameras sind deaktiviert!\n"
          "Nun kannst du dich endlich um die Tür zum Hof kümmern.\n"
          "Du verlässt das Büro und gehst zur Hoftür.\n Um diese zu öffnen benötigst du ")

