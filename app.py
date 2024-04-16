import streamlit as st
from openai import OpenAI


# Set up OpenAI API key
f = open("keys\.openai_api_key.txt")
key = f.read()
client=OpenAI(api_key=key)
st.snow()
# Custom CSS for dark theme
def set_custom_style():
    st.markdown(
        """
        <style>
        .stTextInput>div>div>div>textarea {
            height: 200px; /* Adjust the height as needed */
        }
        
        .st-bj { background-color: #FFFFFF; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Apply custom style
set_custom_style()
# Header
st.title("👩‍💻GenAI App - AI Code Reviewer")
st.subheader("Welcome to GenAI App! The system will now review the provided code.")

#take users input
#prompt= st.text_input("Enter your Python code here:",rows=200)
#take users input
prompt= st.text_area("Enter your Python code here:", height=200)

if st.button("Generate") == True:
    st.balloons()
    response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "system", "content": """You are a helpful AI Assistant.
                                                Given a python code you have to debug the code and you have to show the bugs available in the code as well as you have to provide the corrected code as output"""}
            ]
        )
    #print the response on webapp
    st.write(response.choices[0].message.content)


