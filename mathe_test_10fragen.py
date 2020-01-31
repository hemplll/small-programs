def question1():
    while True:
        answer = input("Was ergibt 2+2*2?\nIst die Antwort a=4; b=6 oder c=8?:")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "b":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "b.", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question2():
    while True:
        answer = input(
            "Was war nochmal der Satz des Pythagoras,(nicht Python)\n'a=a²+b²=c²'; 'b=a²+b²*c²' oder 'c=a²-b²-c²?'")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "a":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "a.", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question3():
    while True:
        answer = input(
            "Bei einer Exponentialfunktion ist der Paramenter b der ...\na=Wachstumsfaktor b=Multiplikationsfaktor c=Streckungsfaktor")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "a":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre","a.""\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question4():
    while True:
        answer = input("Was ergibt 7*7\na=42; b=49 oder c=feinen Sand")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "b" or answer == "c":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "b oder c.", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question5():
    while True:
        answer = input("Pi´s erste Zahlen sind...\na=3.14159; b=3.14156 oder c=3.14258")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "a":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "a", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")

def question6():
    while True:
        answer = input("Heißt es ...\na=Strich vor Punkt; b=Multiplikation vor Division oder c=Punkt vor Strich")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "c":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "c", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question7():
    while True:
        answer = input("Wie lautet die Formel für den Flächeninhalt eines Rechteckes?\na=a+b+c; b=a+b oder c=a*b")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "c":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "c", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question8():
    while True:
        answer = input(
            "Jonas bekommt jeden Monat 10€ von seiner Mutter \nund 15€ von seinem Vater, wie viel Taschengeld bekommt er in einem Jahr insgesamt?\n a=300€; b=340€ oder c=290€")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "a":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "a", "\n")
                return 0
            break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question9():
    while True:
        answer = input(
            "Wenn Jonas sich einen Computer für 600€ kaufen möchte,\nwie lange muss er dann insgesamt sparen?\na=2,5 Jahre; b=1,9 Jahre oder c=2 Jahre")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "c":
                print("Das war richtig! Gut gemacht!\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "c", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


def question10():
    while True:
        answer = input(
            "Wenn ich in diesem Test 200 Punkte zu vergeben hätte, wie viele Punkte hätte dann eine Frage?\n a=10; b=20 oder c=15\n")
        if answer == "a" or answer == "b" or answer == "c":
            if answer == "b":
                print("Das war richtig! Gut gemacht!", "\n")
                return 1
                break
            else:
                print("Das war leider falsch :(\nDie richtige Antwort wäre", "b", "\n")
                return 0
                break
        else:
            print("Das ist keine korrekte Antwort! Antworte bitte mit a, b oder c.")


if __name__ == "__main__":
    print("Hallo! Hast du lust auf ein Mathe Quiz?\nNatürlich was frage ich auch...")
    print("Antworte mit a; b oder c", "\n")
    p1 = question1()
    p2 = question2()
    p3 = question3()
    p4 = question4()
    p5 = question5()
    p6 = question6()
    p7 = question7()
    p8 = question8()
    p9 = question9()
    p10 = question10()
    points = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    if points < 1:
        print(points, "Punkte... Was soll man da noch sagen? Außer Amateur!")
    elif points < 2:
        print(points, "Punkte... Was soll man da noch sagen? Außer Amateur!")
    elif points < 4:
        print(points, "Punkte... Was soll man da noch sagen? Außer Amateur!")
    elif points < 9:
        print("Du bist mit", points,
              "Punkten zwar schon Fortgeschritten, aber hast auch\nnoch Raum für Verbesserungen.")
    else:
        print(points, "Punkte, dass ist schon beachtlich du Profi!")
