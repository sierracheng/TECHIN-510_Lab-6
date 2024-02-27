uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as string:
    string_data = uploaded_file.getvalue().decode("utf-8")
    st.text(string_data)
    # Add your logic to process the file here
