import streamlit as st
from PIL import Image



def display():
    st.title("ABRA: The Comeback")
    st.subheader('by Data Science Fellowship Cohort 8 - Sprint 3 - Group 2 (2FUSE)')
    st.write('Paolo, Kui, Ale, Selin, MaCris (mentored by Aaron)')
    
    title_slide = Image.open('Assets/Images/TitleSlide.PNG')
    
    st.write("")
    st.subheader("WHO IS ABRA?")
    st.write("https://abraofficial.com/")
    who = Image.open("Assets/Images/IntroAbra.PNG")
    st.image(who)

    st.write("")
    st.subheader("ABRA'S DISCOGRAPHY")
    discography = Image.open("Assets/Images/Discography.PNG")
    st.image(discography)
    st.markdown("For more Abra's works, go to: https://www.youtube.com/c/abraofficial/featured") 
    st.markdown("Listen to Abra's collaboration with Chito Miranda: https://youtu.be/9QcIo20wok0")

    st.write("")
    st.markdown("## Objectives")
    objectives = Image.open("Assets/Images/Objectives.PNG")
    st.image(objectives)

    top_pinoy_rappers = Image.open("Assets/Images/TopPinoyRappers.PNG")
    st.image(top_pinoy_rappers)