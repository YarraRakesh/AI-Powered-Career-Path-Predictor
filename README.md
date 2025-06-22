# 🎓 AI-Powered Career Path Predictor

An interactive Streamlit web app that predicts the most suitable engineering career path for students based on their academic scores, technical/soft skills, interests, and learning preferences.

🔗 **Live App**: [https://ai-powered-career-path-predictor-iwiq6iyqwphrw5g9auccqd.streamlit.app/](https://ai-powered-career-path-predictor-iwiq6iyqwphrw5g9auccqd.streamlit.app/)

👤 **Author**: [Rakesh Yarra](http://www.linkedin.com/in/rakeshyarra)

---

## 🚀 Features

- 🔍 Predicts best-fit engineering career path.
- 🎛️ Takes academic, technical, soft skills, and interests as input.
- 🧠 Uses Random Forest ML model for prediction.
- 🏷️ Filters careers based on current and interested branches.
- 🌐 Deployable via Streamlit Cloud.

---

## 📁 Project Structure

├── app.py                        # Streamlit web application
├── model_trainer.py              # ML training script
├── career_data.csv               # Dataset with student features
├── model.pkl                     # Saved ML model and encoders
├── requirements.txt              # Required Python packages
└── README.md                     # Project info and usage guide

📦 Tech Stack
Python
Pandas, NumPy
Scikit-learn
Streamlit
GitHub + Streamlit Cloud (for deployment)

⚙️ Setup
pip install -r requirements.txt
streamlit run app.py

📜 License

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with proper attribution.
