import streamlit as st
from PIL import Image


def display():
    st.write("")
    st.markdown("# Methodology")

    # Forecasting
    st.markdown("## Forecasting")
    forecasting = Image.open("Assets/Images/Method_Forecasting.PNG")
    st.image(forecasting)

    text = " - Forecasting used data from PH Daily Top 200 Charts, and the downloaded Hiphop playlist data."
    st.markdown(text)
    text = " - A time series was generated from the number of streams from 2017-2021."
    st.markdown(text)
    text = " - From the data, the team designed different models to forecast Hiphop streams: **ARIMA**, **ExponentialSmoothing**, **and XGBRegressor**."
    st.markdown(text)

    # Recommender
    st.markdown("## Recommender Engine")
    reco_engine = Image.open("Assets/Images/Method_RecoEngine.PNG")
    st.image(reco_engine)

    st.markdown("### Genre Classifier")
    text = " - A genre classifier was first designed to predict genre probabilities. \n- Classification models like: **KNN, SVM, Random Forest and XGBoost Classifier** were used."
    st.markdown(text)
    text = " - Data was obtained from user playlists of the following genres like: **R&B, Pop, Hiphop, Hard rock, and Funk**."
    st.markdown(text)
    text = " - To predict a genre, the models used audio features like: **tempo, loudness, acousticness, danceability, speechiness, energy, liveness, instrumentalness, key, and mode**."
    st.markdown(text)
    text = " - Features were scaled prior to training the models, then the best model was evaluated using *F1 score*."
    st.markdown(text)
    st.image("Assets/Images/xgb.png")
    st.markdown(" - The Recommender engine used **XGBoost** Classifier with an F-1 Score of 66%.")
    #st.image("Assets/Images/feature_importance.png")
    # st.markdown(" - Tempo, loudness, and acousticness were top features for predicting genres")



    st.markdown("### Distance metrics")
    text = " - Genre probabilities were obtained from the best model and was added as a parameter for distance calculations."
    st.markdown(text)
    text = " - The recommender then used **cosine**, **manhattan**, and **euclidean** distances to evaluate the tracks. \n- Finally, a list of top recommended tracks were generated from the seed track."
    st.markdown(text)


    