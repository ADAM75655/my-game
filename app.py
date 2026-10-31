import streamlit as st
import random
import time
import os
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="لعبة النرد 3D التفاعلية", page_icon="🎲", layout="centered")

# تغيير لون الشاشة للون سومو فاتح
st.markdown("""
    <style>
        .stApp { background-color: #FAEDCD !important; }
        h1, h3, p, label, .stMarkdown { color: #3D3025 !important; }
        .stTextInput input { background-color: #FFFFFF !important; color: #3D3025 !important; border: 2px solid #D4A373 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🎲 تحدي لعبة النرد 3D التفاعلية!")
st.write("✨ **ميزة جديدة:** اضغط ديريكت على النرد وسط المربع الكبير باش يدور ويتبدل! 👋")

LEADERBOARD_FILE = "leaderboard.txt"

def قراءة_المتصدرين():
    scores = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "," in line:
                    name, score = line.strip().split(",")
                    scores.append((name, int(score)))
    scores.sort(key=lambda x: x, reverse=True)
    return scores[:5]

def حفظ_متصدر_جديد(name, score):
    scores = قراءة_المتصدرين()
    scores.append((name, score))
    scores.sort(key=lambda x: x, reverse=True)
    scores = scores[:5]
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        for n, s in scores:
            f.write(f"{n},{s}\n")

# إعداد الذاكرة
if 'عدد_التدويرات' not in st.session_state: st.session_state.عدد_التدويرات = 0
if 'مجموع_النقاط' not in st.session_state: st.session_state.مجموع_النقاط = 0

اسم_اللاعب = st.text_input("اكتب سميتك هنا أولاً لتسجيل نقاطك:", value="آدم البطل")

# استقبال النتيجة من كود الـ JavaScript فاش كيتضغط على النرد
query_params = st.query_params
if "dice_result" in query_params:
    res = int(query_params["dice_result"])
    if "last_total" not in st.session_state or query_params.get("roll_id") != st.session_state.get("last_roll_id"):
        st.session_state.عدد_التدويرات += 1
        st.session_state.مجموع_النقاط += res
        st.session_state.last_roll_id = query_params.get("roll_id")
        st.session_state.الرقم_الأخير = res

# زر الحفظ في لوحة المتصدرين
if st.button("💾 حفظ نتيجتي فلوحة المتصدرين"):
    if st.session_state.مجموع_النقاط > 0:
        حفظ_متصدر_جديد(اسم_اللاعب, st.session_state.مجموع_النقاط)
        st.toast(f"✅ تم حفظ نقاطك بنجاح يا {اسم_اللاعب}!")
        st.session_state.عدد_التدويرات = 0
        st.session_state.مجموع_النقاط = 0
        if "الرقم_الأخير" in st.session_state: del st.session_state.الرقم_الأخير
    else:
        st.warning("خاصك تضغط على النرد وتلعب أولاً! 🎲")

# --- 🎮 كود الـ 3D التفاعلي بالإطار الكبير واللون الجديد ---
# زدت فالعلو لـ 320px وبدلت لون الخلفية للون بني شوكولاتة داكن ودافئ (#4E3629) وكبرت المساحة الداخلية لراحة النرد
roll_id = random.randint(1000, 9999)
html_code = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 320px; background: #4E3629; border-radius: 20px; cursor: pointer; box-shadow: 0 12px 24px rgba(0,0,0,0.25);" onclick="rollDice()">
    <style>
        .scene {{ width: 140px; height: 140px; perspective: 600px; }}
        .cube {{
            width: 100%; height: 100%; position: relative; transform-style: preserve-3d;
            transition: transform 1s ease-out;
            transform: rotateX(0deg) rotateY(0deg);
        }}
        .face {{
            position: absolute; width: 140px; height: 140px; border: 3px solid #fff;
            border-radius: 18px; font-size: 75px; font-weight: bold; display: flex;
            justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4);
        }}
        .front  {{ transform: rotateY(  0deg) translateZ(70px); background: #ff4b4b; }}
        .bottom {{ transform: rotateX(-90deg) translateZ(70px); background: #3b82f6; }}
        .right  {{ transform: rotateY( 90deg) translateZ(70px); background: #10b981; }}
        .left   {{ transform: rotateY(-90deg) translateZ(70px); background: #f59e0b; }}
        .top    {{ transform: rotateX( 90deg) translateZ(70px); background: #8b5cf6; }}
        .back   {{ transform: rotateY(180deg) translateZ(70px); background: #d97706; }}
    </style>
    
    <div class="scene">
        <div class="cube" id="dice">
            <div class="face front">⚀</div>
            <div class="face bottom">⚁</div>
            <div class="face right">⚂</div>
            <div class="face left">⚃</div>
            <div class="face top">⚄</div>
            <div class="face back">⚅</div>
        </div>
    </div>

    <script>
        function rollDice() {{
            const cube = document.getElementById('dice');
            const result = Math.floor(Math.random() * 6) + 1;
            
            const xRand = (Math.floor(Math.random() * 3) + 4) * 360;
            const yRand = (Math.floor(Math.random() * 3) + 4) * 360;
            
            const زوايا = {{
                1: `rotateX(${{xRand}}deg) rotateY(${{yRand}}deg)`,
                2: `rotateX(${{xRand - 90}}deg) rotateY(${{yRand}}deg)`,
                3: `rotateX(${{xRand}}deg) rotateY(${{yRand + 90}}deg)`,
                4: `rotateX(${{xRand}}deg) rotateY(${{yRand - 90}}deg)`,
                5: `rotateX(${{xRand + 90}}deg) rotateY(${{yRand}}deg)`,
                6: `rotateX(${{xRand + 180}}deg) rotateY(${{yRand}}deg)`
            }};
            
            cube.style.transform = زوايا[result];
            
            setTimeout(() => {{
                window.parent.postMessage({{
                    type: 'streamlit:set_query_params',
                    value: {{ dice_result: result, roll_id: '{roll_id}' }}
                }}, '*');
                window.parent.location.reload();
            }}, 1000);
        }}
    </script>
</div>
"""

# زدت فالعلو ديال الـ component باش يتناسب مع حجم الإطار الجديد
components.html(html_code, height=335)

# عرض النتيجة
if "الرقم_الأخير" in st.session_state:
    st.success(f"🎉 جالي الرقم: {st.session_state.الرقم_الأخير}")
    if st.session_state.عدد_التدويرات % 5 == 0:
        st.balloons()
        st.markdown('<div style="background-color: #FFFFFF; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center;"><p style="font-size: 14px; margin: 0; color:#333;">📸 تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p><a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white !important; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a></div>', unsafe_allow_html=True)

st.subheader(f"📊 حصيلتك الحالية: {st.session_state.مجموع_النقاط} نقطة (في {st.session_state.عدد_التدويرات} رمية)")

st.markdown("---")
st.markdown("### 🏆 لوحة المتصدرين العالمية 🏆")
المتصدرون = قراءة_المتصدرين()
if المتصدرون:
    for i, (الاسم, النقط) in enumerate(المتصدرون):
        ميدالية = {0: "🥇", 1: "🥈", 2: "🥉"}.get(i, "👤")
        st.markdown(f"**{ميدالية} المركز {i+1}:** {الاسم} — ✨ **{النقط} نقطة**")
else:
    st.write("اللائحة فارغة دابا، سجل نتيجتك!")
