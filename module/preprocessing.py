import streamlit as st
import pandas as pd
import re
import string
from utils.db import get_dataframe


@st.cache_data
def preprocess(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


@st.cache_data
def get_report_data():
    df = get_dataframe()
    df.drop(['id', 'predicted'], axis=1, inplace=True)
    df.rename(columns={'actual': 'sentiment'}, inplace=True)
    return df


@st.cache_data
def get_raw_data():
    train = pd.read_csv("data/train.txt", names=[
        'text', 'sentiment'], sep=';', encoding='utf-8')
    val = pd.read_csv("data/val.txt", names=[
        'text', 'sentiment'], sep=';', encoding='utf-8')
    test = pd.read_csv("data/test.txt", names=[
        'text', 'sentiment'], sep=';', encoding='utf-8')
    return pd.concat([train, val, test], axis=0)


@st.cache_data
def get_all_data():
    raw = get_raw_data()
    report = get_report_data()
    df = pd.concat([raw, report], axis=0)
    return get_clean_data(df)


def get_clean_data(df):
    df['text'] = df['text'].apply(preprocess)
    label_to_id = {'anger': 0, 'fear': 1, 'joy': 2,
                   'love': 3, 'sadness': 4, 'surprise': 5}
    df['sentiment'] = df['sentiment'].map(label_to_id)
    return df
