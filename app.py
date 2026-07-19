import streamlit as st
import pandas as pd
import PyPDF2
import docx
import sqlite3
from streamlit_option_menu import option_menu
import plotly.express as px
import time

st.set_page_config(page_title="Career Lens AI", page_icon="🎯", layout="wide")

# Updated CSS - Maine yahan sirf styling behtar ki hai, baaki code pura wahi hai
st.markdown("""
<style>
.stApp {background-color: #f0f2f6;}

/* Updated Heading Style */
.main-title {
    font-size: 4.5rem !important;
    text-align: center !important;
    font-weight: 900 !important;
    color: #1e293b !important;
    margin-top: 10px;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    font-size: 1.5rem !important;
    color: #64748b !important;
    font-weight: 500;
    margin-bottom: 30px;
}

.box {background: #ffffff; padding: 25px; border-radius: 15px; margin: 10px 0px; color: #1e293b; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}

.stButton>button {
    background: linear-gradient(90deg, #FF6B6B 0%, #FF8E53 100%);
    color: white; 
    font-weight: bold;
    border-radius: 12px; 
    width: 100%; 
    height: 50px; 
    font-size: 18px; 
    border: none;
}

[data-testid="stMetric"] {background: #ffffff !important; border-radius: 15px; padding: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;}
[data-testid="stMetricLabel"] {color: #64748b !important; font-size: 16px !important;}
[data-testid="stMetricValue"] {color: #1e293b !important; font-weight: bold !important;}
</style>
""", unsafe_allow_html=True)

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text

def find_skills(text):
    skill_list = ['python', 'java', 'sql', 'excel', 'html', 'css', 'javascript',
                  'communication', 'teamwork', 'data analysis', 'tableau', 'power bi', 'git', 'react', 'machine learning']
    found_skills = []
    text = text.lower()
    for skill in skill_list:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))

conn = sqlite3.connect('jobs.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, job_name TEXT, req_skills TEXT, salary TEXT)')

c.execute("SELECT COUNT(*) FROM jobs")
if c.fetchone()[0] == 0:
    job_data = [
        ('Data Analyst', 'python, sql, excel, data analysis, tableau, power bi', '6-12 LPA'),
        ('Web Developer', 'html, css, javascript, react, git', '4-8 LPA'),
        ('Software Engineer', 'python, java, c++, sql, git', '7-15 LPA'),
        ('Data Scientist', 'python, machine learning, statistics, sql, tableau', '10-20 LPA'),
        ('AI Engineer', 'python, machine learning, deep learning', '12-25 LPA'),
        ('Full Stack Developer', 'html, css, javascript, python, sql', '7-14 LPA')
    ]
    c.executemany("INSERT INTO jobs (job_name, req_skills, salary) VALUES (?,?,?)", job_data)
    conn.commit()

df = pd.read_sql_query("SELECT job_name as Job, req_skills as Skills, salary as Salary FROM jobs", conn)
conn.close()

questions = {
    'Data Analyst': {
        "1. What is a Primary Key in SQL?": "It is used to uniquely identify each row in a table. It cannot contain NULL values.",
        "2. Why do we use Pandas in Python?": "For data analysis and manipulation, similar to working with structural spreadsheets.",
        "3. What is data cleaning?": "Fixing incorrect data, handling missing values, and removing duplicate records.",
        "4. What is Tableau?": "A business intelligence tool used for visualizing data through charts and graphs.",
        "5. What is the use of VLOOKUP in Excel?": "To search for a value in one table and retrieve corresponding data from another table.",
        "6. What is A/B Testing?": "Comparing two versions of a webpage or element to see which performs better, such as a Red vs Blue button.",
        "7. What is a KPI?": "Key Performance Indicator - used to measure specific business performance targets.",
        "8. What is an outlier?": "A data point that deviates significantly from the rest of the dataset.",
        "9. What is the primary role of a Data Analyst?": "Extracting insights from raw data and creating comprehensive reports.",
        "10. Rate yourself in SQL out of 5.": "I would rate myself a 4/5, and I am continuously expanding my knowledge."
    },
    'Web Developer': {
        "1. What is HTML?": "The standard markup language used to create the structure of web pages.",
        "2. What is the use of CSS?": "To style and design the visual layout, formatting, and colors of a website.",
        "3. What does JavaScript do?": "It adds interactivity and dynamic behavior to a website.",
        "4. What is React?": "A frontend JavaScript library created by Facebook for building fast user interfaces.",
        "5. How do you make a website responsive?": "By using CSS media queries and flexible layout grid frameworks.",
        "6. Why is Git used?": "For version control, tracking changes in code, and collaborating seamlessly within teams.",
        "7. What is an API?": "An Application Programming Interface, which allows two different software programs to communicate.",
        "8. What is SEO?": "Search Engine Optimization, used to increase a website's visibility on search engines like Google.",
        "9. What is the difference between Frontend and Backend?": "Frontend is what the user interacts with visually; Backend handles data processing and logic behind the scenes.",
        "10. Tell me about your web project.": "I engineered a fully responsive personal portfolio website using structured HTML and CSS layout modules."
    },
    'Default': {
        "1. Please introduce yourself.": "My name is Khushi, and I am currently pursuing the 2nd year of my MCA degree.",
        "2. What are your primary strengths?": "I am a disciplined professional who adapts quickly and masters new technical frameworks efficiently.",
        "3. What are your weaknesses?": "I sometimes rush to complete tasks quickly, but I have developed systematic verification habits to maintain accuracy.",
        "4. Where do you see yourself in 5 years?": "Transitioning into a senior technical leadership role within an established technology firm.",
        "5. Are you comfortable working in a team environment?": "Yes, absolutely. I enjoy collaborative engineering environments and value cross-functional teamwork."
    }
}

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
    st.markdown("### **Khushi**")
    st.caption("MCA 2nd Year")
    st.divider()
    menu = option_menu("Menu", ["Resume Checker", "Analytics", "About"],
                       icons=['house', 'bar-chart', 'info-circle'],
                       styles={"nav-link-selected": {"background-color": "#FF6B6B"}})

if menu == "Resume Checker":
    st.markdown('<p class="main-title">Career Lens AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Smart Resume Checker for Students</p>', unsafe_allow_html=True)
    st.write("")
    st.markdown('</div>', unsafe_allow_html=True)

    my_skills = []
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"], label_visibility="collapsed")

if uploaded_file is not None:
    with st.spinner('🔍 AI is parsing the resume content...'):
        # aage ka code
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"], label_visibility="collapsed")

if uploaded_file is not None:
    with st.spinner('🔍 AI is parsing the resume content...'):
        # aage ka code
            time.sleep(2)
            if uploaded_file.name.endswith('.pdf'):
                resume_data = read_pdf(uploaded_file)
            else:
                resume_data = read_docx(uploaded_file)
            my_skills = find_skills(resume_data)
        st.success(f"✅ **Extracted Skills:** {', '.join(my_skills).title()}")

    if len(my_skills) > 0:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write("### 2️⃣ Select Target Job Profile")
        job = st.selectbox("👇 Choose your target job from the list:", df['Job'])
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🔍 Run Resume Analysis"):
            job_row = df[df['Job'] == job].iloc[0]
            required = [s.strip().lower() for s in job_row['Skills'].split(',')]

            matched = [s for s in required if s in my_skills]
            not_matched = [s for s in required if s not in my_skills]
            score = int((len(matched) / len(required)) * 100)

            st.write("---")
            st.write("### 📊 Metrics Performance Analysis")
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("🎯 Target Job", job)
            c2.metric("💰 Average Salary Range", job_row['Salary'])
            c3.metric("📈 Skill Alignment", f"{len(matched)}/{len(required)}")
            c4.metric("🤖 System ATS Score", f"{score}%")

            st.progress(score)

            if score >= 80:
                st.success("🎉 Excellent! Your profile is highly aligned and ready for this job.")
            elif score >= 50:
                st.warning("⚠️ Good baseline alignment, but some additional upskilling is recommended.")
            else:
                st.error("📚 Significant skill gaps identified. Consider learning the missing competencies.")

            st.write("---")
            col1,col2 = st.columns(2)
            with col1:
                st.markdown("#### ✅ Identified Strong Skills")
                for s in matched:
                    st.success(f"{s.title()}")
            with col2:
                st.markdown("#### ❌ Missing Core Competencies")
                for s in not_matched:
                    st.error(f"{s.title()}")
                    st.link_button(f"📺 Learn {s.title()}", f"https://youtube.com/results?search_query={s}+programming+tutorial")

            st.write("---")
            st.write("### 💬 Target Interview Flashcards - Click to expand answer matrix")
            q = questions.get(job, questions['Default'])
            for que, ans in q.items():
                with st.expander(que):
                    st.write(ans)

elif menu == "Analytics":
    st.markdown('<p class="main-title">📊 Analytics Dashboard</p>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="box">', unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    c1.metric("Total Jobs Indexed", len(df))
    c2.metric("Skills Tracked", "15+")
    c3.metric("Highest Compensation Package", "25 LPA")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### Skills Required per Job")
    skill_no = [len(s.split(',')) for s in df['Skills']]
    fig = px.bar(x=df['Job'], y=skill_no, title="Required Technical Skill Density per Profile", color=df['Job'])
    st.plotly_chart(fig, use_container_width=True)

elif menu == "About":
    st.markdown('<p class="main-title">ℹ️ System Project Specifications</p>', unsafe_allow_html=True)
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.write("### Career Lens AI")
    st.write("This project serves as an automated academic platform engineered for the Master of Computer Applications curriculum. Its goal is to analyze resume metrics against structured workforce requirements.")
    st.write("Upon data ingestion, the platform maps skill distributions and computes an algorithmic percentage score simulating real-world ATS match models.")
    st.write("")
    st.write("**✨ Core Architecture Features:**")
    st.write("- Automated textual parsing and capabilities matrix extraction.")
    st.write("- Profile alignment checks via custom relational datasets.")
    st.write("- Dynamic score visualization tracking match percentages.")
    st.write("- Automatic link resolution redirecting to targeted study courses.")
    st.write("- Pre-configured question banks mapped directly to selected profiles.")
    st.write("- Built-in reporting metrics monitor performance stats.")
    st.write("")
    st.write("**🛠️ Integrated Engineering Stack:** Python, Streamlit Framework, SQLite, Plotly Graphics Engine")
    st.write("**👩‍💻 Lead Project Developer:** Khushi - MCA 2nd Year")
    st.markdown('</div>', unsafe_allow_html=True)
    st.info("Acknowledgment to Faculty Mentors and Evaluators 🙏")
