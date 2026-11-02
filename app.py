import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="معركة 3D طراز جيتياي", page_icon="🎮", layout="centered")

st.markdown("<style>.stApp { background-color: #FAEDCD !important; } h1, p, .stMarkdown { color: #3D3025 !important; }</style>", unsafe_allow_html=True)
st.title("🎮 معركة الأبطال 3D (منظور جيتياي) 🎮")
st.write("✨ **تحديث أسطوري:** محرك ثلاثي الأبعاد كامل وسط الصفحة! اضغط لمشاهدة تأثيرات الحركة الواقعية! 🚀")

try:
    with open("game.html", "r", encoding="utf-8") as f:
        game_html = f.read()
    components.html(game_html, height=620)
except:
    st.error("عفاك صاوب ملف سميتو game.html وحط فيه كود اللعبة!")

st.markdown("---")
st.write("📢 واولاد لقحإشهار لدعم المبرمج الصغير:**")
startio_ad_html = """
<div style="display: flex; justify-content: center; align-items: center; min-height: 100px;">
    <script type="text/javascript" src="https://start.io"></script>
    <script type="text/javascript">
        startio.init("124299136");
        startio.createBanner({ container: document.body, width: 320, height: 50 });
    </script>
</div>
"""
components.html(startio_ad_html, height=120)
