
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.markdown("# Speakers 🔊")
st.sidebar.markdown("# Speakers 🔊")



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


sonos = giveme('sonos')
bose = giveme('bose')
jbl = giveme('jbl')
#st.write(full)

dict = {
    'Sonos':sonos,
    'Bose':bose,
    'JBL':jbl,

}


def graph(company):
    mm = dict[company].set_index('Month')
    x = mm.index
    x = pd.to_datetime(x).values.view(np.int64)
    y = mm.iloc[:, 0]
    p1 = np.polyfit(x,y,1)
    p1polyval = np.polyval(p1,x)
    p2 = np.polyfit(x,y,2)
    p2polyval = np.polyval(p2,x)
    p3 = np.polyfit(x,y,3)
    p3polyval = np.polyval(p3,x)

    fig = px.line(dict[company], x=x
                 , y=p1polyval, title=company+' traffic',#, trendline='lowess'
                #labels=dict(value="Average overall points", variable=p1polyval), height=600
                )
    fig.add_bar(x=x, y=y, name=company+' traffic')
    fig.add_traces(go.Scatter(x= x, y=p2polyval, mode = 'lines', name='p2'))
    fig.add_traces(go.Scatter(x= x, y=p3polyval, mode = 'lines', name='p3'))
    #fig.show()
    return fig


st.plotly_chart(graph('Sonos'), use_container_width=True)
st.plotly_chart(graph('Bose'), use_container_width=True)
st.plotly_chart(graph('JBL'), use_container_width=True)
