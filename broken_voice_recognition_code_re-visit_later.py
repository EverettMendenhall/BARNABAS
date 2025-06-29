import speech_recognition as sr
r = sr.Recognizer()
audio = None

# Check for available microphones
mic_list = sr.Microphone.list_microphone_names()
if not mic_list:
    print("No microphones found. Please connect a microphone and try again.")
else:
    print("Available microphones:")
    for idx, name in enumerate(mic_list):
        print(f"  {idx}: {name}")
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    except Exception as mic_error:
        print(f"Microphone error: {mic_error}")

if audio is not None:
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from service; {e}")
