import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, welcome to my app!")

# Create some data to download (here, a simple text)
text_contents = "This is some sample text for download."

# Add a download button to let users download the text as a file
st.download_button(
    label="Download Text",
    data=text_contents,
    file_name="sample.txt",
    mime="text/plain"
)