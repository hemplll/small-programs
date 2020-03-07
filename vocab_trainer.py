import random
import s
class Entry:
    def __init__(self, englisch, deutsch):
        self.englisch = englisch
        self.deutsch = deutsch
def eintrag():
    while True:
        deutsch = input("Deutsch: ")
        if deutsch == "fertig":
            return
        englisch = input("Englisch: ")
        if englisch == "fertig":
            return
        eintraege.append(Entry(englisch, deutsch))
def save():
    storage = input("In welchen storage möchtest du die Vokabelliste speichern?\nAntworte mit '1', '2' oder '3'")
    if storage == "1":
        eintraege = str(eintraege)
        name_1 = input("Wie soll dein storage heißen?: ")
        storage_1 = open(name_1 + ".txt", "w+")
        storage_1.write(eintraege)
    elif storage == "2":
        pass
    elif storage == "3":
        pass
    else:
        print("Das ist keine gültige Antwort")

def abfrage():
    streak = 0
    trues = 0
    falses = 0
    def quote(trues, falses):
        if trues == 0:
            return 0
        elif falses == 0:
            return 100
        else:
            quote = trues / (falses + trues) * 100
            quote = round(quote)
            return quote
    print("Möchtest du in englisch->deutsch oder in deutsch->englisch abgefragt werden?\nAntworte mit 'ed' oder 'de'")
    l = input(">").lower()
    if l.startswith("e"):
        while True:
            vocab = random.randint(0,len(eintraege) - 1)
            deutsch = input(eintraege[vocab].englisch + " >").lower()
            if deutsch == "stop":
                return
            if eintraege[vocab].deutsch == deutsch:
                print("Richtig")
                streak = streak + 1
                trues = trues + 1
                print("Deine streak", streak, "\nDeine quote:", quote(trues, falses))
            else:
                print("Das war leider falsch")
                streak = streak - streak
                falses = falses + 1
                print("Deine streak", streak, "\nDeine quote:", quote(trues, falses))
    elif l.startswith("d"):
        while True:
            vocab = random.randint(0,len(eintraege) - 1)
            englisch = input(eintraege[vocab].deutsch + " >").lower()
            if englisch == "stop":
                return
            if eintraege[vocab].englisch == englisch:
                print("Richtig")
                streak = streak + 1
                trues = trues + 1
                print("Deine streak", streak, "\nDeine quote:", quote(trues, falses))
            else:
                print("Das war leider falsch")
                streak = streak - streak
                falses = falses + 1
                print("Deine streak", streak, "\nDeine quote:", quote(trues, falses))
    else:
        print("Das ist keine korrekte Eingabe bitte antworte mit 'ed', 'de' oder 'stop'")
if __name__ == "__main__":
    eintraege = []
    print("Hallo zu VoTrain, mit 'help' kannst du dir alle Befehle anzeigen lassen!")
    while True:
        befehl = input(">")
        if befehl == "abfrage":
            abfrage()
        elif befehl == "eintrag":
            eintrag()
        elif befehl == "quit":
            quit(0)
        elif befehl == "save":
            save()
        elif befehl == "load":
            pass
        elif befehl == "help":
            print("Deine Befehle sind 'abfrage', 'eintrag', 'quit' und 'save'")
        else:
            print("Das war keine korrekte Eingabe."
                  "probier es mal mit: 'abfrage', 'eintrag', 'quit' oder 'save'")
