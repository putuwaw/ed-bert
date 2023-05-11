from utils.db import get_dataframe
import streamlit as st

df = get_dataframe()
st.write(df)
