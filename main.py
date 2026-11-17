# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



print("======================================")
print("        STUDY COUNTDOWN 📚")
print("======================================")
print("Willkommen bei deinem Lernplaner!")

pruefungen = []
aufgaben = []
erledigt = []
tagesziel = 3

# Hauptmenü
while True:

    print("")
    print("========== HAUPTMENÜ ==========")
    print("1 - Prüfung hinzufügen")
    print("2 - Meine Prüfungen")
    print("3 - Lernaufgabe hinzufügen")
    print("4 - Aufgaben anzeigen / erledigen")
    print("5 - Lernfortschritt")
    print("6 - Tagesziel festlegen")
    print("7 - Mini-Lernquiz")
    print("8 - Motivation")
    print("9 - Beenden")

    auswahl = input("Wähle eine Zahl: ")

    # Prüfung hinzufügen
    if auswahl == "1":
        fach = input("Wie heißt deine Prüfung? ")
        datum = input("Datum (TT.MM.JJJJ): ")

        pruefungen.append([fach, datum])
        print("✅ Prüfung gespeichert!")

    # Prüfungen anzeigen
    elif auswahl == "2":
        print("")
        print("📅 DEINE PRÜFUNGEN")

        if len(pruefungen) == 0:
            print("Du hast noch keine Prüfungen.")

        for p in pruefungen:
            print(p[0], "- am", p[1])

        print("Tipp: Plane frühzeitig deine Lernzeit!")

    # Lernaufgabe hinzufügen
    elif auswahl == "3":
        aufgabe = input("Was musst du lernen? ")

        if aufgabe != "":
            aufgaben.append(aufgabe)
            erledigt.append(False)
            print("✅ Aufgabe hinzugefügt!")

    # Aufgaben erledigen
    elif auswahl == "4":
        print("")
        print("📝 DEINE LERNAUFGABEN")

        if len(aufgaben) == 0:
            print("Noch keine Aufgaben vorhanden.")

        else:
            for i in range(len(aufgaben)):
                if erledigt[i]:
                    print(i + 1, "✅", aufgaben[i])
                else:
                    print(i + 1, "☐", aufgaben[i])

            nummer = input(
                "Welche Aufgabe hast du erledigt? (0 = zurück): "
            )

            if nummer.isdigit():
                nummer = int(nummer)

                if nummer >= 1 and nummer <= len(aufgaben):
                    erledigt[nummer - 1] = True
                    print("🎉 Super gemacht!")

    # Lernfortschritt
    elif auswahl == "5":
        gesamt = len(aufgaben)
        fertig = erledigt.count(True)

        print("")
        print("📊 DEIN LERNFORTSCHRITT")

        if gesamt > 0:
            prozent = round(fertig / gesamt * 100)

            print("Erledigte Aufgaben:", fertig, "von", gesamt)
            print("Fortschritt:", prozent, "%")

            balken = "🟩" * (prozent // 10)
            leer = "⬜" * (10 - prozent // 10)

            print(balken + leer)

            if prozent == 100:
                print("🏆 Alles geschafft!")
            elif prozent >= 50:
                print("💪 Mehr als die Hälfte geschafft!")
            else:
                print("🌱 Weiter so!")

        else:
            print("Du hast noch keine Lernaufgaben.")

    # Tagesziel
    elif auswahl == "6":
        print("")
        print("🎯 DEIN TAGESZIEL")

        ziel = input("Wie viele Aufgaben möchtest du schaffen? ")

        if ziel.isdigit() and int(ziel) > 0:
            tagesziel = int(ziel)
            print("Dein Tagesziel:", tagesziel, "Aufgaben")

        fertig = erledigt.count(True)

        if fertig >= tagesziel:
            print("🏆 Dein Ziel ist erreicht!")
        else:
            print("Noch", tagesziel - fertig, "Aufgaben bis zum Ziel!")

    # Mini-Quiz
    elif auswahl == "7":
        punkte = 0

        print("")
        print("🧠 MINI-LERNQUIZ")

        antwort = input("Wie viel ist 8 x 7? ")
        if antwort == "56":
            punkte += 1
            print("Richtig! ✅")
        else:
            print("Leider falsch! Richtig ist 56.")

        antwort = input("Wie viele Minuten hat eine Stunde? ")
        if antwort == "60":
            punkte += 1
            print("Richtig! ✅")
        else:
            print("Leider falsch! Richtig ist 60.")

        antwort = input("Wie heißt die Hauptstadt von Frankreich? ")
        if antwort.lower() == "paris":
            punkte += 1
            print("Richtig! ✅")
        else:
            print("Leider falsch! Richtig ist Paris.")

        print("")
        print("Du hast", punkte, "von 3 Punkten erreicht!")

        if punkte == 3:
            print("🏆 Perfekt!")
        elif punkte == 2:
            print("💪 Sehr gut!")
        else:
            print("🌱 Übung macht den Meister!")

    # Motivation
    elif auswahl == "8":
        print("")
        print("💡 MOTIVATION")
        print("Du schaffst das!")
        print("Mache regelmäßig Pausen.")
        print("Lerne jeden Tag ein bisschen.")
        print("Glaube an dich! 🍀")

    # Beenden
    elif auswahl == "9":
        print("Viel Erfolg bei deinen Prüfungen! 📚")
        break

    else:
        print("Bitte gib eine Zahl zwischen 1 und 9 ein.")
