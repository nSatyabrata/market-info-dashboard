import streamlit as st
from app.utils.fetch_data import get_data


# Page title
st.title("Market News")

categories = {
    "Technology": "technology",
    "Science": "science",
    "Business": "business",
    "Health": "health",
}


#handling page number
def change_page_number(page_name: str):
    st.session_state[page_name] += 10


market_news_api_url = st.secrets.market_news_api.url
market_news_api_key = st.secrets.market_news_api.key

market_news_data = get_data(url=market_news_api_url, key=market_news_api_key)

tabs = st.tabs(categories.keys())

for category, tab in zip(categories.keys(),tabs):
    with tab:
        category_data = market_news_data[market_news_data["category"]==categories[category]]

        for data in category_data.iterrows():
            st.divider()
            st.title(body=data[1]['title'], anchor=False)
            data[1]['description']
            st.write(f"[{data[1]['source']}]({data[1]['url']})")
            # if data[4]:
            #     col1, col2 = st.columns([2,4])
            #     with col1:
            #         st.image(
            #             image=data[4],
            #             use_column_width=True,
            #         )
            #     with col2:
            #         st.write(data[0])
            #         st.markdown(f"[{data[3]}]({data[2]})")
