import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="معركة لوس سانتوس 3D", page_icon="🎮", layout="centered")
STARTIO_ACCOUNT_ID = "124299136"

st.markdown("<style>.stApp { background-color: #111827 !important; } h1, p, .stMarkdown { color: #F3F4F6 !important; }</style>", unsafe_allow_html=True)
st.title("🎮 ADAM GTA V: معركة المدينة ثلاثية الأبعاد 🎮")
st.write("✨ **تحديث الواقعية المطلقة:** محرك ثلاثي الأبعاد بأسلوب منظور الشخص الثالث! اضغط وتحكم في المعركة داخل المدينة! 🚀")

html_code = """
<div style="font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background: #1f2937; padding: 15px; border-radius: 20px; direction: rtl; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
    
    <!-- 🏆 لوحة معلومات اللاعب والمهام -->
    <div style="display: flex; justify-content: space-between; width: 100%; max-width: 500px; background: #111827; color: white; padding: 15px; border-radius: 15px; box-shadow: 0 6px 12px rgba(0,0,0,0.4); margin-bottom: 15px; border: 1px solid #374151;">
        <div>
            <h3 style="margin: 0; color: #10b981;">👤 اللاعب: ADAM_PRO</h3>
            <p style="margin: 5px 0 0 0; font-size: 14px;">⭐ المستوى (LEVEL): <span id="hero-level">1</span></p>
            <p style="margin: 5px 0 0 0; font-size: 14px;">💰 أموال العصابة: <span id="hero-gold" style="color: #facc15; font-weight: bold;">$0</span></p>
        </div>
        <div style="text-align: left; border-right: 2px solid #374151; padding-right: 15px;">
            <h4 style="margin: 0; color: #3b82f6;">📜 مهمة المدينة:</h4>
            <p id="quest-text" style="margin: 5px 0 0 0; font-size: 13px; color: #9ca3af;">تصفية 3 من زعماء الشوارع الخطرين!</p>
            <p style="margin: 5px 0 0 0; font-size: 13px; color: #3b82f6;">التقدم: <span id="quest-progress">0</span> / 3</p>
        </div>
    </div>

    <!-- 🎮 ساحة محرك GTA V ثلاثي الأبعاد (Realistic 3D World Container) -->
    <div style="position: relative; width: 100%; max-width: 500px; height: 380px; background: #000; border-radius: 20px; border: 4px solid #111827; box-shadow: 0 15px 35px rgba(0,0,0,0.6); overflow: hidden; perspective: 1200px; perspective-origin: 50% 25%;">
        
        <!-- الأفق الفضائي والغيوم والمدينة في الليل -->
        <div style="position: absolute; top: 0; width: 100%; height: 35%; background: linear-gradient(to bottom, #030712, #0b1528); border-bottom: 3px solid #1f3aa2;">
            <!-- ناطحات سحاب ثلاثية الأبعاد متباعدة في الأفق -->
            <div style="position: absolute; bottom: 0; width: 100%; height: 60px; display: flex; justify-content: space-around; opacity: 0.4;">
                <div style="width: 30px; height: 60px; background: #0c182c; border-top: 2px solid #3b82f6;"></div>
                <div style="width: 45px; height: 90px; background: #081120; margin-top: -30px; border-top: 2px solid #3b82f6;"></div>
                <div style="width: 25px; height: 70px; background: #0f203a; border-top: 2px solid #3b82f6;"></div>
                <div style="width: 40px; height: 50px; background: #0a1424; border-top: 2px solid #3b82f6;"></div>
            </div>
        </div>

        <!-- شوارع مدينة لوس سانتوس الاسفلتية ثلاثية الأبعاد العميقة -->
        <div style="position: absolute; bottom: -100px; width: 100%; height: 90%; background: repeating-linear-gradient(0deg, #1f2937 0px, #1f2937 40px, #111827 40px, #111827 80px); transform: rotateX(65deg); transform-origin: top; box-shadow: inset 0 30px 60px rgba(0,0,0,0.95); border-top: 4px solid #3b82f6;">
            <!-- خطوط الطريق الصفراء ثلاثية الأبعاد الممتدة للعمق -->
            <div style="position: absolute; left: 50%; width: 6px; height: 100%; background: repeating-linear-gradient(to bottom, #facc15 0px, #facc15 40px, transparent 40px, transparent 80px); transform: translateX(-50%); opacity: 0.6;"></div>
        </div>
        
        <!-- طاقة زعيم العصابة -->
        <div style="position: absolute; top: 15px; width: 80%; left: 10%; background: #111; border-radius: 6px; height: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.7); z-index: 10; border: 1px solid #374151;">
            <div id="enemy-hp-bar" style="width: 100%; background: linear-gradient(to right, #dc2626, #f87171); height: 100%; border-radius: 5px; transition: width 0.15s;"></div>
            <span id="enemy-hp-text" style="position: absolute; width: 100%; text-align: center; font-size: 11px; color: white; font-weight: bold; top: 0; text-shadow: 1px 1px 2px #000;">BOSS HP: 100/100</span>
        </div>
        <h3 id="enemy-name" style="position: absolute; top: 36px; width: 100%; text-align: center; color: #ef4444; margin: 0; font-weight: bold; text-shadow: 2px 2px 5px rgba(0,0,0,0.9); z-index: 10; font-size: 15px;">🔥 المافيوزي الضخم بالمدينة</h3>

        <!-- 👹 مجسم الزعيم المستهدف في العمق -->
        <div id="enemy-container" style="position: absolute; top: 22%; left: 50%; transform: translateX(-50%) translateZ(-200px); transform-style: preserve-3d; transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 4;">
            <div style="position: absolute; bottom: -8px; left: 50%; transform: translateX(-50%) rotateX(90deg); width: 110px; height: 35px; background: rgba(0,0,0,0.8); border-radius: 50%; filter: blur(4px);"></div>
            <div id="enemy-sprite" style="font-size: 90px; filter: drop-shadow(0 15px 20px rgba(0,0,0,0.9)); animation: enemyAnimate 3.5s ease-in-out infinite; user-select: none;">👹</div>
        </div>

        <!-- 🥷 مجسم بطل الـ GTA من الخلف في مقدمة الكاميرا (3rd Person View) -->
        <div id="hero-container" style="position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%) translateZ(120px); transform-style: preserve-3d; transition: transform 0.15s ease-out; z-index: 6;">
            <div style="position: absolute; bottom: -12px; left: 50%; transform: translateX(-50%) rotateX(90deg); width: 95px; height: 28px; background: rgba(0,0,0,0.95); border-radius: 50%; filter: blur(3px);"></div>
            <div id="hero-sprite" style="font-size: 85px; filter: drop-shadow(0 8px 12px rgba(0,0,0,0.7)); transform: scaleX(-1); user-select: none; animation: heroIdle 2s ease-in-out infinite;">🥷</div>
        </div>
        
        <!-- مؤثرات الضرر والانفجار المتطايرة -->
        <div id="damage-pop" style="position: absolute; color: #facc15; font-size: 40px; font-weight: bold; display: none; text-shadow: 3px 3px 6px #000; z-index: 20; left: 45%; top: 35%; animation: damageFloat 0.3s ease-out;">💥 -30</div>
    </div>

    <!-- 🕹️ أزرار التحكم والقتال السريع الواقعي -->
    <div style="margin-top: 15px; display: flex; gap: 10px; width: 100%; max-width: 500px;">
        <button onclick="attack(30, 'combo')" style="flex: 1; background: linear-gradient(to bottom, #dc2626, #991b1b); color: white; border: none; padding: 15px; border-radius: 14px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #7f1d1d; transition: 0.1s;">⚔️ ضربة كومبو متتالية</button>
        <button onclick="attack(60, 'special')" style="flex: 1; background: linear-gradient(to bottom, #eab308, #a16207); color: white; border: none; padding: 15px; border-radius: 14px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #713f12; transition: 0.1s;">⚡ ضربة قاضية بالمركبة</button>
    </div>

    <style>
        @keyframes enemyAnimate { 0% { transform: translateY(0px) rotateY(0deg); } 50% { transform: translateY(-8px) rotateY(8deg); } 100% { transform: translateY(0px) rotateY(0deg); } }
        @keyframes heroIdle { 0% { transform: scaleX(-1) translateY(0px); } 50% { transform: scaleX(-1) translateY(-4px); } 100% { transform: scaleX(-1) translateY(0px); } }
        @keyframes damageFloat { 0% { transform: scale(0.6) translateY(15px); opacity: 0; } 100% { transform: scale(1.1) translateY(-15px); opacity: 1; } }
    </style>
    
    <button onclick="resetGame()" style="margin-top: 15px; background: transparent; color: #a8a29e; border: 1px solid #4b5563; padding: 6px 12px; border-radius: 8px; cursor: pointer; font-size: 12px;">🔄 إعادة تعيين المغامرة (RESET)</button>

    <div id="insta-ad" style="display: none; background-color: #111827; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.3); margin-top: 15px; width: 90%; border: 1px solid #374151;">
        <p style="font-size: 14px; margin: 0; color:#e5e7eb;">📸 كملتي مهمة الـ GTA بنجاح! تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
        <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white !important; padding: 6px 12px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px; font-weight: bold;">اضغط للمتابعة الآن</a>
    </div>

    <script>
        let heroLevel = 1, heroGold = 0, monstersDefeated = 0, questTarget = 3, enemyMaxHp = 100, enemyHp = 100, isAttacking = false;
        const monsters = [{ name: "🔥 المافيوزي الضخم بالمدينة", sprite: "👹", hp: 100, gold: 150 }, { name: "🛸 الطائرة المسيرة المعادية", sprite: "🛸", hp: 240, gold: 350 }, { name: "Tank 🤖 المدرعة العسكرية القتالية", sprite: "🤖", hp: 400, gold: 800 }];
        let currentMonsterIndex = 0;

        function attack(maxDmg, type) {
            if (enemyHp <= 0 || isAttacking) return; isAttacking = true;
            let dmg = Math.floor(Math.random() * 20) + (maxDmg - 10); enemyHp -= dmg; if (enemyHp < 0) enemyHp = 0;
            
            document.getElementById('enemy-hp-bar').style.width = (enemyHp / enemyMaxHp) * 100 + '%';
            document.getElementById('enemy-hp-text').innerText = 'BOSS HP: ' + enemyHp + '/' + enemyMaxHp;
            
            const hero = document.getElementById('hero-container'), enemy = document.getElementById('enemy-container'), pop = document.getElementById('damage-pop');
            
