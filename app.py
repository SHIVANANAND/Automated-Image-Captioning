import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input # type: ignore
from tensorflow.keras.preprocessing.image import img_to_array # type: ignore
import pickle

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    button[title="View fullscreen"]{
    visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

# Load the model
model = tf.keras.models.load_model('best_model.h5')

# Function to convert index to word
def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

# Function to generate caption
def predict_caption(model, features, tokenizer, max_length):
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([features, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = idx_to_word(yhat, tokenizer)
        if word is None:
            break
        in_text += " " + word
        if word == 'endseq':
            break
    return in_text

# Function to extract features using VGG16 model
def extract_features(image):
    image = image.resize((224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)
    vgg_model = VGG16(include_top=True, weights='imagenet')
    vgg_model = tf.keras.Model(inputs=vgg_model.input, outputs=vgg_model.layers[-2].output)
    features = vgg_model.predict(image_array, verbose=0)
    return features

# Streamlit app
st.title("Image Captioning")
st.write("Upload an image and get a caption generated by the model.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    features = extract_features(image)
    max_length = 35
    caption = predict_caption(model, features, tokenizer, max_length)

    st.write("Generated Caption:")
    st.write(caption)