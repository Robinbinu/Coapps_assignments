import streamlit as st
from transformers import pipeline


qa_pipeline = pipeline('question-answering')

st.title('Coapps AS4 : Question Answering System')
st.write('Enter a context and a question')

context = st.text_area('Context', 'Enter the context here...')
question = st.text_input('Question', 'Enter the question here...')

if st.button('Get Answer'):
    if context and question:
        result = qa_pipeline({'context': context, 'question': question})
        st.write(f"**Answer:** {result['answer']}")
    else:
        st.write('Please provide both a context and a question.')

