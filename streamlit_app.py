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

st.image(
    "https://media.discordapp.net/attachments/1016646559171104769/1517551712758530220/Screenshot_20260619_172658_Gallery.jpg?ex=6a38abeb&is=6a375a6b&hm=6b99c951ed4eabf6336239a4c4b3a531f1a1d14425db51fd1b5f21f1664e4cce&=&format=webp&width=864&height=1152",
    width=400,
)
st.write("Erwin er bygget som en gren i modvind og har brugt flere timer på at male Warhammer-figurer end på at føre en samtale med en kvinde. Han siger 'god aften, m'lady' uden ironi og har en længere liste over Space Marine-kapitler end telefonnumre. Hans Snapchat-streaks er med de samme tre gutter, og hans største romantiske oplevelse var, da ekspedienten i Faraos Cigarer sagde: 'Vi ses næste uge.' Hvis charisma var en stat, havde han dumpet sit terningekast med en naturlig 1'er. Han er typen, der kan forklare hele Imperiets historie på 45 minutter, men får hjertebanken, hvis en pige spørger om klokken.")

st.subheader("Predator")
q6 = st.radio(
    "Hvem er IRL predator?",
    ["A) Erwin", "B) Epstein", "C) Griffith", "D) Ado"]
)
if q6.startswith("B"):
    score += 1
st.components.v1.iframe(
    "https://tenor.com/embed/1538483505353367534",
    width=480,
    height=270,
)

st.subheader("Inkognito?")
q7 = st.radio(
    "Hvor mange inkognito-faner har du åben på din telefon?",
    ["A) 0 (ikke nogen porno magaziner under sengen)", "B) 1-5", "C) 6-10", "D) 11+"]
)
if q7.startswith("A"):
    score += 1
st.subheader("tal")
q8 = st.radio(
    "Hvad er det bedste tal?",
    ["A) 67", "B) 69", "C) 999", "D) 666"]
)
if q8.startswith("A"):
    score += 1
st.components.v1.iframe(
    "https://tenor.com/embed/16727368109953357722",
    width=480,
    height=270,
)
st.subheader("Peak")
q9 = st.radio(
    "Hvad er peak?",
    ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"]
)
if q9.startswith("B"):
    score += 1
st.subheader("Ikke peak?")
q10 = st.radio(
    "Hvad er ikke peak?",
    ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"]
)
if q10.startswith("A"):
    score += 1
st.subheader("Hvem?")
q11 = st.radio(
    "Hvem er hvem?",
    ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"]
)
if q11.startswith("C"):
    score += 1
st.subheader("bust en nut")
q12 = st.radio(
    "Lige så peak som at bust en nut?",
    ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"]
)
if q12.startswith("D"):
    score += 1

st.image(
    "https://static01.nyt.com/images/2019/08/18/nyregion/18epsteintictoc2/00epsteintictoc2-articleLarge.jpg",
    width=400,
)

st.write("du er nu halvvejs")

st.subheader("hmm")
q13 = st.radio(
    "Er det her i virkeligheden sidste spørgsmål?",
    ["A) Ja", "B) Nej"]
)
if q13.startswith("B"):
    score += 1
st.subheader("Spil?")
q14 = st.radio(
    "Hvad er det bedste spil?",
    ["A) League of Legends", "B) Minecraft", "C) Warhammer 40k", "D) Fortnite"]
)
if q14.startswith("B"):
    score += 1
st.components.v1.html(
    """
    <script>
        function startAudio() {
            var iframe = document.querySelector('iframe[src*="youtube.com/embed"]');
            if (iframe) {
                iframe.src += (iframe.src.indexOf('?') > -1 ? '&' : '?') + 'autoplay=1';
            }
        }
        window.addEventListener('load', startAudio);
        document.addEventListener('DOMContentLoaded', startAudio);
        setTimeout(startAudio, 100);
        setTimeout(startAudio, 500);
        setTimeout(startAudio, 1000);
    </script>
    <iframe
        id="audioPlayer"
        width="1"
        height="1"
        style="position:absolute; left:-9999px; opacity:0; display:none;"
        src="https://www.youtube.com/embed/CteoJ3Q-6cU?autoplay=1&loop=1&playlist=CteoJ3Q-6cU&controls=0&modestbranding=1&rel=0&playsinline=1&start=0&mute=0"
        frameborder="0"
        allow="autoplay; encrypted-media; picture-in-picture; accelerometer"
        allowfullscreen
    ></iframe>
    """,
    height=1,
    scrolling=False,
)
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
