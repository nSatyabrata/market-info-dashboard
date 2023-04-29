import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import timedelta
from plotly.graph_objs import Figure
from app.config.indicators import INDICATORS
from app.utils.fetch_data import get_data


# page title
st.title("Economy Indicator")

economy_api_url = st.secrets.economy_data_api.url
economy_api_key = st.secrets.economy_data_api.key

economy_data = get_data(url=economy_api_url, key=economy_api_key)


@st.cache_data(show_spinner=False, ttl=timedelta(hours=1))
def country_wise_indicator_mapping(indicators: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    """
    Returns country wise economic indicator Name to symbol mapping.

    Args:
        indicators (list[dict[str, str]]): Indicators metadata.

    Returns:
        dict[str, dict[str, str]]: Mapping of countrywise name to symbol.
    """

    mapping = {"India": {}, "United States": {}}

    for indicator in indicators:
        name = indicator["name"].replace(f"{indicator['geo']} - ", "")
        symbol = indicator["symbol"]
        mapping[indicator["geo"]].update({name: symbol})
    
    return mapping


def create_indicator_graph(data: pd.DataFrame, plot_title: str, x_name: str, y_name: str):
    """
        Using given data returns a plot.

    Args:
        data (dict): The data to plot.
        plot_title (str): A title for plot.
        x_name (str): X axis name
        y_name (str): Y axis name
    """
    fig: Figure = px.line(data_frame=data, x="dates", y="values")

    fig.update_layout(
        xaxis_title=x_name,
        yaxis_title=y_name,
        title_text=plot_title,
        title_font_size=30,
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


all_indicators = country_wise_indicator_mapping(indicators=INDICATORS)

tab_in, tab_us = st.tabs([":flag-in: - **India**", ":flag-us: - **United States**"])

with tab_in:
    st.subheader("Indian economy indicators")

    option = st.selectbox(
        "**Choose an indicator**", all_indicators["India"].keys(), index=3
    )

    selected_indian_indicator = all_indicators["India"][option]
    create_indicator_graph(
        data=economy_data[economy_data['ticker_name'] == selected_indian_indicator][['dates', 'values']],
        plot_title=option,
        x_name="X",
        y_name="Y",
    )

with tab_us:
    st.subheader("United states economy indicators")

    option = st.selectbox(
        "**Choose an indicator**", all_indicators["United States"].keys(), index=2
    )

    selected_us_indicator = all_indicators["United States"][option]
    create_indicator_graph(
        data=economy_data[economy_data['ticker_name'] == selected_indian_indicator][['dates', 'values']],
        plot_title=option,
        x_name="X",
        y_name="Y",
    )
