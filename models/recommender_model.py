import pandas as pd
import numpy as np

import streamlit as st
# # Directory
# DATA_csv = "db/data/"
# # Query tracks from CSV file
# CSV = ["top200-genres_RF.csv"]

# Class Recommender
class Recommender():
    tracks    = None

    # Initialize
    def __init__(self, csv):
        self.load_data(csv)

    def load_data(self, csv):
        self.tracks = pd.read_csv(csv)