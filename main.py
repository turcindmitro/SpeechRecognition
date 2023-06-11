import speech_recognition as s_r
import pyttsx3

print(s_r.__version__)
r = s_r.Recognizer()

my_mic = s_r.Microphone(device_index=9)

with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

engine = pyttsx3.init()

try:
    text = r.recognize_google(audio)
    engine.say(text)
except s_r.UnknownValueError:
    engine.say("Sorry, I did not understand that.")
except s_r.RequestError as e:
    engine.say(f"Could not request results; {e}")

engine.runAndWait()



# import speech_recognition as s_r
#
# for index, name in enumerate(s_r.Microphone.list_microphone_names()):
#     print(f"Microphone with name \"{name}\" found for `Microphone(device_index={index})`")