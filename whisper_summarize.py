'''
pip install openai==0.28

install ffmpeg and add to path as indicated in https://phoenixnap.com/kb/ffmpeg-windows for windows

instrucciones of this in teachers stuff.

streamlit for other stuff
''' 
import openai
#https://medium.com/gitconnected/using-the-whisper-api-to-transcribe-audio-files-45fb36d1aa1b

import whisper
# brew install ffmpeg # you may need to install

openai.api_key = "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"
# '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'
model = whisper.load_model("base")

file_path = 'pet_sematary.mp3' # 'MA1.m4a'

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


transcription = transcribe_audio(model, file_path)
summary = CustomChatGPT(transcription)
print(summary)



