import streamlit as st
import random
import time
import os
import streamlit.components.v1 as components

# إعداد الصفحة وتزيينها
st.set_page_config(page_title="لعبة النرد 3D الملونة", page_icon="🎲", layout="centered")
st.title("🎲 تحدي لعبة النرد 3D الملونة!")
st.write("أنا مبرمج وعندي 10 سنوات، صاوبت هاد النرد 3D الملون باش نتحداكم!")

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

# خانة لتسجيل اسم اللاعب
اسم_اللاعب = st.text_input("اكتب سميتك هنا أولاً لتسجيل نقاطك:", value="آدم البطل")

if 'عدد_التدويرات' not in st.session_state:
    st.session_state.عدد_التدويرات = 0
if 'مجموع_النقاط' not in st.session_state:
    st.session_state.مجموع_النقاط = 0
if 'الرقم_الحالي' not in st.session_state:
    st.session_state.الرقم_الحالي = 1
if 'دور_النرد' not in st.session_state:
    st.session_state.دور_النرد = False

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 ارمي النرد 3D الملون! 🎲"):
        st.session_state.عدد_التدويرات += 1
        st.session_state.الرقم_الحالي = random.randint(1, 6)
        st.session_state.مجموع_النقاط += st.session_state.الرقم_الحالي
        st.session_state.دور_النرد = True

with col2:
    if st.button("💾 حفظ نتيجتي فلوحة المتصدرين"):
        if st.session_state.مجموع_النقاط > 0:
            حفظ_متصدر_جديد(اسم_اللاعب, st.session_state.مجموع_النقاط)
            st.toast(f"✅ تم حفظ نقاطك بنجاح يا {اسم_اللاعب}!")
            st.session_state.عدد_التدويرات = 0
            st.session_state.مجموع_النقاط = 0
            st.session_state.دور_النرد = False
        else:
            st.warning("خاصك تلعب وترمي النرد أولاً! 🎲")

# --- 🎮 كود الـ 3D الملون (كل وجه بلون مميز) ---
زوايا_النرد = {
    1: "rotateX(0deg) rotateY(0deg)",
    2: "rotateX(-90deg) rotateY(0deg)",
    3: "rotateX(0deg) rotateY(90deg)",
    4: "rotateX(0deg) rotateY(-90deg)",
    5: "rotateX(90deg) rotateY(0deg)",
    6: "rotateX(180deg) rotateY(0deg)"
}

الزاوية_المستهدفة = زوايا_النرد[st.session_state.الرقم_الحالي]

html_code = f"""
<div style="display: flex; justify-content: center; align-items: center; height: 220px; background: #0e1117; border-radius: 15px;">
    <style>
        .scene {{ width: 100px; height: 100px; perspective: 400px; }}
        .cube {{
            width: 100%; height: 100%; position: relative; transform-style: preserve-3d;
            transform: {الزاوية_المستهدفة};
            {f"animation: roll 1.2s ease-out forwards;" if st.session_state.دور_النرد else ""}
        }}
        .face {{
            position: absolute; width: 100px; height: 100px; border: 2px solid #fff;
            border-radius: 12px; font-size: 55px; font-weight: bold; display: flex;
            justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 20px rgba(0,0,0,0.4);
        }}
        
        /* 🎨 هنا حددنا لون مخصص ومميز لكل نرد (وجه) */
        .front  {{ transform: rotateY(  0deg) translateZ(50px); background: #ff4b4b; }} /* أحمر */
        .bottom {{ transform: rotateX(-90deg) translateZ(50px); background: #3b82f6; }} /* أزرق */
        .right  {{ transform: rotateY( 90deg) translateZ(50px); background: #10b981; }} /* أخضر */
        .left   {{ transform: rotateY(-90deg) translateZ(50px); background: #f59e0b; }} /* برتقالي */
        .top    {{ transform: rotateX( 90deg) translateZ(50px); background: #8b5cf6; }} /* بنفسجي */
        .back   {{ transform: rotateY(180deg) translateZ(50px); background: #d97706; }} /* ذهبي بني */
        
        @keyframes roll {{
            0% {{ transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }}
            30% {{ transform: rotateX(360deg) rotateY(180deg) rotateZ(90deg); }}
            60% {{ transform: rotateX(720deg) rotateY(540deg) rotateZ(180deg); }}
            100% {{ transform: {الزاوية_المستهدفة}; }}
        }}
    </style>
    <div class="scene">
        <div class="cube">
            <div class="face front">⚀</div>
            <div class="face bottom">⚁</div>
            <div class="face right">⚂</div>
            <div class="face left">⚃</div>
            <div class="face top">⚄</div>
            <div class="face back">⚅</div>
        </div>
    </div>
</div>
"""

components.html(html_code, height=230)

if st.session_state.دور_النرد:
    st.success(f"🎉 النرد الملون وقف وجاب ليك الرقم: {st.session_state.الرقم_الحالي}")
    if st.session_state.عدد_التدويرات % 5 == 0:
        st.balloons()
        st.markdown('<div style="background-color: #f0f2f6; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center;"><p style="font-size: 14px; margin: 0;">📸 تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p><a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a></div>', unsafe_allow_html=True)

st.subheader(f"📊 حصيلتك الحالية: {st.session_state.مجموع_النقاط} نقطة (في {st.session_state.عدد_التدويرات} رمية)")

st.markdown("---")
st.markdown("### 🏆 لوحة المتصدرين العالمية (أعلى مجموع نقاط) 🏆")
المتصدرون = قراءة_المتصدرين()

if المتصدرون:
    for i, (الاسم, النقط) in enumerate(المتصدرون):
        ميدالية = {0: "🥇", 1: "🥈", 2: "🥉"}.get(i, "👤")
        st.markdown(f"**{ميدالية} المركز {i+1}:** {الاسم} — ✨ **{النقط} نقطة**")
else:
    st.write("اللائحة فارغة دابا، سجل نتيجتك!")
