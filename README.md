# Healthcare AI All-in-One

This repository contains two easy-to-use healthcare AI projects:

1. **Healthcare AI Samples** (doctor-patient assistant, healthcare summarization, prediction)
2. **Virtual Healthcare Dashboard** (modern web dashboard)

---

## 📦 What’s Inside?

- `healthcare-ai-samples/` — Simple tools and notebooks for:
  - Transcribing doctor-patient conversations
  - Generating clinical notes with AI
  - Summarizing health records and predicting chronic disease
- `virtual-healthcare-dashboard/` — A modern dashboard web app with:
  - Chat-style consultation
  - Patient summaries, risk scores, and history
  - Beautiful, interactive interface

---

# 🚀 How to Use (Step-by-Step)

## 1. Requirements
- Python 3.8 or newer
- Node.js and npm (for dashboard)
- pip (Python package installer)

## 2. Install Everything
Open your terminal and run:
```bash
# Go to this folder
cd /Users/astha/CascadeProjects/healthcare-ai-all

# Install Python dependencies for all tools
cd healthcare-ai-samples
pip install -r requirements.txt
cd ../virtual-healthcare-dashboard/backend
pip install -r requirements.txt
```

## 3. Try the Doctor-Patient Assistant (Streamlit)
```bash
cd ../../healthcare-ai-samples/doctor_patient_assistant
streamlit run app.py
```
- Opens in your browser at [http://localhost:8501](http://localhost:8501)

## 4. Try the Dashboard (Modern Web App)
```bash
cd ../../virtual-healthcare-dashboard/backend
uvicorn main:app --reload
# In a new terminal:
cd ../frontend
npm install  # (first time only)
npm start
```
- Opens in your browser at [http://localhost:3000](http://localhost:3000)

## 5. Try the Notebooks
```bash
# For doctor-patient assistant:
cd ../../healthcare-ai-samples/doctor_patient_assistant
jupyter notebook
# For summarization/prediction:
cd ../../healthcare-ai-samples/healthcare_summarization_prediction
jupyter notebook
```

## 6. API Keys
- For real results, add your Azure Speech and OpenAI API keys where prompted.
- You can use mock data for demo/testing.

---

# 🧠 Azure Services Used

| Service Name                  | Description                                                        |
|------------------------------|--------------------------------------------------------------------|
| Azure Speech-to-Text         | Converts spoken language (audio) into written text. Used for transcribing doctor-patient conversations. |
| Azure OpenAI Service         | Provides access to advanced language models (like GPT) for generating clinical notes, summaries, and more. |
| Azure Text Analytics for Health | Extracts structured medical information (diagnoses, medications, symptoms) from unstructured clinical text. Used for summarizing health records. |

---

# ❓ What Can I Do With This?
- Test healthcare AI tools with your own data
- Explore how AI can help doctors and patients
- See a real dashboard for healthcare analytics
- Use as a starting point for your own healthcare AI projects!

---

**No advanced coding required. Just follow the steps above!**

If you get stuck, check the README files in each folder for more help.



<img width="1427" alt="Screenshot 2025-04-21 at 11 10 40 AM" src="https://github.com/user-attachments/assets/0a7226f6-9a02-41c0-b5f1-8c7987976353" />
<img width="1458" alt="Screenshot 2025-04-21 at 11 11 06 AM" src="https://github.com/user-attachments/assets/e8eee8a5-29a2-48a2-a523-7346bcee23a6" />
