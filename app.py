import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Career Path Predictor", page_icon="🎓")
st.title("🎓 AI-Powered Career Path Predictor")

# Load model
with open("model.pkl", "rb") as f:
    model, le = pickle.load(f)

st.write("### 🔍 Enter your details:")

branch = st.selectbox("Your Current Branch", [
    "CSE/IT", "ECE", "Mechanical", "Electrical", "Civil", "Other"
])

# New inputs
math = st.slider("Math Score", 0, 100, 70)
english = st.slider("English Score", 0, 100, 70)
coding = st.slider("Coding Skill", 0, 100, 70)

loves_tech = st.radio("Do you love technology?", ["Yes", "No"]) == "Yes"
loves_design = st.radio("Do you love design/creativity?", ["Yes", "No"]) == "Yes"
talks_alot = st.slider("Communication Skill (0-1)", 0.0, 1.0, 0.5)
logic = st.slider("Logical Thinking (0-1)", 0.0, 1.0, 0.5)
likes_outdoor = st.radio("Prefer outdoor or site-based work?", ["No", "Yes"]) == "Yes"
research_interest = st.radio("Interested in research/academia?", ["No", "Yes"]) == "Yes"

work_env = st.selectbox("Preferred Work Environment", ["Office/Remote", "Field/Site", "Lab/Research"])
learning_style = st.selectbox("Preferred Learning Style", ["Visual", "Hands-on", "Theoretical"])

st.markdown("### 🧠 Programming Skills:")
knows_python = st.checkbox("Knows Python")
knows_c = st.checkbox("Knows C")
knows_cpp = st.checkbox("Knows C++")
knows_java = st.checkbox("Knows Java")
custom_languages = st.text_input("Other Languages Known (comma-separated)", placeholder="e.g., Verilog, JavaScript, Rust")

st.markdown("### 🧠 Soft Skills:")
team_player = st.checkbox("Team Player")
leadership_score = st.slider("Leadership (0-1)", 0.0, 1.0, 0.5)
adaptability_score = st.slider("Adaptability (0-1)", 0.0, 1.0, 0.5)

st.markdown("### 🔮 Future Tech Interests:")
ai = st.checkbox("Interested in AI/ML")
blockchain = st.checkbox("Interested in Blockchain")
cyber = st.checkbox("Interested in Cybersecurity")
vlsi = st.checkbox("Interested in VLSI")
robotics = st.checkbox("Interested in Robotics")
custom_tech = st.text_input("Other Tech Interests (comma-separated)", placeholder="e.g., Quantum Computing, Edge AI")

# Data formatting
input_data = pd.DataFrame([[
    math, english, coding,
    int(loves_tech), int(loves_design),
    talks_alot, logic,
    int(likes_outdoor), int(research_interest),
    ["Office/Remote", "Field/Site", "Lab/Research"].index(work_env),
    ["Visual", "Hands-on", "Theoretical"].index(learning_style),
    int(knows_python), int(knows_c), int(knows_cpp), int(knows_java),
    int(team_player), leadership_score, adaptability_score,
    int(ai), int(blockchain), int(cyber), int(vlsi), int(robotics)
]], columns=[
    "Math", "English", "Coding", "Loves_Tech", "Loves_Design",
    "Talks_Alot", "Logic", "Likes_Outdoor", "Research_Interest",
    "Work_Env", "Learning_Style", "Knows_Python", "Knows_C",
    "Knows_CPP", "Knows_Java", "Team_Player", "Leadership_Score",
    "Adaptability_Score", "Interested_in_AI", "Interested_in_Blockchain",
    "Interested_in_Cybersecurity", "Interested_in_VLSI", "Interested_in_Robotics"
])

if st.button("Predict My Future Career 🚀"):
    prediction = model.predict(input_data)[0]
    career = le.inverse_transform([prediction])[0]

    st.success(f"🌟 Recommended Career Path: **{career}**")
    st.info(f"📘 Based on your profile and branch: {branch}")

    # Optional: add advice dictionary here later if you want
