import streamlit as st
import requests
import pandas as pd

st.title("🌙 Live SEO Traffic Hunter (Irtaza Fatima)")

# 1. Real-time Google Suggestion Scraper
def get_live_keywords(seed_keyword):
    # Ye Google ki api se real-time sawal nikaalta hai
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={seed_keyword}"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    suggestions = response.json()[1]
    return suggestions

st.subheader("🔥 Log Google par kya dhoond rahe hain?")
main_topic = st.text_input("Topic likhen (maslan: Istikhara):", "Istikhara")

if st.button("Asli Data Nikalo"):
    with st.spinner('Python Google se data nikaal raha hai...'):
        results = get_live_keywords(main_topic)
        
        if results:
            st.success(f"Python ne '{main_topic}' ke bare mein ye 10 sawal dhoonde hain:")
            for i, res in enumerate(results):
                st.write(f"{i+1}. **{res}**")
            
            st.info("💡 Advice: In mein se kisi ek par 5 lines WordPress par likh den.")
        else:
            st.error("Data nahi mil saka.")

# 2. Site Health Checker (Live)
st.subheader("🖥️ Site Check")
if st.button("Check my Site Status"):
    res = requests.get("https://onlineistikharaexpert.com")
    if res.status_code == 200:
        st.balloons()
        st.write("Aapki site live hai aur sahi kaam kar rahi hai!")
