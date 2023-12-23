import sys

sys.path.append("../src")

import streamlit as st
from streamlit_component_video import streamlit_component_video

if "widget_values" not in st.session_state:
    st.session_state.update({
        'widget_values': {},
        'current_time': 0
    })

def make_recording_widget(f):
    def wrapper(label, *args, **kwargs):
        widget_value = f(*args, **kwargs)
        st.session_state.widget_values[label] = widget_value
        return widget_value
    return wrapper


st.write("## Example")

make_recording_widget(streamlit_component_video)(
    label="video_component",
    path="./examples.mp4",
    mimetype="video/mp4",
    track="./examples.vtt",
    current_time=st.session_state["current_time"],
)

st.write(st.session_state["widget_values"])

# Run: cd examples && streamlit run record_current_time.py