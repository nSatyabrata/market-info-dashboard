import streamlit as st
import psycopg2
from indicators import indicators
from psycopg2.extensions import connection
from datetime import timedelta


class DatabaseOperationError(Exception):
    '''Custom exception for database operation error.'''
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionError(Exception):
    '''Custom exception for database connection error.'''
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


@st.cache_resource(show_spinner=False, ttl=timedelta(days=7))
def init_connection() -> connection:
    '''Get database connection.'''

    try:
        retries = 1
        while retries <= 3:
            try:
                conn = psycopg2.connect(**st.secrets["postgres"])
                return conn
            except:
                retries += 1
    except Exception as error:
        raise DatabaseConnectionError(error)


@st.cache_data(show_spinner=False, ttl=timedelta(hours=4))
def fetch_news_data(_db_connection: connection) -> dict:
    '''Get news data from database.'''

    sql_query = '''
        select 
            topic, 
            title, 
            url, 
            summary, 
            banner_image_url, 
            source 
        from market_news
    '''
    with _db_connection.cursor() as cur:
        cur.execute(sql_query)
        rows = cur.fetchall()

    topics = ["blockchain","earnings","ipo","mergers_and_acquisitions","financial_markets","economy_fiscal","economy_monetary","economy_macro","energy_transportation","finance","life_sciences","manufacturing","real_estate","retail_wholesale","technology"]

    data = {topic: [] for topic in topics}
    for row in rows:
        data[row[0]].append({'title': row[1],
                            'url': row[2],
                            'summary': row[3],
                            'banner_image_url': row[4],
                            'source': row[5]})
    return data


@st.cache_data(show_spinner=False)
def fetch_economy_indicator_data(_db_connection: connection) -> dict:
    '''Get economy indicator data from database.'''

    sql_query = '''
        select 
            ticker_name, 
            dates, 
            values 
        from economy_data
    '''
    with _db_connection.cursor() as cur:
        cur.execute(sql_query)
        rows = cur.fetchall()
    
    data = {indicator['symbol']: {'dates':[], 'values':[]} for indicator in indicators}
    for row in rows:
        data[row[0]]['dates'].append(row[1])
        data[row[0]]['values'].append(row[2])
    
    return data