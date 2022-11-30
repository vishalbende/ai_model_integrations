import streamlit as st
import numpy as np
import pandas as pd
import requests
from PIL import Image
import shutil
import io


st.title("Welcome to Puter!")


# st.write("Line Chart in Streamlit")
# # 10 * 2 dimensional data
# chart_data = pd.DataFrame(
#     np.random.randn(10, 2),
#     columns=[f"Col{i+1}" for i in range(2)]
# )

# st.line_chart(chart_data)



tab1, tab2 = st.tabs(["GPT-J 6B", "Stable Defusion"])

with tab1:
    # st.header("GPT-J 6B")
    # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    _input = st.text_input('Input::')
    if st.button("Submit", key='submi2'):
        result = ""
        response = requests.post("http://localhost:8000/v1/gptj6b/",json={
                "input_string": _input
            })
        if response:
            response_json = response.json()
            if response_json:
                result = response_json[0].get('generated_text')
        st.write('result: %s' % result)
    # st.button(label="Submit", key='Submit')

with tab2:
    _input1 = st.text_input('Input::', key='input')
    button1 = st.button("Submit", key='submi1') 
    response = requests.post("http://localhost:8000/v1/stable_defusion2/",json={
                "input_string": _input1
            })
    
    image = None
    if response:
        image = Image.open(io.BytesIO(response.content))
    
    if button1 and image:
        st.image(image)



