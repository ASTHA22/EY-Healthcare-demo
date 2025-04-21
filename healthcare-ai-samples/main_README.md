# Healthcare AI Samples

This repository contains two sample projects for healthcare insurance use cases using Microsoft Azure AI services:

## 1. Doctor-Patient Interaction Assistant
- Real-time transcription of conversations (Azure Speech-to-Text)
- Speaker labeling
- Clinical note generation (Azure OpenAI)

See: `doctor_patient_assistant/README.md`

## 2. Healthcare Summarization & Chronic Disease Prediction
- Summarize healthcare records (Azure Text Analytics/OpenAI)
- Predict chronic disease risk (Azure ML, mock example)

See: `healthcare_summarization_prediction/README.md`

---

# 🚀 Quick Start Guide

## Requirements
- Python 3.8 or newer
- pip (Python package installer)

## Installation

```bash
cd /Users/astha/CascadeProjects/healthcare-ai-samples
pip install -r requirements.txt
```

## Running the Streamlit App (Doctor-Patient Assistant)
```bash
cd doctor_patient_assistant
streamlit run app.py
```
- The app will open in your browser at [http://localhost:8501](http://localhost:8501).

## Running the Jupyter Notebook (Doctor-Patient Assistant)
```bash
cd doctor_patient_assistant
jupyter notebook
```
- Open `notebook.ipynb` and follow the instructions inside.

## Running the Healthcare Summarization & Prediction Notebook
```bash
cd healthcare_summarization_prediction
jupyter notebook
```
- Open `notebook.ipynb` and follow the instructions inside.

## API Keys
- You will need Azure Speech and OpenAI API keys for full functionality.
- Add your keys where prompted in the app or notebook.

---

## Disclaimer
These samples use mock data/audio for demonstration. For production, ensure HIPAA compliance and robust security practices.

---
If you need further help, see the README files in each subfolder for more details.
