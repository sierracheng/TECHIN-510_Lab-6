import fitz  # PyMuPDF

if uploaded_file is not None:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    st.text(text)
    # Now, use `text` with llamaindex for RAG
