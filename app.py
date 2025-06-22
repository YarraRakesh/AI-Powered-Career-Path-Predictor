import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Career Path Predictor", page_icon="🎓")
st.title("🎓 AI-Powered Career Path Predictor")

# Load model and label encoder
with open("model.pkl", "rb") as f:
    model, le = pickle.load(f)

# ---------------- Input Section ----------------
st.write("### 🔍 Enter your details:")

branch = st.selectbox("Your Current Branch", [
    "CSE/IT", "ECE", "Mechanical", "Electrical", "Civil", "Other"
])

interested_branches = st.multiselect(
    "Other Branches You're Interested In (optional)",
    ["CSE/IT", "ECE", "Mechanical", "Electrical", "Civil"]
)

interest_area = st.radio("Which area are you more interested in?", ["Software", "Hardware", "Not Sure"])

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

# ---------------- Data Formatting ----------------
input_data = pd.DataFrame([[math, english, coding,
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

# ---------------- Career Filtering Logic ----------------
career_branch_map = {
    "AI Engineer": ["CSE/IT", "ECE"],
    "Data Scientist": ["CSE/IT", "ECE"],
    "VLSI Engineer": ["ECE", "Electrical"],
    "Cybersecurity Analyst": ["CSE/IT"],
    "Robotics Engineer": ["ECE", "Mechanical"],
    "Full Stack Developer": ["CSE/IT"],
    "Embedded Systems Developer": ["ECE", "Electrical"],
    "IoT Solutions Architect": ["ECE", "CSE/IT", "Electrical"],
    "Cloud Engineer": ["CSE/IT"],
    "DevOps Engineer": ["CSE/IT"],
    "Sustainable Design Engineer": ["Mechanical", "Civil"],
    "Mechanical Design Engineer": ["Mechanical"],
    "Civil Infrastructure Analyst": ["Civil"],
    "Power Electronics Engineer": ["Electrical", "ECE"],
    "Bioinformatics Specialist": ["CSE/IT", "Biotech"],
    "AR/VR Developer": ["CSE/IT", "Design"],
    "Blockchain Developer": ["CSE/IT"],
    "Product Manager": ["CSE/IT", "ECE", "Mechanical"],
    "Technical Writer": ["CSE/IT", "ECE", "Any"],
    "Digital Marketing Analyst": ["Any"]
}

# ---------------- Prediction Button ----------------
if st.button("Predict My Future Career 🚀"):
    probs = model.predict_proba(input_data)[0]
    top_indices = probs.argsort()[::-1]

    valid_branches = [branch] + interested_branches
    filtered_career = None

    for idx in top_indices:
        pred_career = le.inverse_transform([idx])[0]
        valid_for = career_branch_map.get(pred_career, [])
        if "Any" in valid_for or any(b in valid_for for b in valid_branches):
            filtered_career = pred_career
            break

    if filtered_career:
        st.success(f"🌟 Recommended Career Path: **{filtered_career}**")
        st.info(f"📘 Based on your current and interested branches: {', '.join(valid_branches)}")
    else:
        st.warning("⚠️ No matching career found for your selected branches.")

