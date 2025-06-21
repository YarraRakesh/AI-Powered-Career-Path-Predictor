import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Career Path Predictor", page_icon="🎓")
st.title("🎓 AI-Powered Career Path Predictor")

# Load model
with open("model.pkl", "rb") as f:
    model, le = pickle.load(f)

st.write("### 🔍 Enter your details below:")

branch = st.selectbox("Your Current Branch", [
    "CSE/IT", "ECE", "Electrical", "Mechanical", "Civil", "Chemical", "Biotech", "Other"
])

math = st.slider("Math Score", 0, 100, 70)
english = st.slider("English Score", 0, 100, 70)
coding = st.slider("Coding Skill", 0, 100, 70)

loves_tech = st.radio("Do you love technology?", ["Yes", "No"]) == "Yes"
loves_design = st.radio("Do you love design/creativity?", ["Yes", "No"]) == "Yes"
talks_alot = st.slider("Communication Skill (0-1)", 0.0, 1.0, 0.5)
logic = st.slider("Logical Thinking (0-1)", 0.0, 1.0, 0.5)
likes_outdoor = st.radio("Prefer outdoor or site-based work?", ["No", "Yes"]) == "Yes"
research_interest = st.radio("Are you interested in research/academia?", ["No", "Yes"]) == "Yes"

# Convert to input format
input_data = pd.DataFrame([[
    math, english, coding,
    int(loves_tech), int(loves_design),
    talks_alot, logic,
    int(likes_outdoor), int(research_interest)
]], columns=[
    "Math", "English", "Coding", "Loves_Tech", "Loves_Design",
    "Talks_Alot", "Logic", "Likes_Outdoor", "Research_Interest"
])

if st.button("Predict My Future Career 🚀"):
    prediction = model.predict(input_data)[0]
    career = le.inverse_transform([prediction])[0]

    st.success(f"🌟 Recommended Career Path: **{career}**")
    st.info(f"📘 Based on your interest in {branch}, this is a great fit!")

    # 🎯 Career Advice Dictionary
    advice = {
        "Software Engineer": "Focus on DSA, Python/Java, and system design.",
        "AI Engineer": "Master Python, ML libraries (scikit-learn, TensorFlow), and Math.",
        "Data Scientist": "Focus on data cleaning, statistics, ML models, and visualization.",
        "Cybersecurity Analyst": "Learn network security, firewalls, Linux, and CEH basics.",
        "UX Designer": "Build design portfolios, learn Figma, Adobe XD, and user testing.",
        "VLSI Engineer": "Practice Verilog, DSA, and EDA tools like Cadence or Synopsys.",
        "Embedded Developer": "Focus on C/C++, microcontrollers (AVR, ARM), and RTOS.",
        "Mechanical Engineer": "Learn CAD tools (AutoCAD, SolidWorks), and thermodynamics.",
        "Design Engineer (Mech)": "Master simulation and design tools like CATIA, Creo.",
        "Civil Site Engineer": "Focus on fieldwork, project planning, and civil drawing tools.",
        "Structural Engineer": "Strengthen knowledge in RCC, STAAD Pro, and structures.",
        "Electrical Power Engineer": "Study circuits, power systems, and simulation tools.",
        "Electronics R&D Engineer": "Explore PCB design, research papers, and embedded Linux.",
        "Graphic Designer": "Learn Photoshop, Illustrator, and design principles.",
        "HR Manager": "Build communication, team leadership, and HR tools like Zoho.",
        "DevOps Engineer": "Learn Docker, Jenkins, cloud (AWS), and CI/CD pipelines.",
        "Environmental Analyst": "Focus on sustainability, field sampling, and GIS tools.",
        "Sales Executive": "Improve people skills, CRM tools, and target tracking.",
        "Full Stack Developer": "Learn frontend (React), backend (Node.js/Python), and APIs.",
        "Digital Marketer": "Master SEO, SEM, content marketing, and analytics.",
        "Content Writer": "Focus on blogging, SEO writing, and audience research.",
        "Marketing Specialist": "Study branding, email campaigns, and conversion metrics.",
        "Public Relations": "Polish communication, event management, and media handling."
    }

    # Show career advice
    if career in advice:
        st.write("🎯 **To achieve this career, you should:**")
        st.success(advice[career])
