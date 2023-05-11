from sqlalchemy import create_engine
import streamlit as st


def get_connection():
    url = get_url()
    engine = create_engine(url)
    connection = engine.connect()
    return connection


def get_url() -> str:
    db_username = st.secrets["db_username"]
    db_password = st.secrets["db_password"]
    db_host = st.secrets["db_host"]
    db_port = st.secrets["db_port"]
    db_name = st.secrets["db_name"]
    return f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"


def get_dataframe():
    conn = st.experimental_connection('mysql', type='sql')
    df = conn.query('SELECT * from report;', ttl=0)
    return df
