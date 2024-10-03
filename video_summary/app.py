import streamlit as st
import os
import tempfile
import google.generativeai as genai
import whisper
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Load Whisper model
whisper_model = whisper.load_model("base")

def extract_audio(file_path, output_path):
    audio = AudioSegment.from_file(file_path)
    audio.export(output_path, format="wav")

def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]

def summarize_text(text):
    prompt = f"Summarize the following text into concise notes:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def process_file(uploaded_file):
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_audio:
        audio_path = tmp_audio.name

    try:
        if file_extension in ['.mp4', '.mov', '.avi']:
            with st.spinner("Extracting audio from video..."):
                extract_audio(file_path, audio_path)
        elif file_extension in ['.m4a', '.wav', '.mp3']:
            with st.spinner("Converting audio to WAV format..."):
                extract_audio(file_path, audio_path)
        else:
            st.error("Unsupported file format. Please upload a video or audio file.")
            return None, None

        with st.spinner("Transcribing audio..."):
            transcription = transcribe_audio(audio_path)

        with st.spinner("Generating notes from transcription..."):
            notes = summarize_text(transcription)

        return transcription, notes

    finally:
        # Clean up temporary files
        os.unlink(file_path)
        os.unlink(audio_path)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = data.decode()
    href = f'<a href="data:text/plain;charset=utf-8,{bin_str}" download="{file_label}">{file_label}</a>'
    return href

def main():
    st.title("Video/Audio to Notes Converter")

    uploaded_file = st.file_uploader("Choose a video or audio file", type=["mp4", "mov", "avi", "m4a", "wav", "mp3"])

    if uploaded_file is not None:
        if st.button("Process File"):
            transcription, notes = process_file(uploaded_file)
            if transcription and notes:
                st.subheader("Generated Notes:")
                st.write(notes)

                # Create temporary files for download
                with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as tmp_transcript:
                    tmp_transcript.write(transcription)
                    transcript_path = tmp_transcript.name

                with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as tmp_summary:
                    tmp_summary.write(notes)
                    summary_path = tmp_summary.name

                # Provide download options
                st.markdown("### Download Options")
                st.markdown(get_binary_file_downloader_html(transcript_path, 'Download Full Transcript'), unsafe_allow_html=True)
                st.markdown(get_binary_file_downloader_html(summary_path, 'Download Summary'), unsafe_allow_html=True)

                # Clean up temporary files
                os.unlink(transcript_path)
                os.unlink(summary_path)

if __name__ == "__main__":
    main()