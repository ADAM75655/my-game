import streamlit as st
import random
import time
import os

# إعداد الصفحة وتزيينها
st.set_page_config(page_title="لعبة النرد الذكية", page_icon="🎲")
st.title("🎲 تحدي لعبة النرد العالمية مع لوحة المتصدرين!")
st.write("أنا مبرمج وعندي 10 سنوات، صاوبت هاد اللعبة باش نتحداكم فزهركم!")

# ملف مخفي لحفظ النقاط باش ما يتمسحوش فاش نديروا ريفريش
LEADERBOARD_FILE = "leaderboard.txt"

# دالة لقراءة لوحة المتصدرين من الملف
def قراءة_المتصدرين():
    scores = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "," in line:
                    name, score = line.strip().split(",")
                    scores.append((name, int(score)))
    # ترتيب المتصدرين من الأكبر للأصغر
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5] # أعلى 5 فقط

# دالة لحفظ لاعب جديد في لوحة المتصدرين
def حفظ_متصدر_جديد(name, score):
    scores = قراءة_المتصدرين()
    scores.append((name, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:5] # الاحتفاظ بأعلى 5 فقط
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        for n, s in scores:
            f.write(f"{n},{s}\n")

# خانة لتسجيل اسم اللاعب
اسم_اللاعب = st.text_input("اكتب سميتك هنا أولاً لتسجيل نقاطك:", value="آدم البطل")

# إعداد كاونتر للتدويرات والمجموع فذاكرة الموقع
if 'عدد_التدويرات' not in st.session_state:
    st.session_state.عدد_التدويرات = 0
if 'مجموع_النقاط' not in st.session_state:
    st.session_state.مجموع_النقاط = 0

# أزرار التحكم
col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 ارمي النرد دابا! 🎲"):
        st.session_state.عدد_التدويرات += 1
        st.write("🔄 جاري رمي النرد...")
        time.sleep(0.4)
        
        الرقم_المحصل = random.randint(1, 6)
        st.session_state.مجموع_النقاط += الرقم_المحصل
        
        رموز_النرد = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{رموز_النرد[الرقم_المحصل]}</h1>", unsafe_allow_html=True)
        st.success(f"🎉 جبتي الرقم: {الرقم_المحصل}")
        
        # إعلان إنستغرام كل 5 تدويرات
        if st.session_state.عدد_التدويرات % 5 == 0:
            st.balloons()
            st.markdown("""
            <div style="background-color: #f0f2f6; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center;">
                <p style="font-size: 14px; margin: 0;">📸 تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
                <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a>
            </div>
            """, unsafe_allow_html=True)

with col2:
    # زر مخصص لحفظ النتيجة الحالية في اللوحة وإنهاء اللعبة
    if st.button("💾 حفظ نتيجتي فلوحة المتصدرين"):
        if st.session_state.مجموع_النقاط > 0:
            حفظ_متصدر_جديد(اسم_اللاعب, st.session_state.مجموع_النقاط)
            st.toast(f"✅ تم حفظ نقاطك بنجاح يا {اسم_اللاعب}!")
            # إعادة تصغير العدادات للاعب القادم
            st.session_state.عدد_التدويرات = 0
            st.session_state.مجموع_النقاط = 0
        else:
            st.warning("خاصك تلعب وترمي النرد أولاً باش تجمع النقاط! 🎲")

# عرض النتيجة الحالية للاعب
st.subheader(f"📊 حصيلتك الحالية: {st.session_state.مجموع_النقاط} نقطة (في {st.session_state.عدد_التدويرات} رمية)")

# 🏆 عرض لوحة المتصدرين بشكل جميل ومستمر في الأسفل
st.markdown("---")
st.markdown("### 🏆 لوحة المتصدرين العالمية (أعلى مجموع نقاط) 🏆")
المتصدرون = قراءة_المتصدرين()

if المتصدرون:
    for i, (الاسم, النقط) in enumerate(المتصدرون):
        # تزيين المراكز الثلاثة الأولى بميداليات
        ميداليات = {0: "🥇", 1: "🥈", 2: "🥉"}
        ميدالية = ميداليات.get(i, "👤")
        st.markdown(f"**{ميدالية} المركز {i+1}:** {الاسم} — ✨ **{النقط} نقطة**")
else:
    st.write("اللائحة فارغة دابا، كون أنت أول واحد كيسجل النتيجة ديالو! 🚀")
