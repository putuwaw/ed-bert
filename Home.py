import streamlit as st
from module.bert import predict


st.header("Emotion Detection")
st.write("This is a simple emotion detection web app using streamlit and tensorflow")

option = st.selectbox("Model", ("BERT", "New Model"))

text = st.text_area("Text")
if st.button("Predict"):
    with st.spinner('Predicting...'):
        result = ""
        if option == "BERT":
            result = predict(text)
        else:
            result = predict(text, 1)
        st.subheader("Result")
        st.write(f"Predicted Emotion: {result}")
