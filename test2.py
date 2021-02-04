
import discord
import json
from discord.ext import commands
import datetime
import asyncio
import random
import time


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = '.', intent=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('testing...'))
    print ('test is ready.')


                    
@client.command()
async def ts(ctx):
    member = ctx.author
    with open('status.json', 'r') as f:
        status = json.load(f)
    try:
        status = status[str(member.id)]['status']
    except:
        status = 'No Status has been set.'
    
    try:
        with open('banvouch.json', 'r') as f:
            v = json.load(f)
            print(v[str(member.id)])
            await ctx.send(f"⚠️ {member.mention}, you're banned from this feature. Please contact support for assistance.")
    except:
        try:
            with open('vouch.json', 'r') as f:
                v = json.load(f)
                print(v[str(member.id)])
                v = v[str(member.id)]
        except:
            v = 0
        orange = '#f07600'
        yellow = '#fff300'
        yg = '#9ed711'
        green = '#09ce27'
        red = '#ff0000'
        blue = '#004cff'
        try:
            with open('overwrite.json', 'r') as f:
                ow = json.load(f)
            oww = ow[str(member.id)] * 10
                
        except:
            oww = v
        with open('color.json', 'r') as f:
            ec = json.load(f)
        if (member.id == 401255477733752854) or (member.id == 465105906942869505):
            o = 'Level 5'
            c = 'Owner 👑'
            try:
                embed_color = ec[str(member.id)]
            except:
                embed_color = 0x004cff
        elif (oww<-1) and (oww>11):
            o = 'Level 0'
            c = 'Suspicious Trader⚠️'
            embed_color = 0xff0000
        elif (oww<10) and (oww>-1):
            o = 'Level 1'
            c = 'Random Trader❗'
            embed_color = 0xfff300
        elif (oww>9) and (oww<20):
            o = 'Level 2'
            c = 'Regular Trader❕'
            try:
                embed_color = ec[str(member.id)]
            except:
                embed_color = 0x9ed711
        elif (oww>19) and (oww<31):
            o = 'Level 3'
            c = 'Trusted Trader✅'
            try:
                embed_color = ec[str(member.id)]
            except:
                embed_color = 0x09ce27
        elif (oww>39) and (oww<51):
            o = 'Level 4'
            c = 'Middleman 👤'
            try:
                embed_color = ec[str(member.id)]
            except:
                embed_color = 0x004cff
        try:
            with open('owner.json', 'r') as f:
                lel = json.load(f)
                print(lel[str(member.id)])
                owner = True
        except:
            owner = False
        try:
            with open('coowner.json', 'r') as f:
                lel = json.load(f)
                print(lel[str(member.id)])
                coowner = True
        except:
            coowner = False
        embed = discord.Embed(description = f'{status}', color = embed_color)
        embed.set_author(name = f"{member}'s Trade Shop", icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/780107697924079676.png?v=1") 
        ovcheck = True
        if (owner == False) and (coowner == False): 
            embed.add_field(name = "🎖️ Trade Reputation 🎖️", value = f"❔┃{o} - {c}")
            ovcheck = False
        elif (owner == True) and (coowner == False):
            owvouch = 'Smokepole'
        elif (owner == False) and (coowner == True):
            owvouch = 'Shadowzz'
        elif (owner == True) and (coowner == True):
            owvouch = 'Smokepole, Shadowzz'
        if ovcheck == True:
            embed.add_field(name = "🎖️ Trade Reputation 🎖️", value = f"""❔┃{o} - {c}
    👑┃Ownervouch: {owvouch}""")
        try:
            gg = sl[str(member.id)]
            if gg == 1:
                h = f'''1.{s[str(member.id)][0]}'''
            elif gg == 9:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
5.{s[str(member.id)][4]}
6.{s[str(member.id)][5]}
7.{s[str(member.id)][6]}
8.{s[str(member.id)][7]}
9.{s[str(member.id)][8]}'''
            elif gg == 8:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
5.{s[str(member.id)][4]}
6.{s[str(member.id)][5]}
7.{s[str(member.id)][6]}
8.{s[str(member.id)][7]}'''
            elif gg == 7:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
5.{s[str(member.id)][4]}
6.{s[str(member.id)][5]}
7.{s[str(member.id)][6]}
'''
            elif gg == 6:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
5.{s[str(member.id)][4]}
6.{s[str(member.id)][5]}
'''
            elif gg == 5:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
5.{s[str(member.id)][4]}
'''
            elif gg == 4:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
'''
            elif gg == 3:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
'''
            elif gg == 2:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
'''
            elif gg == 10:
                h = f'''1.{s[str(member.id)][0]}
2.{s[str(member.id)][1]}
3.{s[str(member.id)][2]}
4.{s[str(member.id)][3]}
5.{s[str(member.id)][4]}
6.{s[str(member.id)][5]}
7.{s[str(member.id)][6]}
8.{s[str(member.id)][7]}
9.{s[str(member.id)][8]}
10.{s[str(member.id)][9]}'''
        except:
            h = '''None'''
        embed.add_field(name = "<:WOW:767604318739103775>Trade Shops", value = h, inline=False)
        with open('status.json', 'r') as f:
            status = json.load(f)
        try:
            if status[str(member.id)]['mm'] == 0:
                mm = '❌'
            elif status[str(member.id)]['mm'] == 1:
                mm = '✅'
        except:
            mm = '⚠️'
        try:
            if status[str(member.id)]['neg'] == 0:
                neg = '❌'
            elif status[str(member.id)]['neg'] == 1:
                neg = '✅'
        except:
            neg = '⚠️'
        try:
            if status[str(member.id)]['st'] == 0:
                st = '❌'
            elif status[str(member.id)]['st'] == 1:
                st = '✅'
        except:
            st = '⚠️'
        try:
            if status[str(member.id)]['bt'] == 0:
                bt = '❌'
            elif status[str(member.id)]['bt'] == 1:
                bt = '✅'
        except:
            bt = '⚠️'
        embed.add_field(name = '✅Info', value = f'''👤┃Trade with middleman {mm}
🤝┃Negotiating {neg}
📤┃TAX covered by shop-host by selling {st}
📥┃TAX covered by shop-host by buying {bt}''')
        embed.set_footer(text = "Scuffed Shop - Setup your own trade shop with !tshelp", icon_url = ctx.guild.icon_url)
        await ctx.send(embed = embed)
@client.command()
async def tsadd(ctx, *, msg_info):
    member = ctx.author
    with open('shoplist.json', 'r') as f:
        sl = json.load(f)
    try:
        if sl[str(member.id)] != 10:
            sl[str(member.id)] += 1
            with open('shoplist.json', 'w') as f:
                json.dump(sl, f, indent=4)
            with open('shop.json', 'r') as f:
                s = json.load(f)
            s[str(member.id)].append(msg_info)
            with open('shop.json', 'w') as f:
                json.dump(s, f, indent=4)
                
            await ctx.send('Info has been added to trade shop!')
        else:
            ctx.send('You have the limit of 10 trade shops. Please type `!vs remove <no.>` to remove one of your trade shops.')
    except:
        sl[str(member.id)] = 1
        with open('shoplist.json', 'w') as f:
            json.dump(sl, f, indent=4)
        with open('shop.json', 'r') as f:
            s = json.load(f)
            msgg = []
            msgg.append(msg_info)
        with open('shop.json', 'w') as f:
            s[str(member.id)] = msgg
            json.dump(s, f, indent=4)
        await ctx.send('Info has been added to trade shop!')
@client.command()
async def tsdel(ctx, msg_info):
    try:
        msg_info = int(msg_info)
        with open('shoplist.json', 'r') as f:
            sl = json.load(f)
        with open('shop.json', 'r') as f:
            s = json.load(f)

        sl[str(member.id)] -= 1
        s[str(member.id)].pop(msg_info-1)
        if sl[str(member.id)] == 0:
            sl.pop(str(member.id))
            s.pop(str(member.id))
        with open('shop.json', 'w') as f:
            json.dump(s, f, indent=4)
        with open('shoplist.json', 'w') as f:
            json.dump(sl, f, indent=4)
        await ctx.send("Deleted trade shop.")
    except:
        await ctx.send('Please mention the number of the trade shop to delete.')
@client.command()
async def tsedit(ctx, position : int, *, msg_info):
    member = ctx.author
    with open('shoplist.json', 'r') as f:
        sl = json.load(f)
    with open('shop.json', 'r') as f:
        s = json.load(f)
    try:
        ebrslbfsffr = sl[str(member.id)]
        if position < sl[str(member.id)] + 1:
            s[str(member.id)][position - 1] = msg_info
            with open('shop.json', 'w') as f:
                json.dump(s, f, indent=4)
            await ctx.send(f"Successfuly updated Trade Reputation with the id {position} to {msg_info}") 
        else:
            await ctx.send('Invalid Trade Shop ID')
    except:
        await ctx.send("Ay mate, you don't have a trade shop set up!")

@client.command()
async def tscolor(ctx, a=None):
    member = ctx.author
    if a != None:
        try:
            a = int(a.replace("#", ""), 16)
            a = int(hex(a), 0)
            embed = discord.Embed(title = 'Preview', description = "Answer 1 to confirm this color, anything else will cancel it.", color = a)
            await ctx.send(embed = embed)
            def check(m):
                return m.author == ctx.author and m.guild == ctx.guild
            try:
                msg = await client.wait_for('message', timeout = 60.0, check=check)
            except asyncio.TimeoutError:
                await member.send(f'Time out {member}.')
            else:
                if msg.content == '1':
                    with open('color.json', 'r') as f:
                        c = json.load(f)
                    c[str(member.id)] = a
                    with open('color.json', 'w') as f:
                        json.dump(c, f, indent=4)
                    await ctx.send('Done!')
                else:
                    await ctx.send('Cancelled')
        except:
            await ctx.send("Invalid hexadecimal code.")     
    else:
        with open('color.json', 'r') as f:
            c = json.load(f)
        c.pop(str(member.id))
        with open('color.json', 'w') as f:
            json.dump(c, f, indent=4)
        await ctx.send("Reset trade shop embed color")

@client.command()
async def tsset(ctx, decider, *, a=None):
    member = ctx.author
    if decider == 'status':
        with open("status.json", 'r') as f:
            s = json.load(f)
        if a != None:
            try:
                ggs = s[str(member.id)]
            except:
                s[str(member.id)] = {}
            s[str(member.id)]['status'] = a
            with open('status.json', 'w') as f:
                json.dump(s, f)
            await ctx.send(f'Set your trade shop status to - {a}')
        else:
            try:
                with open('status.json', 'r') as f:
                    s = json.load(f)
                s[str(member.id)].pop('status')
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                await ctx.send("Reset your trade shop status.")
            except: 
                await ctx.send("You didn't set any trade shop status to reset it.")
    elif decider == 'mm':
        with open("status.json", 'r') as f:
            s = json.load(f)
        if a != None:
            try:
                ggs = s[str(member.id)]
            except:
                s[str(member.id)] = {}
            wowo = True
            if a == 'true':
                wow = 1
            elif a == 'false':
                wow = 0
            else:
                wowo = False
                await ctx.send(f'Mate, you either gotta send true or false, not {a}')
            if wowo == True:
                s[str(member.id)]['mm'] =  wow
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                if wow == 1:
                    ss = 'true'
                if wow == 0:
                    ss = 'false'
                await ctx.send(f'Changed your middleman status to {ss}')
        else:
            try:
                with open('status.json', 'r') as f:
                    s = json.load(f)
                s[str(member.id)].pop('mm')
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                await ctx.send("Reset your mm status.")
            except: 
                await ctx.send("You didn't set any mm status to reset it.")
    elif decider == 'neg':
        with open("status.json", 'r') as f:
            s = json.load(f)
        if a != None:
            try:
                ggs = s[str(member.id)]
            except:
                s[str(member.id)] = {}
            wowo = True
            if a == 'true':
                wow = 1
            elif a == 'false':
                wow = 0
            else:
                wowo = False
                await ctx.send(f'Mate, you either gotta send true or false, not {a}')
            if wowo == True:
                s[str(member.id)]['neg'] =  wow
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                if wow == 1:
                    ss = 'true'
                if wow == 0:
                    ss = 'false'
                await ctx.send(f'Changed your negotiation status to {ss}')
        else:
            try:
                with open('status.json', 'r') as f:
                    s = json.load(f)
                s[str(member.id)].pop('neg')
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                await ctx.send("Reset your negotiation status.")
            except: 
                await ctx.send("You didn't set any negotiation status to reset it.")
    elif decider == 'selltax':
        with open("status.json", 'r') as f:
            s = json.load(f)
        if a != None:
            try:
                ggs = s[str(member.id)]
            except:
                s[str(member.id)] = {}
            wowo = True
            if a == 'true':
                wow = 1
            elif a == 'false':
                wow = 0
            else:
                wowo = False
                await ctx.send(f'Mate, you either gotta send true or false, not {a}')
            if wowo == True:
                s[str(member.id)]['st'] =  wow
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                if wow == 1:
                    ss = 'true'
                if wow == 0:
                    ss = 'false'
                await ctx.send(f'Changed your sell tax status to {ss}')
        else:
            try:
                with open('status.json', 'r') as f:
                    s = json.load(f)
                s[str(member.id)].pop('st')
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                await ctx.send("Reset your sell tax status.")
            except: 
                await ctx.send("You didn't set any sell tax status to reset it.")
    elif decider == 'buytax':
        with open("status.json", 'r') as f:
            s = json.load(f)
        if a != None:
            try:
                ggs = s[str(member.id)]
            except:
                s[str(member.id)] = {}
            wowo = True
            if a == 'true':
                wow = 1
            elif a == 'false':
                wow = 0
            else:
                wowo = False
                await ctx.send(f'Mate, you either gotta send true or false, not {a}')
            if wowo == True:
                s[str(member.id)]['bt'] =  wow
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                if wow == 1:
                    ss = 'true'
                if wow == 0:
                    ss = 'false'
                await ctx.send(f'Changed your buy tax status to {ss}')
        else:
            try:
                with open('status.json', 'r') as f:
                    s = json.load(f)
                s[str(member.id)].pop('bt')
                with open('status.json', 'w') as f:
                    json.dump(s, f, indent=4)
                await ctx.send("Reset your buy tx status.")
            except: 
                await ctx.send("You didn't set any buy tax status to reset it.")

@client.command()
async def tshelp(ctx):
    embed = discord.Embed(title = "Run the commands below to setup your shop:", description = """!tsset status <your text>
▪︎Sets up your custom status at the top.

!tsset <number> <your text>
▪︎Will add your offers to the trade shop.

!tsset mm <true/false>
▪︎Accepting/Rejecting interaction with middlemans

!tsset neg <true/false>
▪︎Accepting/Rejecting negotiations 

!tsset selltax <true/false>
▪︎Covering the TAX during selling

!tsset buytax <true/false>
▪︎Covering the TAX during buying

⚠️ - Not set.
✅ - Agreed.
❌ - Disagreed.

Still need help? Contact our support!""")
    embed.set_author(name = "Scuffed Trade Shop", icon_url = ctx.guild.icon_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/780107697924079676.png?v=1")
    embed.set_footer(text="Scuffed Shop - Don't get scammed!", icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


client.run('Nzk3ODM0MDk0NDM2MTU1NDAy.X_sO5w.YQnxyi40QFZ18dPLqfNMd6VzDk0')