import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
import firebase_admin
from firebase_admin import credentials, auth
import time
import re
from pathlib import Path

# Set the page title and favicon
st.set_page_config(page_title="Dream Interpretation AI", page_icon=":purple[🌙]:")

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style.css"

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add a title and description with Markdown formatting
st.title("Dream Interpretation AI")
st.markdown("Welcome to the **Dream Interpretation AI**. Enter details about your dream, and let's explore its meaning!")
st.sidebar.header("About Dream Interpretation AI")
st.sidebar.info("This AI helps you interpret and understand your dreams by generating symbolized descriptions.")

with st.form(key="dream_form"):
    user_dream = st.text_area("Enter Your Dream", height=100)
    analyze_button = st.form_submit_button("Analyze Dream", help="Click to interpret your dream")

    if analyze_button:
        min_words = 5
        min_chars = 20
        words_count = len(user_dream.split())
        chars_count = len(user_dream)

        if words_count < min_words or chars_count < min_chars:
            st.warning("Please enter a more detailed dream before analyzing.")
        else:
            st.markdown("Connecting to your mind... 🌐")
            time.sleep(5)
            st.markdown("Accessing your neural network... 🧠")
            time.sleep(3)
            st.markdown("Retrieving dream data from your mind... 💭")
            time.sleep(3)

            with st.spinner("Analyzing your dream..."):
                time.sleep(3)
                # API key (replace with your own key)
                openai_api_key = st.secrets["OPENAI_API_KEY"]
                # Set up OpenAI language model
                llms = OpenAI(api_key=openai_api_key)
                # Define prompt template
                template1 = f"Tell me about my dream and symbolize it. This is my dream description: {user_dream}."
                PromptTemplate_Dream = PromptTemplate(
                    input_variables=["dream"],
                    template=template1,
                )
                # Create language model chain
                dream_chain = LLMChain(llm=llms, prompt=PromptTemplate_Dream, output_key="dream_desc")
                chains = SequentialChain(
                    chains=[dream_chain],
                    input_variables=['dream'],
                    output_variables=['dream_desc']
                )
                # Get the result
                result = chains({'dream': user_dream})

            # Display dream details with enhanced formatting
            st.markdown("## Dream Analysis")
            st.success(result['dream_desc'])

# AdSense code
st.markdown("""
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3252101951306223" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

# Developer Information
st.markdown("---")
st.markdown("<h3 id='developer-info'>Developer Information</h3>", unsafe_allow_html=True)
st.markdown("<p>Developed by <a href='https://media.licdn.com/dms/image/D4D16AQGe9lT5wOkN1w/profile-displaybackgroundimage-shrink_350_1400/0/1703914975852?e=1709769600&v=beta&t=HnSgDcAsdQm_XgxRskLSGVsEc0z8eOlvp-tewuVbGIU' target='new_tab'>Shaikh Zayan</a> | GitHub: <a href='https://github.com/ShaikhZayan' target='new_tab'>GitHub Profile</a> | LinkedIn: <a href='https://www.linkedin.com/in/shaikhzayan-fullstack-engineer-developer/' target='new_tab'>LinkedIn Profile</a> | Upwork: <a href='https://www.upwork.com/freelancers/~01f36bd710bf8ce6c2' target='new_tab'>Upwork Profile</a></p>", unsafe_allow_html=True)
st.markdown("<p><i><b>Dream Interpretation AI</b> powered by Shaikh Zayan</i></p>", unsafe_allow_html=True)
st.markdown("<p><i>For entertainment purposes only. Interpretations are subjective.</i></p>", unsafe_allow_html=True)
