import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.markdown(
    "<h1 style='text-align: center;'>Understanding Failure Patterns in Voice Assistants</h1>",
    unsafe_allow_html=True
)
st.markdown("""
When voice assistants fail, not everyone is affected equally.  
    Explore how technical failures in voice assistants intersect with user identity and behavior.  
Our dashboard reveals patterns in failure type, accent-related disparities, and how users adapt—or don’t—after being misunderstood.

Use the interactive charts below to dig into:
- Which failures are most common and how they vary across user demographics
- How users repeat or adjust speech after specific kinds of breakdowns
- What design implications emerge when certain groups bear more burden than others
""")

df = pd.read_csv('voice-assistant-failures.csv')
