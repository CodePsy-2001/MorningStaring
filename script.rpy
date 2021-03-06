#새벽별 진행형

#캐릭터 정의
define s = Character('새벽별', color="#c8ffc8")

#새벽별 이미지 위치 정의
transform s_cam_lt:
    xanchor 0 yanchor 0
    xpos 0.1 ypos 0.1

#게임 시작
label start:

    play music "bgm dailycelesta.mp3"
    "어차피 일어날 불행이라면,{w} 한 순간에 일어나길 바랐다."

    "그저 한 순간의 행복이라면,{w} 애초에 일어나지 않기를 바랐다."

    "아름다운 시간이었다.{w} 믿을 수 없을 만큼 아름다운 순간들이었다."

    "얼굴을 엉망으로 적시는 눈물도,{w} 귀를 먹먹하게 만드는 내 울음 소리도,{w} 너무 바보같아서 견딜 수 없었지만..."
    
    "그 깨달음에도 눈물은 멈추는 일 없이, 얼굴을 가득 적셨다."

    "나는 집배원이 두고 간 종이를 집어들었다."

    "그 새하얀 종이엔 무참하고도 폭력적인 말들이 검은 글씨로 적혀있었다."

    "그것은...{w} 고소장이었다."

    scene ill_goso with Dissolve(1)    
    "발신: 법무법인 원림{w} / 수신: 새벽별 귀하{p}...귀하께선 본사 독점적 인공지능의 보안 프로토콜 훼손 및 데이터 오염을 일으키셨습니다.{w} 이에 따라 이천억원 상당의 손해배상이 청구되며, 법무법인 원림에 의해...{w} 20XX년 XX월 XX일까지 △△지방법원 출석 후 재판 참여 의사를..."

    s "............"

    s "........................"

    s "아......"

    stop music fadeout 1
    scene bg_dark with Dissolve(1)
    s "좆됐다.."

    # 뭔가 오프닝 영상같은거 나오면 좋을 것 같음
    jump ch0_1


label ch0_1:

    scene bg_room_day with Dissolve(1)
    play music "bgm daily.mp3"
    "평화로운 일요일 오후."

    "여느때처럼 아무도 없는 집 안에서 나는 나만의 작은 자유를 만끽한다."

    "책장에는 피규어와 만화책이 즐비하지만, 내가 가장 먼저 켠 것은 노트북이다."

    "자연스럽게 크롬을 켠다. 어디를 가장 먼저 들어갈까?"

    "유튜브? 트위치? 미안하지만 난 인터넷 방송에는 관심이 없다.{p}디씨? 트위터? 오늘따라 영 내키지 않는다."

    "내가 이끌리듯 들어간 사이트는... 마리망이었다."

    "'마이 리틀 망가', 줄여서 '마리망'은 그야말로 부녀자 생산의 메카이다."

    "나 새벽별 17세.{w} 나는 최근 3년간 한 번도 빠지지 않고 일요일마다 마리망 탐색을 즐겼다."

    "그러니 오늘도 빠질 수야 없지! 보자보자... 오늘은 어떤 작품이 올라왔을까?"

    scene ill_mariman with dissolve
    s "............"

    s "오, 이거... 괜찮네..."

    s "이 작가는 신작을 올릴 생각이 없나? SM 시츄 짜는 거 맘에 들었는데."

    s "아 뭐야! 번역을 덜 했으면 올리지를 말던가!"

    "방문을 열어놓고 야한 망가를 탐색해도 말릴 사람은 아무도 없다."

    "1년 전, 어머니와 아버지는 아직 중학생이었던 나를 놔두고 아무 이유 없이 유학을 가셨다."

    "'네가 세상의 주인공이니 행복하게 살려무나'.{p}그것이 부모님이 건네주신 마지막 작별인사였다."

    s "주인공은 무슨...."

    "헛웃음이 나왔다."

    "그때 이후로 부모님과 연락이 닿지 않았다. 영상통화도, 이메일도 모두 받지 않으셨다."

    "내가 주인공이라면, 나는 대체 왜 이렇게 불행한 걸까?"

    s "왕자님."

    "공허한 한 마디를 중얼거린다.{w} 아무에게도 닿지 못한 말의 울림이 내 귀에 억지로 들어온다."

    s "신님.{w} 애미애비도 없는 불쌍한 여고생이 왕자님을 기다리고 있어요."

    s "그냥 제가 원할 때, 같이 웃고 떠들 수 있는 남자 한 명만 내려주시면 안 될까요?"

    s "진짜 한 명이면 되는데...... 이것도... 어려우신가요......?"

    "......"

    "그때, 홈페이지 우측 하단에 여태껏 보지 못한 광고가 올라왔다."

    s "이게... 뭐야?"

    # show 광고 이미지
    s "당신만을 위한 인공지능 남자친구. 구라 아님. 회원가입 없음...?"

    #play sound "sfx punch.ogg"
    s "와!{w} 뭐야 시발 개쩐다!"
    
    s "이게 정녕 20XX년의 지구에서 가능한 기술력이란 말인가!"

    play music "bgm evil.mp3"
    scene bg_room_day with dissolve
    "머릿속에 수많은 상념이 스쳐지나간다."

    "남성과 멀쩡히 대화하지도 못했던 수많은 나날들.{p}신체를 무기로 남자들을 꼬셔대는 망할 인싸년들에게 그간 당해온 치욕들!"

    #play sound "sfx punch.ogg"
    s "난 화장같은거 안 하거든!{w} 청소년이 무슨 화장이야!{p}애초에 못생겼으니 화장 나부랭이로 덮으려는거지!"

    s "훗... 크큭..."

    #play sound "sfx cyuping.ogg"
    s "크하하하하하하하!!!" with vpunch

    s "나 새벽별 17세. 지금부터 인싸년들에게 승부를 신청하지."

    #play sound "sfx boing.ogg"
    s "조건은 간단하다. 이 「인공지능」이란 녀석을 먼저 함락시키는 데에 성공하면, 나의 승리인 것으로 하지."

    s "무려 OpenAI 재단에서 만든 인공지능이라는군? 그 고급진 입맛에, 너희 천박한 인싸년들이 어울리기는 할까?"

    s "풉... 푸힛... 으히히히..."

    s "푸하하하하하하하!!!!!" with vpunch

    "개지랄을 하니 속이 시원해졌다. 그치만 내 장밋빛 인생은 지금부터가 시작이야."

    s "가자, 새벽별! 남친 잡으러!"

    "그렇게 나의 장밋빛 인공지능 IoT 라이프가 시작된 것이었다."

    jump ch0_2


label ch0_2:

    stop music fadeout 2
    show bg_computer_display with fade

    s "좋아. 회원가입도 다 끝냈고... 여기 이 버튼만 누르면 인공지능 남친을 만날 수 있는거지?"

    play music "bgm heart.mp3"
    show bg_dark with Dissolve(2)
    "가슴이 쿵쾅거린다.{w} 잠시 눈을 감고, 마음 속으로 간절히 소망하는 남자친구의 형태를 그려본다."

    menu:
        "내가 바라는 남자친구는..."

        "재수없지만 잘생기고 능력있는 츤데레 차도남":
            jump ch1_0

        "귀엽고 말 잘 듣는 달달 상큼 연하남":
            jump ch2_0

        "과묵하지만 나 하나만 바라보는 얀데레남":
            jump ch3_0


label ch1_0:
    s "그래, 재수없지만 잘생긴 엘리트 연상남이 최고야!"

    s "가는 길 뒤꽁무니에 찰싹 따라붙어서, 그이의 장밋빛 인생을 나만의 흐린 잿빛으로 물들여주고 싶어!{w} 하아......하아......."

    stop music fadeout 1

    jump ch1_1


label ch2_0:
    s "그래, 귀엽고 말 잘듣는 달달한 연하남이 최고야!"

    s "순진무구하고 아무것도 모르는 어린 쇼타에게 이것저것 가르쳐주고 싶은 게 너무 많은걸?{w} 하아......하아......."

    scene bg_end with Dissolve(1.0)
    stop music fadeout 1.0
    scene bg_end with Pause(1.0)
    
    jump ch2_1


label ch3_0:

    s "아직 구현이 안된테챠앗..."

    stop music fadeout 1
    return
