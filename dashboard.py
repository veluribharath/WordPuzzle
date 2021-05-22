import streamlit as st
from dict_words import get_dictionary_words

st.title('Word Puzzle')

text_input = st.text_input("Enter your letters/word!")

text_input = text_input.lower().strip()

"Your Text Input: ", text_input

output_dict = get_dictionary_words(text_input)

# left_column, right_column, launch_column = st.beta_columns(3)

if st.sidebar.checkbox("Show Overall Output"):
    "Output :", output_dict

length_of_word = st.radio('Select Length of Word', [x for x in range(3,len(text_input)+1)])

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

"Output : ", output_dict[length_of_word]