import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:

    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)
    print("Recognizing..")
try:
    print("System Output:"+r.recognize_google(audio))
except Exception:
    print("Something went wrong.")

# with open('recordaudio.wav', 'wb') as f:
#     f.write(audio.get_wav_data())
