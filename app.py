import streamlit as st

st.header("Image Caption Generator")
st.write("Image caption generator is a model which generates caption based on the features present in the input image.")
st.subheader("DATASET")
st.write("The dataset used here is the FLICKR 8K which consists of around 8091 images along with 5 captions for each images. If you have a powerful system with more than 16 GB RAM and a graphic card with more than 4 GB of memory, you can try to take FLICKR 30K which has around 30,000 images with captions.")
st.subheader("OUTPUT")
st.image("image caption.png")
