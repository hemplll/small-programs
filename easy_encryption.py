class Encryption:
    def __init__(self):
        self.alph = ['#', 'f', 'T', '$', 'X', '6', 'v', 'W', 'J', '1', '=', 'm', '+', 'M', '*', 'D', '/', 's', 'K', 'd', '{', '!', '<', '8', 'R', 'e', '-', 'B', 'k', 'o', 'n', '>', ')', 'P', 'z', '@', '.', ' ', 'L', '(', 'Z', 't', ':', 'V', 'i', '7', 'u', "'", 'j', ';', 'Y', 'h', '~', 'x', 'q', 'A', 'H', '}', '^', '3', ',', 'r', 'O', 'g', '2', '&', 'C', '%', 'c', '[', 'p', 'y', '4', '9', 'a', 'I', 'N', 'S', 'l', 'b', 'w', 'Q', '?', '5', 'U', '0', '`', '|', ']', '_', 'F', 'G', 'E', 'ß']
        self.encrypted_text = []
        self.decrypted_text = []
        self.encrypted_text_1 = ""
        self.decrypted_text_1 = ""
        self.pin = ""
        self.lol = 0
    def encryptor(self):
        self.number = 0
        self.text = input("Gib deinen zu verschlüsselnen text ein!\n> ")
        while True:
            self.pin_proto = input("Gib bitte eine Zahl zwischen 2 und 90 ein, diese Zahl wird dein Pin!\n> ")
            if 3 > len(self.pin_proto) > 0 and int(self.pin_proto):
                    break
            else:
                print("Das war wohl keine richtige Eingabe ...")
        for i in self.text:
            self.number = 0
            for a in self.alph:
                if i == a:
                    try:
                        self.encrypted_text.append(self.alph[int(self.number) + int(self.pin_proto)])
                    except:
                        self.encrypted_text.append(self.alph[(int(self.number) + int(self.pin_proto)) - len(self.alph)])
                self.number += 1
        for i in self.encrypted_text:
            self.encrypted_text_1 = self.encrypted_text_1 + i
        print("Verschlüsselter Text:\n" + self.encrypted_text_1)

    def decryptor(self):
        self.text = input("Wie lautet dein verschlüsselter Text?\n> ")
        self.pin = input("Wie lautet dein Pin?\n> ")

        self.number_1 = 0
        for i in self.text:
            self.number = 0
            for a in self.alph:
                if i == a:
                    try:
                        self.decrypted_text.append(self.alph[int(self.number) - int(self.pin)])
                    except:
                        self.decrypted_text.append(self.alph[(int(self.number) - int(self.pin)) - len(self.alph)])
                self.number += 1
        for i in self.decrypted_text:
            self.decrypted_text_1 = self.decrypted_text_1 + i
        print("Entschlüsselter Text:\n" + self.decrypted_text_1)



if __name__ == "__main__":
    encryption = Encryption()
    while True:
        user_input = input("Möchtest du 'v'erschlüsseln,'e'ntschlüsseln oder 'b'eenden?\n> ").lower()
        if user_input.startswith("v"):
            encryption.encryptor()
        elif user_input.startswith("e"):
            encryption.decryptor()
            quit(0)
        elif user_input.startswith("b"):
            quit(0)
        else:
            print("invalid input")