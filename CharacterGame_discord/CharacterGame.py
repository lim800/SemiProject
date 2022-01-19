from sqlite3 import Timestamp
import discord, asyncio, datetime, pytz, random

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)





chlist = ["뽀로로","둘리","마시마로","안젤리나 졸리", "오드리 헵번", "다코타 패닝", "제시카 알바", "스칼렛 요한슨", "톰 행크스", "브래드 피트", "이소룡", "찰리 채플린", "한효주", "한가인", "한예슬", "엄정화", "임수정",\
    "손예진", "김혜수", "김하늘(여)", "이광수", "장동건", "조승우", "조인성", "최민식", "권상우", "강남길", "류준열" , "류승범", "배용준", "최지우", "송승헌",\
        "이순신", "펭수", "호머 심슨", "미키마우스", "미니마우스", "용가리", "고질라", "도라에몽", "알라딘", "지니(애니)", "자스민", "피카츄", "파이리", "꼬부기", "피노키오", "뚱이(스폰지밥)", "스폰지밥",\
            "라바", "마리오", "리마리오", "헬로키티", "홍콩할매", "프랑켄슈타인", "짱구", "무민", "스누피", "그루트", "아이언맨", "토르", "헐크", "캡틴아메리카", "블랙위도우",\
                "스파이더맨", "배트맨", "슈퍼맨", "라이언(카카오)", "무지(카카오)", "닉퓨리", "산타클로스", "루돌프", "신데렐라", "백설공주", "라푼젤", \
                    "아톰", "소닉", "코코몽", "모아나", "드라큘라", "요술공주밍키", "세일러문", "토토로", "라바", "뽀빠이", "후뢰쉬맨", "잭스페로우", "버즈(토이스토리)", "우디(토이스토리)",\
                        "모나리자", "곰돌이푸", "미니언즈", "쿵푸팬더", "도날드덕", "스머프", "가가멜", "팅커벨", "피터팬", "구피(디즈니)", "스티치(디즈니)", "뮬란", "포카혼타스", "보라돌이(텔레토비)", "뚜비(텔레토비)",\
                            "베토벤", "나이팅게일", "잔다르크", "나폴레옹", "칭기즈칸", "비틀즈", "엘비스 프레슬리", "월트 디즈니", "피카소", "아인슈타인", "파티고라스", "뉴턴", \
                                "세익스피어", "콜럼버스", "레오나르도 다빈치", "에디슨", "히틀러", "간디", "트럼프", "오바마", "빌 게이츠", "일론머스크", "장영실", "김두한", "시라소니", "홍길동", "임꺽정", "로빈후드", \
                                    "파브르", "방탄소년단", "나훈아", "혜민스님", "손흥민", "메시", "크리스티아누 호날두", "박지성", "류현진", "김정은", "김연경", "이재용", \
                                        "윤여정", "강형욱", "백종원", "유재석", "김종국", "박보검", "임영응", "박막례 할머니", "바이든", "GD", "신동엽", "홍석천", "설민석", "설현",\
                                            "조세호", "강호동", "이영지", "블랙핑크", "안영미", "한소희", "김희철", "아이유", "유희열", "옥동자", "허경영", "장나라", "마이클잭슨", "KCM",\
                                                "마동석", "프레디 머큐리", "김연아", "양현석", "서태지", "차범근", "송가인", "트와이스", "EXO", "셜록홈즈",\
                                                    "김전일", "코난", "호크아이", "로키", "타노스"]

players = []
playerId = []


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!help"))
async def my_background_task():
    
    await client.wait_until_ready()

@client.event
async def on_message(message):
    global players, chlist, playerId
    
    if message.content == "!help":
        embed2 = discord.Embed(title= "게임설명", description="상대방에게 적절한 질문을 해서 자신과 매치된 캐릭터 이름을 먼저 맞추면 즐거운 게임", color=0x00ff00)
        embed = discord.Embed(title= "명령어 목록", description="!join: 자신을 참가자 목록에 추가 \n\n!out: 자신을 참가자 목록에서 제외 \n\n!list: 현재 참가자 목록을 출력 \n\n!start: 참가자들에게 캐릭터목록 전달 \n\n!end: 참가자 목록을 비우고 게임을 끝냄", timestamp=datetime.datetime.now(pytz.timezone('US/Pacific')), color=0x00ff00)
        await message.channel.send (embed=embed2)
        await message.channel.send (embed=embed)

    if message.content == "!join":
        if message.author.name in players:
            embed = discord.Embed(description="이미 등록됨", color=0x00ff00)
            await message.channel.send (embed=embed)
        else:
            embed = discord.Embed(description="{} 확인!".format(message.author.name), color=0x00ff00)
            await message.channel.send (embed=embed)
            players.append(message.author.name)            
            playerId.append(message.author.id)

    if message.content == "!out":
        if message.author.name in players:
            players.remove(message.author.name)
            playerID.remove(message.author.id)
            embed = discord.Embed(description="{} 제외됨".format(message.author.name), color=0x00ff00)
            await message.channel.send (embed=embed)
        else:
            embed = discord.Embed(description="목록에 존재하지 않음", color=0x00ff00)
            await message.channel.send (embed=embed)
    
    if message.content == "!list":
        if len(players) == 0:
            embed = discord.Embed(description="참가자가 1도 없음", color=0x00ff00)
            await message.channel.send (embed=embed)
        else:
            playlist = ""
            for i in players:
                playlist = playlist + i + "  "            
            embed = discord.Embed(description="{}명 참가: {}".format(len(players), playlist), color=0x00ff00)
            await message.channel.send (embed=embed)

    if message.content == "!end":
        players = []
        await message.channel.send ("게임 끝!")

    if message.content == "!start":
        playerdic = {}
        for i in range(0,len(players)):
            n = random.randint(0,len(chlist))
            playerdic[players[i]]=chlist[n]

        for index, i in enumerate(players):
            embed = discord.Embed(title= "Character List", timestamp=datetime.datetime.now(pytz.timezone('US/Pacific')), color=0xddff00)        
            for key, value in playerdic.items():
                if i == key:
                    continue
                else:
                    embed.add_field(name="{} ".format(key), value="{}".format(value), inline=False)                 
                embed.set_footer(icon_url="https://img.extmovie.com/files/attach/images/135/534/451/049/1c01894bb88088392ab19c88ffd6cd64.jpeg")
            await client.wait_until_ready()
            user = client.get_user(playerId[index])            
            await user.send(embed=embed)

        embed2 = discord.Embed(description="캐릭터 전송 완료!", color=0x00ff00)
        await message.channel.send(embed=embed2)

    if message.content == "!test":
        await client.wait_until_ready()
        ch = client.get_user(int(84815145758388224))      
        await ch.send("test")

client.loop.create_task(my_background_task())
client.run('OTMzMTg4NzY1NTM3NjY5MjIw.Yed5ww.zQtGQp38omhTa4iqEv6UFihnRi0')