import tensorflow as tf
import streamlit as st
from module import preprocessing
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, TFBertModel
from keras.layers import Dense, Input, GlobalMaxPool1D, Dropout
from keras.models import Model
from keras.optimizers import Adam
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy
import numpy as np


@st.cache_resource
def create_model():
    df = preprocessing.get_all_data()
    train_data, test_data = train_test_split(
        df, test_size=0.3, random_state=42, shuffle=True, stratify=df.Sentiment)

    model_name = 'bert-base-uncased'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    bert_model = TFBertModel.from_pretrained(model_name)

    max_len = 40
    X_train = tokenizer(text=train_data.Input.tolist(),
                        add_special_tokens=True,
                        return_tensors='tf',
                        max_length=max_len,
                        padding=True,
                        truncation=True,
                        return_token_type_ids=False,
                        return_attention_mask=True,
                        verbose=True
                        )

    X_test = tokenizer(text=test_data.Input.tolist(),
                       add_special_tokens=True,
                       return_tensors='tf',
                       max_length=max_len,
                       padding=True,
                       truncation=True,
                       return_token_type_ids=False,
                       return_attention_mask=True,
                       verbose=True
                       )

    input_ids = Input(shape=(max_len,), name='input_ids', dtype=tf.int32)
    attention_mask = Input(
        shape=(max_len,), name='attention_mask', dtype=tf.int32)

    embeddings = bert_model(input_ids, attention_mask=attention_mask)[0]
    output = GlobalMaxPool1D()(embeddings)
    output = Dense(units=128, activation='relu')(output)
    output = Dropout(0.1)(output)
    output = Dense(units=64, activation='relu')(output)
    output = Dense(units=32, activation='relu')(output)
    y = Dense(units=6, activation='softmax')(output)

    model = Model(inputs=[input_ids, attention_mask], outputs=y)
    model.compile(loss=CategoricalCrossentropy(from_logits=True),
                  optimizer=Adam(learning_rate=5e-5,
                                 epsilon=1e-8, clipnorm=1.0),
                  metrics=CategoricalAccuracy('balanced_accuracy'))

    return model


@st.cache_resource
def load_model():
    model_name = 'bert-base-uncased'
    bert_model = TFBertModel.from_pretrained(model_name)
    max_len = 40
    input_ids = Input(shape=(max_len,), name='input_ids', dtype=tf.int32)
    attention_mask = Input(
        shape=(max_len,), name='attention_mask', dtype=tf.int32)

    embeddings = bert_model(input_ids, attention_mask=attention_mask)[0]
    output = GlobalMaxPool1D()(embeddings)
    output = Dense(units=128, activation='relu')(output)
    output = Dropout(0.1)(output)
    output = Dense(units=64, activation='relu')(output)
    output = Dense(units=32, activation='relu')(output)
    y = Dense(units=6, activation='softmax')(output)

    model = Model(inputs=[input_ids, attention_mask], outputs=y)
    model.load_weights('models/ed-bert.h5')
    return model


@st.cache_data
def predict(text, kind=0):
    id_to_label = {0: 'anger', 1: 'fear', 2: 'joy',
                   3: 'love', 4: 'sadness', 5: 'surprise'}
    model_name = 'bert-base-uncased'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if kind == 1:
        model = create_model()
    else:
        model = load_model()
    x_val = tokenizer(
        text=text,
        add_special_tokens=True,
        max_length=40,
        truncation=True,
        padding='max_length',
        return_tensors='tf',
        return_token_type_ids=False,
        return_attention_mask=True,
        verbose=True
    )
    validation = model.predict(
        {'input_ids': x_val['input_ids'], 'attention_mask': x_val['attention_mask']})*100

    return id_to_label[np.argmax(validation)]
