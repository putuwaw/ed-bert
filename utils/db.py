from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.report import report
import streamlit as st
import pandas as pd


def get_connection():
    url = get_url()
    if len(url) < 30:
        url = "mysql+pymysql://root:root@db:3306/ed_bert"
    print(url)
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
    engine = create_engine(get_url())
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(report).all()
    return pd.DataFrame(result)
