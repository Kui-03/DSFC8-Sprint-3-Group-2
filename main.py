import streamlit as st

from st_pages import conclusion, introduction, methodology, time_series
from st_pages.recommender import Recommender_Page

def initialize():
    PAGES = [
        'Introduction',
        'Methodology',
        'Time Series Analysis and Forecasting',
        'Recommendation Engine',
        'Conclusion and Recommendations'
    ]

    page = st.sidebar.radio("Page Navigation", PAGES)

    if page == 'Introduction':
        introduction.display()
    elif page == 'Methodology':
        methodology.display()
    elif page == 'Time Series Analysis and Forecasting':
        time_series.display()
    elif page == 'Recommendation Engine':
        on = Recommender_Page()
        #recommendation_engine.display()
    elif page == 'Conclusion and Recommendations':
        conclusion.display()

if __name__ == "__main__":
    initialize() 
