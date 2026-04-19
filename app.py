import streamlit as st
import pickle


model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Melodex", page_icon="🎵")

st.title("🎵 Melodex")
st.write("Classify song mood using ML")

st.markdown("### Enter Song Features")


energy = st.slider("Energy", 0.0, 1.0, 0.5)
tempo = st.slider("Tempo", 50, 200, 100)
valence = st.slider("Valence", 0.0, 1.0, 0.5)
danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)
loudness = st.slider("Loudness", -60.0, 0.0, -10.0)


if st.button("Predict Mood"):

    features = [[energy, tempo, valence, danceability, acousticness, loudness]]
    prediction = model.predict(features)[0]

    captions = {
        "Energetic": "⚡ Perfect for workouts",
        "Happy": "☀️ Uplifting vibes",
        "Calm": "🌊 Relax and chill",
        "Sad": "🌧️ Emotional mood"
    }

    st.success(f"Predicted Mood: {prediction}")
    st.write(captions[prediction])