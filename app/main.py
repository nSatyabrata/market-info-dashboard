"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import time


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon=":newspaper:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

df


x = [i for i in range(2000)]
y = [i*10 for i in range(2000)]
# d = {i: [j*i for j in range(20000)] for i in range(500)}
st.checkbox("Use container width", value=False, key="use_container_width")
st.checkbox("Search through dataframe")
st.dataframe({"X": x, "Y": y}, use_container_width=st.session_state.use_container_width)
# st.dataframe(d)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    # with st.spinner("Loading..."):
    #     time.sleep(1)
    st.success("Done!")

'xyz'