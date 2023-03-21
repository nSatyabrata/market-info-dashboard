import streamlit as st
from database.db import fetch_news_data, init_connection

# Page title
st.title("Market News")

# database connection
conn = init_connection()

# get news data
news_data = fetch_news_data(conn)

len(news_data)