import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="لعبة القتال ثلاثية الأبعاد 3D", page_icon="⚔️", layout="centered")

# معرف حساب Start.io الحقيقي ديال آدم
STARTIO_ACCOUNT_ID = "124299136"

# تغيير لون الشاشة للون سومو فاتح وهادئ
st.markdown("""
    <style>
        .stApp { background-color: #FAEDCD !important; }
        h1, p, .stMarkdown { color: #3D3025 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("⚔️ معركة الأبطال الواقعية ثلاثية الأبعاد 3D ⚔️")
st.write("✨ **تحديث أسطوري:** ساحة معركة 3D تفاعلية متحركة! اضغط على الأزرار لبدء الملحمة واجمع الذهب! 🚀")

# كود اللعبة بالكامل بـ HTML + CSS + JS مدمج مع محرك ثلاثي الأبعاد مصغر لسرعة خيالية
html_code = """
<div style="font-family: 'Segoe UI', Tahoma, sans-serif; display: flex; flex-direction: column; align-items: center; background: #FAEDCD; padding: 10px; border-radius: 15px; direction: rtl;">
    
    <!-- 🏆 لوحة معلومات البطل والمهام -->
    <div style="display: flex; justify-content: space-between; width: 100%; max-width: 500px; background: #4E3629; color: white; padding: 15px; border-radius: 15px; box-shadow: 0 6px 12px rgba(0,0,0,0.2); margin-bottom: 15px;">
        <div>
            <h3 style="margin: 0; color: #f59e0b;">👤 البطل: آدم 3D</h3>
            <p style="margin: 5px 0 0 0;">⭐ المستوى: <span id="hero-level">1</span></p>
            <p style="margin: 5px 0 0 0;">💰 الذهب: <span id="hero-gold" style="color: #f59e0b; font-weight: bold;">0</span></p>
        </div>
        <div style="text-align: left; border-right: 2px solid #D4A373; padding-right: 15px;">
            <h4 style="margin: 0; color: #10b981;">📜 المهمة الحالية:</h4>
            <p id="quest-text" style="margin: 5px 0 0 0; font-size: 14px;">هزم 3 ديال وحوش الغابة الرقمية!</p>
            <p style="margin: 5px 0 0 0; font-size: 13px; color: #a7f3d0;">التقدم: <span id="quest-progress">0</span> / 3</p>
        </div>
    </div>

    <!-- 🎮 ساحة المعركة ثلاثية الأبعاد (3D Arena) -->
    <div style="position: relative; width: 100%; max-width: 500px; height: 320px; background: linear-gradient(to bottom, #1a0c02, #4a2711); border-radius: 20px; border: 4px solid #4E3629; box-shadow: 0 12px 24px rgba(0,0,0,0.3); overflow: hidden; perspective: 800px;">
        
        <!-- الأرضية ثلاثية الأبعاد المائلة لتعطي عمق واقعي (3D Floor Perspective) -->
        <div style="position: absolute; bottom: 0; width: 100%; height: 50%; background: repeating-linear-gradient(45deg, #2b170c 0px, #2b170c 20px, #3d2112 20px, #3d2112 40px); transform: rotateX(60deg); transform-origin: bottom; box-shadow: inset 0 20px 30px rgba(0,0,0,0.6); border-top: 2px solid #5c341a;"></div>
        
        <!-- طاقة الوحش -->
        <div style="position: absolute; top: 15px; width: 80%; left: 10%; background: #333; border-radius: 10px; height: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.5); z-index: 10;">
            <div id="enemy-hp-bar" style="width: 100%; background: linear-gradient(to right, #ff4b4b, #ff7676); height: 100%; border-radius: 10px; transition: width 0.2s;"></div>
            <span id="enemy-hp-text" style="position: absolute; width: 100%; text-align: center; font-size: 11px; color: white; font-weight: bold; top: 0; text-shadow: 1px 1px #000;">HP: 100/100</span>
        </div>
        
        <h3 id="enemy-name" style="position: absolute; top: 38px; width: 100%; text-align: center; color: #ff7676; margin: 0; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); z-index: 10;">👹 غول الغابة العملاق</h3>

        <!-- مجسم الوحش ثلاثي الأبعاد المتحرك (3D Object Shadow and Matrix) -->
        <div id="enemy-container" style="position: absolute; bottom: 60px; left: 50%; transform: translateX(-50%) translateZ(0px); transform-style: preserve-3d; transition: transform 0.1s ease-out; z-index: 5;">
            <!-- الظل الواقعي تحت المجسم -->
            <div style="position: absolute; bottom: -10px; left: 50%; transform: translateX(-50%) rotateX(90deg); width: 120px; height: 40px; background: rgba(0,0,0,0.6); border-radius: 50%; filter: blur(4px);"></div>
            <!-- مجسم الوحش -->
            <div id="enemy-sprite" style="font-size: 95px; filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.7)); user-select: none; animation: float3d 3s ease-in-out infinite;">👹</div>
        </div>
        
        <!-- نص الضربات المتطاير في الفضاء ثلاثي الأبعاد -->
        <div id="damage-pop" style="position: absolute; color: #ffeb3b; font-size: 36px; font-weight: bold; display: none; text-shadow: 3px 3px 6px #000; z-index: 20; left: 45%; top: 40%; animation: popUp 0.3s ease-out;">💥 -25</div>
    </div>

    <!-- 🕹️ أزرار الهجوم والمضاربة السريعة -->
    <div style="margin-top: 15px; display: flex; gap: 10px; width: 100%; max-width: 500px;">
        <button onclick="attack(25, 'سريع')" style="flex: 1; background: linear-gradient(to bottom, #ff4b4b, #d32f2f); color: white; border: none; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #b91c1c; transition: 0.1s;">⚔️ هجوم خاطف 3D</button>
        <button onclick="attack(55, 'قوي')" style="flex: 1; background: linear-gradient(to bottom, #d97706, #b45309); color: white; border: none; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #78350f; transition: 0.1s;">💥 ضربة زلزال واقعية</button>
    </div>

    <!-- أنيميشن الجرافيكس الواقعي والعمق ثلاثي الأبعاد CSS -->
    <style>
        @keyframes float3d {
            0% { transform: translateY(0px) rotateY(0deg) rotateX(0deg); }
            50% { transform: translateY(-15px) rotateY(15deg) rotateX(5deg); }
            100% { transform: translateY(0px) rotateY(0deg) rotateX(0deg); }
        }
        @keyframes popUp {
            0% { transform: scale(0.5) translateY(20px); opacity: 0; }
            100% { transform: scale(1.2) translateY(-20px); opacity: 1; }
        }
    </style>

    <button onclick="resetGame()" style="margin-top: 15px; background: transparent; color: #3D3025; border: 1px solid #3D3025; padding: 5px 10px; border-radius: 8px; cursor: pointer; font-size: 12px;">🔄 إعادة بدء المغامرة</button>

    <!-- 📸 إعلان إنستغرام الذكي عند إكمال المهام -->
    <div id="insta-ad" style="display: none; background-color: #FFFFFF; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 15px; width: 90%;">
        <p style="font-size: 14px; margin: 0; color:#333;">📸 كملتي المهمة الـ 3D بنجاح! تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
        <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a>
    </div>

    <script>
        let heroLevel = 1;
        let heroGold = 0;
        let monstersDefeated = 0;
        let questTarget = 3;
        
        let enemyMaxHp = 100;
        let enemyHp = 100;
        let isAttacking = false;
        
        const monsters = [
            { name: "👹 غول الغابة العملاق", sprite: "👹", hp: 100, gold: 30 },
            { name: "🐉 تنين الحمم الأسطوري", sprite: "🐉", hp: 200, gold: 65 },
            { name: "🤖 غازي المجرات الآلي", sprite: "🤖", hp: 320, gold: 120 }
        ];
        let currentMonsterIndex = 0;

        function attack(maxDmg, type) {
            if (enemyHp <= 0 || isAttacking) return;
            isAttacking = true;
            
            let dmg = Math.floor(Math.random() * 18) + (maxDmg - 12);
            enemyHp -= dmg;
            if (enemyHp < 0) enemyHp = 0;
            
            let hpPercent = (enemyHp / enemyMaxHp) * 100;
            document.getElementById('enemy-hp-bar').style.width = hpPercent + '%';
            document.getElementById('enemy-hp-text').innerText = 'HP: ' + enemyHp + '/' + enemyMaxHp;
            
            // تأثير ضربة 3D واقعية (ارجاع مجسم الوحش للخلف واهتزازه بقوة في المحاور الثلاثة)
            const container = document.getElementById('enemy-container');
            container.style.transform = "translateX(-50%) translateZ(-80px) rotateX(-20deg) scale(0.85)";
            
            const pop = document.getElementById('damage-pop');
            pop.innerText = '💥 -' + dmg;
            pop.style.display = 'block';
            
            setTimeout(() => {
                container.style.transform = "translateX(-50%) translateZ(0px) rotateX(0deg) scale(1)";
                pop.style.display = 'none';
                isAttacking = false;
                if (enemyHp <= 0) {
                    monsterDied();
                }
            }, 250);
        }

        function monsterDied() {
            let goldEarned = monsters[currentMonsterIndex].gold;
            heroGold += goldEarned;
            monstersDefeated++;
            
            document.getElementById('hero-gold').innerText = heroGold;
            
            if (monstersDefeated <= questTarget) {
                document.getElementById('quest-progress').innerText = monstersDefeated;
            }
            
            if (monstersDefeated === questTarget) {
                heroLevel++;
                document.getElementById('hero-level').innerText = heroLevel;
                document.getElementById('insta-ad').style.display = 'block';
                document.getElementById('quest-text').innerText = "تمت المهمة الـ 3D! تابع سحق الوحوش!";
            }
            
            currentMonsterIndex = (currentMonsterIndex + 1) % monsters.length;
            enemyMaxHp = monsters[currentMonsterIndex].hp + (heroLevel * 30);
            enemyHp = enemyMaxHp;
            
            // تأثير تلاشي الوحش وظهور الوحش الـ 3D الجديد
            const sprite = document.getElementById('enemy-sprite');
