import streamlit as st
import random

st.set_page_config(page_title="لعبة تخمين الأرقام", page_icon="🎲")
st.title("🎲 لعبة تخمين الأرقام الذكية!")
st.write("أنا مبرمج وعندي 10 سنوات، صاوبت هاد اللعبة باش نتحداكم! واش تقدروا تقشعوا الرقم اللي مخبي؟")

if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 20)

guess = st.number_input("اختار رقم بين 1 و 20:", min_value=1, max_value=20, step=1)

if st.button("تحقق من تخميني! 🚀"):
    if guess == st.session_state.secret_number:
        st.success(f"🎉 واااو! برافو عليك! الرقم الصحيح هو فعلاً {st.session_state.secret_number}! أنت ذكي جداً!")
        st.session_state.secret_number = random.randint(1, 20)
    elif guess < st.session_state.secret_number:
        st.warning("📉 هههه لا، الرقم اللي مخبي كبر من هادشي! جرب رقم كبر. 🆙")
    else:
        st.warning("📈 ممم لا، الرقم اللي مخبي صغر من هادشي! جرب رقم صغر. ⬇️")
