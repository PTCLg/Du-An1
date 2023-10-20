import os
import random
import datetime
from playsound import playsound
import time
from pygame import mixer
import speech_recognition as sr
from gtts import gTTS
from time import strftime
import pyttsx3
import wikipedia
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bardapi import Bard


# chuyển văn bản thành âm thanh
def speak(text):
    print("Trợ Lý ảo:  ", text)
    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")


# chuyển giọng nói thành văn bản
def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trợ Lý Ảo:  Đang nghe ! -- __ -- !")

        # ear_robot.pause_threshold = 4
        audio = ear_robot.record(source , duration= 4)
        # audio = ear_robot.listen(source, phrase_time_limit=5)

        try:
            print(("Trợ Lý Ảo :  ...  "))
            text = ear_robot.recognize_google(audio, language="vi-VN")
            print("Tôi:  ", text)
            return text
        except Exception as ex:
            print("Trợ Lý Ảo:  Lỗi Rồi ! ... !")
            return 0


def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        ear_robot.pause_threshold = 2
        print("Đang nghe ===========================")
        audio = ear_robot.listen(source)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        speak("Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
        text = input("Mời nhập: ")
    return text.lower()

def stop():
    speak("Hẹn gặp lại sau nha ! ... ")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Trợ Lý Ảo không nghe rõ bạn nói. Vui lòng nói lại nha !")
    time.sleep(3)
    stop()
    return 0

# # tìm kiếm thông tin ( định nghĩa )
# def search(info): 
#     wikipedia.set_lang('vi')
#     language = 'vi'
#     path = ChromeDriverManager().install()
#     voice = pyttsx3.init()
#     In = input("Nhập thông tin cần search: ")
#     result = wikipedia.summary(In)
#     print(result)
#     voice.say(result)
#     voice.runAndWait()

# tìm kiếm thời gian
def get_time(text):
    now = datetime.datetime.now()
    def speak(text):
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("voice", "vi-VN")
        engine.say(text)
        engine.runAndWait()
    if "giờ" in text or "ngày" in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút")

        

# # Báo thức

# def get_alarm():
#     alarmHour = int(input("Nhập giờ: "))
#     alarmMin = int(input("Nhập phút: "))
#     alarmSec = int(input("Nhập giây: "))
#     alarmAP = input("Nhập am / pm: ")

#     if alarmAP == "pm":
#         alarmHour+=12
#     while True:
#         if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute and alarmSec == datetime.datetime.now().second:
#             print("Báo thức sắp đến")
#             play_random_music()
#             break

# def play_random_music():
#     music_file = 'Dậy Đi.mp3'
#     if os.path.isfile(music_file):
#         mixer.init()
#         mixer.music.load('Dậy Đi.mp3')
#         mixer.music.play()
#         while True:
#             stop = input("Nhập 'stop' để dừng âm thanh: ")
#             if stop.lower() == 'stop':
#                 mixer.music.stop()
#                 break

# mixer.init()
# get_alarm()


# Chao hoi


# ke chuyen
def story():
    os.environ["_BARD_API_KEY"] = "bggoE2FdeHrX-GP0laq1s5Z8SaZ1iR-Q9ZEuWqOQDhsajy3uGccB1-Mi5xDn48yAHXSeCw."
    message = input("Nhập nội dung: ")
    print(Bard().get_answer(str(message)))
    response = Bard().get_answer(str(message))

    def convert_to_voice(text):
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("voice", "vi-VN")
        engine.say(text)
        engine.runAndWait()
        
     # in văn bản ra
    print(response)
    
    # đọc văn bản đó lên
    convert_to_voice(response)

# nói 
speak("Xin chào. Bạn tên là gì ?") 
global robot_name
robot_name = "tên"
global name
name = get_text()
if name:
    speak(f'Xin chào bạn {name}.')
    speak(f'Bạn cần LÝ HÀNH giúp gì không ạ ?')

        
    