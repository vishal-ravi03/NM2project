from dotenv import load_dotenv
from langchain_google_genai.llms import GoogleGenerativeAI
import streamlit as st
import PyPDF2 as pdf
import os
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
GEMINI_API_KEY=st.sidebar.text_input(label="Enter your Gemini-pro API key")
    
# Ensure necessary environment variables are loaded
# api_key = os.getenv(GEMINI_API_KEY)


# Generate the LL response
def get_response(input):
    try:
        llm = GoogleGenerativeAI(
            api_key=GEMINI_API_KEY,  # Ensure the api_key is passed correctly
            model="gemini-2.0-flash"
        )
        response = llm.invoke(input)
        return response
    except Exception as e:
        return f"An error occurred: {e}"

def input_file(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

input_prompt = """

Hey, you are the world's best and very experienced ATS (Application Tracking System). I need you to evaluate the user's resume: {text} against the job description: {jd}. Assign a matching percentage based on the job description, and assist in improving the resume. I want the response in the following format: and filter 
Key Metrics:

Matching Score: 0-100%
Keyword Relevance: High, Medium, or Low
Recommendation Confidence: 0-100%
- Percentage Matching Based on Job Description
- Missing Keywords 
- Profile Summary
- Accepted or Rejected Percentage %
- suggest the job for this resume

"""
st.title("Applicant tracking system®")
st.info("Applicant tracking system for Resumes")
st.header("""


              ᯓ🏃🏻‍♀️‍➡️ Get Your Dream Job ᯓ🏃🏻


""")
st.caption("ALL THE BEST")
st.sidebar.info(
    "This Advanced ATS uses state-of-the-art AI to evaluate resumes. "
    "It calculates a matching percentage against a job description, identifies missing keywords, "
    "generates a profile summary, and suggests the best job fit. \n\n"
    "Key Metrics:\n"
    "- Matching Score: 0-100%\n"
    "- Keyword Relevance: High, Medium, or Low\n"
    "- Recommendation Confidence: 0-100%\n\n"
    "Built with LangChain and powered by Google Gemini-pro."
    
)

st.sidebar.feedback("stars")
st.sidebar.link_button(url="https://www.template.net/business/resume/fresher-engineer-resume-template/",label="How to Bulid a resume !",icon="📄")
st.sidebar.caption("Developer Info")
st.sidebar.info(icon="👨🏻‍💻",body="Developer Name: Vigneshwaran "" Main Domain : AI engineer ")
jd = st.text_area("Paste the job description")
file1 = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload")
submit = st.button("Submit")


if submit: 
    if file1 is not None:
        with st.spinner("Analysing please wait........"):     
            text = input_file(file1) 
            prompt = input_prompt.format(text=text, jd=jd)
            response_stream = get_response(prompt)
            st.write(response_stream)
            
            # # Display the response in a streaming fashion
            # output_placeholder = st.empty()
            # full_response = ""
            # for chunk in response_stream:
            #     full_response += chunk
            #     output_placeholder.markdown(full_response)
            st.success("Analysis complete!")  # Show success message
            st.sidebar.balloons() 
             
