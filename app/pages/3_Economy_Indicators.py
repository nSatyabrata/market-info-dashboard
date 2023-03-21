import streamlit as st
import plotly.express as px
from indicators import indicators
from database.db import fetch_economy_indicator_data, init_connection

# page title
st.title("Economy Indicator")

# database connection
conn = init_connection()

# get news data
economy_data = fetch_economy_indicator_data(conn)

# country wise indicators
all_indicators = {
    'India' : {},
    'United States' : {}
}

for indicator in indicators:
    all_indicators[indicator['geo']].update(
        {f"{indicator['symbol']} - {indicator['name']}": indicator['symbol']}
    )

tab_in, tab_us = st.tabs([":flag-in: - **India**", ":flag-us: - **United States**"])

with tab_in:
    st.subheader("Indian economy indicators")

    option = st.selectbox(
        "**Choose an indicator**",
        all_indicators['India'].keys(),
        index=3
    )

    selected_indian_indicator = all_indicators['India'][option]
    st.line_chart(economy_data[selected_indian_indicator], x='dates', y='values')

with tab_us:
    st.subheader("United states economy indicators")

    option = st.selectbox(
        "**Choose an indicator**",
        all_indicators['United States'].keys(),
        index=2
    )

    selected_us_indicator = all_indicators['United States'][option]
    st.line_chart(economy_data[selected_us_indicator], x='dates', y='values')
