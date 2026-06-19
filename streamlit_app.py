import streamlit as st

# App konfiguration
st.set_page_config(page_title="Erdwin Studentertrial/totur 🎓", page_icon="🎓")

# Farver og stil
st.markdown(
    """
    <style>
    .big-font {
        font-size:28px !important;
        color: #C1121F;
    }
    .emoji {
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titel og intro
st.markdown('<p class="big-font">🎓 Tillykke med huen, Erdwin! 🎓</p>', unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/1/15/Dansk_student_hue.png", width=150)
st.write("Tillyke med huen Erdwin")
st.write("Velkommen til din helt egen quiz – en lille del af din studentergave fra dine ynglings venner, der altid vil dig kun godt :). 🎁")
st.write("Vi er glade for, at du har gennemført gymnasiet og har klaret dig godt untagen idræt...! 👏")

# Introslider
gladhed = st.slider("På en skala fra 1-10, hvor glad er du for at være færdig med gymnasiet? 🎓", 1, 10)

# Dynamisk respons baseret på valg
if gladhed < 5:
    st.write("😅 Hmm... du kunne vist godt være lidt gladere.")
elif 5 <= gladhed <= 7:
    st.write("😊 Det lyder som en lettelse – godt gået!")
else:
    st.write("🎉 Fantastisk! Det har du også fortjent.")

st.markdown("---")

# Spørgsmål og svar
score = 0

st.subheader("Om dig")
q1 = st.radio(
    "Hvor gammel er du?",
    ["A) 20", "B) 18", "C) 19", "D) 17", "E) Ingen ved"]
)
if q1.startswith("E"):
    score += 1

st.subheader("Drikke?")
q2 = st.radio(
    "Hvor mange øl kommer du til at drikke idag",
    ["A) 239", "B) 20", "C) 1 (fat svag)", "D) 30"]
)
if q2.startswith("A"):
    score += 1
    st.write("🎉 Fantastisk! Det har du også fortjent.")
elif q2.startswith("B"):
    st.write("😅 Hmm... er det ikke lidt for lidt.")
elif q2.startswith("C"):
    st.write("😊 Hvad fuck er det, ain't no way!")
elif q2.startswith("D"):
    st.write("Det var lidt bedre, men er det virkelig nok?.")

st.subheader("日本語")
q3 = st.radio(
    "日本では、どんなフレーズを一番よく使いますか？",
    ["A) すみません", "B) よかったら、少し話さない？なんか、すごく気になってて。", "C) 私はハングリーネガダロ", "D) キャラメルラテをアイスで、シロップ多め、氷少なめでお願いします。"]
)
if q3.startswith("C"):
    score += 1
st.subheader("Ado")
q4 = st.radio(
    "Ado har en sang der hedder 'where winds meet'",
    ["A) Ja", "B) Nej"]
)
if q4.startswith("A"):
    score += 1
st.subheader("Færdig?")
q5 = st.radio(
    "Hvornår går vi hjem?",
    ["A) Kl. Når solen står op", "B) Kl.22:00", "C) Kl. 24:00", "D) Efter Kl. 03:00"]
)
if q5.startswith("D"):
    score += 1
st.image ("https://media.discordapp.net/attachments/1016646559171104769/1517551712758530220/Screenshot_20260619_172658_Gallery.jpg?ex=6a36b1ab&is=6a35602b&hm=e9ff9b0f66d58b993afc31b44dfe40ba8118c8f1519213bb2f54b1b68bed6521&=&format=webp&width=864&height=1152")    
  
st.subheader("Spørgsmål 4: Gaveindpakning")
q = st.number_input("Hvor mange møtrikker blev brugt i indpakningen?", min_value=0, max_value=100, step=1)
if q == 50:
    score += 1

st.subheader("Spørgsmål 5: Berserk – karakter")
q5 = st.radio(
    "Hvilken af disse karakterer i Berserk bliver kendt som 'The White Hawk'?",
    ["A) Guts", "B) Skull Knight", "C) Griffith", "D) Serpico"]
)
if q5.startswith("C"):
    score += 1

st.markdown("---")

# Resultat
if st.button("🔐 Vis resultat"):
    st.subheader("🎉 Resultat 🎉")
    st.write(f"Du fik {score} ud af 5 rigtige!")
    
    if score >= 4:
        st.success("Tillykke – du har gennemført quizen! 🎉")

        st.markdown(
            """
Vi er glade for, at du har gennemført gymnasiet og har klaret dig godt – det er virkelig sejt gået.  
Gaven er et tilskud til dine fremtidsplaner fra os tre – **Ulla, Niels og Asbjørn** – og vi ønsker dig alt det bedste i det næste kapitel.

Uanset om fremtiden byder på en rejse til Japan eller et kørekort, så håber vi, du får et fantastisk sabbatår og et stærkt afsæt videre. 🌞✈️🚗

**TILLYKKE, Kristoffer!** 🎓🇩🇰❤️

Tak fordi du legede med – og tillykke igen fra os alle tre! 💸🎈
            """
        )
    else:
        st.warning("Hmm, prøv igen og se, om du kan få adgang til gaven... 😉")
