import streamlit as st
import random
import time

# إعداد الصفحة وتزيينها
st.set_page_config(page_title="لعبة النرد الذكية", page_icon="🎲")
st.title("🎲 تحدي لعبة النرد العالمية!")
st.write("أنا مبرمج وعندي 10 سنوات، صاوبت هاد اللعبة باش نتحداكم فزهركم!")

# خانة لتسجيل اسم اللاعب
اسم_اللاعب = st.text_input("اكتب سميتك هنا أولاً:", value="آدم البطل")

# إعداد كاونتر يحسب عدد التدويرات فذاكرة الموقع
if 'عدد_التدويرات' not in st.session_state:
    st.session_state.عدد_التدويرات = 0

# زر رمي النرد
if st.button("🎲 ارمي النرد دابا! 🎲"):
    # زيادة عدد التدويرات بـ 1
    st.session_state.عدد_التدويرات += 1
    
    st.write("🔄 جاري رمي النرد... تفاءل خير!")
    time.sleep(0.4)
    
    # اختيار رقم عشوائي
    الرقم_المحصل = random.randint(1, 6)
    
    # تحديد إيموجي النرد
    رموز_النرد = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    ايموجي_النرد = رموز_النرد[الرقم_المحصل]
    
    # عرض النتيجة
    st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{ايموجي_النرد}</h1>", unsafe_allow_html=True)
    st.success(f"🎉 تبارك الله! {اسم_اللاعب} جاب الرقم: {الرقم_المحصل}")
    st.info(f"📊 هادي التدويرة رقم: {st.session_state.عدد_التدويرات}")
    
    # 🌟 الشرط الذكي: كل ما يوصل عدد التدويرات لمضاعفات 5 غايظهر الإعلان
    if st.session_state.عدد_التدويرات % 5 == 0:
        st.balloons() # طيران النفاخات
        
        # صندوق إعلان ملون واحترافي لتابعنا على إنستغرام
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; margin-top: 20px;">
            <h3 style="color: #E1306C; margin-bottom: 5px;">📸 إعلان للمتابعين الأوفياء!</h3>
            <p style="font-size: 16px; color: #333;">تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل دائماً بالجديد من المبرمج آدم! 🚀</p>
            <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 10px 20px; text-decoration: none; border-radius: 20px; font-weight: bold; display: inline-block; margin-top: 10px;">اضغط هنا للمتابعة دابا 👋</a>
        </div>
        """, unsafe_allow_html=True)
