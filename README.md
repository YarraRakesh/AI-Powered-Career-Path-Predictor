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

MIT License
Copyright (c) 2025 Rakesh Yarra
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
