import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="لعبة القتال والمهام", page_icon="⚔️", layout="centered")

# معرف حساب Start.io الحقيقي ديال آدم
STARTIO_ACCOUNT_ID = "124299136"

# تغيير لون الشاشة للون سومو فاتح وهادئ
st.markdown("""
    <style>
        .stApp { background-color: #FAEDCD !important; }
        h1, p, .stMarkdown { color: #3D3025 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("⚔️ لعبة ملاحم الأبطال: قتال ومهام! ⚔️")
st.write("✨ **تحديث جديد:** اضغط على أزرار الهجوم لضرب الوحوش، كمل المهام، واجمع الذهب! 🚀")

# كود اللعبة كامل بـ HTML + CSS + JS لتفادي مشاكل f-string فبايثون
html_code = """
<div style="font-family: 'Segoe UI', Tahoma, sans-serif; display: flex; flex-direction: column; align-items: center; background: #FAEDCD; padding: 10px; border-radius: 15px; direction: rtl;">
    
    <!-- 🏆 لوحة معلومات البطل والمهام -->
    <div style="display: flex; justify-content: space-between; width: 100%; max-width: 450px; background: #4E3629; color: white; padding: 15px; border-radius: 15px; box-shadow: 0 6px 12px rgba(0,0,0,0.2); margin-bottom: 15px;">
        <div>
            <h3 style="margin: 0; color: #f59e0b;">👤 البطل: آدم</h3>
            <p style="margin: 5px 0 0 0;">⭐ المستوى: <span id="hero-level">1</span></p>
            <p style="margin: 5px 0 0 0;">💰 الذهب: <span id="hero-gold" style="color: #f59e0b; font-weight: bold;">0</span></p>
        </div>
        <div style="text-align: left; border-right: 2px solid #D4A373; padding-right: 15px;">
            <h4 style="margin: 0; color: #10b981;">📜 المهمة الحالية:</h4>
            <p id="quest-text" style="margin: 5px 0 0 0; font-size: 14px;">هزم 3 ديال وحوش الغابة!</p>
            <p style="margin: 5px 0 0 0; font-size: 13px; color: #a7f3d0;">التقدم: <span id="quest-progress">0</span> / 3</p>
        </div>
    </div>

    <!-- 🎮 ساحة المعركة والمضاربة -->
    <div style="position: relative; display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%; max-width: 450px; height: 300px; background: #2b1d16; border-radius: 20px; border: 4px solid #4E3629; box-shadow: 0 12px 24px rgba(0,0,0,0.3); overflow: hidden;">
        
        <!-- طاقة الوحش -->
        <div style="width: 80%; background: #555; border-radius: 10px; height: 15px; margin-bottom: 10px; position: relative;">
            <div id="enemy-hp-bar" style="width: 100%; background: #ff4b4b; height: 100%; border-radius: 10px; transition: width 0.2s;"></div>
            <span id="enemy-hp-text" style="position: absolute; width: 100%; text-align: center; font-size: 11px; color: white; font-weight: bold; top: 0;">HP: 100/100</span>
        </div>
        
        <!-- اسم وصورة الوحش الافتراضية -->
        <h3 id="enemy-name" style="color: #ff4b4b; margin: 5px 0;">👹 وحش الغابة الأخضر</h3>
        <div id="enemy-sprite" style="font-size: 80px; margin: 20px 0; transition: transform 0.1s; user-select: none;">👹</div>
        
        <!-- نص الضربات المتطاير -->
        <div id="damage-pop" style="position: absolute; color: #ffeb3b; font-size: 30px; font-weight: bold; display: none; text-shadow: 2px 2px #000;">💥 -25</div>
    </div>

    <!-- 🕹️ أزرار الهجوم والمضاربة السريعة -->
    <div style="margin-top: 15px; display: flex; gap: 10px; width: 100%; max-width: 450px;">
        <button onclick="attack(20, 'سريع')" style="flex: 1; background: #ff4b4b; color: white; border: none; padding: 12px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 4px #b91c1c;">⚔️ هجوم سريع</button>
        <button onclick="attack(45, 'قوي')" style="flex: 1; background: #d97706; color: white; border: none; padding: 12px; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 4px #b45309;">💥 ضربة قاضية</button>
    </div>

    <button onclick="resetGame()" style="margin-top: 15px; background: transparent; color: #3D3025; border: 1px solid #3D3025; padding: 5px 10px; border-radius: 8px; cursor: pointer; font-size: 12px;">🔄 إعادة بدء المغامرة</button>

    <!-- 📸 إعلان إنستغرام الذكي عند إكمال المهام -->
    <div id="insta-ad" style="display: none; background-color: #FFFFFF; padding: 15px; border-radius: 15px; border-left: 5px solid #E1306C; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 15px; width: 90%;">
        <p style="font-size: 14px; margin: 0; color:#333;">📸 كملتي المهمة بنجاح! تابعنا في إنستغرام <strong style="color: #E1306C;">oughilas</strong> لتتوصل بالجديد! 🚀</p>
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
            { name: "👹 وحش الغابة الأخضر", sprite: "👹", hp: 100, gold: 20 },
            { name: "🐉 التنين الصخري الأسود", sprite: "🐉", hp: 180, gold: 50 },
            { name: "🤖 الآلي المقاتل المدمر", sprite: "🤖", hp: 250, gold: 90 }
        ];
        let currentMonsterIndex = 0;

        function attack(maxDmg, type) {
            if (enemyHp <= 0 || isAttacking) return;
            isAttacking = true;
            
            let dmg = Math.floor(Math.random() * 15) + (maxDmg - 10);
            enemyHp -= dmg;
            if (enemyHp < 0) enemyHp = 0;
            
            let hpPercent = (enemyHp / enemyMaxHp) * 100;
            document.getElementById('enemy-hp-bar').style.width = hpPercent + '%';
            document.getElementById('enemy-hp-text').innerText = 'HP: ' + enemyHp + '/' + enemyMaxHp;
            
            const sprite = document.getElementById('enemy-sprite');
            sprite.style.transform = "scale(0.8) rotate(10deg)";
            
            const pop = document.getElementById('damage-pop');
            pop.innerText = '💥 -' + dmg;
            pop.style.display = 'block';
            
            setTimeout(() => {
                sprite.style.transform = "scale(1) rotate(0deg)";
                pop.style.display = 'none';
                isAttacking = false;
                if (enemyHp <= 0) {
                    monsterDied();
                }
            }, 200);
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
                document.getElementById('quest-text').innerText = "تمت المهمة! تابع القتال الحر!";
            }
            
            currentMonsterIndex = (currentMonsterIndex + 1) % monsters.length;
            if (heroLevel > 1) {
                enemyMaxHp = monsters[currentMonsterIndex].hp + (heroLevel * 20);
            } else {
                enemyMaxHp = monsters[currentMonsterIndex].hp;
            }
            
            enemyHp = enemyMaxHp;
            
            setTimeout(() => {
                document.getElementById('enemy-name').innerText = monsters[currentMonsterIndex].name;
                document.getElementById('enemy-sprite').innerText = monsters[currentMonsterIndex].sprite;
                document.getElementById('enemy-hp-bar').style.width = '100%';
                document.getElementById('enemy-hp-text').innerText = 'HP: ' + enemyHp + '/' + enemyMaxHp;
            }, 500);
        }

        function resetGame() {
            heroLevel = 1;
            heroGold = 0;
            monstersDefeated = 0;
            currentMonsterIndex = 0;
            enemyMaxHp = 100;
            enemyHp = 100;
            
            document.getElementById('hero-level').innerText = heroLevel;
            document.getElementById('hero-gold').innerText = heroGold;
            document.getElementById('quest-progress').innerText = 0;
            document.getElementById('quest-text').innerText = "هزم 3 ديال وحوش الغابة!";
            document.getElementById('enemy-name').innerText = monsters[0].name;
            document.getElementById('enemy-sprite').innerText = monsters[0].sprite;
            document.getElementById('enemy-hp-bar').style.width = '100%';
            document.getElementById('enemy-hp-text').innerText = 'HP: 100/100';
            document.getElementById('insta-ad').style.display = 'none';
        }
    </script>
</div>
"""

components.html(html_code, height=560)

# --- 💰 مساحة إعلان Start.io للويب مربوطة بالـ ID ديالك بشكل نقي ---
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
