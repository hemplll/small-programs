import discord
def roulette():
    async def on_message(self, message):
        if message.content == "$roulette help":
            await message.channel.send("""Für Roulette: $roulette BID eingeben, wobei BID = black/red/number""")
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
            await message.channel.send("§§Du hast gewonnen§§")
        else:
            await message.channel.send("Du hast leider verloren")