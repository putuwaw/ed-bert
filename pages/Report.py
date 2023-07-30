import streamlit as st
from utils.db import get_connection
from models.report import report

st.header("Report")
st.write("Report the missed classification here")

text = st.text_area("Text")
emotions = ['anger', 'fear', 'joy', 'love', 'sadness', 'surprise']

predicted = st.selectbox("Predicted", emotions)
actual_emotions = [x for x in emotions if x != predicted]

actual = st.selectbox("Actual", actual_emotions)
if st.button("Report"):
    with st.spinner('Reporting...'):
        data = {'text': str.lower(text), 'predicted': str.lower(
            predicted), 'actual': str.lower(actual)}

        connection = get_connection()

        insert_query = report.insert().values(**data)
        connection.execute(insert_query)
        connection.commit()
        connection.close()
    st.success("Successfully reported!")
    st.balloons()
