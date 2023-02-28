from os import sync,getenv
import discord
from datetime import datetime, timedelta
from flask import Flask
import threading
#from dotenv import load_dotenv


# get .env
#load_dotenv()
# get serverid txtid
SERVER_ID = int(getenv("SERVER"))
TXT_ID = int(getenv("TEXT"))
print("Success > Got SERVER and TEXT ID.")
app = Flask(__name__)
client = discord.Client(intents=discord.Intents.all())


# client start
@client.event
async def on_ready():
  print("Success > Login.")


# event on voicechat
@client.event
async def on_voice_state_update(member, before, after):
  print("Log > Event was called.")
  if member.guild.id == SERVER_ID:
    if before.channel != after.channel:
      now = datetime.utcnow() + timedelta(hours=9)
      alert_channel = client.get_channel(TXT_ID)
      if before.channel is None:
        msg = f"== {now:%m/%d %H:%M} ==\n{member.name} さん <#{after.channel.id}> へようこそ！"
        print(msg)
        await alert_channel.send(msg)
      elif after.channel is None:
        msg = f"== {now:%m/%d %H:%M} ==\n{member.name} さん <#{before.channel.id}> へまた来てね！"
        print(msg)
        await alert_channel.send(msg)


@app.route('/')
def hello():
    name = "discordbotです"
    return name
# run client

def main():
  
    client.run(getenv("TOKEN"))

def main1():
    app.run(debug=True)

if __name__ == "__main__":
   main()
