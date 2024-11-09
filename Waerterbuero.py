import time

#import Zelle
#def start_cell():
    #Zelle.run()

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

    i=2
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

    i = 2
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

    i = 2
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

def waechterbuero():
    print("Im Wächterbüro angekommen, schaust du dich um und entdeckst die Steuerung der\n"
    "Überwachungskameras. Diese musst du für deine Flucht unbedingt deaktivieren!\n"
    "Du gehst zum Terminal und siehst, dass du einen USB-Stick zum Entriegeln brauchst.\n"
    "Du schaust dich um und siehst in dem Raum einen Schrank, einen Schreibtisch und einen Stuhl.")
    kommando = input("Was möchtest du dir als erstes Ansehen? Schrank / Schreibtisch / Stuhl")

    if kommando == "Stuhl":
        print("Der Stuhl quietscht als du dich drauf setzt und du merkst einen Gegenstand\n"
              "in der Rückenlehne.Du nimmst dir eine Schere und schneidest die Rückenlehne auf")
