
import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

# -------------------------------
# CUSTOM CSS (FIXED ✨)
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #667eea, #764ba2);
}

/* Card Styling */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    color: #333; /* FIX: text visible */
}

/* ONLY title white */
h1 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown("<h1 style='text-align:center;'>✨ AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>Upload your resume and match it with your dream job 💼</p>", unsafe_allow_html=True)

# -------------------------------
# FUNCTIONS
# -------------------------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text.lower()

def extract_skills(text):
    skills_list = [
        "python", "java", "c", "c++", "sql", "machine learning",
        "data analysis", "html", "css", "javascript", "react"
    ]
    return [skill for skill in skills_list if skill in text]

def skill_match(resume_text, jd_text):
    jd_skills = extract_skills(jd_text)
    resume_skills = extract_skills(resume_text)

    if len(jd_skills) == 0:
        return 0

    matched = [skill for skill in jd_skills if skill in resume_skills]
    return (len(matched) / len(jd_skills)) * 100

def keyword_match(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0] * 100

def experience_match(resume_text):
    if "year" in resume_text or "experience" in resume_text:
        return 80
    return 50

def ats_check(resume_text):
    sections = ["education", "skills", "experience", "projects"]
    found = [sec for sec in sections if sec in resume_text]

    ats_score = (len(found) / len(sections)) * 100

    suggestions = []
    if "projects" not in resume_text:
        suggestions.append("📌 Add projects to showcase your skills")
    if "skills" not in resume_text:
        suggestions.append("🛠 Include a clear skills section")
    if "experience" not in resume_text:
        suggestions.append("💼 Mention internships or experience")

    return ats_score, suggestions

# -------------------------------
# INPUT SECTION
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])

with col2:
    jd_text = st.text_area("📝 Paste Job Description")

# -------------------------------
# PROCESSING
# -------------------------------
if uploaded_file and jd_text:

    resume_text = extract_text_from_pdf(uploaded_file)

    skills_score = skill_match(resume_text, jd_text)
    keyword_score = keyword_match(resume_text, jd_text)
    exp_score = experience_match(resume_text)

    final_score = (skills_score * 0.4 +
                   keyword_score * 0.4 +
                   exp_score * 0.2)

    ats_score, ats_suggestions = ats_check(resume_text)

    # -------------------------------
    # OUTPUT
    # -------------------------------
    st.markdown("---")

    st.markdown(f"""
    <div class='card'>
        <h2 style='color:#333;'>🎯 Overall Score: {final_score:.2f}%</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("🧠 Skills Match", f"{skills_score:.2f}%")
    col2.metric("🔍 Keyword Match", f"{keyword_score:.2f}%")
    col3.metric("💼 Experience", f"{exp_score:.2f}%")

    st.markdown("---")

    st.markdown(f"""
    <div class='card'>
        <h3 style='color:#333;'>🎯 ATS Score: {ats_score:.2f}%</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💬 Smart Suggestions")

    if final_score > 80:
        st.success("🔥 Amazing! Your resume is highly aligned with the job.")
    elif final_score > 60:
        st.warning("👍 Good job! Improve a few areas to increase your chances.")
    else:
        st.error("⚠️ Your resume needs improvement to match this role.")

    for suggestion in ats_suggestions:
        st.write(suggestion)

