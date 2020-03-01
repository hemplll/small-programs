import random
import asyncio

class Game:
    def __init__(self):
        self.commands = """Das sind die aktuellen commands: inventar; help; info_'jeweilige Waffe'"""
        self.body_characteristics = ["Sofasportler  ", "Alibi-Fittnessstudiomitgliedschaft-Besitzer", "morgens-Joggengeher                           ","Sportler                                       ", "Triathlet                                         " ]
        self.weapon_characteristics = [ "Dolch", "Machete", "stumpfe Axt", "alte Klinge  ", "stumpfes Ritterschwert", "scharfes Ritterschwert  ", "Platin-Langschwert        "]
        self.armor_characteristics = ["alte Kutte", "leichtes Kettenhemd", "verstärktes Kettenhemd", "leichter Harnisch       ", "verstärkter Harnisch       ", "rostige Komplettrüstung     ", "verstärkte Komplettrüstung     ", "Platin-Komplettrüstung          "]
        self.punkte = 0
        self.player_lives = 3
        self.boss_lives = 4


    def ready_fünf_punkte_check(self):
        if self.punkte < 5:
            return False
        else:
            return True
    def fight_info(self):
        print("Mit wem möchtest du kämpfen?")
        print("Links siehst du ein", self.enemy, "mit den Eigenschaften:")
        print(self.print_enemy_links_characteristics())
        print("\nGeradevoraus siehst du ein", self.enemy, "mit den Eigenschaften:")
        print(self.print_enemy_geradevoraus_characteristics())
        print("\nRechts siehst du ein", self.enemy, "mit den Eigenschaften:")
        print(self.print_enemy_rechts_characteristics())
        print("\n'help' für die aktuellen commands")

    def stats(self):
        print("Hier sind deine stats:")
        print(self.print_player_characteristics())
        print("Punkte:", self.punkte)
        print("Leben:", self.player_lives)

    def set_orientation(self):
        print("Möchtest du auf Seiten der Allianz oder der Horde Kämpfen?")
        while True:
            self.setting = input(">").lower()
            if self.setting.startswith("a"):
                self.orientation = "Allianz"
                print("""Du möchtest dich der Allianz anschließen, mmh... Zu feige für die Horde oder ein loyaler 
                und treu ergebener Diener seines Landes.""")
                self.enemy = "Ork"
                self.enemy = str(self.enemy)
                self.enemy_boss = "Sauron Anführer der Horde"
                break
            elif self.setting.startswith("h"):
                self.orientation = "Horde"
                print("""Du hast also entschlossen dich der Horde anzuschließen, den aus der Zivilisation verbannten
                 und von allen, außer ihnen selbst gehassten? Du hast echt Mut, ohne jeden Zweifel ...""")
                self.enemy = "Soldat"
                self.enemy = str(self.enemy)
                self.enemy_boss = "König Ludwig der XIV."
                break
            else:
                print("Bitte antworte mit 'Horde' oder 'Allianz'")
    def set_player_characteristics(self):
        self.player_body_characteristics = random.choice(self.body_characteristics)
        self.player_weopon_characteristics = random.choice(self.weapon_characteristics)
        self.player_armor_characteristics = random.choice(self.armor_characteristics)

    def set_enemy_links_characteristics(self):
        self.enemy_links_body_characteristics = random.choice(self.body_characteristics)
        self.enemy_links_weopon_characteristics = random.choice(self.weapon_characteristics)
        self.enemy_links_armor_characteristics = random.choice(self.armor_characteristics)
    def set_enemy_rechts_characteristics(self):
        self.enemy_rechts_body_characteristics = random.choice(self.body_characteristics)
        self.enemy_rechts_weopon_characteristics = random.choice(self.weapon_characteristics)
        self.enemy_rechts_armor_characteristics = random.choice(self.armor_characteristics)
    def set_enemy_geradevoraus_characteristics(self):
        self.enemy_geradevoraus_body_characteristics = random.choice(self.body_characteristics)
        self.enemy_geradevoraus_weopon_characteristics = random.choice(self.weapon_characteristics)
        self.enemy_geradevoraus_armor_characteristics = random.choice(self.armor_characteristics)

    def print_enemy_rechts_characteristics(self):
        print("Körperbau:", self.enemy_rechts_body_characteristics, "\nWaffe:", self.enemy_rechts_weopon_characteristics, "\nRüstung:", self.enemy_rechts_armor_characteristics)

    def print_enemy_links_characteristics(self):
        print("Körperbau:", self.enemy_links_body_characteristics, "\nWaffe:",
              self.enemy_links_weopon_characteristics, "\nRüstung:", self.enemy_links_armor_characteristics)
    def print_enemy_geradevoraus_characteristics(self):
        print("Körperbau:", self.enemy_geradevoraus_body_characteristics, "\nWaffe:", self.enemy_geradevoraus_weopon_characteristics, "\nRüstung:", self.enemy_geradevoraus_armor_characteristics)

    def print_player_characteristics(self):
        print("Körperbau:", self.player_body_characteristics, "\nWaffe:", self.player_weopon_characteristics, "\nRüstung:", self.player_armor_characteristics)
    def set_name(self):
        print("So viel dazu, nun müssen wir erstmal einen passenden Namen finden.")
        self.player_name = input(">")
    def introduction(self):
        print("""Hallo ... wie auch immer du heißt. Du bist hier in einem auf strategischen Kämpfen basierenden Universum gefangen.
         Um zu entfliehen und in dein langweiliges Leben zurückzukehren musst du an den Universe-Traveller kommen. Dieser 
         befindet sich in dem Tresor von Hyanes - Hyanes ist die Hauptstadt dieses Universums. In dieser Stadt tobt jedoch
         gerade eine gewaltige Schlacht zwischen der Horde und der Allianz und um an den besagten Tresor zu kommen musst
         du dich einer Seite anschließen und für sie die Schlacht gewinnen. Wenn du dominant und überlegen kämpfst wirst 
         du ihnen auffallen und sie werden dich zu ihrem König machen. So bekommst du Zugriff zu ihrem Tresor und kannst
         Nachhause.""")
    def beginning(self):
        print("""Also um die Schlacht für uns zu entscheiden musst du den gegnerischen Anführer besiegen, 
        um den aber erst zu finden musst du 10 Punkte erreichen. Außerdem hast du nur 3 Leben.
        Du kannst immer 'help' in die Konsole eingeben um dir alle Befehle anzeigen zu lassen.""")
        print("""Insgesamt gibt es bei einfachen Kämpfen immer drei Kategorien und wenn du in der mehrzahl besser bist 
        als dein Gegner, solltest du den Kampf ohne Probleme für dich entscheiden. Um deine Eigenschaften, Punkte und
         verbleibenen Leben zu sehen gebe einfach 'stats' ein, mit 'weiter' gehts LOS!!! :)""")
        while True:
            self.user_input_1 = input(">").lower()
            if self.user_input_1 == "stats":
                print(self.stats())
            elif self.user_input_1 == "help":
                print(self.commands)
            elif self.user_input_1 == "weiter":
                break
            else:
                print("Das ist kein gültiger command.('help' für hilfe)")
    def fight(self):
        while not self.ready_fünf_punkte_check():
            if self.player_lives == 0:
                print("Du hast keine Leben mehr:(\nGAME_OVER")
                exit(0)
            self.player_fight_stats = 0
            self.player_fight_stats = int(self.player_fight_stats)
            self.commands = """Das sind die aktuellen commands:
                'Links', 'Rechts' oder 'Geradevoraus' um den Gegner zu wählen;
                'stats' für deine Fähigkeiten und Punkte"""
            self.set_enemy_links_characteristics()
            self.set_enemy_rechts_characteristics()
            self.set_enemy_geradevoraus_characteristics()
            self.fight_info()
            while True:
                self.enemy_choice = input(">").lower()
                if self.enemy_choice == "help":
                    print(self.commands)
                elif self.enemy_choice == "links":
                    if len(self.enemy_links_body_characteristics) <= len(self.player_body_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if len(self.enemy_links_weopon_characteristics) <= len(self.player_weopon_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if len(self.enemy_links_armor_characteristics) <= len(self.player_armor_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if self.player_fight_stats > 1:
                        print("Du hast gewonnen!")
                        self.punkte = self.punkte + 1
                        break
                    else:
                        print("Du hast leider verloren :(\n"
                              "und bekommst ein Leben abgezogen")
                        self.player_lives = self.player_lives - 1
                        break
                elif self.enemy_choice == "stats":
                    self.stats()
                elif self.enemy_choice == "geradevoraus":
                    if len(self.enemy_geradevoraus_body_characteristics) <= len(self.player_body_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if len(self.enemy_geradevoraus_weopon_characteristics) <= len(self.player_weopon_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if len(self.enemy_geradevoraus_armor_characteristics) <= len(self.player_armor_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if self.player_fight_stats > 1:
                        print("Du hast gewonnen!")
                        self.punkte = self.punkte + 1
                        break
                    else:
                        print("Du hast leider verloren :(\n"
                              "und bommst ein Leben abgezogen")
                        self.player_lives = self.player_lives - 1
                        break
                elif self.enemy_choice == "rechts":
                    if len(self.enemy_rechts_body_characteristics) <= len(self.player_body_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if len(self.enemy_rechts_weopon_characteristics) <= len(self.player_weopon_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if len(self.enemy_rechts_armor_characteristics) <= len(self.player_armor_characteristics):
                        self.player_fight_stats = self.player_fight_stats + 1
                    if self.player_fight_stats > 1:
                        print("Du hast gewonnen!")
                        self.punkte = self.punkte + 1
                        break
                    else:
                        print("Du hast leider verloren :(\n"
                              "und bommst ein Leben abgezogen")
                        self.player_lives = self.player_lives - 1
                        break
                else:
                    print("Das ist kein gültiger command, 'help' für Hilfe")
    def boss_fight(self):
        self.commands = """Die aktuellen commands sind:'ja' oder 'nein' und 'stats'"""
        print("Bei drei Treffern hast du den Anführer besiegt, aber pass auf der Anführer ist so stark das du dir \nkeinen Patzer leisten kannst!")
        print(self.enemy_boss, "Sieh eine an, du möchtest gegen mich antreten?")
        #Frage 1
        print("""1. Du siehst, dass der gegnerische Anführer eine Rüstung trägt, die als sie neu war, eine Stärke von 25 hatte.
        Aber du schätzt, dass sie schon mindestens 10 Monde im Einsatz ist und dass die stärke einer Waffe je nach Benutzung
        pro Mond 5% von ihrer ursprünglichen Stärke verliert. Außerdem weißt du, dass deine Waffe eine
         Stärke ursprüngliche Stärke von 20 hat und auf dem Schaft erst ein halbes Dutzend Mondesstriche sind.
        Lohnt sich deiner Meinung nach ein Angriff auf seine Rüstung?
        'help' für die aktuellen commands!""")
        while True:
            self.user_choice = input(">").lower()
            if self.user_choice == "ja":
                print("""Du holst zum Schlag aus und durchbrichst seine Rüstung, er kommt ins Taumeln und du kannst deinen
                      ersten Treffer landen.""")
                break
            elif self.user_choice == "nein":
                print("""Du entscheidest dich für einen Angriff auf seine Beine doch er sieht es kommen und erwischt dich :(
                    GAME_OVER""")
                exit(0)
            elif self.user_choice == "help":
                print(self.commands)
            elif self.user_choice == "stats":
                print("Die leben vom Anführer:", self.boss_lives)
            else:
                print("Das ist kein gültiger command, 'help' für Hilfe")
        print("""Als nächstes fällt dir ein Riss in der Mitte seines Kettenhemdes, welcher ungefähr 4 cm breit ist, auf.
        Und du musst überlegen ob dein Schwert dünn genug ist um durch ihn hindurch zu kommen. Die spitze deines Schwertes
        hat einen Winkel von 30 Grad und das Schwert verläuft gleichschenklich. Du errechnest dir, dass du aufgrund der vielen
        Lagen der Kleidung mindestens 10 cm eindringen musst. Lohnt sich deiner Meinung nach ein Angriff auf den Riss?
        'help' für die aktuellen commands!""")
        while True:
            self.user_choice = input(">").lower()
            if self.user_choice == "ja":
                print("""Du stichst zu, doch dein Schwert dringt nicht tief genug ein und im gegenzug bekommst du einen 
                Hieb von seiner Keule ab :(
                GAME_OVER""")
                exit(0)
            elif self.user_choice == "nein":
                print("""Du entscheidest dich für eine Antäuschung auf sein Kettenhemd, doch in Wahrheit weichst du aus
                 und erwischst seinen Kopf mit einem geziehlten Tritt.""")
                break
            elif self.user_choice == "help":
                print(self.commands)
            elif self.user_choice == "stats":
                print("Die leben vom Anführer:", self.boss_lives)
            else:
                print("Das ist kein gültiger command, 'help' für Hilfe")
        print("""Nach dem du zwei Angriffe gekonnt abgewehrt hast fällt dir auf, dass er eine Geschwindigkeit von 4,5 
            Schlägen pro Sekunde und eine Kondition von 10 haben muss. Du schätzt deine Ausdauer auf 17 - das ist die 
            Geschwindigkeit mal die Kondition durch drei. Lohnt es sich deiner Meinung nach auf Ausdauer zu spielen?
            'help' für die aktuellen commands!""")
        while True:
            self.user_choice = input(">").lower()
            if self.user_choice == "ja":
                print("""Nach ca. 5 Minuten wildem umhergetanze, ohne viel action wird er langsamer und du kannst ihn 
                besiegen""")
                break
            elif self.user_choice == "nein":
                print("""Du probierst es schnell zu beenden doch er haut dich mit seiner Keule um :(""")
            elif self.user_choice == "help":
                print(self.commands)
            elif self.user_choice == "stats":
                print("Die leben vom Anführer:", self.boss_lives)
            else:
                print("Das ist kein gültiger command, 'help' für Hilfe")
        print("Du hast gewonnen und kannst nun Nachhause zurückkehren :)")








if __name__ == "__main__":
    game = Game()
    game.introduction()
    game.set_orientation()
    game.set_name()
    game.set_player_characteristics()
    game.beginning()
    game.fight()
    game.boss_fight()