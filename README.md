# 🎵 Melodex 

### Song Mood Classification using Machine Learning

---

## 📌 Project Overview

Melodex is a machine learning-based project that classifies songs into different emotional moods  **Energetic, Happy, Calm, and Sad**  using audio features from a Spotify dataset. The system combines data preprocessing, feature engineering, and a Decision Tree classifier, along with a simple interactive interface for demonstration.

---

## 🧠 Problem Statement

Music plays a significant role in influencing human emotions. However, automatically identifying the emotional tone of a song is challenging.

This project aims to:

* Analyze song metadata (audio features)
* Classify songs into emotional categories
* Provide an interactive way to explore predictions

---

## 📊 Dataset

* Source: Kaggle Spotify Songs Dataset
* Format: CSV file
* Imported using **pandas**

### Original Features Included:

```
'Unnamed: 0', 'track_id', 'artists', 'album_name', 'track_name',
'popularity', 'duration_ms', 'explicit', 'danceability', 'energy',
'key', 'loudness', 'mode', 'speechiness', 'acousticness',
'instrumentalness', 'liveness', 'valence', 'tempo',
'time_signature', 'track_genre'
```

---

## 🧹 Data Preprocessing

### Removed Unnecessary Columns (Noise Reduction):

```
'Unnamed: 0', 'track_id', 'artists', 'album_name', 'track_name'
```

### Selected Relevant Features for Training:

```
'energy',
'tempo',
'valence',
'danceability',
'acousticness',
'loudness',
'speechiness',
'instrumentalness',
'liveness'
```

These features represent the **audio characteristics** of songs and are most relevant for mood detection.

---

## 🏷️ Feature Engineering (Mood Label Creation)

Since the dataset did not include mood labels, we created a new target variable **`mood`** using rule based logic based on audio features.

### Initial Distribution:

```
Happy       80769
Sad         16983
Energetic   14548
Calm         1700
```

---

## ⚠️ Problem: Imbalanced Dataset

* “Happy” class dominated the dataset
* “Calm” class had very low representation

### Issue:

This causes **model bias**, where predictions would mostly be “Happy”.

---

## ⚖️ Solution: Dataset Balancing

We applied **undersampling** to balance class distribution.

### Final Balanced Dataset:

```
Calm        1700
Energetic   1700
Happy       1700
Sad         1700
```

This ensures fair learning and prevents bias.

---

## 🤖 Machine Learning Model

* **Type:** Supervised Learning
* **Problem Type:** Classification
* **Algorithm Used:** Decision Tree Classifier

### Why Decision Tree?

* Easy to understand and interpret
* Works well with structured data
* Suitable for rule-based patterns

---

## 📈 Model Performance

* **Accuracy:** `0.9992647058823529` (~99.9%)

### Explanation:

The high accuracy is due to:

* Clearly defined decision boundaries
* Labels generated using rule-based logic

> The model effectively learned the patterns used to create the labels.

---

## 💻 Interface

A simple interface was built using **Streamlit** to:

* Select songs from a dropdown (top popular songs)
* Predict mood using trained ML model
* Display results with captions and song details

---

## 🎯 Features

* Clean and processed dataset
* Balanced class distribution
* Machine learning-based classification
* Interactive UI for demonstration
* Real-time prediction

---

## 🚀 Future Improvements

* Use real labeled datasets instead of rule based labels
* Integrate Spotify API for real-time song input
* Use advanced models (Random Forest, Neural Networks)
* Improve UI/UX design

---

## 🧠 Conclusion

Melodex AI demonstrates how machine learning can be used to interpret emotional patterns in music using audio features. The project highlights key ML concepts such as preprocessing, feature selection, handling imbalanced data, and model deployment.

---

## 👥 Team

Harshwardhan Chhangani
Arush Jain
Akshan Paunikar
Abhas Naite

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## ▶️ How to Run

```bash
pip install streamlit scikit-learn pandas
streamlit run app.py
```

---

## 📌 Final Note

This project combines both **data science and practical implementation**, making it a strong foundation for future AI/ML systems.

---

