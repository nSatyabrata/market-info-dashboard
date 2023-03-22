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
    name = indicator['name'].replace(f"{indicator['geo']} - ", "")
    symbol = indicator['symbol']
    all_indicators[indicator['geo']].update({name: symbol})


def create_indicator_graph(data: dict, plot_title: str, x_name: str, y_name: str):
    '''Plot graph for given indicator data.'''

    fig = px.line(data_frame=data, x='dates', y='values')

    fig.update_layout(
        xaxis_title=x_name,
        yaxis_title=y_name,
        title_text=plot_title,
        title_font_size=30
    )

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

tab_in, tab_us = st.tabs([":flag-in: - **India**", ":flag-us: - **United States**"])

with tab_in:
    st.subheader("Indian economy indicators")

    option = st.selectbox(
        "**Choose an indicator**",
        all_indicators['India'].keys(),
        index=3
    )

    selected_indian_indicator = all_indicators['India'][option]
    create_indicator_graph(
        data=economy_data[selected_indian_indicator], 
        plot_title=option,
        x_name="X",
        y_name="Y"
    )

with tab_us:
    st.subheader("United states economy indicators")

    option = st.selectbox(
        "**Choose an indicator**",
        all_indicators['United States'].keys(),
        index=2
    )

    selected_us_indicator = all_indicators['United States'][option]
    create_indicator_graph(
        data=economy_data[selected_us_indicator], 
        plot_title=option,
        x_name="X",
        y_name="Y"
    )
