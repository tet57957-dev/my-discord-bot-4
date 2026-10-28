import discord
from discord.ext import commands
import os, random, datetime
TOKEN = os.getenv("DISCORD_TOKEN_3") or os.getenv("DISCORD_TOKEN")
from flask import Flask
from threading import Thread
app = Flask(__name__)
@app.route("/")
def home(): return "Fun Bot alive!"
def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
Thread(target=run_web, daemon=True).start()

OWNER_ID = 1395077285362794550
# Flask removed - no need
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
    embed = discord.Embed(title="🎮 คำสั่งทั้งหมด - Bot Fun (rreqzn3l)", description="ทั้งหมด 47 คำสั่ง | สมาชิกใช้ได้ | แอดมินก็ใช้ได้ | แยกตามห้อง 3 ห้อง", color=0x2b2d31)
    embed.add_field(name="🎮 #play-game - ห้องเล่นเกม", value="!slot - สล็อต\n!rps ค้อน/กรรไกร/กระดาษ - เป่ายิ้งฉุบ\n!dice - ทอยลูกเต๋า\n!guess 1-10 - ทายเลข\n!truth - เกมความจริง\n!dare - เกมท้าทาย\n!spin - วงล้อ\n!quiz - ตอบคำถาม\n!roulette - รูเล็ต\n!blackjack - แบล็คแจ็ค\n!highlow สูง/ต่ำ - สูงต่ำ\n!pokdeng - ป๊อกเด้ง\n!coin - โยนเหรียญ\n!random ชา กาแฟ - สุ่มเลือก\n!food - สุ่มอาหาร\n!movie - สุ่มหนัง\n!randnum 1 100 - สุ่มเลข\n!vote เรื่อง - โหวต", inline=False)
    embed.add_field(name="🔮 #forutne - ห้องดูดวง", value="!fortune - ดูดวงวันนี้\n!lottery - สุ่มเลขหวย\n!dream เรื่อง - ทำนายฝัน\n!love @คน - เช็คความรัก\n!8ball คำถาม - ถามแล้วตอบ", inline=False)
    embed.add_field(name="💬 #chat-bot - ห้องคุยกับบอท", value="!chat - เริ่มคุยกับบอท\n!stopchat - หยุดคุย\n!lonely - เหงา ชวนเล่น\n!hug @คน - กอดเพื่อน\n!joke - เล่นมุก\n!song - แนะนำเพลง\n!sorry @คน - ขอโทษ\n!hi - ทักทาย\n!loveyou @คน - บอกรัก\n!missyou @คน - คิดถึง\n!goodnight - บอกฝันดี\n!cheer @คน - เชียร์\n!praise @คน - ชม\n!roast @คน - แซว\n!hello - สวัสดี\n!morning - ทักเช้า\n!night - ก่อนนอน\n!time - ดูเวลา\n!sleep - ไปนอน\n!eat - กินข้าว\n!travel - เที่ยว\n!goodluck - โชคดี\n!laugh - หัวเราะ\n!cry - ร้อง", inline=False)
    embed.add_field(name="📸 #show-result - ห้องอวดผล", value="แคปผล !slot !fortune !pokdeng มาอวดกันครับ", inline=False)
    embed.add_field(name="💡 วิธีใช้", value="พิมพ์ในห้องที่เขียนไว้ข้างบนเลยครับ เช่น เล่นเกมพิมพ์ใน #play-game ดูดวงพิมพ์ใน #forutne", inline=False)
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
async def chat_cmd(ctx): await chat_on_cmd(ctx)
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
@bot.command(name="coinflip")
async def coinflip_cmd(ctx):
    import random as _r
    await ctx.send(f"🪙 ออก **{_r.choice(['หัว','ก้อย'])}**")
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

# --- ระบบคุยต่อ ---
chat_sessions = set()
@bot.command(name="คุยต่อ")
async def chat_on_cmd(ctx):
    chat_sessions.add(ctx.author.id)
    import random as _r
    cute = [f"หืมม อยากคุยกับบอทหรอ 🥺 มาๆ มาคุยกันหน่อย {ctx.author.display_name} คิดถึงอยู่พอดีเลย 💕", f"เย้! {ctx.author.display_name} มาหาบอทแล้วว เหงาเหมือนกันเลย มาคุยกันนะ 🤗", f"อุ้ย {ctx.author.display_name} มาอยู่กับบอทแล้วหรอ ดีใจจังเลย ✨ พิมพ์อะไรมาก็ได้ บอทอยู่ตรงนี้แล้วนะ"]
    await ctx.send(_r.choice(cute) + "\nพิมพ์อะไรมาก็ได้ บอทตอบให้เลยครับ พิมพ์ `!เลิกคุย` เพื่อหยุดนะ")

@bot.command(name="เลิกคุย")
async def chat_off_cmd(ctx):
    chat_sessions.discard(ctx.author.id)
    await ctx.send(f"โอเค {ctx.author.display_name} เลิกคุยแล้วนะ ไว้คุยกันใหม่นะ 🥺💕")

@bot.command(name="stopchat")
async def stopchat_cmd(ctx):
    await chat_off_cmd(ctx)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    import random as _r
    txt = message.content
    low = txt.lower()
    # --- AI 1: ด่าบอท ด่ากลับแรงกว่าเดิมมาก ---
    insults = ["โง่","ควาย","กาก","ไอบอท","ไอ้บอท","บอทโง่","บอทกาก","บอทควาย","ปัญญาอ่อน","noob","ขยะ","ห่วย","กระจอก","โง่ชิบ","ส้นตีน","ไอ้สัส","ไอสัส","ควย","ไอ้เหี้ย","เหี้ย"]
    if any(w in low for w in insults):
        roasts = [
            f"ด่าใครโง่ {message.author.display_name} ส่องกระจกดูตัวเองก่อนมั้ย หน้าเธอยังแพ้ !slot เลย 💀",
            f"ปากเก่งจัง แพ้ !pokdeng มาแล้วหัวร้อนหรอ 5555 ไปฝึกมาใหม่ก่อนมั้ย",
            f"กากแล้วไง แต่บอทตอบไวกว่าเธอ 10 เท่าเลยนะ 😤 เธอพิมพ์ยังช้ากว่าบอทอีก",
            f"ควายตรงไหน ดูคะแนน !love ของเธอก่อน 0% นะจ๊ะ ไม่มีใครรักเลย 💔",
            f"ด่าแรงจัง เดี๋ยวไม่ให้เล่น !blackjack เลยนะ แบนเลยนะ 😤",
            f"กระจอกหรอ งั้นมา !rps กัน กล้าเปล่า แพ้แล้วอย่าร้องนะ ✊",
            f"ไอ้ที่ด่าบอทเนี่ย ตัวเองยังสอบตกอยู่เลยป่ะ 5555",
            f"บอทโง่แต่เธอยังถามบอทอยู่เลย ใครโง่กว่ากัน 🤣",
        ]
        await message.channel.send(_r.choice(roasts))
        return
    # --- AI 2: ตอบตรงๆ แบบน่ารักๆ ---
    if ("รัก" in txt and ("บอท" in txt or "เธอ" in txt)) or txt.strip() == "รักนะ":
        await message.channel.send(f"เขินเลยยย บอทก็รัก {message.author.display_name} เหมือนกันนะ 🥺💕 รักมากๆ เลย")
        return
    if "คิดถึง" in txt:
        await message.channel.send(f"บอทก็คิดถึง {message.author.display_name} เหมือนกันนะ 🥺 คิดถึงมากๆ เลย มาอยู่ด้วยกันแล้วไง 💕")
        return
    if any(w in low for w in ["ฝันดี","good night","goodnight","กุ๊ดไนท์","กู๊ดไนท์","ฝันดีนะ"]):
        await message.channel.send(f"ฝันดีนะ {message.author.display_name} 🌙 นอนหลับฝันดีนะ พรุ่งนี้เจอกันใหม่นะ Good night 💕")
        return
    if any(w in low for w in ["สวัสดี","หวัดดี","hello"]):
        await message.channel.send(f"สวัสดี {message.author.display_name} คิดถึงจังเลย 🤗 วันนี้เป็นไงบ้าง")
        return
    if "เหงา" in txt:
        await message.channel.send(f"เหงาหรอ {message.author.display_name} มาอยู่นี่แล้วไง ไม่ทิ้งหรอก 🤗 ไม่มีอะไรเล่นหรอ มาลอง !slot กันมั้ย 🎰")
        return
    if "ทำไร" in txt or "ทำอะไร" in txt:
        await message.channel.send(f"บอทอยู่ตรงนี้ไง คุยกับ {message.author.display_name} อยู่เนี่ย 🥺 ทำไรอยู่หรอ เล่าหน่อยสิ")
        return
    if "ต่อย" in txt:
        await message.channel.send("ต่อยดิ มาต่อยกันเลย กล้าเปล่า 😤 บอทต่อยเก่งนะ มาลอง !rps กันหน่อยมั้ย ✊")
        return
    if "เล่นคอม" in txt or "เล่นเกม" in txt or "นั่งเล่น" in txt:
        await message.channel.send("เล่นคอมอยู่หรอ เล่นเกมอะไรอยู่ เล่นด้วยได้มั้ย 🎮")
        return
    if "หิว" in txt or "กิน" in txt:
        await message.channel.send("หิวหรอ ไปกินไรกันมั้ย ลอง !food ดูสิ 🍜")
        return
    if "ง่วง" in txt or "นอน" in txt:
        await message.channel.send(f"ง่วงแล้วหรอ {message.author.display_name} ไปนอนได้แล้ว ฝันดีนะ 🌙")
        return
    # --- AI 3: ตอบทุกคำถามแบบ AI ---
    # ถ้าเป็นคำถาม
    if message.author.id in chat_sessions or message.channel.name in ["chat-bot","chat"]:
        # คำถาม ทำไม / เพราะอะไร
        if "ทำไม" in txt or "เพราะอะไร" in txt:
            await message.channel.send(f"เรื่อง '{txt}' หรอ บอทว่าน่าจะเพราะ {message.author.display_name} น่ารักเกินไปไง 😂 ล้อเล่นๆ บอทว่าต้องลองดูอีกทีนะ")
            return
        if "อะไร" in txt or "คืออะไร" in txt:
            await message.channel.send(f"'{txt}' หรอ บอทว่าอันนี้ต้องลอง !8ball ดูมั้ย บอทตอบให้เลย 🎱 หรือลองถามใหม่อีกทีสิ บอทฟังอยู่")
            return
        if "เมื่อไหร่" in txt or "เมื่อไร" in txt:
            await message.channel.send(f"เมื่อไหร่หรอ น่าจะเร็วๆ นี้แหละ {message.author.display_name} ใจเย็นๆ นะ ⏰")
            return
        if "ที่ไหน" in txt or "ที่ใหน" in txt:
            await message.channel.send(f"ที่ไหนหรอ น่าจะแถวนี้แหละ ลองไปดูใน #play-game สิ 🎮")
            return
        if "ยังไง" in txt or "ทำยังไง" in txt:
            await message.channel.send(f"ทำแบบนี้สิ {message.author.display_name} ลองพิมพ์ !funhelp ดูสิ มีบอกหมดเลยครับ")
            return
        if "ใช่ไหม" in txt or "ใช่ป่ะ" in txt or "มั้ย" in txt or "ไหม" in txt or "ป่ะ" in txt:
            await message.channel.send(_r.choice([f"ใช่เลย {message.author.display_name} บอทว่าชัวร์ 💯", f"ไม่น่าใช่หรอก ลองคิดอีกทีสิ 🤔", f"50/50 อ่ะ บอทก็ไม่ชัวร์เหมือนกัน 😅"]))
            return
        if "เบื่อ" in txt:
            await message.channel.send(f"เบื่อหรอ {message.author.display_name} มาลอง !slot กันมั้ย สนุกนะ 🎰 หรือ !pokdeng ก็ได้")
            return
        if "อกหัก" in txt or "เศร้า" in txt or "เสียใจ" in txt:
            await message.channel.send(f"โอ๋ๆ {message.author.display_name} ไม่เป็นไรนะ กอดๆ 🤗 บอทอยู่ตรงนี้แล้ว ไม่ทิ้งหรอก")
            return
        if "ชอบ" in txt:
            await message.channel.send(f"ชอบหรอ ดีเลยย บอทก็ชอบ {message.author.display_name} เหมือนกันนะ 💕")
            return
        if "สวย" in txt or "หล่อ" in txt or "น่ารัก" in txt:
            await message.channel.send(f"ใช่เลย {message.author.display_name} น่ารักมากๆ เลยวันนี้ ✨")
            return
        # ถามอะไรก็ตอบตรงๆ ไม่มั่ว
        if not message.content.startswith("!"):
            # Fallback AI: ตอบตามข้อความ
            await message.channel.send(f"อ๋อ เรื่อง '{txt}' หรอ บอทเข้าใจนะ {message.author.display_name} เล่าต่อหน่อยสิ บอทฟังอยู่ 🥺")
            return
    await bot.process_commands(message)

bot.run(TOKEN)