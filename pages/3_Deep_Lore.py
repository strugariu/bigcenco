import streamlit as st

# Setari pagina
st.set_page_config(page_title="Deep Lore", page_icon="🕵️‍♂️", layout="centered")

# Titlu
st.markdown("<h1 style='text-align: center; color: #8b0000;'>🕵️‍♂️ Deep Lore: Dincolo de legendă</h1>", unsafe_allow_html=True)
st.divider()

# --- 1. Viata fara Big Cenco ---
st.subheader("🌑 Viața fără Big Cenco")
st.error("""
Un peisaj dezolant. O eroare în matrice. Un abis fără fund.
Viața fără Big Cenco **este tortură pură**. Soarele ar refuza să răsară, iar berea s-ar încălzi instantaneu în pahar. Omenirea nu este pregătită pentru un astfel de scenariu apocaliptic.
""")

st.divider()

# --- 2. Grupul MAAC ---
st.subheader("📂 Grupul MAAC")
st.warning("🚧 **DOSAR CLASIFICAT - WORK IN PROGRESS** 🚧 \n\n*Informațiile despre Grupul MAAC sunt prea periculoase pentru a fi expuse momentan. Doar cei inițiați vor înțelege.*")

st.divider()

# --- 3. O zi din viata lui ---
st.subheader("⏱️ O zi din viața lui Big Cenco")
st.write("Pentru un muritor, e o viață întreagă. Pentru Big Cenco, e doar o marți obișnuită.")

# Folosim blockquote-uri pentru un efect de timeline
st.markdown("""
> **05:00** – Se trezește. (Soarele cere permisiunea să răsară).
>
> **05:05** – Face 10 flotări. (Nu se ridică el, ci împinge Pământul în jos).
>
> **06:00** – Îi face temele Mariei. 
>
> **10:00** – Merge la fotbal. Rupe glezne și distruge cariere.
>
> **14:00** – Salvează 3 copii de la înec. În același timp. Fără să se ude.
>
> **16:00** – Merge la înmormântarea lui Vlad Boscencu. (F în chat). 🪦
>
> **18:00** – Merge la călărit cu Brad Pitt. Brad Pitt e cel care ține calul.
>
> **20:00** – Vindecă orbii.
>
> **23:00** – Bea o bere și se culcă.
""")

st.divider()

# --- 4. Provocari si rezolvari ---
st.subheader("⚔️ Provocările și Rezolvările")
col_prov, col_rez = st.columns(2)

with col_prov:
    st.markdown("### Ce îi stă în cale?")
    st.write("Homosexualii si ungurii (tot aia).")

with col_rez:
    st.markdown("### Cum se rezolvă?")
    st.write("Nu stă la discuții. **Îi dezintegrează pe toți.** Dă delete la fișierele lor din univers.")