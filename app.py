import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="لعبة النرد 3D السريعة", page_icon="🎲", layout="centered")

# معرف حساب Start.io الحقيقي ديال آدم
STARTIO_ACCOUNT_ID = "124299136"

# تغيير لون الشاشة للون سومو فاتح
st.markdown("""
    <style>
        .stApp { background-color: #FAEDCD !important; }
        h1, p, .stMarkdown { color: #3D3025 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🎲 تحدي لعبة النرد 3D التفاعلية السريعة!")
st.write("✨ **تحديث جديد:** تم حذف الـ Actualiser! اضغط على النرد دابا وسير كيطير 🚀")

# كود HTML + CSS + JS كامل مكمول باش يتحسب كلشي فالبلاصة بلا ريفريش
html_code = f"""
<div style="font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background: #FAEDCD; padding: 10px; border-radius: 15px;">
    
    <!-- 🎮 إطار النرد البني الكبير -->
    <div style="display: flex; justify-content: center; align-items: center; width: 100%; max-width: 450px; height: 280px; background: #4E3629; border-radius: 20px; cursor: pointer; box-shadow: 0 12px 24px rgba(0,0,0,0.25);" onclick="rollDice()">
        <div style="width: 140px; height: 140px; perspective: 600px;">
            <div id="dice" style="width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 0.8s ease-out; transform: rotateX(0deg) rotateY(0deg);">
                <div style="position: absolute; width: 140px; height: 140px; border: 3px solid #fff; border-radius: 18px; font-size: 75px; font-weight: bold; display: flex; justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4); transform: rotateY(0deg) translateZ(70px); background: #ff4b4b;">⚀</div>
                <div style="position: absolute; width: 140px; height: 140px; border: 3px solid #fff; border-radius: 18px; font-size: 75px; font-weight: bold; display: flex; justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4); transform: rotateX(-90deg) translateZ(70px); background: #3b82f6;">⚁</div>
                <div style="position: absolute; width: 140px; height: 140px; border: 3px solid #fff; border-radius: 18px; font-size: 75px; font-weight: bold; display: flex; justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4); transform: rotateY(90deg) translateZ(70px); background: #10b981;">⚂</div>
                <div style="position: absolute; width: 140px; height: 140px; border: 3px solid #fff; border-radius: 18px; font-size: 75px; font-weight: bold; display: flex; justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4); transform: rotateY(-90deg) translateZ(70px); background: #f59e0b;">⚃</div>
                <div style="position: absolute; width: 140px; height: 140px; border: 3px solid #fff; border-radius: 18px; font-size: 75px; font-weight: bold; display: flex; justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4); transform: rotateX(90deg) translateZ(70px); background: #8b5cf6;">⚄</div>
                <div style="position: absolute; width: 140px; height: 140px; border: 3px solid #fff; border-radius: 18px; font-size: 75px; font-weight: bold; display: flex; justify-content: center; align-items: center; color: white; box-shadow: inset 0 0 25px rgba(0,0,0,0.4); transform: rotateY(180deg) translateZ(70px); background: #d97706;">⚅</div>
            </div>
        </div>
    </div>

    <!-- 📊 عداد النقاط الذكي سرييييع جداً وبدون لاغ -->
    <div style="margin-top: 20px; text-align: center; color: #3D3025; direction: rtl;">
        <h3 id="result-text" style="margin: 5px 0; color: #10b981; display: none;">🎉 جالي الرقم: <span id="current-dice">0</span></h3>
        <h2 style="margin: 10px 0;">📊 حصيلتك الحالية: <span id="total-score" style="color: #ff4b4b;">0</span> نقطة (في <span id="roll-count" style="color: #3b82f6;">0</span> رمية)</h2>
        <button onclick="resetScore()" style="background-color: #3D3025; color: white; border: none; padding: 8px 16px; border-radius: 10px; cursor: pointer; font-weight: bold;">🔄 إعادة تصفير النقاط</button>
    </div>

    <!-- 📸 إعلان إنستغرام الذكي (كيظهر فكل 5 رميات تلقائياً بلا ريفريش) -->
    <div id="insta-ad" style="display: none; background-color: #FFFFFF; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 15px; width: 90%;">
        <p style="font-size: 14px; margin: 0; color:#333;">📸 تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
        <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a>
    </div>

    <script>
        let totalScore = 0;
        let rollCount = 0;

        function rollDice() {{
            const cube = document.getElementById('dice');
            const result = Math.floor(Math.random() * 6) + 1;
            
            const xRand = (Math.floor(Math.random() * 3) + 4) * 360;
            const yRand = (Math.floor(Math.random() * 3) + 4) * 360;
            
            const angles = {{
                1: `rotateX(${{xRand}}deg) rotateY(${{yRand}}deg)`,
                2: `rotateX(${{xRand - 90}}deg) rotateY(${{yRand}}deg)`,
                3: `rotateX(${{xRand}}deg) rotateY(${{yRand + 90}}deg)`,
                4: `rotateX(${{xRand}}deg) rotateY(${{yRand - 90}}deg)`,
                5: `rotateX(${{xRand + 90}}deg) rotateY(${{yRand}}deg)`,
                6: `rotateX(${{xRand + 180}}deg) rotateY(${{yRand}}deg)`
            }};
            
            cube.style.transform = angles[result];
            
            // تحديث الحسابات فورا بعد 800 مللي ثانية (قبل ما تسالي الدورة بشوية لسرعة خيالية)
            setTimeout(() => {{
                rollCount++;
                totalScore += result;
                
                document.getElementById('current-dice').innerText = result;
                document.getElementById('result-text').style.display = 'block';
                document.getElementById('total-score').innerText = totalScore;
                document.getElementById('roll-count').innerText = rollCount;
                
                // إظهار إعلان الإنستغرام كل 5 رميات
                if(rollCount % 5 === 0) {{
                    document.getElementById('insta-ad').style.display = 'block';
                }} else {{
                    document.getElementById('insta-ad').style.display = 'none';
                }}
            }}, 800);
        }}

        function resetScore() {{
            totalScore = 0;
            rollCount = 0;
            document.getElementById('total-score').innerText = totalScore;
            document.getElementById('roll-count').innerText = rollCount;
            document.getElementById('result-text').style.display = 'none';
            document.getElementById('insta-ad').style.display = 'none';
        }}
    </script>
</div>
"""

# عرض اللعبة الكاملة فالموقع
components.html(html_code, height=520)

# --- 💰 مساحة إعلان Start.io للويب المستقرة فمكانها ---
st.markdown("---")
st.write("📢 **إشهار لدعم المبرمج الصغير:**")

startio_ad_html = f"""
<div style="display: flex; justify-content: center; align-items: center; min-height: 100px;">
    <script type="text/javascript" src="https://start.io"></script>
    <script type="text/javascript">
        startio.init("{STARTIO_ACCOUNT_ID}");
        startio.createBanner({{
            container: document.body,
            width: 320,
            height: 50
        }});
    </script>
</div>
"""
components.html(startio_ad_html, height=120)
