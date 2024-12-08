import openai
import streamlit as st
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)
prompt = """You need to extract some words from the given passage. 
            You will receive a passage from user input
            then analyze the passage and extract some words considered important for intermediate french learners
            The writing is delimited by <TEXT> and </TEXT> tags.
            List the extracted words in a JSON array, in the list of dict form, one result per line.
            Each extracted word should have 3 fields:
            - "word" - the extracted word
            - "part of speech" - the part of speech of the extracted word
            - "translation" - the translated word from French to English
           
            Don't say anything at first. Wait for the user to say something.
"""
st.title('Helpful French Vocab')
st.markdown('give AI the passage you want to learn the vocabulaire. wait a minute for the helpful result! fyi : the given vocabulaire is for intermediate level')
        
user_input =st.text_input("Enter your French passage: ","French Passage here")
if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    st.markdown('**AI response:**')
    result = response.choices[0].message.content
    
    res_dict = json.loads(result)
    print(res_dict)
    
    vocab_tableau = pd.DataFrame.from_dict(res_dict)
    print(vocab_tableau)
    st.table(vocab_tableau)
