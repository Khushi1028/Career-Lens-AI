import streamlit as st
import pandas as pd
import PyPDF2
import docx
import plotly.express as px
from streamlit_option_menu import option_menu
import io

# Page Config
st.set_page_config(page_title="Career Lens AI", layout="wide", page_icon="🎯")

# CSS - Sirf expander fix
st.markdown("""
<style>
    [data-testid="stExpander"] summary { color: inherit !important; }
</style>
""", unsafe_allow_html=True)

# Function to read resume
def read_resume(file):
    text = ""
    if file.name.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file.name.endswith('.txt'):
        text = file.getvalue().decode("utf-8")
    return text

# Sidebar Menu
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("Khushi")
    st.caption("MCA 2nd Year")
    
    selected = option_menu(
        "Menu",
        ["Resume Checker", "Analytics", "About"],
        icons=['house', 'bar-chart', 'info-circle'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#262730"},
            "icon": {"color": "white", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color": "white"},
            "nav-link-selected": {"background-color": "#FF4B4B", "color": "white"},
        }
    )

# Main Page
if selected == "Resume Checker":
    st.title("🎯 Career Lens AI")
    st.subheader("AI Powered Resume Analyzer")
    
    # YAHI PE UPLOAD OPTION HAI
    uploaded_file = st.file_uploader("1 Upload Your Resume", type=['pdf', 'docx', 'txt'])
    
    st.subheader("2 Select Target Job Profile")
    job_profile = st.selectbox(
        "Select your Target Job",
        ["AI Engineer", "Data Scientist", "Web Developer", "ML Engineer"]
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File Uploaded: {uploaded_file.name}")
        
        if st.button("🚀 Run Resume Analysis", type="primary"):
            with st.spinner("Analyzing your resume..."):
                resume_text = read_resume(uploaded_file)
                
                # Dummy Analysis - tum isme apna AI logic daal dena
                st.success("Analysis Complete!")
                
                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1: st.metric("Target Job", job_profile)
                with col2: st.metric("Avg Salary", "12-20 LPA")
                with col3: st.metric("Skill Alignment", "1/3")
                with col4: st.metric("ATS Score", "33%")
                    
                st.warning("📦 Significant skill gaps identified. Consider learning the missing competencies.")
                
                # Skills
                col1, col2 = st.columns(2)
                with col1:
                    st.success("✅ Identified Strong Skills")
                    st.info("Python")
                with col2:
                    st.error("❌ Missing Core Competencies")
                    st.write("Machine Learning")
                    st.button("📚 Learn Machine Learning")
                    st.write("Deep Learning")
                    st.button("📚 Learn Deep Learning")
                
                # Flashcards
                st.subheader("💬 Target Interview Flashcards")
                with st.expander("1. Please introduce yourself."):
                    st.write("Answer: I am MCA 2nd year student passionate about AI and ML...")
                with st.expander("2. What are your primary strengths?"):
                    st.write("Answer: My strengths are Python, Problem Solving...")
                with st.expander("3. Where do you see yourself in 5 years?"):
                    st.write("Answer: I see myself as an AI Engineer...")

elif selected == "Analytics":
    st.header("📊 Analytics Page")
    st.write("Yaha tumhara progress dikhega")
    
elif selected == "About":
    st.header("ℹ️ About Career Lens AI")
    st.write("Ye app tumhare resume ko scan karke job ke hisab se score deta hai")
