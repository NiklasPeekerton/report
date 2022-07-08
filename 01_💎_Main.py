
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("# Main 💎")
st.sidebar.markdown("# Main 💎")



#@st.cache()#hash_funcs={MongoClient: id}
def get_client():
    return MongoClient(**st.secrets["mongo"])

@st.experimental_memo
def giveme():
    client = get_client()
    db = client.report
    collection = db.traffic
    traffic = collection.find()
    trafficdf = pd.DataFrame(traffic)
    return trafficdf


full = giveme()
st.write(full)
