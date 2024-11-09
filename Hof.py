from itertools import filterfalse

#if übergang == True:
code{}
def gefängnishof_1()
    print("Du hast in der nächsten Stufe den Gefängnishof erreicht und musst einen Weg finden in den Wachturm zu gelangeben")
    print("Als du über den Hof gehst siehst du mehrere einzelne Stationen")
    print("Du kommst auf dem Weg zum Wachturm an einer Treppe, einer Bank mit Tisch und einer Kiste vorbei, in der Werkzeuge liegen")
    print("Der Wachturm ist verschlossen und man benötigt einen Schlüssel, um hineinzukommen")

    schlüssel_gefunden = False
    teilcode_gefunden = False
    tür_wachturm = False

    while True:
        print("Du siehst dir nochmals die Umgebung an ")
        kommando = input("Zu welcher Station möchstest du gehen?").lower()

        if kommando == "treppe":
            if schlüssel_gefunden = False:
                print("unter der Treppe liegt ein Schlüssel")
                schlüssel_gefunden = True
            else:
                print("Die Treppe wurde bereits untersucht")
        elif kommando == "kiste"
            if teilcode_gefunden = False
                print("in der Kiste ist ein Zettel mit einem Code: 2357")
                code ["Teil1"] = input(int("Bitte gib den Code ein"))
            else:
                print("Die Kiste wurde bereits untersucht")
        elif kommando == "bank"
        else:
            print("unbekannter Befehl. Versuche: bank treppe kiste")



