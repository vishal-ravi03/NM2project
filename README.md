# NM2project


Welcome to the Applicant Tracking System (ATS) project! This advanced ATS uses state-of-the-art AI to evaluate resumes. It calculates a matching percentage against a job description, identifies missing keywords, generates a profile summary, and suggests the best job fit.

## Features
- **Matching Score**: 0-100%
- **Keyword Relevance**: High, Medium, or Low
- **Recommendation Confidence**: 0-100%
- **Percentage Matching Based on Job Description**
- **Missing Keywords**
- **Profile Summary**
- **Accepted or Rejected Percentage**
- **Job Suggestions**

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- PyPDF2
- dotenv
- LangChain with Google Gemini-pro API

### Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/ats.git
    cd ats
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root directory and add your Gemini-pro API key:
    ```env
    GEMINI_API_KEY=your_gemini_pro_api_key_here
    ```

## Usage
1. Run the Streamlit application:
    ```bash
    streamlit run ats.py
    ```

2. Open your browser and navigate to the local server URL (usually http://localhost:8501).

3. Enter your Gemini-pro API key in the sidebar and paste the job description into the provided text area.

4. Upload your resume in PDF format and click the "Submit" button.

5. Wait for the analysis to complete, and view the results including the matching score, missing keywords, profile summary, and job suggestions.

## Developer Info
- **Developer Name**: Vigneshwaran
- **Domain**: AI Engineer

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

## Links
- [How to Build a Resume](https://www.template.net/business/resume/fresher-engineer-resume-template/)
- [Streamlit Live app! ](https://applicanttrackingsystem-vdp8vhjofhxtdgnw8ngybr.streamlit.app/)

---

Feel free to customize this README file further to suit your project's needs. Happy coding! 🚀
