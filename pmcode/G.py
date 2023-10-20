# import tkinter as tk
# import speech_recognition as sr
# import pyttsx3
# from PIL import Image, ImageTk
# import os
# from gtts import gTTS
# import playsound
# import re

# class VoiceToTextApp:
#     def __init__(self, root):
#         self.root = root
#         self.robot_name = "Genius"  
#         self.root.configure(bg='#cafafe') 
#         self.recognizer = sr.Recognizer()
#         self.microphone = sr.Microphone()
#         self.engine = pyttsx3.init()
#         voices = self.engine.getProperty('voices')
#         for voice in voices:
#             if 'vietnamese' in voice.languages:
#                 self.engine.setProperty('voice', voice.id)
#                 break
#         current_voice = self.engine.getProperty('voice')
#         print(current_voice)
#         self.frame = tk.Frame(root, bg='#cafafe')
#         self.frame.pack(fill='both', expand=True)
#         self.text_widget = tk.Text(self.frame, bg='#c6f4be', width=50, height=14, font='Inter 16')        
#         self.text_widget.place(relx=0.5, rely=0.52, anchor=tk.CENTER)         
#         img = Image.open("Ellipse 1.png")
#         img = img.resize((50, 50), Image.LANCZOS)
#         self.button_img = ImageTk.PhotoImage(img)
#         self.button = tk.Button(root, image=self.button_img, command=self.AI, borderwidth=0, highlightcolor='black', bg='#cafafe', highlightbackground='black')
#         self.button.place(x=400, y=535, width=50, height=50)       
#         self.sb() 
#     def greet(self):
#         default = 'Chào bạn, tôi là trợ lý Genius!!! Tôi có thể giúp gì?'
#         self.speak(default)
#     def speak(self, text):
#     # Thêm văn bản vào widget Text
#         self.text_widget.insert(tk.END, "Genius: " + text + '\n')
#         self.text_widget.see(tk.END)  # Auto-scroll to the end
#         self.root.update_idletasks()  # Update the GUI
#         tts = gTTS(text=text, lang="vi", slow=False)
#         tts.save("sound.mp3")
#         playsound.playsound("sound.mp3", True)
#         os.remove("sound.mp3")

#     def get_audio(self):
#         ear_robot = sr.Recognizer()
#         with sr.Microphone() as source:
#             print(f"{self.robot_name}:  Đang nghe ! -- __ -- !")
#             audio = ear_robot.record(source , duration= 4)
#             try:
#                 print((f"{self.robot_name} :  ...  "))
#                 text = ear_robot.recognize_google(audio, language="vi-VN")
#                 print("Tôi:  ", text)
#                 self.text_widget.insert(tk.END, "User: " + text + '\n')  # Insert user's spoken text into Text widget
#                 self.text_widget.see(tk.END)  # Auto-scroll to the end
#                 self.root.update_idletasks()  # Update the GUI
#                 return text
#             except Exception as ex:
#                 print(f"{self.robot_name}:  Lỗi Rồi ! ... !")
#                 return 0

#     def get_audio_2(self):
#         ear_robot = sr.Recognizer()
#         with sr.Microphone() as source:
#             ear_robot.pause_threshold = 2
#             print(f"{self.robot_name}: Đang nghe ======")
#             audio = ear_robot.listen(source)
#             try:
#                 text = ear_robot.recognize_google(audio, language="vi-VN")
#             except:
#                 self.speak(f"{self.robot_name}: Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
#                 text = input(f"{self.robot_name}: Mời nhập: ")
#             return text.lower()
#     def AI(self):
#         self.speak("Xin chào. Bạn tên là gì ?")
#         name = self.get_audio()
#         if name:
#             self.speak(f'Xin chào bạn {name}.')
#             self.speak(f'Bạn cần {self.robot_name} giúp gì không ?')
#             tt1 = self.get_audio()
#             if 'có' in tt1 or 'yes' in tt1:
#                 self.chat_human()

#     def chat_human(self):         
#         self.speak(f'Bạn muốn {self.robot_name} làm gì nào ?')

#     def sb(self):
#         lb = tk.Label(self.root, text='TRỢ LÝ ẢO GENIUS', font='Inter 28 bold', fg='black', bg='#cafafe')
#         lb.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# root = tk.Tk()
# root.geometry('850x650+320+90')
# root.title('Genius')
# # root.iconbitmap('E:\cnpm\da1\pmcode')
# app = VoiceToTextApp(root)
# root.after(1000, app.greet)
# root.mainloop()


# import os
# import playsound
# import pygame
# import tkinter as tk
# from tkinter import filedialog
# from tkinter.ttk import Progressbar 
# import customtkinter as ctk
# from mutagen.mp3 import MP3
# import threading
# import time

# # Setup app
# app = tk.Tk()
# app.configure(bg='#f2f5f9')
# # Tạo main window
# app.geometry('470x400+560+165')
# app.title('Genius Music')
# app.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
# app.resizable(False, False)

# # Tạo label 
# lb = tk.Label(app, text='Genius Music' ,font='Lato 18 bold')
# lb.place(relx=0.301, rely=0.04)

# # Tạo chức năng 
# def find_ms():
#     pass 
# def slt_ms():
#     pass
# def next_ms():
#     pass
# def pre_ms():
#     pass
# def play_ms():
#     pass
# def pause_ms():
#     pass

# # Tạo Button
# btn_find = ctk.CTkButton(app, text='Find Music' , font=('Lato' , 14 , 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=30, command=find_ms)
# btn_find.place(x=20, y=35)

# btn_slt = ctk.CTkButton(app, text='Select Folder' , font=('Lato' , 14 , 'bold'), border_width=2, bg_color='transparent', corner_radius=10, width=30, command=slt_ms)
# btn_slt.place(x=330, y=35)

# btn_pre = ctk.CTkButton(app, text='<', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=10, width=17, height=28, command=pre_ms)
# btn_pre.place(x=100, y=320)

# btn_next = ctk.CTkButton(app, text='>', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=10, width=17, height=28, command=next_ms)
# btn_next.place(x=335, y=320)

# btn_play = ctk.CTkButton(app, text='Play', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=10, width=50, height=28, command=play_ms)
# btn_play.place(x=155, y=320)

# btn_pause = ctk.CTkButton(app, text='Pause', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=10, width=25, height=28, command=pause_ms)
# btn_pause.place(x=245, y=320)






# class VoiceToTextApp:
#     pass
# def play():
#     pass


# app.mainloop()

import tkinter as tk
from tkinter import ttk

app = tk.Tk()

style = ttk.Style()
style.configure("TFrame", background="black", borderwidth=3, relief="solid")

fr = ttk.Frame(app)
fr.place(anchor='center', x=254, y=205, relheight=0.55)

app.mainloop()
