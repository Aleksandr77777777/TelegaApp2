from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
app = Client("my_account")
@app.on_message(filters.command("spam", prefixes=".")& filters.me)
def echo(client, message):
    ttt = message.text
    prefixxx = ttt.split(".spam ", maxsplit=1)[1]
    prefixxx = prefixxx.lstrip("num")
    vvv = prefixxx.split(" ", maxsplit=1)[0]
    num = int(vvv)
    rere = prefixxx.lstrip(vvv+" ")
    message.edit(rere)
    i=0
    while i<num:
        message.reply_text(rere)
        i=i+1

@app.on_message(filters.command("typing", prefixes=".")& filters.me)
def type(client,message):
    Ortext = message.text.split(".typing ",maxsplit = 1)[1]
    text = Ortext
    tbp = ""
    tupingSumbol = "..."
    while(tbp != Ortext):
        try:
            message.edit(tbp+ tupingSumbol)
            sleep(0.05)
            tbp = tbp + text[0]
            text = text[1:]
            message.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            sleep(e.x)
@app.on_message(filters.command("start", prefixes=".")& filters.me)
def rerere(client,message):
    rere = message.text.split(".start ",maxsplit = 1)[1]
    message.edit(rere)
    i = 1
    while True:
        i=i+1
        message.edit(rere*i)
        sleep(1)
@app.on_message(filters.command("sec", prefixes=".")& filters.me)
def rerere(client,message):
    message.edit("1\n")
    i = 1
    while True:
        i=i+1
        message.edit(str(i)+"\n")
        sleep(1)

app.run()
