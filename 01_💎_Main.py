
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
    trafficdf = trafficdf.drop(columns=['_id'])
    return trafficdf


full = giveme()
st.write(full)

fig = px.bar(full, x="Month"
             , y=['Desktop','Mobile'], title="test"
            #labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)
