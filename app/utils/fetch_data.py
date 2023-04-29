# fetch_data.py
"""
Fetch data using API urls.
"""

from datetime import timedelta
import requests
import streamlit as st
import pandas as pd


@st.cache_data(show_spinner=False, ttl=timedelta(hours=1))
def get_data(url: str, key: str) -> pd.DataFrame:
    """
    Returns response data using given url and key.
    
    Args:
        url (str): A URL from where we are quering the data.
        key (str): Key to access the data.

    Returns:
        pd.DataFrame: Dataframe with records.
    """

    headers = {"apikey": key, "Authorization": "Bearer" + key}
    response = requests.get(url, headers=headers, timeout=10).json()
    data = pd.DataFrame(data=response)
    
    return data
