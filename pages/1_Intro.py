import streamlit as st

# Setari pagina
st.set_page_config(page_title="Intro - Cine e Big Cenco", page_icon="📖", layout="centered")

# --- MAGIA CSS PENTRU FUNDALUL BALATRO ---
# Folosim un gradient animat cu paleta de culori a lui Big Cenco (Mov, Roz, Sange)
st.markdown("""
<style>
    /* Tintim containerul principal al aplicatiei */
    .stApp {
        background: linear-gradient(-45deg, #4b0082, #ff1493, #8b0000, #800080);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
    }

    /* Animatia care plimba gradientul */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Umbra pe text ca sa poata fi citit pe fundalul care se misca */
    h1, h2, h3, p, li, span {
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
        color: white !important;
    }

    /* Facem containerele gen st.info si st.error putin transparente ca sa se vada fundalul prin ele */
    div[data-testid="stAlert"] {
        background-color: rgba(0, 0, 0, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Titlul principal cu un pic de stil
st.markdown("<h1 style='text-align: center;'>📖 Geneza: Cine este Big Cenco?</h1>", unsafe_allow_html=True)
st.divider()

# --- SPATIU PENTRU POZA TA ---
# Cand ai poza generata (ex: cenco_suprem.png), inlocuieste linia st.info de mai jos cu:
# st.image("assets/cenco_suprem.png", use_column_width=True, caption="Adevarata fata a perfectiunii")
st.image("assets/big_cenco_kawaii.jpg", caption="Adevarata fata a perfectiunii")
st.divider()

# Partea de definitie - Ubermensch-ul
st.subheader("Entitatea Absolută")
st.write("""
Big Cenco nu este doar un om, un simplu șef sau un lider oarecare. El este **legenda vie**, mitul umblător pe pământ, manifestarea în carne și oase a perfecțiunii. 

Vorbim despre *Übermensch*-ul suprem, superomul absolut. Pentru unii este profetul, pentru alții este mesia, iar pentru restul... anticristul în același timp. Este echilibrul perfect între lumină și întuneric.
""")

st.divider()

# Originile numelui si reputatiei
col_nume, col_rep = st.columns(2)

with col_nume:
    st.info(
        "⚽ **Originea Numelui** \n\nNumele de *Big Cenco* nu i-a fost dat de zei, ci a fost forjat pe teren. A venit, pur și simplu, **de la fotbal**.")

with col_rep:
    st.info(
        "🦫 **Sursa Reputației** \n\nȘi-a căpătat reputația și puterea absolută nu prin fapte de vitejie plictisitoare, ci prin **înțelegerile obscure făcute cu castorii**. Pactul rămâne un secret bine păstrat.")

st.divider()

# Cazierul si atrocitatile
st.subheader("Cazierul Istoric (A nu se citi noaptea)")
st.error("""
**Bilanțul oficial al victimelor și pagubelor colaterale:**
* Este responsabil pentru aproximativ majoritatea victimelor din foametea chinezească.
* **2 orașe** au fost eradicate complet de pe fața pământului dintr-un simplu capriciu.
* **50 de clădiri** bombardate (probabil se uita urât la ele).
* A lăsat o întreagă rasă de animale pe cale de dispariție.
* Este arhitectul din umbră din spatele **dispariției pisicilor portocalii**.
""")

st.divider()

# Profilul si preferintele
st.subheader("Profil Psihologic și Preferințe")

col1, col2 = st.columns(2)

with col1:
    st.markdown("🎵 **Melodia preferată:**")
    st.write("*Filmul R. Kelly cu dulapul (Trapped in the Closet)*")

    st.markdown("🎮 **Activitatea preferată:**")
    st.write("*League of Legends* (acolo unde sufletele se duc să fie distruse, el se duce să se relaxeze)")

with col2:
    st.markdown("🎨 **Paleta de culori a sufletului său:**")
    st.write("1. Mov pătrățele")
    st.write("2. Roz gaoz")
    st.write("3. Sânge de dușmani")

st.divider()

# Mostenirea
st.subheader("Moștenirea")
st.write(
    "👑 **Urmași / Moștenitori:** *Necunoscut*. Lumea pur și simplu nu este pregătită pentru o continuitate a acestei entități.")
st.write("🦆 **Dacă ar fi un joc video, ar fi:** *Duck Duck Goose* (pentru că doar el decide cine fuge și cine pică).")