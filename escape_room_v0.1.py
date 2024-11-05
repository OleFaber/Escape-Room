password = 'Code'

# ANSI-Farb-Code für Grün
GREEN = "\033[92m"
RESET = "\033[0m"

# Textausgabe mit grün hervorgehobenen Buchstaben für das Lösungswort
print("Du öffnest langsam die Augen und findest dich in einem düsteren Raum wieder.")
print("Eine digitale Uhr an der Wand zeigt, dass du nur 30 Minuten Zeit hast, um hier rauszukommen.")
print(f"Neben dir liegt ein zerknitterter Zettel, auf dem nur ein einziges Wort zu lesen ist: {GREEN}C{RESET}haos.")
print("Im Raum siehst du ein seltsames Schloss mit vier Buchstaben und einige mysteriöse Hinweise an den Wänden.")
print(f"Es scheint, als bräuchtest du einen {GREEN}O{RESET}pen-Code, um das Schloss zu öffnen.")
print(f"Dein Herz schlägt schneller, als du eine Nachricht auf dem Bildschirm liest: „Nur derjenige, der den richtigen Co{GREEN}D{RESET}e entschlüsseln kann, wird entkommen.“")
print(f"Du machst dich auf die Suche nach weiteren Hinweisen im Raum, aber ein Gefühl sagt dir, dass du das richtige {GREEN}E{RESET}lement bereits in den Händen hältst.")


i = 0
while i <= 3:
    text1 = input("Gebe das Password ein: ")
    if i == 2:
        print('Wollen Sie einen Tipp?')
        if input('Ja/Nein: ') == 'Ja':
            # Hinweis zur Entschlüsselung des Lösungsworts
            print("\nHinweis: Die grün hervorgehobenen Buchstaben ergeben das Lösungswort. Kannst du es entschlüsseln?")
    if text1 == password:
        print('Glückwunsch, Sie sind nun im nächsten Raum!')
        i = 4
    else:
        print('Das Passwort ist falsch!')
        i = i + 1

