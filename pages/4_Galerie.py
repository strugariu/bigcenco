import streamlit as st
import random

# Setari pagina
st.set_page_config(page_title="Arhiva MAAC - Galerie", page_icon="📸", layout="wide")

st.markdown("<h1 style='text-align: center;'>📸 Arhiva Clasificată</h1>", unsafe_allow_html=True)
st.write("Aici sunt documentate vizual momentele de grație ale Marelui Big Cenco. Ordinea pozelor este aleatorie, pentru că Big Cenco nu urmează un timeline liniar ca noi, muritorii.")
st.divider()

# Lista masiva de poze + descrierile aferente
galerie = [
    # --- POZELE ORIGINALE ---
    {
        "path": "assets/real_foc.jpg",
        "caption": "🔥 Big Cenco controlând elementul focului prin simplă telepatie."
    },
    {
        "path": "assets/real_trabuc.jpg",
        "caption": "🚬 Savurând trabucul victoriei după ce a mai șters un oraș de pe hartă."
    },
    {
        "path": "assets/real_munte.jpg",
        "caption": "⛰️ Big Cenco pe munte, acceptând ofrande de la muritorii de rând."
    },
    {
        "path": "assets/big_cenco_mog.jpg",
        "caption": "👁️ Big Cenco judecând aspru și privindu-i pe toți de sus."
    },

    # --- POZELE AI (Setul 1) ---
    {
        "path": "assets/gangster.png",
        "caption": "🔫 Rezolvând o 'dispută teritorială' pe străzi. Cu vorba bună, evident."
    },
    {
        "path": "assets/pescuit_1.png",
        "caption": "🦫 Pactul original cu castorii, parafat la o partidă relaxantă de pescuit de sturioni."
    },
    {
        "path": "assets/pescuit_2.png",
        "caption": "📜 Dovezile arheologice ale Entității Absolute, sculptate direct în stâncă."
    },
    {
        "path": "assets/bun_samaritean.png",
        "caption": "🍲 Big Cenco rezolvând foametea (probabil cea pe care tot el a provocat-o în prealabil)."
    },
    {
        "path": "assets/pilot.png",
        "caption": "✈️ Căpitanul Cenco la manșa zborului MAAC Airlines. Urmează turbulențe intenționate."
    },
    {
        "path": "assets/viego.png",
        "caption": "⚽ Transferul intergalactic: Semnând cu Regele Întunericului pentru echipa Castorilor."
    },
    {
        "path": "assets/satana.png",
        "caption": "🔥 Redactarea contractului stelar. Clauza 4: dispariția definitivă a pisicilor portocalii."
    },
    {
        "path": "assets/entitatea_absoluta.png",
        "caption": "🌌 Übermensch-ul suprem în habitatul său natural, jonglând cu planete, fulgere și o minge de fotbal."
    },
    {
        "path": "assets/prof.png",
        "caption": "🌹 Prof. Univ. Dr. Big Cenco predând 'Sexologie Academică'. Prezență obligatorie și 100%."
    },
    {
        "path": "assets/cercetator.png",
        "caption": "🧪 Cercetătorul Big Cenco sintetizând leacul pentru orbire folosindu-se doar de propriile lacrimi."
    },

    # --- POZELE AI (Setul 2 - Cele noi) ---
    {
        "path": "assets/red_carpet_2.png",
        "caption": "📸 Big Cenco pe covorul roșu, refuzând politicos un Oscar pentru că a depășit acest nivel."
    },
    {
        "path": "assets/sef.png",
        "caption": "🍹 Cenco's Beach Bar & Grill. Unde servește cocktailuri colorate și judecă aspru turiștii."
    },
    {
        "path": "assets/semnatura.png",
        "caption": "📖 Lansarea best-seller-ului 'Legende despre Big Cenco'. Autografe date cu milă pentru fanii de rând."
    },
    {
        "path": "assets/red_carpet.png",
        "caption": "🙌 'The Übermensch Event'. Fanii știu deja adevărul suprem: Big Cenco este Profetul."
    }
]

# Amestecam pozele random la fiecare refresh al paginii
random.shuffle(galerie)

# Afisam pozele pe 2 coloane
col1, col2 = st.columns(2)

for index, item in enumerate(galerie):
    try:
        # AICI AM SCHIMBAT use_column_width CU use_container_width PENTRU A SCAPA DE WARNING
        if index % 2 == 0:
            with col1:
                st.image(item["path"], caption=item["caption"], use_container_width=True)
        else:
            with col2:
                st.image(item["path"], caption=item["caption"], use_container_width=True)
    except FileNotFoundError:
        if index % 2 == 0:
            with col1:
                st.error(f"⚠️ Lipsă fișier: Te rog redenumește poza corespunzătoare în **{item['path']}**")
        else:
            with col2:
                st.error(f"⚠️ Lipsă fișier: Te rog redenumește poza corespunzătoare în **{item['path']}**")