import discord
import asyncio
from captcha.image import ImageCaptcha
import random
import re
import openpyxl
import datetime
import requests
import openpyxl
from json import loads
import os








client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    print('작동을 시작합니다')
    print(client.user.name)
    print(client.user.id)
    
    
    


@client.event
async def on_message(message):
    
    
    
    if message.content.startswith("잘가"):
        await message.channel.send("ㅃ2")

    if message.content.startswith("같이"):
        await message.channel.send("저도요?")

    if message.content.startswith("아니"):
        await message.channel.send("네.....")

    if message.content.startswith("아니"):
        await message.channel.send()
    

    if message.content.startswith("DM"):
        author = message.guild.get_member(int(message.mentions[0].id))
        msg = message.content[23:]

        await author.send(msg)
        await message.delete()
        await message.channel.send("보냄")
        

    if message.content.startswith("글자 맞추기"):
        image_capcha = ImageCaptcha()
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        image_capcha.write(a, name)

        await message.channel.send(file=discord.File(name))


    if message.content.startswith("20070731"):
        await message.channel.send("https://cdn.discordapp.com/attachments/634011516462694420/684367431560593438/20200303_204856.jpg")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("시간초과입니다")
            return

        if msg.content == a:
            await message.channel.send("정답입니다.")
        else:
            await message.channel.send("틀렸습니다.")



    

    if message.content == "하이":
        rand = random.randint(1, 10)
        if rand == 1:
            await message.channel.send('왜')
        if rand == 2:
            await message.channel.send('뭐')
        if rand == 3:
            await message.channel.send('뭐라고 해야돼죠?')
        if rand == 4:
            await message.channel.send('예?!')
        if rand == 5:
            await message.channel.send('뭐가요')
        if rand == 6:
            await message.channel.send('저 아세요?')
        if rand == 7:
            await message.channel.send('.......?')
        if rand == 8:
            await message.channel.send('말 안할레요')
        if rand == 9:
            await message.channel.send('안녕하세요')
        if rand == 10:
            await message.channel.send('어쩌라고요')
    

    if message.content.startswith("배그"):
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(683281911191306316))
        await message.delete()
    if message.content.startswith("레식"):
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await message.delete()
    if message.content.startswith("옵치"):
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(683180832617529355))
        await message.delete()
    if message.content.startswith("히오스"):
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(683963334495698948))
        await message.delete()
    if message.content.startswith("즐겜방"):
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721881839534295))
        await message.delete()
    
    if message.content.startswith("롤러코스트"):
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
    
    
    
    
    if message.content.startswith("무작위롤코"):
        go = message.content.split(" ")
        rand = random.randint(1, len(go)-1)
        choiceresult = go[rand]
        await message.channel.send(f"{choiceresult}님이 당첨되셨어요")
        userid = choiceresult.id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)






    if message.content.startswith("아무거나"):
        go = message.content.split(" ")
        rand = random.randint(1, len(go)-1)
        choiceresult = go[rand]
        await message.channel.send(f"{choiceresult}")
            


    if message.content == "팀":
        rand = random.randint(1, 2)
        userid = message.author.id
        if rand == 1:
            await message.channel.send('팀 1')
            await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        if rand == 2:
            await message.channel.send('팀 2')
            await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))



    if message.content.startswith("봇소개"):
        embed = discord.Embed(title="봇소개를 할게요" ,description=f"사용 설명서 \n\n\n \n 봇소개 -- 봇을 소개합니다 \n \n \n하이 -- 랜덤으로 대답을 합니다 \n \n \n(음성채널 이름) -- 그 채널로 이동합니다  \n \n \n팀 -- 팀1,팀2 중 무작위로 골라 그 채널로 이동합니다 \n \n \n랜덤 <시작 숫자>~<끝 숫자> -- 시작 숫자와 끝 숫자 중 무작위로 하나를 고릅니다 \n \n \n",color=0xcccccc)
        embed.set_footer(text = "끝!!!!!!") 
        embed.set_image(url=client.user.avatar_url)
        await message.channel.send(message.channel, embed=embed)


        
    if message.content.startswith('투표'):
        votetitle = message.content[3:]
        embed = discord.Embed(title = f"{votetitle}")
        msg = await message.channel.send(embed = embed)
        await msg.add_reaction('⭕')
        await msg.add_reaction('❌')
        


        
    if message.content.startswith("건의사항"):
        gesh = message.content[5:]
        geshmember = message.guild.get_member(int(492645332908507137))
        embed = discord.Embed(title = f"{message.author}님이 건의사항을 추가하였습니다",description=f"{gesh}라고 건의했습니다")
        await geshmember.send(embed=embed)
        await message.delete()
        



        

    if message.content.startswith("사진"):
        embed = discord.Embed()
        file = discord.File("./image.png", "image.png")
        embed.title = "테스트"
        embed.set_image(url="attachment://image.png")
        embed.set_thumbnail(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)
        


    



    if message.content.startswith('랜덤'):
        rcount = re.findall('\d+', message.content)
        await message.channel.send(f':game_die:{str(random.randint(int(rcount[0]), int(rcount[1])))}')


    


    if '씨발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '시발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'TLqkf' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'tlqkf' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'fuck' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'Fuck' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '느금마' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '니얼굴' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '새끼' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '좆' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'NIGGA' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if 'nigga' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if '섹스' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if 'BITCH' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if '병신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '쎅스' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '쎽스' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨12발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨1발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '섹12스' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '븅신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '뼝신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '좆' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '쓰벌' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨벌' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨이발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '스발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '스벌' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()


    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    
    
    
    if message.content.startswith("야동"):
        await message.channel.send("http://www.smpa.go.kr/home/homeIndex.do?menuCode=www")
        await message.delete()


    if message.content.startswith("diehdfd"):
        await message.channel.send("http://size99.com/")
        await message.delete()



    if message.content.startswith("안수현 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683294645458960385/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1582977669143.jpeg")
    if message.content.startswith("박재우 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683294552823824404/1562920039212.jpg")
    if message.content.startswith("공유현 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683295199983828992/fasdfafsd.PNG")
    if message.content.startswith("이지호 얼굴"):
        await message.channel.send("금지")
    if message.content.startswith("김규현 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683295924877131827/sdfasdfdafs.PNG")
    if message.content.startswith("이우린 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683296867798614019/received_186248989355530.jpeg")
    if message.content.startswith("김유석 얼굴"):
        await message.channel.send("안돼")
    if message.content.startswith("강준서 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/682938772085932055/683870359090364540/sadffasdasfdafsdfadsasdfasfdasfd.jpg")



   
    if message.content.startswith("핑"):
        ping = client.latency
        await message.channel.send(f'현재 핑은 {ping}ms 입니다')
   
   
   
   
   
    if '시간' in message.content:
        now = datetime.datetime.now()
        
        await message.channel.send(f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 입니다')



    elif message.content.startswith('내정보'):
        roles=[role for role in message.author.roles]
        embed=discord.Embed(colour=message.author.color, timestamp=message.created_at)
        embed.set_author(name=f"유저정보 - {message.author}")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        embed.add_field(name="아이디", value=message.author.id)
        embed.add_field(name="닉네임", value=message.author.display_name)
        embed.add_field(name="계정 생성 시간", value=message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="가입 시간", value=message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="가장 높은 역할", value=message.author.top_role.mention)
        embed.add_field(name="봇", value=message.author.bot)
        await message.channel.send(embed=embed)





    if message.content.startswith("가위바위보"):
        rand = random.randint(1, 3)
        result = message.content[6:]
        
        if rand == 1:
            await message.channel.send(":v: 가위")
            if result == ("보"):
                await message.channel.send(":worried: 제가 졌네요")
            if result == ("바위"):
                await message.channel.send(":grin: 제가 이겼네요")
            if result == ("가위"):
                await message.channel.send(":neutral_face: 저랑 비겼네요")
        
        if rand == 2:
            await message.channel.send(":fist: 바위")
            if result == ("보"):
                await message.channel.send(":worried: 제가 졌네요")
            if result == ("바위"):
                await message.channel.send(":neutral_face: 저랑 비겼네요")
            if result == ("가위"):
                await message.channel.send(":grin: 제가 이겼네요")
       
        if rand == 3:
            await message.channel.send(":hand_splayed: 보")
            if result == ("보"):
                await message.channel.send(":neutral_face: 저랑 비겼네요")
            if result == ("바위"):
                await message.channel.send(":grin: 제가 이겼네요")
            if result == ("가위"):
                await message.channel.send(":worried: 제가 졌네요")
        

        
    if message.content.startswith("닉넴"):
        ja = random.randint(1, 14)
        mo = random.randint(1, 12)
        qo = message.content[3:5]
        ja2 = random.randint(1, 14)
        mo2 = random.randint(1, 12)
        qo2 = message.content[6:8]
        qoja = random.randint(1, 14)
        qoja2 = random.randint(1, 14)
        if ja == 1:
            jab = ("ㄱ")
        if ja == 2:
            jab = ("ㄴ")
        if ja == 3:
            jab = ("ㄷ")
        if ja == 4:
            jab = ("라")
        if ja == 5:
            jab = ("ㅁ")
        if ja == 6:
            jab = ("ㅂ")
        if ja == 7:
            jab = ("ㅅ")
        if ja == 8:
            jab = ("ㅇ")
        if ja == 9:
            jab = ("ㅈ")
        if ja == 10:
            jab = ("ㅊ")
        if ja == 11:
            jab = ("ㅋ")
        if ja == 12:
            jab = ("ㅌ")
        if ja == 13:
            jab =  ("ㅍ")
        if ja == 14:
            jab = ("ㅎ")



        
        
        
        
        
        
        
        
        if mo == 1:
            mob = ("ㅏ")
        if mo == 2:
            mob = ("ㅑ")
        if mo == 3:
            mob = ("ㅓ")
        if mo == 4:
            mob = ("ㅕ")
        if mo == 5:
            mob = ("ㅗ")
        if mo == 6:
            mob = ("ㅛ")
        if mo == 7:
            mob = ("ㅜ")
        if mo == 8:
            mob = ("ㅠ")
        if mo == 9:
            mob = ("ㅡ")
        if mo == 10:
            mob = ("ㅣ")
        if mo == 11:
            mob = ("ㅐ")
        if mo == 12:
            mob = ("ㅔ")
        if mo == 13:
            mob = ("ㅖ")




        if qo == ("받침"):
            if qoja == 1:
                qojab = ("ㄱ")
            if qoja == 2:
                qojab = ("ㄴ")
            if qoja == 3:
                qojab = ("ㄷ")
            if qoja == 4:
                qojab = ("ㄹ")
            if qoja == 5:
                qojab = ("ㅁ")
            if qoja == 6:
                qojab = ("ㅂ")
            if qoja == 7:
                qojab = ("ㅅ")
            if qoja == 8:
                qojab = ("ㅇ")
            if qoja == 9:
                qojab = ("ㅈ")
            if qoja == 10:
                qojab = ("ㅊ")
            if qoja == 11:
                qojab = ("ㅋ")
            if qoja == 12:
                qojab = ("ㅌ")
            if qoja == 13:
                qojab = ("ㅍ")
            if qoja == 14:
                qojab = ("ㅎ")



            

        if ja2 == 1:
            ja2b = ("ㄱ")
        if ja2 == 2:
            ja2b = ("ㄴ")
        if ja2 == 3:
            ja2b = ("ㄷ")
        if ja2 == 4:
            ja2b = ("ㄹ")
        if ja2 == 5:
            ja2b = ("ㅁ")
        if ja2 == 6:
            ja2b = ("ㅂ")
        if ja2 == 7:
            ja2b = ("ㅅ")
        if ja2 == 8:
            ja2b = ("ㅇ")
        if ja2 == 9:
            ja2b = ("ㅈ")
        if ja2 == 10:
            ja2b = ("ㅊ")
        if ja2 == 11:
            ja2b = ("ㅋ")
        if ja2 == 12:
            ja2b = ("ㅌ")
        if ja2 == 13:
            ja2b = ("ㅍ")
        if ja2 == 14:
            ja2b = ("ㅎ")




        if mo2 == 1:
            mo2b = ("ㅏ")
        if mo2 == 2:
            mo2b = ("ㅑ")
        if mo2 == 3:
            mo2b = ("ㅓ")
        if mo2 == 4:
            mo2b = ("ㅕ")
        if mo2 == 5:
            mo2b = ("ㅗ")
        if mo2 == 6:
            mo2b = ("ㅛ")
        if mo2 == 7:
            mo2b = ("ㅜ")
        if mo2 == 8:
            mo2b = ("ㅠ")
        if mo2 == 9:
            mo2b = ("ㅡ")
        if mo2 == 10:
            mo2b = ("ㅣ")
        if mo2 == 11:
            mo2b = ("ㅐ")
        if mo2 == 12:
            mo2b = ("ㅔ")
        if mo2 == 13:
            mo2b = ("ㅖ")


        

        

        if qo2 == ("받침"):
            if qoja2 == 1:
                qoja2b = ("ㄱ")
            if qoja2 == 2:
                qoja2b = ("ㄴ")
            if qoja2 == 3:
                qoja2b = ("ㄷ")
            if qoja2 == 4:
                qoja2b = ("ㄹ")
            if qoja2 == 5:
                qoja2b = ("ㅁ")
            if qoja2 == 6:
                qoja2b = ("ㅂ")
            if qoja2 == 7:
                qoja2b = ("ㅅ")
            if qoja2 == 8:
                qoja2b = ("ㅇ")
            if qoja2 == 9:
                qoja2b = ("ㅈ")
            if qoja2 == 10:
                qoja2b = ("ㅊ")
            if qoja2 == 11:
                qoja2b = ("ㅋ")
            if qoja2 == 12:
                qoja2b = ("ㅌ")
            if qoja2 == 13:
                qoja2b = ("ㅍ")
            if qoja2 == 14:
                qoja2b = ("ㅎ")






        await message.content.send(f'{jab}{mob}{qojab}{ja2b}{mo2b}{qoja2b}')



        
        

    







    if message.content.startswith('명령어추가'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        strsss=message.content.split('명령어추가')[1]
        q=strsss.split("/")[0]
        a=strsss.split("/")[1]
        i = 1
        while sheet["A" + str(i)].value != None:
            i+=1
        sheet["A" + str(i)].value = str(q[1:])
        sheet["B" + str(i)].value = str(a)
        sheet["C" + str(i)].value = str(message.author.id)
        sheet["D" + str(i)].value = str(message.author)
        await message.channel.send("[" + str(q[1:]) + "]라고 말하면 [" + str(a) + "]라고 대답하는 것을 배웠어!")
        file.save("기억.xlsx")
    


    
        

    
    
    
   
    
    
    
      
        
        

access_token = os.environ["bottoken"]
client.run("access_token")
