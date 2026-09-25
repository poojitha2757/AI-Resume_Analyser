# AI-Resume_Analyser
An AI-powered Resume Analyzer built using **Python** and **Streamlit** that compares a resume with a job description and provides a matching score, ATS score, and improvement suggestions.

## Features

* Upload a **PDF resume**
* Paste a **Job Description**
* Extracts text from the resume using **pdfplumber**
* Calculates **Skills Match Score**
* Calculates **Keyword Match Score** using **TF-IDF** and **Cosine Similarity**
* Performs a basic **Experience Check**
* Generates an **ATS Score**
* Provides suggestions to improve resume quality

## Demo

<AsyncImage query="AI Resume Analyzer Streamlit app screenshot" aspectRatio="16:9"/>

## Tech Stack

* Python
* Streamlit
* pdfplumber
* scikit-learn

  * TF-IDF Vectorizer
  * Cosine Similarity

## Project Structure

```text
AI_Resume_Analyzer/
│── app.py
│── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/AI_Resume_Analyzer.git
cd AI_Resume_Analyzer
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Run the application.

```bash
streamlit run app.py
```

## How It Works

1. Upload a resume in PDF format.
2. Paste the job description.
3. The application extracts text from both inputs.
4. It compares the resume and job description using:

   * Skill matching
   * TF-IDF keyword similarity
   * Basic experience detection
5. A final score and ATS score are displayed along with improvement suggestions.

## Scoring Logic

The final score is calculated using:

| Component        | Weight |
| ---------------- | ------ |
| Skills Match     | 40%    |
| Keyword Match    | 40%    |
| Experience Check | 20%    |

The ATS score checks whether the resume contains important sections such as:

* Education
* Skills
* Experience
* Projects

If any section is missing, the application suggests improvements.

## Example Output

* Overall Match Score
* Skills Match %
* Keyword Match %
* Experience Score
* ATS Score
* Resume Improvement Suggestions

## Future Improvements

* Support DOCX resumes
* Detect more technical skills automatically
* Improve experience extraction using NLP
* Resume keyword highlighting
* Multiple resume comparison

## Author

**Poojitha Puligundla**

B.Tech AI & ML Student
