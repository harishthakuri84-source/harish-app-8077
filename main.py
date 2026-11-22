import streamlit as st
from engine import generate_video

st.set_page_config(page_title="Studio-V-Pro", layout="wide")
st.title("Studio-V-Pro: AI Video Engine")

script = st.text_area("Video Script:")
if st.button("Generate"):
    with st.spinner("Processing..."):
        result = generate_video(script)
        st.success(f"Video ready: {result}")
