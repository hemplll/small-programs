def coinflip():
    async def on_message(self, message):
        coin=["Kopf","Zahl"]
        if message.content == ("!coinflip"):
            message.channel.send(random.choice(coin))