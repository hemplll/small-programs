import discord
import random

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop")

    #Roulette
    async def on_message(self, message):
        if message.author == client.user:
            return
        elif message.content.startswith("$roulette"):
            if message.content == "$roulette help":
                await message.channel.send("""Für Roulette: $roulette BID eingeben, wobei BID = black/red/number(0-36)""")
            elif message.content.startswith("$roulette"):
                bid = message.content.split(" ")[1]
            bid_param = -3
            if bid.lower() == "black":
                bid_param = -1
            elif bid.lower() == "red":
                bid_param = -2
            else:
                try:
                    bid_param = int(bid)
                except:
                    bid_param = -3
            if bid_param == -3:
                await message.channel.send("Ungültige Eingabe")
                return
            result = random.randint(0, 36)
            if bid_param == -1:
                won = result % 2 == 0 and not result == 0
            elif bid_param == -2:
                won = result % 2 == 1
            else:
                won = result == bid_param
            if won:
                await message.channel.send("$$Du hast gewonnen$$")
            else:
                await message.channel.send("Du hast leider verloren")




        elif message.content == ("!coinflip"):
            coin = ["Kopf", "Zahl"]
            await message.channel.send(random.choice(coin))
        elif message.content == ("!help"):
            await message.channel.send("Meine aktuellen Commands sind:\n$roulette help\n!coinflip\n!sonne\n!ferdi")
        elif message.content == ("!sonne"):
            items = [":sunny:",":cherries:",":lemon:",":tangerine:",":strawberry:"]
            item1 = random.choice(items)
            item2 = random.choice(items)
            item3 = random.choice(items)
            result = [item1, item2, item3]
            await message.channel.send(result)
            if result == [":sunny:",":sunny:",":sunny:"]:
                await message.channel.send("Du hast gewonnen!:partying_face:")
            elif result == [":cherries:",":cherries:",":cherries:",]:
                await message.channel.send("Du hast gewonnen!:partying_face:")
            elif result == [":lemon:",":lemon:",":lemon:",]:
                await message.channel.send("Du hast gewonnen!:partying_face:")
            elif result == [":tangerine:",":tangerine:",":tangerine:"]:
                await message.channel.send("Du hast gewonnen!:partying_face:")
            elif result == [":strawberry:",":strawberry:",":strawberry:"]:
                await message.channel.send("Du hast gewonnen!:partying_face:")
            else:
                await message.channel.send("Du hast leider verloren :cry:")

        elif message.content == ("!ferdi"):
            await message.channel.send("Ferdi ist leider an Autismus und ADHS erkrankt :cry:")



client= MyClient()
client.run("NjcyNjAwOTQ1Mjg4NTQ0MzA2.XjN3Eg.6TenXWkXmDcpVox9pHxHAvGBC4o")
