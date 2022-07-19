import base64
from mmap import PAGESIZE
import os
from pydoc import doc
from tkinter import Image
from turtle import width
from PyPDF2 import PdfFileReader
import pandas as pd
import streamlit as st
from textwrap import wrap
from zmq import HELLO_MSG 
import doc2text


header = st.container()
pdf2text = st.container()
quesgen = st.container()
@st.cache



def load_image(image_file):
    img = Image.open(image_file)
    return img
        
def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count=pdfReader.numPages
    all_page_text = " "
    for i in range(count):
         page = pdfReader.getPage(1)
         all_page_text+=page.extractText()
    return all_page_text
def main():
    st.title("MCQ GENERATOR")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice=="Home":
        st.subheader("Home")
        docx_file = st.file_uploader("upload here:",type=["pdf","docx","txt"])
        if st.button("process"):
            if docx_file is not None:
                file_details = {"filename":docx_file.name, "filetype":docx_file.type,"filesize":docx_file.size}
                st.write(file_details)
                if docx_file.type == "text/plain":
                    raw_text = str(docx_file.read(),"utf-8")
                    st.write(raw_text)
                    st.text(raw_text)
                elif docx_file.type == "application/pdf":
                    raw_text=read_pdf(docx_file)
                    st.write(raw_text)
        
       
                
        else:
            raw_text = doc2text.process(docx_file)
            st.write(raw_text)

            st.text(raw_text)

if __name__ == '__main__':
    main()
