import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
from PIL import Image

import plotly.express as px

def display():
    st.header("Time Series Analysis and Forecasting")

    st.markdown("""
How will hip-hop fare in the future?
To answer this question, let's evaluate its total performance
in terms of the Spotify Top 200 charts. 

The group extracted data from playlists that are marked as hip-hop
and the Spotify Top 200 daily charts data from 2017-2021 which they merged
to get the songs in the Spotify Top 200 daily charts data which are hip-hop

Thh group then summed the data to get a time series of the sum of the number
of streams of hip-hop songs in that Top 200. Below is the time series generated.
    """)

    data = pd.read_csv(
        os.getcwd()+'/data/daily_charts/hiphop_daily_charts.csv'
    )

    data['date'] = pd.to_datetime(data['date'])

    # st.table(data)

    fig = px.line(data, x='date', y='streams', title='Spotify Hiphop Daily Charts')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
Feel Free to interact with the time series to see some interesting points.

In the time series, we see interesting points:

1. A Sudden shift in the number of streams of hip-hop in between the end of 2019 and the start of 2020
2. A sudden spike in hiphop streams at December 31, 2020

First lets analyze that sudden shift in the data starting around late November 2019
    """)

    st.subheader("The Sudden Shift in the Number of Streams in the Hip-hop Genre")

    st.markdown("""
Let's check the data from the 15th of every month from November 2019 to January 2020. The data is shown below:
    """)

    nov = pd.read_csv(
        os.getcwd()+'/data/daily_charts/hiphop_playlist_nov_15_2019.csv'
    )[['date', 'position', 'track_name', 'artist', 'streams']]

    dec = pd.read_csv(
        os.getcwd()+'/data/daily_charts/hiphop_playlist_dec_15_2019.csv'
    )[['date', 'position', 'track_name', 'artist', 'streams']]

    jan = pd.read_csv(
        os.getcwd()+'/data/daily_charts/hiphop_playlist_jan_15_2020.csv'
    )[['date', 'position', 'track_name', 'artist', 'streams']]

    feb = pd.read_csv(
        os.getcwd()+'/data/daily_charts/hiphop_playlist_feb_15_2020.csv'
    )[['date', 'position', 'track_name', 'artist', 'streams']]

    st.write("Table 1a: Hiphop activity on November 15, 2019")
    st.table(nov)

    st.write("Table 1b: Hiphop activity on December 15, 2019")
    st.table(dec)

    st.write("Table 1c: Hiphop activity on January 15, 2020")
    st.table(jan)

    st.write("Table 1d: Hiphop activity on February 15, 2020")
    st.table(feb)

    st.markdown("""
From the above data, we can see the following observations:

1. At around November, it was just 2 artists contributing to the total number of streams.
2. By January, we see a significant increase in the number of songs and artists contributing to the sum.

The sudden shift can be explained in 2 ways:

1. People suddenly had an appreciation for hiphop and their songs
2. Hiphop artists gradually increased in number by 2020. 
    """)

    st.subheader("The Sudden spike at December 31, 2020")

    st.markdown("""
The data found in december 31, 2020 is shown as follows:
    """)

    dec_31 = pd.read_csv(
        os.getcwd()+'/data/daily_charts/hiphop_playlist_dec_31_2020.csv'
    )[['date', 'position', 'track_name', 'artist', 'streams']]

    st.table(dec_31)

    st.markdown("""
As we can see, there is a significant number of artists contributing to the sum of the number of streams like Lil Nas X, Drake, and Pop Smoke.
However, it is important to also consider the date and the condition this date was in. December 31, 2020 was the first new years
where the world is under lockdown from COVID-19 thus new years celebrations with families were not possible. 

Hip-hop songs are often party songs or known as "Hype", and it seems to be apt in its use in a new year's celebration. As substitute to a normal party outside,
there is an increase in streams through zoom using spotify or streams from people who celebrated alone or with a small group of people.

In short, no party = no party music. What is the substitute for this? Hiphop music.
    """)

    st.header("Time Series Forecasting")

    st.markdown("""
Given those points, where then is Hiphop heading? Being under a subgenre of hiphop, we want to see a possible upper bound in our client, ABRA's number of streams and popularity.

The group tried to forecast the trend of the total sum of Hiphop in the next month to see where they will go.
We created 3 Models that would help get us this insight:

1. ARIMA
2. ExponentialSmoothing
3. XGBRegressor

First, let's check how their forecasts compare to true values.
    """)

    arima_valid = Image.open(os.getcwd()+'/Assets/Images/ARIMA_validation.jpg')
    exponential_valid = Image.open(os.getcwd()+'/Assets/Images/Expo_Validation.jpg')
    ml_valid = Image.open(os.getcwd()+'/Assets/Images/ML_Validation.jpg')

    st.image(arima_valid, caption="ARIMA Validation Performance")
    st.image(exponential_valid, caption="Exponential Smoothing Validation Performance")
    st.image(ml_valid, caption="XGBoost Validation Performance")

    st.markdown("""
As we can see, The XGBoost was able to learn a very close estimate of the trend using walk_forward_validation.
There is a big anomaly present in the Valid Set namely the big gap between September to October. This was a limitation
on the ML Model. Perhaps more engineering is required for the ML Model to learn the spike.

Using the XGBoost Model, we are able to forecast where hiphop will be going for the next month
    """)

    ml_fore = Image.open(os.getcwd()+'/Assets/Images/ML_Forecast.jpg')

    st.image(ml_fore, caption="Hiphop Number of Streams forecast for the next month")

    st.markdown("""
After 2 months, it plateau at around 230000 streams for the genre. In the next month, 
the model predicts that the number of streams of hiphop would hover around 235,000 then plummet to 220,000 then
settle at around 230,000 streams.

This result tells us that the future of hiphop is bright. Having a consistent amount of streams, 
means that any artist pursuing this genre is likely to arrive at this boundary of 230,000 streams.

As for ABRA, this tells us that there is still a lot more to improve in terms of streams.
If he continues on this path, he can garner at most an average of 230,000 streams until next month!
    """)





    

