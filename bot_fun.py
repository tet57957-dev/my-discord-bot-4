import discord
from discord.ext import commands
import os, random, datetime
TOKEN = os.getenv("DISCORD_TOKEN_3") or os.getenv("DISCORD_TOKEN")
OWNER_ID = 1395077285362794550
from flask import Flask
from threading import Thread
app = Flask(__name__)
@app.route("/")
def home(): return "Fun Bot alive!"
def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
Thread(target=run_web, daemon=True).start()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"🎮 บอทสนุกออนไลน์แล้ว: {bot.user}")

# สมาชิกทุกคนใช้ได้
@bot.command(name="ดวง")
async def duang_cmd(ctx, *, name=None):
    user = name or ctx.author.display_name
    luck = random.choice(["ดีมาก 🌟","ดี 😊","ปานกลาง 😐","ระวังหน่อย ⚠️","แย่หน่อย 😅"])
    love = random.randint(0,100)
    money = random.randint(0,100)
    embed = discord.Embed(title=f"🔮 ดวงวันนี้ของ {user}", color=0x9b59b6)
    embed.add_field(name="🍀 ดวงโดยรวม", value=luck, inline=False)
    embed.add_field(name="❤️ ดวงความรัก", value=f"{love}%", inline=True)
    embed.add_field(name="💰 ดวงการเงิน", value=f"{money}%", inline=True)
    embed.add_field(name="🎨 สีนำโชค", value=random.choice(["แดง","เขียว","เหลือง","น้ำเงิน","ชมพู","ม่วง"]), inline=True)
    embed.add_field(name="🔢 เลขนำโชค", value=str(random.randint(0,99)), inline=True)
    await ctx.send(embed=embed)

@bot.command(name="slot")
async def slot_cmd(ctx):
    emojis = ["🍒","🍋","🍊","🍇","⭐","💎"]
    a,b,c = random.choices(emojis, k=3)
    result = "🎉 แจ็คพอต! ถูก 3 อัน!" if a==b==c else "😊 เกือบแล้ว ลองใหม่" if a==b or b==c or a==c else "😅 ไม่ถูก ลองใหม่"
    await ctx.send(f"🎰 | {a} | {b} | {c} |\n{result}")

@bot.command(name="coin")
async def coin_cmd(ctx):
    await ctx.send(f"🪙 {random.choice(['หัว','ก้อย'])}")

@bot.command(name="8ball")
async def ball_cmd(ctx, *, q=None):
    if not q:
        await ctx.send("❌ พิมพ์แบบนี้ครับ: !8ball จะสอบผ่านไหม"); return
    ans = random.choice(["ใช่แน่นอน ✅","ไม่น่าใช่ ❌","50/50 🤔","ลองดูอีกที 🔮","ชัวร์ 100% 💯","อย่าเพิ่งถามตอนนี้ 😅"])
    await ctx.send(f"🎱 คำถาม: {q}\nคำตอบ: {ans}")

@bot.command(name="love")
async def love_cmd(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("❌ พิมพ์แบบนี้ครับ: !love @คน"); return
    pct = random.randint(0,100)
    bar = "❤️" * (pct//20) + "🤍" * (5 - pct//20)
    await ctx.send(f"💕 {ctx.author.display_name} ❤️ {member.display_name}\n{bar} {pct}%")

@bot.command(name="funhelp")
async def funhelp_cmd(ctx):
    embed = discord.Embed(title="🎮 บอทสนุก - rreqzn3l", description="สมาชิกทุกคนใช้ได้ | แอดมินก็ใช้ได้ | ทั้งหมด 47 คำสั่ง", color=0x2b2d31)
    embed.add_field(name="🎮 เล่นเกม (1)", value="!fortune/!ดวง ดูดวง | !slot/!สล็อต สล็อต | !coin โยนเหรียญ | !8ball ถามตอบ | !love เช็คความรัก", inline=False)
    embed.add_field(name="🎮 เล่นเกม (2)", value="!lottery/!หวย หวย | !random/!สุ่ม สุ่ม | !dream/!ฝัน ทำนายฝัน | !food สุ่มอาหาร | !movie สุ่มหนัง | !randnum สุ่มเลข | !vote โหวต", inline=False)
    embed.add_field(name="💬 คุยกับบอท", value="!chat/!คุยต่อ คุยต่อ | !stopchat/!เลิกคุย หยุดคุย | !lonely/!เหงา เหงา | !hug/!กอด กอด | !joke/!มุก มุก | !song/!เพลง เพลง | !sorry/!ขอโทษ ขอโทษ", inline=False)
    embed.add_field(name="💕 น่ารัก", value="!hi/!ทัก ทัก | !loveyou/!บอกรัก บอกรัก | !missyou/!คิดถึง คิดถึง | !goodnight/!ฝันดี ฝันดี | !cheer/!เชียร์ เชียร์ | !praise/!ชม ชม | !roast/!ด่า แซว", inline=False)
    embed.add_field(name="👋 ทักทาย", value="!hello/!สวัสดี สวัสดี | !morning เช้า | !night ก่อนนอน | !time/!เวลา เวลา | !invite/!ชวน ชวน | !sleep/!นอน นอน | !eat/!กิน กิน | !travel/!เที่ยว เที่ยว | !goodluck/!โชคดี โชคดี | !laugh หัวเราะ | !cry ร้อง", inline=False)
    embed.add_field(name="🎲 เกมเพิ่ม", value="!rps เป่ายิ้งฉุบ | !dice ทอยลูกเต๋า | !guess 1-10 ทายเลข | !truth ความจริง | !dare ท้าทาย | !spin วงล้อ | !quiz ตอบคำถาม | !roulette รูเล็ต | !blackjack แบล็คแจ็ค | !highlow สูงต่ำ | !pokdeng ป๊อกเด้ง", inline=False)
    embed.add_field(name="💡 วิธีใช้", value="พิมพ์ในห้อง #chat ได้เลย ไม่ต้องเป็นแอดมิน | !chat แล้วพิมพ์อะไรก็ได้ บอทตอบให้เลย", inline=False)
    await ctx.send(embed=embed)

# --- คำสั่งเล่นเกมเพิ่ม สำคัญๆ ---
@bot.command(name="rps")
async def rps_cmd(ctx, choice: str = None):
    import random as _r
    if not choice:
        await ctx.send("❌ พิมพ์แบบนี้ครับ: !rps ค้อน / กรรไกร / กระดาษ"); return
    botc = _r.choice(["ค้อน","กรรไกร","กระดาษ"])
    emoji = {"ค้อน":"✊","กรรไกร":"✌️","กระดาษ":"🖐️"}
    win = "ชนะ 🎉" if (choice=="ค้อน" and botc=="กรรไกร") or (choice=="กรรไกร" and botc=="กระดาษ") or (choice=="กระดาษ" and botc=="ค้อน") else "แพ้ 😅" if choice!=botc else "เสมอ 🤝"
    await ctx.send(f"{emoji.get(choice,'❓')} คุณ: {choice} vs {emoji.get(botc)} บอท: {botc} -> {win}")

@bot.command(name="dice")
async def dice_cmd(ctx):
    import random as _r
    await ctx.send(f"🎲 ทอยได้: {_r.randint(1,6)}")

@bot.command(name="guess")
async def guess_cmd(ctx, n: int = 0):
    import random as _r
    target = _r.randint(1,10)
    if n==0:
        await ctx.send("❌ พิมพ์แบบนี้ครับ: !guess 1-10"); return
    if n==target:
        await ctx.send(f"🎉 ถูก! เลขคือ {target}")
    else:
        await ctx.send(f"😅 ไม่ถูก เลขคือ {target} ลองใหม่")

@bot.command(name="truth")
async def truth_cmd(ctx):
    import random as _r
    qs = ["เคยแอบชอบใครในดิสนี้มั้ย?","เคยโกหกแฟนมั้ย?","กลัวอะไรมากที่สุด?","เคยร้องไห้เพราะเกมมั้ย?"]
    await ctx.send(f"🙊 Truth: {_r.choice(qs)}")

@bot.command(name="dare")
async def dare_cmd(ctx):
    import random as _r
    ds = ["ส่งสติกเกอร์น่ารักๆ 1 อัน","พิมพ์ 'รักบอท' 3 รอบ","บอกฝันดีเพื่อน 1 คน","ร้องเพลง 1 ท่อน"]
    await ctx.send(f"😈 Dare: {_r.choice(ds)}")

@bot.command(name="spin")
async def spin_cmd(ctx):
    import random as _r
    await ctx.send(f"🎡 วงล้อ: {_r.choice(['ได้เงิน','ได้ใจ','ได้แฟน','ได้กิน','ได้เที่ยว'])}")


@bot.command(name="quiz")
async def quiz_cmd(ctx):
    import random as _r
    q=[("ประเทศไทยเมืองหลวงคืออะไร?","กรุงเทพ"),("2+2=?","4"),("สีของท้องฟ้าคืออะไร?","ฟ้า")]
    qq,aa=_r.choice(q)
    await ctx.send(f"🧠 Quiz: {qq} (ตอบในใจนะ คำตอบคือ {aa})")

@bot.command(name="roulette")
async def roulette_cmd(ctx, bet: str = None):
    import random as _r
    n=_r.randint(0,36)
    color="🔴 แดง" if n%2==1 else "⚫ ดำ" if n!=0 else "🟢 0"
    await ctx.send(f"🎰 รูเล็ต: ออก {n} {color}")

# --- เพิ่มคำสั่งสำคัญๆ ให้ครบ 30-40 ---
@bot.command(name="fortune")
async def fortune_cmd(ctx, *, name=None): await duang_cmd(ctx, name=name)
@bot.command(name="lottery")
async def lottery_cmd(ctx):
    import random as _r
    await ctx.send(f"🎰 เลขหวย: {_r.randint(0,99):02d} / {_r.randint(0,999):03d}")
@bot.command(name="random")
async def random_cmd(ctx, *, items=None):
    import random as _r
    if not items: await ctx.send("❌ พิมพ์แบบนี้ครับ: !random ชา กาแฟ"); return
    await ctx.send(f"🎲 สุ่มได้: **{_r.choice(items.split())}**")
@bot.command(name="dream")
async def dream_cmd(ctx, *, txt=None):
    import random as _r
    await ctx.send(f"💤 ฝันเรื่อง {txt or 'เมื่อคืน'}: {_r.choice(['ฝันดี จะมีโชค ✨','ฝันดี จะเจอคนถูกใจ ❤️','ระวังของหาย ⚠️','เงินกำลังจะเข้า 💰'])}")
@bot.command(name="food")
async def food_cmd(ctx):
    import random as _r
    await ctx.send(f"🍜 วันนี้กิน: **{_r.choice(['ข้าวผัด','ก๋วยเตี๋ยว','ชาบู','หมูกระทะ','ส้มตำ','ข้าวมันไก่','พิซซ่า','ซูชิ'])}**")
@bot.command(name="movie")
async def movie_cmd(ctx):
    import random as _r
    await ctx.send(f"🎬 วันนี้ดู: **{_r.choice(['Your Name','One Piece','Demon Slayer','Harry Potter','Spider-Man'])}**")
@bot.command(name="randnum")
async def randnum_cmd(ctx, a: int = 1, b: int = 100):
    import random as _r
    await ctx.send(f"🎲 สุ่มเลข {a}-{b}: **{_r.randint(a,b)}**")
@bot.command(name="vote")
async def vote_cmd(ctx, *, txt=None): await ctx.send(f"📊 โหวต: {txt or 'เรื่องที่โหวต'} 👍 = เห็นด้วย / 👎 = ไม่เห็นด้วย")
@bot.command(name="chat")
async def chat_cmd(ctx): await ctx.send("💬 อยากคุยกับบอทหรอ 🥺 พิมพ์ !คุยต่อ เลยครับ")
@bot.command(name="hug")
async def hug_cmd(ctx, member: discord.Member = None):
    if not member: await ctx.send("🤗 กอดตัวเองก่อนนะ"); return
    await ctx.send(f"🤗 {ctx.author.display_name} กอด {member.display_name} แล้วว")
@bot.command(name="joke")
async def joke_cmd(ctx):
    import random as _r
    await ctx.send(_r.choice(["ทำไมปลาไม่เล่นไพ่? กลัวโดนจับว่าโกง 😂","ไก่กับไข่อะไรเกิดก่อน? ไก่ครับ เพราะไข่ไม่มีมือเปิดประตู 🐔","ทำไมคอมถึงเย็น? เพราะมีพัดลม 😆"]))
@bot.command(name="song")
async def song_cmd(ctx):
    import random as _r
    await ctx.send(_r.choice(["🎵 ลองฟัง: ใจฟู - Three Man Down","🎵 เพลงนี้ดี: ดาวหางฮัลเลย์","🎵 แนะนำ: ซ่อนกลิ่น - Palmy"]))
@bot.command(name="lonely")
async def lonely_cmd(ctx): await ctx.send("เหงาหรอ มาอยู่นี่แล้วไง 🤗 ไม่มีอะไรเล่นหรอ มาลอง !slot กันมั้ย 🎰")
@bot.command(name="blackjack")
async def blackjack_cmd(ctx):
    import random as _r
    u=_r.randint(2,21); b=_r.randint(2,21)
    res="ชนะ 🎉" if u>b else "แพ้ 😅" if u<b else "เสมอ 🤝"
    await ctx.send(f"🃏 คุณได้ {u} vs บอทได้ {b} -> {res}")
@bot.command(name="highlow")
async def highlow_cmd(ctx, choice: str = None):
    import random as _r
    n=_r.randint(1,10)
    if not choice: await ctx.send("❌ พิมพ์ !highlow สูง/ต่ำ"); return
    win = (choice=="สูง" and n>5) or (choice=="ต่ำ" and n<6)
    await ctx.send(f"🎲 ออก {n} -> {'ถูก 🎉' if win else 'ไม่ถูก 😅'}")
@bot.command(name="goodnight")
async def goodnight_cmd(ctx): await ctx.send(f"🌙 ฝันดีนะ {ctx.author.display_name} ✨")
@bot.command(name="hello")
async def hello_cmd(ctx): await ctx.send(f"👋 สวัสดี {ctx.author.display_name} ครับ")
@bot.command(name="love2")
async def love2_cmd(ctx, member: discord.Member = None):
    import random as _r
    if not member: await ctx.send("❌ พิมพ์ !love @คน"); return
    pct=_r.randint(0,100)
    await ctx.send(f"💕 {ctx.author.display_name} ❤️ {member.display_name} {pct}%")
@bot.command(name="time")
async def time_cmd(ctx):
    import datetime
    await ctx.send(f"🕐 ตอนนี้ {datetime.datetime.now().strftime('%H:%M')} ครับ")
@bot.command(name="cheer")
async def cheer_cmd(ctx, member: discord.Member = None):
    if not member: await ctx.send("📣 สู้ๆ ครับ!"); return
    await ctx.send(f"📣 สู้ๆ {member.display_name} ครับ!")
@bot.command(name="ask")
async def ask_cmd(ctx, *, q=None):
    import random as _r
    if not q: await ctx.send("ถามอะไรครับ !ask เรื่องที่อยากถาม"); return
    await ctx.send(_r.choice([f"เรื่อง '{q}' ผมว่าดีนะ","ไม่แน่ใจ ลองถามคนอื่นดู","ใช่เลย","ไม่น่าใช่"]))

# --- เพิ่มให้ครบ 46 คำสั่ง ---
@bot.command(name="8ball")
async def ball8_cmd(ctx, *, q=None):
    import random as _r
    await ctx.send(f"🎱 {_r.choice(['ใช่เลย','ไม่น่าใช่','ชัวร์','ลองเสี่ยงดู','ไม่รู้ดิ','แน่นอน','50/50'])}")
@bot.command(name="coinflip")
async def coinflip_cmd(ctx):
    import random as _r
    await ctx.send(f"🪙 ออก **{_r.choice(['หัว','ก้อย'])}**")
@bot.command(name="love")
async def love_cmd(ctx, member: discord.Member = None):
    import random as _r
    if not member: await ctx.send("❌ พิมพ์ !love @คน"); return
    await ctx.send(f"💕 {ctx.author.display_name} ❤️ {member.display_name} {_r.randint(0,100)}%")
@bot.command(name="roast")
async def roast_cmd(ctx, member: discord.Member = None):
    import random as _r
    if not member: await ctx.send("❌ พิมพ์ !roast @คน"); return
    await ctx.send(f"😂 {member.display_name} {_r.choice(['ยังเล่นไม่เก่งแต่หัวร้อนเก่ง','นอนน้อยแต่เล่นเยอะ','แพ้บ่อยแต่ปากเก่ง'])}")
@bot.command(name="praise")
async def praise_cmd(ctx, member: discord.Member = None):
    if not member: await ctx.send("✨ ชมทุกคนเก่งหมดครับ"); return
    await ctx.send(f"✨ {member.display_name} เก่งมากครับ")
@bot.command(name="missyou")
async def miss_cmd(ctx, member: discord.Member = None):
    if not member: await ctx.send("คิดถึงทุกคนครับ 🥺"); return
    await ctx.send(f"💌 {ctx.author.display_name} คิดถึง {member.display_name} ครับ")
@bot.command(name="goodluck")
async def luck_cmd(ctx, member: discord.Member = None):
    if not member: await ctx.send("🍀 โชคดีนะครับ"); return
    await ctx.send(f"🍀 โชคดีนะ {member.display_name}")
@bot.command(name="sleep")
async def sleep_cmd(ctx): await ctx.send("😴 ไปนอนได้แล้ว ฝันดีนะ")
@bot.command(name="eat")
async def eat_cmd(ctx): await ctx.send("🍜 ไปกินข้าวกันเถอะ")
@bot.command(name="travel")
async def travel_cmd(ctx): await ctx.send("✈️ อยากไปเที่ยวที่ไหนครับ")
@bot.command(name="hi")
async def hi_cmd(ctx): await ctx.send(f"👋 สวัสดีครับ {ctx.author.display_name}")


@bot.command(name="pokdeng")
async def pokdeng_cmd(ctx):
    import random as _r
    suits=["♥️","♦️","♣️","♠️"]
    ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def draw():
        return _r.choice(ranks), _r.choice(suits)
    def score(cards):
        s=0
        for r,_ in cards:
            if r in ["J","Q","K"]: s+=0
            elif r=="A": s+=1
            else: s+=int(r)
        return s%10
    def is_pok(cards):
        return score(cards) in [8,9]
    u=[draw(),draw()]
    b=[draw(),draw()]
    us=score(u); bs=score(b)
    # ป๊อกเด้ง 2 ใบแต้ม 8/9 = ป๊อก
    # เด้ง: ดอกเดียวกันทั้ง 2 ใบ = เด้ง, 3 ใบดอกเดียวกัน = เด้ง
    def is_deng(cards): return cards[0][1]==cards[1][1]
    u_str=" ".join([f"{r}{s}" for r,s in u])
    b_str=" ".join([f"{r}{s}" for r,s in b])
    upok="ป๊อก!" if is_pok(u) else ""
    bPok="ป๊อก!" if is_pok(b) else ""
    udeng="เด้ง!" if is_deng(u) else ""
    bdeng="เด้ง!" if is_deng(b) else ""
    if us>bs: res="🎉 คุณชนะ!"
    elif us<bs: res="😅 คุณแพ้!"
    else: res="🤝 เสมอ!"
    await ctx.send(f"🃏 ป๊อกเด้ง\nคุณ: {u_str} = {us} แต้ม {upok} {udeng}\nบอท: {b_str} = {bs} แต้ม {bPok} {bdeng}\n{res}")

bot.run(TOKEN)