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
        st.experimental_memo.clear()

    # Load Scalers
    @st.experimental_memo(suppress_st_warning=True)
    def load_scalers(_self):
        getfeature_cols = ["tempo","loudness","acousticness","danceability","speechiness",
                   "energy","liveness","instrumentalness","key","mode"]
        sc={}
        for f in getfeature_cols:
            s = j.load(DATA_tra+"{0}.mdl".format(f))
            sc[f] = s
        _self.feature_cols = getfeature_cols
        _self.scaler = sc

    # Scale track data
    @st.experimental_memo(suppress_st_warning=True)
    def scale(_self, df):
        for f in _self.feature_cols:
            df[f] = _self.scaler[f].transform(df[[f]])
        return df

    # Load the appropriate Seed data by query, sample: Tirador - Abra
    @st.experimental_memo(suppress_st_warning=True)
    def get_seed(_self, q=["0G3S4MVnjb8w30RZk04PI9"], col=["track_id"]):
        # Query from available CSV files
        for i, file in enumerate(CSV):
            df=pd.read_csv(DATA_csv+file)

            # Filter Query
            for index, getcol in enumerate(col):
                df = df[df[getcol] == q[index]]

            seed_track_data = df.head(1)
            if seed_track_data.shape[0] > 0: break

        # Generate Seed
        _self.seed = Seed(seed_track_data.track_id)
        _self.seed.data = seed_track_data
        _self.seed.feature_cols = _self.feature_cols

        # Scale data if main artist CSV file:
        if i == 0:
            _self.seed.data = _self.scale(_self.seed.data)
            _self.seed.data = _self.classifier.predict(_self.seed)

        del seed_track_data, df

