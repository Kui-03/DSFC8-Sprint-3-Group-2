import pandas as pd
import numpy as np
import joblib as j
from models.seed_model import Seed
from models.classifier_model import Classifier
import streamlit as st

# Directory
DATA_clf = "db/clf_models/"
DATA_tra = "db/transformers/"
DATA_csv = "db/data/"

# Query track data csv list
CSV = ["abra.csv", "top200-genres.csv"]

# Class SeedService
class SeedService():
    # Init variables
    feature_cols    = None
    seed            = None
    scaler          = None
    classifier      = None

    # Initialize
    def __init__(self):
        self.load_scalers()
        self.classifier = Classifier()
        self.get_seed()

    # Load Scalers
    def load_scalers(self):
        getfeature_cols = ["tempo","loudness","acousticness","danceability","speechiness",
                   "energy","liveness","instrumentalness","key","mode"]
        sc={}
        for f in getfeature_cols:
            s = j.load(DATA_tra+"{0}.mdl".format(f))
            sc[f] = s

        self.feature_cols = getfeature_cols
        self.scaler = sc
        del s, sc

    # Scale track data
    def scale(self, df):
        for f in self.feature_cols:
            df[f] = self.scaler[f].transform(df[[f]])
        return df

    # Load the appropriate Seed data by query, sample: Tirador - Abra
    def get_seed(self, q=["0G3S4MVnjb8w30RZk04PI9"], col=["track_id"]):
        # Query from available CSV files
        for i, file in enumerate(CSV):
            df=pd.read_csv(DATA_csv+file)

            # Filter Query
            for index, getcol in enumerate(col):
                df = df[df[getcol] == q[index]]

            seed_track_data = df.head(1)
            if seed_track_data.shape[0] > 0: break

        # Generate Seed
        self.seed = Seed(seed_track_data.track_id)
        self.seed.data = seed_track_data
        self.seed.feature_cols = self.feature_cols

        # Scale data if main artist CSV file:
        if i == 0:
            self.seed.data = self.scale(self.seed.data)
            self.seed.data = self.classifier.predict(self.seed)

        del seed_track_data, df

