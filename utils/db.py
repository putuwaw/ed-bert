from sqlalchemy import create_engine
import streamlit as st


def get_connection():
    url = get_url()
    engine = create_engine(url)
    connection = engine.connect()
    return connection


def get_url() -> str:
    username = st.secrets["connections"]["mysql"]["username"]
    password = st.secrets["connections"]["mysql"]["password"]
    host = st.secrets["connections"]["mysql"]["host"]
    port = st.secrets["connections"]["mysql"]["port"]
    name = st.secrets["connections"]["mysql"]["database"]
    return f"mysql+pymysql://{username}:{password}@{host}:{port}/{name}"


def get_dataframe():
    conn = st.experimental_connection('mysql', type='sql')
    df = conn.query('SELECT * from report;', ttl=3600)
    return df
