
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

client = get_client()
db = client.report
    
@st.experimental_memo
def giveme(company):
    
    mycol = db[company]
    collection = mycol.find()
    companydf = pd.DataFrame(collection)
    companydf = companydf.drop(columns=['_id'])
    return companydf


full = giveme('uhaul')
st.write(full)

fig = px.bar(full, x="Month"
             , y=['Desktop','Mobile'], title="Uhaul traffic"
            #labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)
