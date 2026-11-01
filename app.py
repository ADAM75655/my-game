import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="لعبة القتال ثلاثية الأبعاد 3D", page_icon="⚔️", layout="centered")

STARTIO_ACCOUNT_ID = "124299136"

st.markdown("<style>.stApp { background-color: #FAEDCD !important; } h1, p, .stMarkdown { color: #3D3025 !important; }</style>", unsafe_allow_html=True)
st.title("⚔️ معركة الأبطال الواقعية ثلاثية الأبعاد 3D ⚔️")
st.write("✨ **تحديث أسطوري:** ساحة معركة 3D تفاعلية متحركة! اضغط على الأزرار لبدء الملحمة واجمع الذهب! 🚀")

html_code = """
<div style="font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background: #FAEDCD; padding: 10px; border-radius: 15px; direction: rtl;">
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
    <div style="position: relative; width: 100%; max-width: 500px; height: 320px; background: linear-gradient(to bottom, #1a0c02, #4a2711); border-radius: 20px; border: 4px solid #4E3629; box-shadow: 0 12px 24px rgba(0,0,0,0.3); overflow: hidden; perspective: 800px;">
        <div style="position: absolute; bottom: 0; width: 100%; height: 50%; background: repeating-linear-gradient(45deg, #2b170c 0px, #2b170c 20px, #3d2112 20px, #3d2112 40px); transform: rotateX(60deg); transform-origin: bottom; box-shadow: inset 0 20px 30px rgba(0,0,0,0.6); border-top: 2px solid #5c341a;"></div>
        <div style="position: absolute; top: 15px; width: 80%; left: 10%; background: #333; border-radius: 10px; height: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.5); z-index: 10;">
            <div id="enemy-hp-bar" style="width: 100%; background: linear-gradient(to right, #ff4b4b, #ff7676); height: 100%; border-radius: 10px; transition: width 0.2s;"></div>
            <span id="enemy-hp-text" style="position: absolute; width: 100%; text-align: center; font-size: 11px; color: white; font-weight: bold; top: 0; text-shadow: 1px 1px #000;">HP: 100/100</span>
        </div>
        <h3 id="enemy-name" style="position: absolute; top: 38px; width: 100%; text-align: center; color: #ff7676; margin: 0; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); z-index: 10;">👹 غول الغابة العملاق</h3>
        <div id="enemy-container" style="position: absolute; bottom: 60px; left: 50%; transform: translateX(-50%) translateZ(0px); transform-style: preserve-3d; transition: transform 0.1s ease-out; z-index: 5;">
            <div style="position: absolute; bottom: -10px; left: 50%; transform: translateX(-50%) rotateX(90deg); width: 120px; height: 40px; background: rgba(0,0,0,0.6); border-radius: 50%; filter: blur(4px);"></div>
            <div id="enemy-sprite" style="font-size: 95px; filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.7)); user-select: none; animation: float3d 3s ease-in-out infinite;">👹</div>
        </div>
        <div id="damage-pop" style="position: absolute; color: #ffeb3b; font-size: 36px; font-weight: bold; display: none; text-shadow: 3px 3px 6px #000; z-index: 20; left: 45%; top: 40%;">💥 -25</div>
    </div>
    <div style="margin-top: 15px; display: flex; gap: 10px; width: 100%; max-width: 500px;">
        <button onclick="attack(25)" style="flex: 1; background: linear-gradient(to bottom, #ff4b4b, #d32f2f); color: white; border: none; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #b91c1c;">⚔️ هجوم خاطف 3D</button>
        <button onclick="attack(55)" style="flex: 1; background: linear-gradient(to bottom, #d97706, #b45309); color: white; border: none; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 5px #78350f;">💥 ضربة زلزال واقعية</button>
    </div>
    <style>
        @keyframes float3d { 0% { transform: translateY(0px) rotateY(0deg); } 50% { transform: translateY(-15px) rotateY(15deg); } 100% { transform: translateY(0px) rotateY(0deg); } }
    </style>
    <button onclick="resetGame()" style="margin-top: 15px; background: transparent; color: #3D3025; border: 1px solid #3D3025; padding: 5px 10px; border-radius: 8px; cursor: pointer; font-size: 12px;">🔄 إعادة بدء المغامرة</button>
    <div id="insta-ad" style="display: none; background-color: #FFFFFF; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 15px; width: 90%;">
        <p style="font-size: 14px; margin: 0; color:#333;">📸 كملتي المهمة بنجاح! تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
        <a href="https://instagram.com" target="_blank" style="background-color: #E1306C; color: white; padding: 5px 10px; text-decoration: none; border-radius: 15px; font-size: 12px; display: inline-block; margin-top: 5px;">اضغط للمتابعة</a>
    </div>
    <script>
        let heroLevel = 1, heroGold = 0, monstersDefeated = 0, questTarget = 3, enemyMaxHp = 100, enemyHp = 100, isAttacking = false;
        const monsters = [{ name: "👹 غول الغابة العملاق", sprite: "👹", hp: 100, gold: 30 }, { name: "🐉 تنين الحمم الأسطوري", sprite: "🐉", hp: 200, gold: 65 }, { name: "🤖 غازي المجرات الآلي", sprite: "🤖", hp: 320, gold: 120 }];
        let currentMonsterIndex = 0;
        function attack(maxDmg) {
            if (enemyHp <= 0 || isAttacking) return;
            isAttacking = true;
            let dmg = Math.floor(Math.random() * 18) + (maxDmg - 12);
            enemyHp -= dmg; if (enemyHp < 0) enemyHp = 0;
            document.getElementById('enemy-hp-bar').style.width = (enemyHp / enemyMaxHp) * 100 + '%';
            document.getElementById('enemy-hp-text').innerText = 'HP: ' + enemyHp + '/' + enemyMaxHp;
            const container = document.getElementById('enemy-container');
            container.style.transform = "translateX(-50%) translateZ(-60px) scale(0.85)";
            const pop = document.getElementById('damage-pop'); pop.innerText = '💥 -' + dmg; pop.style.display = 'block';
            setTimeout(() => {
                container.style.transform = "translateX(-50%) translateZ(0px) scale(1)";
                pop.style.display = 'none'; isAttacking = false;
                if (enemyHp <= 0) monsterDied();
            }, 250);
        }
        function monsterDied() {
            heroGold += monsters[currentMonsterIndex].gold; monstersDefeated++;
            document.getElementById('hero-gold').innerText = heroGold;
            if (monstersDefeated <= questTarget) document.getElementById('quest-progress').innerText = monstersDefeated;
            if (monstersDefeated === questTarget) {
                heroLevel++; document.getElementById('hero-level').innerText = heroLevel;
                document.getElementById('insta-ad').style.display = 'block';
                document.getElementById('quest-text').innerText = "تمت المهمة الـ 3D!";
            }
            currentMonsterIndex = (currentMonsterIndex + 1) % monsters.length;
            enemyMaxHp = monsters[currentMonsterIndex].hp + (heroLevel * 30); enemyHp = enemyMaxHp;
            const sprite = document.getElementById('enemy-sprite'); sprite.style.opacity = '0';
            setTimeout(() => {
                document.getElementById('enemy-name').innerText = monsters[currentMonsterIndex].name;
                sprite.innerText = monsters[currentMonsterIndex].sprite; sprite.style.opacity = '1';
                document.getElementById('enemy-hp-bar').style.width = '100%';
                document.getElementById('enemy-hp-text').innerText = 'HP: ' + enemyHp + '/' + enemyMaxHp;
            }, 400);
        }
        function resetGame() {
            heroLevel = 1; heroGold = 0; monstersDefeated = 0; currentMonsterIndex = 0; enemyMaxHp = 100; enemyHp = 100;
            document.getElementById('hero-level').innerText = 1; document.getElementById('hero-gold').innerText = 0;
            document.getElementById('quest-progress').innerText = 0; document.getElementById('quest-text').innerText = "هزم 3 ديال وحوش الغابة الرقمية!";
            document.getElementById('enemy-name').innerText = monsters[0].name; document.getElementById('enemy-sprite').innerText = monsters[0].sprite;
            document.getElementById('enemy-hp-bar').style.width = '100%'; document.getElementById('enemy-hp-text').innerText = 'HP: 100/100';
            document.getElementById('insta-ad').style.display = 'none';
        }
    </script>
</div>
"""

components.html(html_code, height=580)

st.markdown("---")
st.write("📢 **إشهار لدعم المبرمج الصغير:**")
startio_ad_html = f"""
<div style="display: flex; justify-content: center; align-items: center; min-height: 100px;">
    <script type="text/javascript" src="https://start.io"></script>
    <script type="text/javascript">
        startio.init("{STARTIO_ACCOUNT_ID}");
        startio.createBanner({{ container: document.body, width: 320, height: 50 }});
    </script>
</div>
"""
components.html(startio_ad_html, height=120)
