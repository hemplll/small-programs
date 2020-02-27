print("Dieses Programm rechnet den Umfang und den Radius eines Dreieckes aus.")
Radius=input("Wie lautet ihr Radius in Zentimeter?:")
Radius=float(Radius)
pi=3.14159265359

umfang = Radius*2*pi
flächeninhalt= Radius*Radius*pi 
print("Umfang:", round(umfang,2), "Flächeninhalt:", round(flächeninhalt,2))
