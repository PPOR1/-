import streamlit as st

# 페이지 설정
st.set_page_config(page_title="나의 소울 포켓몬 찾기! 🎮", page_icon="⭐", layout="centered")

# 타이틀 및 소개
st.title(" 몬스터볼 속 내 소울 포켓몬은? ")
st.subheader("내 MBTI를 선택하면 찰떡궁합인 포켓몬과 성격을 알려줄게! 😎")
st.markdown("---")

# MBTI별 포켓몬 데이터 (PokeAPI 공식 스프라이트 이미지 URL 적용!)
pokemon_data = {
    "ISTJ": {
        "name": "메타그로스 (Metagross) 🤖",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/376.png",
        "desc": "4개의 뇌로 컴퓨터보다 빠른 계산을 하는 메타그로스! 정확하고 원칙을 중요시하며, 한 번 맡은 일은 끝까지 책임지는 너의 진중한 모습과 똑 닮았어. 조용하지만 엄청난 능력을 숨겨둔 능력자 스타일이야."
    },
    "ISFJ": {
        "name": "럭키 (Chansey) 🥚",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
        "desc": "다친 포켓몬을 보면 그냥 지나치지 못하고 영양 가득한 알을 나눠주는 럭키! 주변 사람들을 세심하게 챙기고 위로해 주는 따뜻한 마음씨를 가진 너는 모두가 곁에 두고 싶어 하는 최고의 천사야."
    },
    "INFJ": {
        "name": "에브이 (Espeon) 🔮",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/196.png",
        "desc": "공기의 흐름을 읽어 상대방의 기분과 미래를 예측하는 에브이! 통찰력이 깊고 조용하면서도 내면의 신념이 뚜렷한 너의 모습과 닮았어. 남들은 잘 모르는 깊은 속내와 예술적인 감수성을 가졌지."
    },
    "INTJ": {
        "name": "앱솔 (Absol) 📐",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/359.png",
        "desc": "오해를 받더라도 묵묵히 재난을 예견하고 사람들을 도우려는 앱솔! 날카로운 분석력과 전략적인 두뇌를 가진 너처럼, 독립적이고 미래를 내다보는 눈이 탁월해. 완벽주의자 성향이 매력적이야."
    },
    "ISTP": {
        "name": "개굴닌자 (Greninja) 🥷",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png",
        "desc": "민첩하고 냉철하게 상황을 판단해서 해결하는 개굴닌자! 말보다는 행동으로 보여주는 스타일이지? 손재주가 좋거나 도구를 다루는 데 능숙하고, 위기 상황에서도 당황하지 않는 쿨한 매력의 소유자야."
    },
    "ISFP": {
        "name": "메타몽 (Ditto) 🍮",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
        "desc": "어떤 포켓몬이든 똑같이 변신할 수 있는 말랑말랑 메타몽! 주변 환경에 유연하게 적응하고 사람들의 의견을 잘 맞춰주는 평화주의자야. 예술적 감각이 뛰어나고 자유를 사랑하는 따뜻한 영혼이지."
    },
    "INFP": {
        "name": "따라큐 (Mimikyu) 🧸",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/778.png",
        "desc": "사랑받고 싶어서 피카츄 탈을 쓰고 다니는 수줍은 따라큐! 겉으로는 조용해 보이지만 속마음은 누구보다 따뜻하고 정이 많아. 나만의 깊은 상상 세계가 있고 감수성이 엄청 풍부한 스타일이야."
    },
    "INTP": {
        "name": "후딘 (Alakazam) 🥄",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
        "desc": "뇌가 계속 자라나서 IQ가 5000이나 된다는 천재 후딘! 호기심이 많아서 '왜?'라는 질문을 달고 살며, 논리적인 분석과 아이디어 내는 걸 좋아하지? 복잡한 문제를 풀 때 짜릿함을 느끼는 브레인이야."
    },
    "ESTP": {
        "name": "괴력몬 (Machamp) 💪",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
        "desc": "지치지 않는 체력과 파워로 행동이 먼저 나가는 괴력몬! 생각만 하기보다는 직접 부딪치며 배우는 에너자이저야. 적응력이 만렙이라 어떤 상황이든 유쾌하게 극복하는 현장 중심형 행동파!"
    },
    "ESFP": {
        "name": "이브이 (Eevee) 🦊",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "desc": "무엇으로든 진화할 수 있는 무한 매력과 사랑스러움을 가진 이브이! 어디서나 분위기 메이커 역할을 톡톡히 하는 인간 비타민이야. 새로운 사람, 재밌는 일이라면 눈을 반짝이는 핵인싸 성격이지."
    },
    "ENFP": {
        "name": "뮤 (Mew) 🌟",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
        "desc": "모든 포켓몬의 유전자를 가져 자유자재로 날아다니는 호기심 대장 뮤! 통통 튀는 아이디어와 긍정 파워로 가득 차 있어서 지루할 틈이 없어. 가끔 덤벙대기도 하지만 사랑할 수밖에 없는 자유로운 영혼!"
    },
    "ENTP": {
        "name": "팬텀 (Gengar) 😈",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "desc": "기발한 장난으로 사람들을 깜짝 놀라게 만드는 장난꾸러기 팬텀! 머리 회전이 엄청 빠르고 토론이나 말싸움에서 절대 지지 않는 말재주를 가졌어. 고정관념을 깨부수는 기발한 아이디어 뱅크야."
    },
    "ESTJ": {
        "name": "거북왕 (Blastoise) 🐢",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "desc": "든든한 등껍질과 강력한 물대포로 무리를 듬직하게 이끄는 거북왕! 리더십이 뛰어나고 계획대로 착착 일을 진행하는 대장 스타일이야. 규칙을 잘 지키고 현실 감각이 뛰어나서 조장 맡기 딱 좋은 사람!"
    },
    "ESFJ": {
        "name": "해피너스 (Blissey) 💕",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "desc": "슬퍼하는 포켓몬에게 행복해지는 알을 나눠주는 사랑 넘치는 해피너스! 리액션이 장인급이고 주변 친구들의 기념일이나 소소한 변화를 귀신같이 챙겨줘. 인기가 많고 협동하는 걸 좋아하는 다정한 사람이야."
    },
    "ENFJ": {
        "name": "님피아 (Sylveon) 🎀",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/700.png",
        "desc": "리본 모양 더듬이로 마음을 평온하게 만드는 파동을 보내는 님피아! 정의롭고 카리스마가 있으면서도 다른 사람을 이끄는 따뜻한 리더십이 있어. 친구들의 성장을 진심으로 응원해 주는 멋진 멘토 스타일!"
    },
    "ENTJ": {
        "name": "뮤츠 (Mewtwo) 🔥",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "desc": "압도적인 포스와 카리스마로 전장을 지배하는 전설의 포켓몬 뮤츠! 야망이 크고 목표가 생기면 그 누구보다 효율적이고 강력하게 밀어붙여. 비전을 제시하고 조직을 승리로 이끄는 타고난 보스 스타일이지."
    }
}

# 셀렉트 박스로 MBTI 선택받기
mbti_list = list(pokemon_data.keys())
selected_mbti = st.selectbox("👉 너의 MBTI를 골라봐!", mbti_list)

# 버튼 클릭 시 결과 오픈!
if st.button("🔴 몬스터볼 던지기!!"):
    st.balloons() # 화면에 풍선 팡팡 터지는 효과!
    
    # 선택된 데이터 매칭
    pokemon = pokemon_data[selected_mbti]
    
    # 결과 레이아웃 구성
    st.markdown(f"## ⚡ {selected_mbti}의 소울몬은... 바로 너다! ⚡")
    
    # 2단 레이아웃 (왼쪽: 이미지, 오른쪽: 설명)
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        # PokeAPI 스프라이트 이미지는 크기가 작을 수 있어서 width를 적당히 조절해 출력해!
        st.image(pokemon["img"], width=250)
        
    with col2:
        st.markdown(f"### ✨ {pokemon['name']}")
        st.write(pokemon["desc"])
        
    st.success(f"💡 이미지 주소 변경 완료! 깔끔한 도감 도트 이미지로 멋지게 작동할 거야! 🐾")
