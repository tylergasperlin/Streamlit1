import streamlit as st

# Center the title using HTML and CSS
st.markdown("<h1 style='text-align: center;'>My First Streamlit App</h1>", unsafe_allow_html=True)

# Center the text using HTML and CSS
st.markdown("<p style='text-align: center;'>Hello, welcome to my app!</p>", unsafe_allow_html=True)

# Create some data to download
text_contents = "This is some sample text for download."

# Create three columns with the middle column twice as wide as the others
col1, col2, col3 = st.columns([1, 2, 1])

# Place the download button in the center column
with col2:
    st.download_button(
        label="Download Text",
        data=text_contents,
        file_name="sample.txt",
        mime="text/plain",
        use_container_width=True  # Ensure the button expands to the column's width
    )
