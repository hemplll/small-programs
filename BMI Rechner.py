print("Dieses Programm zeigt ihnen ihren BMI Wert!")
gewicht=input("Wie viel wiegen Sie?(in kg):")
körpergröße=input("Wie groß sind Sie?:")
körpergröße=float(körpergröße)
gewicht=float(gewicht)
geschlecht=input("Welches biologische Geschlecht haben sie:")
alter=input("Wie alt sind sie?:")
bmi=gewicht/(körpergröße*körpergröße)
alter=float(alter)
if alter<=24:
    if geschlecht == "Weiblich" or geschlecht=="weiblich":
        if bmi >18.4 and bmi <23.4:
            print("Sie haben Normalgewicht")
        elif bmi >17.7 and bmi <18.3:
            print("Sie sind Untergewichtig")
        elif bmi <17.6:
            print("Sie sind stark Untergewichtig")
        elif bmi >23.5 and  bmi <25.0:
            print("Sie sind Übergewichtig")
        elif bmi >25:
            print("Sie sind stark Übergewichtig")
    else:
        if bmi >19.4 and bmi <24.4:
            print("Sie haben Normalgewicht")
        elif bmi >18.7 and bmi <19.3:
            print("Sie sind Untergewichtig")
        elif bmi <18.6:
            print("Sie sind stark Untergewichtig")
        elif bmi >24.5 and  bmi <26.0:
            print("Sie sind Übergewichtig")
        elif bmi >26:
            print("Sie sind stark Übergewichtig")
elif alter<=34:
    if geschlecht == "Weiblich"or geschlecht=="weiblich":
        if bmi >19.4 and bmi <24.4:
            print("Sie haben Normalgewicht")
        elif bmi >18.7 and bmi <18.3:
            print("Sie sind Untergewichtig")
        elif bmi <18.6:
            print("Sie sind stark Untergewichtig")
        elif bmi >24.5 and  bmi <26.0:
            print("Sie sind Übergewichtig")
        elif bmi >26:
            print("Sie sind stark Übergewichtig")
    else:
        if bmi >20.4 and bmi <25.4:
            print("Sie haben Normalgewicht")
        elif bmi >19.7 and bmi <20.3:
            print("Sie sind Untergewichtig")
        elif bmi <19.6:
            print("Sie sind stark Untergewichtig")
        elif bmi >25.5 and  bmi <27.0:
            print("Sie sind Übergewichtig")
        elif bmi >27:
            print("Sie sind stark Übergewichtig")
else:
    if geschlecht == "Weiblich"or geschlecht=="weiblich":
        if bmi >20.4 and bmi <25.4:
            print("Sie haben Normalgewicht")
        elif bmi >19.7 and bmi <20.3:
            print("Sie sind Untergewichtig")
        elif bmi <19.6:
            print("Sie sind stark Untergewichtig")
        elif bmi >25.5 and  bmi <27.0:
            print("Sie sind Übergewichtig")
        elif bmi >27:
            print("Sie sind stark Übergewichtig")
    else:
        if bmi >21.4 and bmi <26.4:
            print("Sie haben Normalgewicht")
        elif bmi >20.7 and bmi <21.3:
            print("Sie sind Untergewichtig")
        elif bmi <20.6:
            print("Sie sind stark Untergewichtig")
        elif bmi >26.5 and  bmi <28.0:
            print("Sie sind Übergewichtig")
        elif bmi >28:
            print("Sie sind stark Übergewichtig")

