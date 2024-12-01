import time
zellennummern = {}  #Dictionarie für die Zellennummern erstellt
def flur(): #Funktion für die Informationen aus dem Flur
    print("Du schleichst den Flur in Richtung Wärterbüro entlang und kommst dabei an drei Zellen vorbei!")
    print("Zelle 151")
    time.sleep(7)
    print("Zelle 24")
    time.sleep(4)
    print("Zelle 2")
    print("Um dir die Nummern zu merken, schreibst du sie dir auf den Arm!")
    zellennummern ["zelle_1"] = input("Nummer der ersten Zelle:")   #Eingabe wird im Dictionary gespeichert
    zellennummern ["zelle_2"] = input("Nummer der zweiten Zelle:")  #Eingabe wird im Dictionary gespeichert
    zellennummern ["zelle_3"] = input("Nummer der dritten Zelle:")  #Eingabe wird im Dictionary gespeichert
flur()  #Starten der Flur-Funktion
def tuer_waerterbuero():
    print("An der Tür ist ein PIN-Pad angebracht. Es wird eine vierstellige PIN benötigt")
    print("____")
    print("Vor ein paar Tagen konntest du die Wärter über eine Änderung des Codes belauschen.\n"
          "Du kannst dich leider nur noch an wenig erinnern.\n"
          "Die erste Stelle des Codes war die Quersumme der ersten Zellennummer.")
    i=5
    while i>=0: #While-Schleife für die Eingabe und Verarbeitung der ersten Ziffer des Pin-Codes
        while True: #Ausnahmebehandlung für den Value Error
            try:
                pin_1 = int(input("1.Zahl:"))   # Eingabe der ersten Zahl des Pin-Codes
                break
            except ValueError:
                print("Bitte gib eine Ganzzahl ein!")
        if pin_1 == 7:  #Vergleich der eingegebenen Zahl und der Lösung
            print(pin_1,"___")  #Ausgabe des Zahlenfeldes
            break
        else:   #Wenn die Zahl falsch ist wird der folgende Codeblock abgearbeitet
            print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch",i,"Versuche")
            if i == 0:
                print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                flur() #Rückschritt in erste Funktion
            i-=1
    print("Für die zweite Ziffer haben die Wachleute irgendwas von Modulo Zelle 1 durch Zelle 3 gefaselt")#Aufgabe für die zweite Ziffer
    zahl_1 = int(zellennummern.get("zelle_1"))  #Variable erstellen und Zahl aus Dictionary holen
    zahl_2 = int(zellennummern.get("zelle_3"))  #Variable erstellen und Zahl aus Dictionary holen
    ergebniss_2 = zahl_1 % zahl_2               #Berechnung mit den beiden Zahlen durchführen und in der Variable speichern
    j = 5
    while j >= 0:   #Schleife zur Eingabe und Verarbeitung der zweiten Ziffer des Pin-Codes
        while True: #Ausnahmebehandlung für den Value Error
            try:
                pin_2 = int(input("2.Zahl:"))   #Eingabe der zweiten Ziffer des Pin-Codes
                break
            except ValueError:
                print("Bitte gib eine Ganzzahl ein!")
        if pin_2 == ergebniss_2:    #Vergleich der beiden Variablen ob die Zahlen übereinstimmen
            print(pin_1, pin_2,"__")
            break
        else:
            print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
            if j == 0:
                print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                flur()  #Rückschritt in erste Funktion
            j -= 1
    print("Die letzen beiden Ziffern der PIN sind die Ziffern der zweiten Zelle umgekehrt!")
    zahl_3 = int(zellennummern.get("zelle_2"))  #Zahlenwert aus dem Dictionary holen
    ergebniss_34 = str(zahl_3)[::-1]    #Zahlenwert umdrehen und in der variable speichern
    ergebniss_34 = int(ergebniss_34)    #Str in Int umwandeln um damit weiterarbeiten zu können
    k = 5
    while k >= 0:   #Schleife zur Eingabe und Verarbeitung der dritten und vierten Ziffer des Pin-Codes
        while True: #Ausnahmebehandlung für den Value Error
            try:
                pin_34 = int(input("Dritte und vierte Ziffer:"))    #Eingabe der letzen beiden Ziffern des Pin-Codes
                break
            except ValueError:
                print("Bitte gib eine Ganzzahl ein!")
        if pin_34 == ergebniss_34:  #Vergleich von Eingabe und Ergebnis
            print(pin_1,pin_2,pin_34)
            break
        else:
            print("Das Zahlenfeld blinkt rot auf! Pass auf du hast noch", i, "Versuche")
            if k == 0:
                print("Der Wächter hat sie bemerkt und bringt sie zurück in Ihre Zelle!")
                flur()  #Rückschritt in erste Funktion
            k -= 1
    print("Die Tür zum Wächterbüro öffnet sich und du gehst hinein!")
tuer_waerterbuero() #Starten der Wärterbürotür-Funktion
def waerterbuero(): #Erstellen des nächsten Raumes über eine Funktion
    print("Im Wärterbüro angekommen, schaust du dich um und entdeckst die Steuerung der\n"
    "Überwachungskameras. Diese musst du für deine Flucht unbedingt deaktivieren!\n"
    "Du gehst zum Terminal und siehst, dass du einen USB-Stick zum Entriegeln brauchst.\n"
    "Du schaust dich um und siehst in dem Raum einen Schrank, einen Schreibtisch, eine kleine Schachtel und einen Stuhl.")
    found = False
    schere = False  # Variable auf False gesetzt, Schere noch nicht gefunden
    while found == False:    #While-Schleife für die Auswahl von Orten zum suchen
        kommando = input("Was möchtest du dir als erstes Ansehen? Schrank / Schreibtisch / Stuhl / Schachtel").lower()  #Variable in denen die Auswahl gespeicchert wird
        if kommando == "stuhl" and schere == True: #Stuhl ausgewählt
            print("Der Stuhl quietscht als du dich drauf setzt.\n"
                  "Du merkst, wie dir etwas in den Rücken sticht.\n"
                  "Du beginnst die Stelle mit deiner Schere aufzuschneiden und findest den USB-Stick!")
            found = True
            break
        if kommando == "stuhl" and schere == False: #Stuhl ausgewählt und Schere gefunden
            print("Du siehst in dem Stuhl einen USB-Stick-förmigen Abdruck.\n"
                  "Hättest du nur eine Schere um den Stuhl aufzuschneiden")
        if kommando == "schrank":   #Schrank ausgewählt
            print("Du öffnest die Schranktüren und es fallen dir lauter Ordner entgegen.\n"
                  "Hier hat wohl seit Jahren keiner mehr aufgeräumt!\n"
                  "Du durchsuchst die Ordner, aber findest leider keinen USB-Stick!")
            found = False
        if kommando == "schreibtisch":  #Schreitisch ausgewählt
            print("Du gehst zum Schreibtisch und öffnest die Schubladen, leider findest du keinen USB-Stick!")
            found = False
        if kommando == "schachtel": #Schachtel ausgewählt
            print("Du hebst die Schachtel auf und versuchst sie zu öffnen. Der Verschluss klemmt. \n"
                  "Mit ein bisschen Kraft lässt sich die Schachtel dennoch öffnen und du findest eine Schere!")
            schere = True #Variable Schere wird auf True gesetzt
        if kommando != "schrank" and kommando != "schreibtisch" and kommando != "stuhl" and kommando != "schachtel":    #Ausnahmebehandlung von falscher Eingabe
            print("Bitte gib einen der angegebenen Gegenstände ein!")
    if found == True:    #USB-Stick wurde gefunden und das Programm läuft weiter
        print("Mit dem USB-Stick kannst du endlich die Kameras deaktivieren.")
        time.sleep(1)
        print("Das Display der Kamerasteuerung blinkt rot auf, als du den USB-Stick einsteckst!\n"
              "Die Kameras sind deaktiviert!\n"
              "Nun kannst du dich endlich um die Tür zum Hof kümmern.\n"
              "Du verlässt das Büro und gehst Richtung Hoftür.")
waerterbuero()  #Starten der Wärterbüro-Funktion
def flur_2():   #Erstellen der Funktion flur_2
    print("Auf dem Weg zur Hoftür musst du durch eine weitere Tür.\n"
          "Während du zu der Tür läufst, gehst du an drei Spinden vorbei.\n"
          "An der Tür angekommen, siehts du, dass die Tür durch eine Nutmutter verschlossen ist.\n"
          "Um diese zu lösen benötigst du ein passendes Werkzeug!")
    while True: #While-Schleife für die Auswahlmöglichkeiten der Schränke
        wahl = input("Welchen Schrank möchtest du durchsuchen? 1, 2 oder 3?")   #Erstellen der Variable für die Auswahl
        if wahl == "1": #Anwahl 1 wird verarbeitet
            print("Du öffnest den Schrank 1 und findest die Gefängniskleidung!")
        if wahl == "2": #Anwahl 2 wird verarbeitet
            print("Du öffnest den Schrank 2 und findest Geschirr für die Kantine")
        if wahl == "3": #Anwahl 3 wird verarbeitet
            print("Du öffnest den Schrank 3 und findest drei Werkzeuge!\n"
                  "einen Maulschlüssel, einen Hakenschlüssel und einen Schraubendreher!")
            break #Schleife wird abgebrochen
    print("Wieder an der Tür angekommen, musst du dich entscheiden welches Werkzeug du verwenden möchtest!")
    while True:
        auswahl = input("Welches Werkzeug möchtest du ausprobieren? Maulschlüssel / Hakenschlüssel / Schraubendreher").lower()
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
    while True: #While Schleife zum Auswerten der Eingabe des Spielers
        farbe_1 = input("Welche Farbe ergibt diese Kombination?").lower()  #Eingabe der Lösung des Spielers
        if farbe_1 == "orange":
            print("Das war richtig!")
            break
        else:
            print("Falsch! Bitte probier es erneut! Achte auch auf die Rechtschreibung!")
    print("Das Display leuchtet BLAU auf!")
    time.sleep(2)
    print("Das Display leuchtet GELB auf!")
    time.sleep(2)
    while True: #While Schleife zum Auswerten der Eingabe des Spielers
        farbe_2 = input("Welche Farbe ergibt die Kombination?").lower() #Eingabe der Lösung des Spielers
        if farbe_2 == "grün":
            print("Das war richtig!")
            break
        else:
            print("Falsch! Bitte probier es erneut! Achte auch auf die Rechtschreibung!")
    print("Das Display leuchtet LILA auf!")
    time.sleep(2)
    farbe_3 = input("Was ist die Komplementärfarbe von Lila?").lower()   #Eingabe der Lösung des Spielers
    while True: #While Schleife zum Auswerten der Eingabe des Spielers
        if farbe_3 == "gelb":
            print("Das war richtig!")
            break
        else:
            print("Falsch! Bitte probier es erneut! Kleiner Tipp: Die Farbe der Sonnenblume!")
    print("Das Display leuchtet MAGENTA auf!")
    time.sleep(2)
    while True: #While Schleife zum Auswerten der Eingabe des Spielers
        antwort = input("Welches Unternehmen verbindest du mit der Farbe?").lower() #Eingabe der Lösung des Spielers
        if antwort == "telekom":    #Vergleich von Antwort mit Lösung
            print("Das war richtig!")
            break
        else:
            print("Falsch! Bitte probier es erneut! Kleiner Tipp: Sie kümmern sich um Internet!")
    print("Das Display leuchtet WEIß auf!")
    while True: #While Schleife zum Auswerten der Eingabe des Spielers
        antwort = input("Welchen Kontinent verbindest du mit der Farbe?").lower() #Eingabe der Lösung des Spielers
        if antwort == "antarktis":    #Vergleich von Antwort mit Lösung
            print("Das war richtig!")
            break
        else:
            print("Falsch! Bitte probier es erneut! Kleiner Tipp: Dort leben Pinguine!")
    print("Das Display leuchtet GRÜN auf und die Hoftür entriegelt sich!")
hoftuer()   #Starten der Hoftür-Funktion

