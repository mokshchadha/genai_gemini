import streamlit as st
import os
import tempfile
import google.generativeai as genai
import whisper
from pydub import AudioSegment
from dotenv import load_dotenv
load_dotenv()

# Configure the Gemini model
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Load Whisper model
whisper_model = whisper.load_model("base")

def extract_audio(video_path, audio_path):
    audio = AudioSegment.from_file(video_path, format="mp4")
    audio.export(audio_path, format="wav")

def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]

def summarize_text(text):
    prompt = f"Summarize the following text into concise notes:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def process_video(video_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_video:
        tmp_video.write(video_file.read())
        video_path = tmp_video.name

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_audio:
        audio_path = tmp_audio.name

    try:
        with st.spinner("Extracting audio from video..."):
            extract_audio(video_path, audio_path)

        with st.spinner("Transcribing audio..."):
            transcription = transcribe_audio(audio_path)

        with st.spinner("Generating notes from transcription..."):
            notes = summarize_text(transcription)

        return notes

    finally:
        # Clean up temporary files
        os.unlink(video_path)
        os.unlink(audio_path)

def main():
    st.title("Video to Notes Converter")

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        if st.button("Process Video"):
            notes = process_video(uploaded_file)
            st.subheader("Generated Notes:")
            st.write(notes)

if __name__ == "__main__":
    main()