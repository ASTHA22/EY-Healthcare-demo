import streamlit as st
import azure.cognitiveservices.speech as speechsdk
import openai
import os

st.title("Doctor-Patient Interaction Assistant")

# User inputs for API keys
speech_key = st.text_input("Azure Speech Key", type="password")
speech_region = st.text_input("Azure Speech Region")
openai_key = st.text_input("Azure OpenAI Key", type="password")
openai_endpoint = st.text_input("Azure OpenAI Endpoint (https://...)")

uploaded_audio = st.file_uploader("Upload doctor-patient audio (WAV)", type=["wav"])

if uploaded_audio and speech_key and speech_region and openai_key and openai_endpoint:
    # Save uploaded file
    audio_path = "temp_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(uploaded_audio.read())
    
    # Transcribe audio
    st.write("Transcribing audio with Azure Speech-to-Text...")
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    audio_input = speechsdk.AudioConfig(filename=audio_path)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    result = recognizer.recognize_once()
    transcription = result.text
    st.subheader("Transcription")
    st.write(transcription)
    
    # Generate clinical notes
    st.write("Generating clinical notes with Azure OpenAI...")
    openai.api_type = "azure"
    openai.api_base = openai_endpoint
    openai.api_key = openai_key
    openai.api_version = "2023-03-15-preview"
    prompt = f"Summarize this conversation into clinical notes: {transcription}"
    try:
        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        notes = response['choices'][0]['message']['content']
        st.subheader("Clinical Notes")
        st.write(notes)
    except Exception as e:
        st.error(f"OpenAI error: {e}")

    # Clean up
    os.remove(audio_path)
else:
    st.info("Enter API keys/endpoint and upload a WAV audio file to begin.")
