import streamlit as st
from dict_words import get_dictionary_words

st.title('Word Puzzle')

text_input = st.text_input("Enter your letters/word!")

"Your Text Input: ", text_input.lower()

output_dict = get_dictionary_words(text_input)

"Output :", output_dict
