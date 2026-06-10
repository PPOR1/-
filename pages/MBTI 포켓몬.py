import streamlit as st

# 페이지 설정
st.set_page_config(page_title="나의 소울 포켓몬 찾기! 🎮", page_icon="⭐", layout="centered")

# 타이틀 및 소개
st.title(" 몬스터볼 속 내 소울 포켓몬은? ")
st.subheader("내 MBTI를 선택하면 찰떡궁합인 포켓몬과 성격을 알려줄게! 😎")
st.markdown("---")

# MBTI별 포켓몬 데이터 (이미지는 포켓몬 공식 도감 이미지 URL 사용)
pokemon_data = {
    "ISTJ": {
        "name": "메타그로스 (Metagross) 🤖",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/376.png",
        "desc": "4개의 뇌로 컴퓨터보다 빠른 계산을 하는 메타그로스! 정확하고 원칙을 중요시하며, 한 번 맡은 일은 끝까지 책임지는 너의 진중한 모습과 똑 닮았어. 조용하지만 엄청난 능력을 숨겨둔 능력자 스타일이야."
    },
    "ISFJ": {
        "name": "럭키 (Chansey) 🥚",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/113.png",
        "desc": "다친 포켓몬을 보면 그냥 지나치지 못하고 영양 가득한 알을 나눠주는 럭키! 주변 사람들을 세심하게 챙기고 위로해 주는 따뜻한 마음씨를 가진 너는 모두가 곁에 두고 싶어 하는 최고의 천사야."
    },
    "INFJ": {
        "name": "에브이 (Espeon) 🔮",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/196.png",
        "desc": "공기의 흐름을 읽어 상대방의 기분과 미래를 예측하는 에브이! 통찰력이 깊고 조용하면서도 내면의 신념이 뚜렷한 너의 모습과 닮았어. 남들은 잘 모르는 깊은 속내와 예술적인 감수성을 가졌지."
    },
    "INTJ": {
        "name": "앱솔 (Absol) 📐",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/359.png",
        "desc": "오해를 받더라도 묵묵히 재난을 예견하고 사람들을 도우려는 앱솔! 날카로운 분석력과 전략적인 두뇌를 가진 너처럼, 독립적이고 미래를 내다보는 눈이 탁월해. 완벽주의자 성향이 매력적이야."
    },
    "ISTP": {
        "name": "개굴닌자 (Greninja) 🥷",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/658.png",
        "desc": "민첩하고 냉철하게 상황을 판단해서 해결하는 개굴닌자! 말보다는 행동으로 보여주는 스타일이지? 손재주가 좋거나 도구를 다루는 데 능숙하고, 위기 상황에서도 당황하지 않는 쿨한 매력의 소유자야."
    },
    "ISFP": {
        "name": "메타몽 (Ditto) 🍮",
        "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/132.png",
        "desc": "어떤 포켓몬이든 똑같이 변신할 수 있는 말랑말랑 메타몽! 주변 환경에 유연하게 적응하고 사람들의 의견을 잘 맞춰주는 평화주의자야. 예술적 감각이 뛰어나고 자유를 사랑하는 따뜻한 영혼이지."
    },
    "INFP": {
        "name": "따라큐 (Mimikyu) 🧸",
        "img": "https://assets.pokemon
