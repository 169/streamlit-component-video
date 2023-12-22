import sys

sys.path.append("../src")

import streamlit as st
from streamlit_component_video import streamlit_component_video

if 'video' not in st.session_state:
    st.session_state['video'] = {
        'mimetype': "video/mp4",
        'video': "",
        'track': "",
    }

def click_handler():
    st.session_state['video'] = dict(
        video="./examples.mp4",
        mimetype="video/mp4",
        track="./examples.vtt",
    )

st.write("## Example")
st.button("Click", on_click=click_handler)
video = streamlit_component_video(
        video=st.session_state['video']['video'],
        mimetype=st.session_state['video']['mimetype'],
        track=st.session_state['video']['track'],
    )

# Run: cd examples && streamlit run if_statement.py