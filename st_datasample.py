# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : xx.py
# Time       ：2021/9/11 19:02
# Author     ：
# version    ：python 3.9
# Description：
"""
# CMD Run Command ： streamlit run /Users/xx.py --server.port 8501

import pandas as pd
import streamlit as st
from coding import input_sample
from coding import analysis

with st.sidebar:
    Username = st.text_input('Username', 'calvinish')
    Password = st.text_input('password', 'kKS8NAQmdgSqT1c8')


# Uses st.cache_resource to only run once.
@st.cache_resource
def get_mongo():
    return input_sample.get_mongodb(Username, Password)


@st.cache_resource
def get_col(db, col):
    items = client[db][col].find()
    items = list(items)
    return items


client = get_mongo()
with st.sidebar:
    db_name = st.selectbox('Database', client.list_database_names())
    col_name = st.selectbox('Collection', client[db_name].list_collection_names())
    #if st.button('Renew'):
    #    get_col.clear()
    st.write('current_db:', db_name)
    st.write('current_col:', col_name)

data = get_col(db_name, col_name)
df = pd.DataFrame(data)

st.dataframe(df.head())
des = analysis.df_des(df)
st.dataframe(des)

st.write('xin2')
keys = set(key for dict_ in data for key in dict_.keys())
st.write(list(keys))
value_name = st.text_input('value_name','')
values = []
for i in data:
    values.append(i[value_name])
st.dataframe(values)

