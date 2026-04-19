import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("model.pkl", "rb"))


df = pd.read_csv("dataset.csv")


df = df.drop(columns=['Unnamed: 0','track_id','album_name'])
df = df.dropna()


df_top = df.sort_values(by="popularity", ascending=False).head(50)


df_top['display'] = df_top['track_name'] + " - " + df_top['artists']

st.title("🎵 Melodex ")
st.write("Select a song to predict its mood")


song_display = st.selectbox("Choose a song", df_top['display'])

if st.button("Predict Mood"):

    
    song = df_top[df_top['display'] == song_display].iloc[0]

    
    features = [[
        song['energy'],
        song['tempo'],
        song['valence'],
        song['danceability'],
        song['acousticness'],
        song['loudness']
    ]]


    prediction = model.predict(features)[0]

    captions = {
        "Energetic": "⚡ Perfect for workouts",
        "Happy": "☀️ Uplifting vibes",
        "Calm": "🌊 Relax and chill",
        "Sad": "🌧️ Emotional mood"
    }

   
    st.success(f"🎯 Mood: {prediction}")
    st.write(captions[prediction])

    # Extra info (looks pro 🔥)
    st.markdown("### Song Details")
    st.write(f"**Song:** {song['track_name']}")
    st.write(f"**Artist:** {song['artists']}")
    st.write(f"**Popularity:** {song['popularity']}")