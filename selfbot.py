"""
Github: AndyOnTop
Website: https://andyon.top

Please read the readme.md before you do anything.

Also plz dont leach
"""
from discord.ext import commands
import discord
import time
import datetime

print("Starting please wait.")

token = "Put your alt discord account token here."
discord_id = "459887206501187586" # Put your main discord accounts id here, the account has to be in the server you're sending the commmand in.
bot = commands.Bot("/--/", self_bot=True)
now = datetime.datetime.now()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ANDY ON TOP")) # You can delete this line or change ducchub to your server name, its just a custom status
    print("""
           _   _ _______     __   ____  _   _   _______ ____  _____  
     /\   | \ | |  __ \ \   / /  / __ \| \ | | |__   __/ __ \|  __ \ 
    /  \  |  \| | |  | \ \_/ /  | |  | |  \| |    | | | |  | | |__) |
   / /\ \ | . ` | |  | |\   /   | |  | | . ` |    | | | |  | |  ___/ 
  / ____ \| |\  | |__| | | |    | |__| | |\  |    | | | |__| | |     
 /_/    \_\_| \_|_____/  |_|     \____/|_| \_|    |_|  \____/|_|     
                                                                     
                            Credits:
                        Github: AndyOnTop
                    Website: https://andyon.top
                                                                     """)

@bot.command()
async def farm(ctx):
    print("Starting farm.")
    while True:
        await ctx.send('pls beg')
        print("sent 'pls beg' " + str(now))
        time.sleep(5)
        await ctx.send('pls pm')
        print("sent 'pls pm' " + str(now))
        time.sleep(3)
        await ctx.send('f')
        print("sent 'f' (answering to pls pm) " + str(now))
        time.sleep(5)
        await ctx.send('pls search')
        print("sent 'pls search' " + str(now))
        time.sleep(2)
        await ctx.send('air')
        print("sent 'air' (answer to option) " + str(now))
        time.sleep(7)
        await ctx.send('pls fish')
        print("sent 'pls fish' " + str(now))
        time.sleep(2)
        await ctx.send("pls hunt")
        print("sent 'pls hunt' " + str(now))
        time.sleep(5)
        await ctx.send("pls sell fish all")
        print("sent 'pls sell fish all' " + str(now))
        time.sleep(5)
        await ctx.send("pls sell boar all")
        print("sent 'pls sell boar all' " + str(now))
        time.sleep(5)
        await ctx.send("pls give <@" + discord_id + "> all")
        print("sent 'pls give <@'" + discord_id + "> " + "Gives money to your main" + str(now))
        time.sleep(5)



bot.run(token, bot=False)