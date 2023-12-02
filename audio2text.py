import streamlit as st
import openai
import tempfile
import whisper
import os

openai.api_key = "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"

st.title("Summarization of Audio Content")
st.write('\n\n')

# ------------------------------------------------------------------------------------------------------------------

# File path is retrieved by using streamlit's file uploader. A temporary directoy is created
# where the file is uploaded, so that we can get the path as a string.

file_path = ''
uploaded_file = st.file_uploader("File upload")
if uploaded_file:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())


# ------------------------------------------------------------------------------------------------------------------

# Functions for transcription and summarizing of audio.

model = whisper.load_model("base")

def transcribe_audio(model, file_path):
    transcript = model.transcribe(file_path)
    return transcript['text']

def CustomChatGPT(user_input):
    messages = [{"role": "system", "content": "You are an office administer, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    return ChatGPT_reply

# -----------------------------------------------------------------------------------------------------------------

# When the button is pressed, the summary starts being generated. It checks that there was a file selected.

if st.button('Generate summary'):
     text = ''
     if file_path != '':
          transcription = transcribe_audio(model, file_path)
          summary = CustomChatGPT(transcription)
          st.write(summary)
     else:
          text = "Please, select an audio file."
          st.write(text)
else:
	st.write("Press the above button.")

