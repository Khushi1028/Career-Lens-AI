import streamlit as st
import pandas as pd
import PyPDF2
import docx
import plotly.express as px
from streamlit_option_menu import option_menu

# Page Config
st.set_page_config(page_title="Career Lens AI", layout="wide", page_icon="🎯")

# CSS FIX - Text dikhne ke liye
st.markdown("""
<style>
    .stApp { background-color: #F8F9FA; color: black; }
    h1, h2, h3, h4, h5, h6, p, div, span, label { color: black !important; }
    [data-testid="stExpander"] { color: black !important; }
    [data-testid="stExpander"] div { color: black !important; }
    .st-emotion-cache-1r6slb0 { color: black !important; }
</style>
""", unsafe_allow_html=True)

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
    st.header("2 Select Target Job Profile")
    
    job_profile = st.selectbox(
        "Select your Target Job",
        ["AI Engineer", "Data Scientist", "Web Developer", "ML Engineer"]
    )
    
    if st.button("🚀 Run Resume Analysis", type="primary"):
        st.success("Analysis Complete!")
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Target Job", "AI E...")
        with col2:
            st.metric("Average Sala...", "12-2...")
        with col3:
            st.metric("Skill Alignment", "1/3")
        with col4:
            st.metric("System ATS Sc...", "33%")
            
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
        st.subheader("💬 Target Interview Flashcards - Click to expand answer matrix")
        with st.expander("1. Please introduce yourself."):
            st.write("Answer: I am MCA 2nd year student passionate about AI and ML...")
        with st.expander("2. What are your primary strengths?"):
            st.write("Answer: My strengths are Python, Problem Solving and Learning new things quickly...")
        with st.expander("3. Where do you see yourself in 5 years?"):
            st.write("Answer: I see myself as an AI Engineer working on real world problems...")

elif selected == "Analytics":
    st.header("📊 Analytics Page")
    st.write("Yaha tumhara progress dikhega")
    
elif selected == "About":
    st.header("ℹ️ About")
    st.write("Career Lens AI - Resume ko AI se check karo")
