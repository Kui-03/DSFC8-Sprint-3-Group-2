import streamlit as st
from PIL import Image


def display():
    st.title("Conclusions and Recommendations")

    st.write("")
    st.subheader("Conclusion")
    st.write("")
    conclusion = Image.open("Assets\Images\Conclusion.PNG")
    st.image(conclusion)
    
    st.write("")
    st.subheader("Recommendations")
    recommendations = Image.open("Assets\Images\Recommendations.PNG")
    st.image(recommendations)