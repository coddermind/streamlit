import PyPDF2
import google.generativeai as genai
import streamlit as st

# Configure Gemini AI API key
genai.configure(api_key="AIzaSyDiD2uaAgrBrWqx3K5HqLH2xaGAm4AIZoo")  # Replace with your actual API key

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to ask a question using Gemini AI
def ask_question_from_pdf(pdf_text, question):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Specify the model you want to use
    prompt = f"{pdf_text}\n\nBased on the document above, answer the following question:\n{question}"
    
    response = model.generate_content(prompt)
    
    return response.text

# Streamlit UI
st.title("PDF Question-Answering with Abrar's AI")

# Step 1: File uploader for PDF
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:
    # Step 2: Extract text from the uploaded PDF
    with st.spinner("Extracting text from the PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extraction completed!")

        # Display the extracted text (optional)
        st.subheader("Ask any Question about Document")
        # st.text_area("Extracted Text", pdf_text, height=200)

        # Step 3: Ask a question based on the extracted text
        question = st.text_input("Ask a question about the document:")
        if st.button("Get Answer"):
            with st.spinner("Generating answer..."):
                answer = ask_question_from_pdf(pdf_text, question)
                st.subheader("Answer")
                st.write(answer)
