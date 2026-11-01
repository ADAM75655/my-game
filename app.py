import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="معركة 3D طراز جيتياي", page_icon="🎮", layout="centered")

STARTIO_ACCOUNT_ID = "124299136"

st.markdown("<style>.stApp { background-color: #FAEDCD !important; } h1, p, .stMarkdown { color: #3D3025 !important; }</style>", unsafe_allow_html=True)
st.title("🎮 معركة الأبطال 3D (منظور جيتياي) 🎮")
st.write("✨ **تحديث أسطوري:** محرك ثلاثي الأبعاد كامل وسط الصفحة! اضغط لمشاهدة تأثيرات الحركة الواقعية! 🚀")

html_code = """
<div style="font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background: #FAEDCD; padding: 10px; border-radius: 15px; direction: rtl;">
    
    <!-- 🏆 لوحة معلومات البطل والمهام -->
    <div style="display: flex; justify-content: space-between; width: 100%; max-width: 500px; background: #4E3629; color: white; padding: 15px; border-radius: 15px; box-shadow: 0 6px 12px rgba(0,0,0,0.2); margin-bottom: 15px;">
        <div>
            <h3 style="margin: 0; color: #f59e0b;">👤 اللاعب: آدم 3D</h3>
            <p style="margin: 5px 0 0 0;">⭐ لفل: <span id="hero-level">1</span></p>
            <p style="margin: 5px 0 0 0;">💰 الذهب: <span id="hero-gold" style="color: #f59e0b; font-weight: bold;">0</span></p>
        </div>
        <div style="text-align: left; border-right: 2px solid #D4A373; padding-right: 15px;">
            <h4 style="margin: 0; color: #10b981;">📜 المهمة الحالية:</h4>
            <p id="quest-text" style="margin: 5px 0 0 0; font-size: 14px;">سحق 3 وحوش في الساحة ثلاثية الأبعاد!</p>
            <p style="margin: 5px 0 0 0; font-size: 13px; color: #a7f3d0;">التقدم: <span id="quest-progress">0</span> / 3</p>
        </div>
    </div>

    <!-- 🎮 ساحة المعركة ثلاثية الأبعاد العميقة (GTA Perspective Arena) -->
    <div style="position: relative; width: 100%; max-width: 500px; height: 350px; background: linear-gradient(to bottom, #0b1d3a, #1a365d); border-radius: 20px; border: 4px solid #4E3629; box-shadow: 0 12px 24px rgba(0,0,0,0.4); overflow: hidden; perspective: 1000px; perspective-origin: 50% 30%;">
        
        <!-- الأفق والمدينة الرقمية في الخلفية -->
        <div style="position: absolute; top: 0; width: 100%; height: 40%; background: linear-gradient(to bottom, #020813, #0b1d3a); border-bottom: 2px solid #1e3a8a;">
            <div style="position: absolute; bottom: 0; width: 100%; height: 40px; opacity: 0.3; background: repeating-linear-gradient(90deg, #3b82f6 0px, #3b82f6 10px, transparent 10px, transparent 30px);"></div>
        </div>

        <!-- الأرضية 3D الممتدة للداخل لتعطي منظور جيتياي الحقيقي -->
        <div style="position: absolute; bottom: -50px; width: 100%; height: 75%; background: repeating-linear-gradient(0deg, #1f2937 0px, #1f2937 30px, #111827 30px, #111827 60px); transform: rotateX(60deg); transform-origin: top; box-shadow: inset 0 20px 50px rgba(0,0,0,0.9); border-top: 4px solid #3b82f6;"></div>
        
        <!-- شريط طاقة العدو المطور -->
        <div style="position: absolute; top: 15px; width: 80%; left: 10%; background: #222; border-radius: 10px; height: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.6); z-index: 10;">
            <div id="enemy-hp-bar" style="width: 100%; background: linear-gradient(to right, #ef4444, #f87171); height: 100%; border-radius: 10px; transition: width 0.2s;"></div>
            <span id="enemy-hp-text" style="position: absolute; width: 100%; text-align: center; font-size: 11px; color: white; font-weight: bold; top: 0; text-shadow: 1px 1px #000;">HP: 100/100</span>
        </div>
        <h3 id="enemy-name" style="position: absolute; top: 38px; width: 100%; text-align: center; color: #f87171; margin: 0; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); z-index: 10;">👹 زعيم العصابة الضخم</h3>

        <!-- 🏢 مجسم العدو (3D Target) فالعلو والعمق -->
        <div id="enemy-container" style="position: absolute; top: 25%; left: 50%; transform: translateX(-50%) translateZ(-150px); transform-style: preserve-3d; transition: transform 0.2s; z-index: 4;">
            <div style="position: absolute; bottom: -5px; left: 50%; transform: translateX(-50%) rotateX(90deg); width: 100px; height: 30px; background: rgba(0,0,0,0.7); border-radius: 50%; filter: blur(5px);"></div>
            <div id="enemy-sprite" style="font-size: 85px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.8)); animation: enemyFloat 4s ease-in-out infinite;">👹</div>
        </div>

        <!-- 👤 مجسم البطل من الخلف (GTA 3rd Person Perspective) -->
        <div id="hero-container" style="position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%) translateZ(100px); transform-style: preserve-3d; transition: transform 0.15s; z-index: 6;">
            <div style="position: absolute; bottom: -10px; left: 50%; transform: translateX(-50%) rotateX(90deg); width: 90px; height: 25px; background: rgba(0,0,0,0.8); border-radius: 50%; filter: blur(3px);"></div>
            <!-- البطل يرى من الخلف وهو يرتدي بذلته جاهز للمضاربة -->
            <div id="hero-sprite" style="font-size: 75px; filter: drop-shadow(0 5px 10px rgba(0,0,0,0.6)); transform: scaleX(-1);">🥷</div>
        </div>
        
        <!-- نص الضربات المتطاير في البعد الثالث -->
        <div id="damage-pop" style="position: absolute; color: #facc15; font-size: 38px; font-weight: bold; display: none; text-shadow: 3px 3px 6px #000; z-index: 20; left: 45%; top: 35%;">💥 -25</div>
    </div>

    <!-- 🕹️ أزرار التحكم القتالي الاحترافي -->
    <div style="margin-top: 15px; display: flex; gap: 10px; width: 100%; max-width: 500px;">
        <button onclick="attack(25, 'dash')" style="flex: 1; background: linear-gradient(to bottom, #ef4444, #b91c1c); color: white; border: none; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #7f1d1d;">⚔️ هجوم اندفاعي 3D</button>
        <button onclick="attack(55, 'jump')" style="flex: 1; background: linear-gradient(to bottom, #f59e0b, #b45309); color: white; border: none; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #78350f;">⚡ ضربة قاضية واقعية</button>
    </div>

    <style>
        @keyframes enemyFloat { 0% { transform: translateY(0px) rotateY(0deg); } 50% { transform: translateY(-10px) rotateY(10deg); } 100% { transform: translateY(0px) rotateY(0deg); } }
    </style>
    
    <button onclick="resetGame()" style="margin-top: 15px; background: transparent; color: #3D3025; border: 1px solid #3D3025; padding: 5px 10px; border-radius: 8px; cursor: pointer; font-size: 12px;">🔄 إعادة بدء المغامرة</button>

    <div id="insta-ad" style="display: none; background-color: #FFFFFF; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 15px; width: 90%;">
        <p style="font-size: 14px; margin: 0; color:#333;">📸 كملتي المهمة بنجاح! تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
        <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a>
    </div>

    <script>
        let heroLevel = 1, heroGold = 0, monstersDefeated = 0, questTarget = 3, enemyMaxHp = 100, enemyHp = 100, isAttacking = false;
        const monsters = [{ name: "👹 زعيم العصابة الضخم", sprite: "👹", hp: 100, gold: 35 }, { name: "🐉 التنين الرقمي الطائر", sprite: "🐉", hp: 220, gold: 70 }, { name: "🤖 الآلي المدمر المستقبلي", sprite: "🤖", hp: 350, gold: 130 }];
        let currentMonsterIndex = 0;

        function attack(maxDmg, type) {
            if (enemyHp <= 0 || isAttacking) return;
            isAttacking = true;
            
            let dmg = Math.floor(Math.random() * 20) + (maxDmg - 10);
            enemyHp -= dmg; if (enemyHp < 0) enemyHp = 0;
            
            document.getElementById('enemy-hp-bar').style.width = (enemyHp / enemyMaxHp) * 100 + '%';
            document.getElementById('enemy-hp-text').innerText = 'HP: ' + enemyHp + '/' + enemyMaxHp;
            
            const hero = document.getElementById('hero-container');
            const enemy = document.getElementById('enemy-container');
            const pop = document.getElementById('damage-pop');
            
            // محاكاة حركة القفز أو الاندفاع ثلاثي الأبعاد نحو العدو فالعالم (3D Camera Dash Effect)
            if (type === 'dash') {
                hero.style.transform = "translateX(-50%) translateZ(20px) translateY(-30px) scale(1.1)";
                enemy.style.transform = "translateX(-50%) translateZ(-190px) rotateX(-15deg)";
            } else {
                hero.style.transform = "translateX(-50%) translateZ(50px) translateY(-60px) scale(1.2)";
                enemy.style.transform = "translateX(-50%) translateZ(-210px) rotateY(20deg)";
            }
            
            pop.innerText = '💥 -' + dmg; pop.style.display = 'block';
            
            setTimeout(() => {
                hero.style.transform = "translateX(-50%) translateZ(100px) translateY(0px) scale(1)";
                enemy.style.transform = "translateX(-50%) translateZ(-150px) rotateX(0deg) rotateY(0deg)";
                pop.style.display = 'none'; 
                isAttacking = false;
                if (enemyHp <= 0) monsterDied();
            }, 300);
        }

        function monsterDied() {
            heroGold += monsters[currentMonsterIndex].gold; monstersDefeated++;
            document.getElementById('hero-gold').innerText = heroGold;
            if (monstersDefeated <= questTarget) document.getElementById('quest-progress').innerText = monstersDefeated;
            
            if (monstersDefeated === questTarget) {
                heroLevel++; document.getElementById('hero-level').innerText = heroLevel;
