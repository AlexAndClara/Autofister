import streamlit as st

# App konfiguration
st.set_page_config(page_title="Erdwin Studentertrial/totur 🎓", page_icon="🎓")

# Session state for music start
if "music_started" not in st.session_state:
    st.session_state.music_started = False

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

# Start Quiz button
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("START QUIZZ", key="start_music_button", use_container_width=True):
        st.session_state.music_started = True

# Hidden audio player placeholder
st.components.v1.html(
    """
    <iframe
        id="audioPlayer"
        width="1"
        height="1"
        style="position:absolute; left:-9999px; opacity:0; display:none;"
        src=""
        frameborder="0"
        allow="autoplay; encrypted-media; picture-in-picture; accelerometer"
        allowfullscreen
    ></iframe>
    """,
    height=1,
    scrolling=False,
)

# Start music script when button is clicked
if st.session_state.music_started:
    st.components.v1.html(
        """
        <script>
            function startAudio() {
                console.log('startAudio called');
                var iframe = document.getElementById('audioPlayer');
                console.log('iframe found:', iframe);
                if (iframe) {
                    var url = 'https://www.youtube.com/embed/CteoJ3Q-6cU?list=RDCteoJ3Q-6cU&autoplay=1&loop=1&playlist=RDCteoJ3Q-6cU&controls=0&modestbranding=1&rel=0&playsinline=1&mute=0';
                    iframe.src = url;
                    console.log('src set to:', url);
                }
            }
            startAudio();
            setTimeout(startAudio, 50);
            setTimeout(startAudio, 200);
            setTimeout(startAudio, 500);
        </script>
        """,
        height=1,
        scrolling=False,
    )

# Only show quiz after button is clicked
if not st.session_state.music_started:
    st.stop()

# Initialize session state for questions
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}

# Define all questions
questions = [
    {
        "title": "Om dig",
        "question": "Hvor gammel er du?",
        "type": "radio",
        "options": ["A) 20", "B) 18", "C) 19", "D) 17", "E) Ingen ved"],
        "correct": "E"
    },
    {
        "title": "Drikke?",
        "question": "Hvor mange øl kommer du til at drikke idag",
        "type": "radio",
        "options": ["A) 239", "B) 20", "C) 1 (fat svag)", "D) 30"],
        "correct": "A"
    },
    {
        "title": "日本語",
        "question": "日本では、どんなフレーズを一番よく使いますか？",
        "type": "radio",
        "options": ["A) すみません", "B) よかったら、少し話さない？なんか、すごく気になってて。", "C) 私はハングリーネガダロ", "D) キャラメルラテをアイスで、シロップ多め、氷少なめでお願いします。"],
        "correct": "C"
    },
    {
        "title": "Ado",
        "question": "Ado har en sang der hedder 'where winds meet'",
        "type": "radio",
        "options": ["A) Ja", "B) Nej"],
        "correct": "A"
    },
    {
        "title": "Færdig?",
        "question": "Hvornår går vi hjem?",
        "type": "radio",
        "options": ["A) Kl. Når solen står op", "B) Kl.22:00", "C) Kl. 24:00", "D) Efter Kl. 03:00"],
        "correct": "D"
    },
    {
        "title": "Erwin",
        "question": "Se billedet og læs teksten om Erwin. Tryk videre, når du er klar.",
        "type": "info",
        "image": "https://media.discordapp.net/attachments/1016646559171104769/1517551712758530220/Screenshot_20260619_172658_Gallery.jpg?ex=6a38abeb&is=6a375a6b&hm=6b99c951ed4eabf6336239a4c4b3a531f1a1d14425db51fd1b5f21f1664e4cce&=&format=webp&width=864&height=1152",
        "text": "Erwin er bygget som en gren i modvind og har brugt flere timer på at male Warhammer-figurer end på at føre en samtale med en kvinde. Han siger 'god aften, m'lady' uden ironi og har en længere liste over Space Marine-kapitler end telefonnumre. Hans Snapchat-streaks er med de samme tre gutter, og hans største romantiske oplevelse var, da ekspedienten i Faraos Cigarer sagde: 'Vi ses næste uge.' Hvis charisma var en stat, havde han dumpet sit terningekast med en naturlig 1'er. Han er typen, der kan forklare hele Imperiets historie på 45 minutter, men får hjertebanken, hvis en pige spørger om klokken.",
    },
    {
        "title": "Predator",
        "question": "Hvem er IRL predator?",
        "type": "radio",
        "options": ["A) Erwin", "B) Epstein", "C) Griffith", "D) Ado"],
        "correct": "D"
    },
    {
        "title": "Inkognito?",
        "question": "Hvor mange inkognito-faner har du åben på din telefon?",
        "type": "radio",
        "options": ["A) 0 (ikke nogen, han har porno magaziner under sengen)", "B) 1-5", "C) 6-10", "D) 11+"],
        "correct": "A"
    },
    {
        "title": "tal",
        "question": "Hvad er det bedste tal?",
        "type": "radio",
        "options": ["A) 67", "B) 69", "C) 999", "D) 666"],
        "correct": "A"
    },
    {
        "title": "Peak",
        "question": "Hvad er peak?",
        "type": "radio",
        "options": ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"],
        "correct": "B"
    },
    {
        "title": "Ikke peak?",
        "question": "Hvad er ikke peak?",
        "type": "radio",
        "options": ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"],
        "correct": "A"
    },
    {
        "title": "Hvem?",
        "question": "Hvem er hvem?",
        "type": "radio",
        "options": ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"],
        "correct": "C"
    },
    {
        "title": "Halvvejs",
        "question": "Du er nu halvvejs gennem quizzen!",
        "type": "info",
        "text": "Godt gået! Du er nu halvvejs. Tryk videre for at fortsætte.",
    },
    {
        "title": "bust en nut",
        "question": "Lige så peak som at bust en nut?",
        "type": "radio",
        "options": ["A) Erwin", "B) Alex & Kristoffer", "C) Ado", "D) Blive rapet af Epstein"],
        "correct": "D"
    },
    {
        "title": "Billedet",
        "question": "Se billedet og læs teksten. Tryk videre, når du er klar.",
        "type": "info",
        "image": "https://static01.nyt.com/images/2019/08/18/nyregion/18epsteintictoc2/00epsteintictoc2-articleLarge.jpg?quality=75&auto=webp&disable=upscale",
        "text": "Her er billedet til spørgsmålet.",
    },
    {
        "title": "hmm",
        "question": "Er det her i virkeligheden sidste spørgsmål?",
        "type": "radio",
        "options": ["A) Ja", "B) Nej"],
        "correct": "B"
    },
    {
        "title": "Spil?",
        "question": "Hvad er det bedste spil?",
        "type": "radio",
        "options": ["A) League of Legends", "B) Minecraft", "C) Warhammer 40k", "D) Fortnite"],
        "correct": "B"
    },
    {
        "title": "Spørgsmål 4: Gaveindpakning",
        "question": "Hvor mange møtrikker blev brugt i indpakningen?",
        "type": "number",
        "correct": 138
    }
]

# Show current question
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.subheader(q["title"])
    
    if q["type"] == "number":
        answer = st.number_input(q["question"], min_value=0, max_value=200, step=1, key=f"q_{st.session_state.current_question}")
        st.session_state.scores[st.session_state.current_question] = answer
    elif q["type"] == "info":
        st.write(q["question"])
        if q.get("image"):
            st.image(q["image"], width=400)
        if q.get("text"):
            st.write(q["text"])
    else:
        answer = st.radio(q["question"], q["options"], key=f"q_{st.session_state.current_question}")
        if answer:
            st.session_state.scores[st.session_state.current_question] = answer
    
    # Show special extra content for certain question indices
    if st.session_state.current_question == 6:  # With Predator question
        st.components.v1.iframe(
            "https://tenor.com/embed/1538483505353367534",
            width=480,
            height=270,
        )
    
    if st.session_state.current_question == 7:  # After question 8
        st.components.v1.iframe(
            "https://tenor.com/embed/16727368109953357722",
            width=480,
            height=270,
        )
    
    # Next button
    col1, col2 = st.columns(2)
    with col2:
        if st.button("Næste spørgsmål →", key=f"next_{st.session_state.current_question}", use_container_width=True):
            st.session_state.current_question += 1
            st.rerun()
else:
    # Show results
    st.markdown("---")
    st.subheader("🎉 Resultat 🎉")
    
    # Calculate score
    score = 0
    for idx, q in enumerate(questions):
        if idx in st.session_state.scores:
            if q.get("type") == "number":
                if st.session_state.scores[idx] == q["correct"]:
                    score += 1
            else:
                if st.session_state.scores[idx].startswith(q["correct"]):
                    score += 1
    
    st.write(f"Du fik {score} ud af {len(questions)} rigtige!")
    
    if score >= len(questions) - 2:
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
    
    # Restart button
    if st.button("Start quizzen igen", use_container_width=True):
        st.session_state.current_question = 0
        st.session_state.scores = {}
        st.rerun()
