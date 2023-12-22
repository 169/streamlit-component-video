import sys

sys.path.append("../src")

import streamlit as st
from streamlit_component_video import streamlit_component_video


st.write("## Example")
video = streamlit_component_video(
    video="./examples.mp4",
    mimetype="video/mp4",
    track="./examples.vtt",
)
st.write(video)

# Run: cd examples && streamlit run basic.py