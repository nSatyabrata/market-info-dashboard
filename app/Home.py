import streamlit as st
from app.utils.fetch_data import get_data


st.set_page_config(
    page_title="News App",
    page_icon=":newspaper:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)
