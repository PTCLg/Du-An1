from pygame.locals import *
import speech_recognition as sr
from time import strftime
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage
import os
import playsound
from gtts import gTTS


def speak(text): 
    app.update_idletasks() 
    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")

# Tạo hàm hướng dẫn trò chuyện
def tc():
    speak('Tạo hàm hướng dẫn trò chuyện')

# Tạo hàm hướng dẫn tìm kiếm thông tin
def search():
    speak('Tạo hàm hướng dẫn tìm kiếm thông tin')

# Tạo hàm hướng dẫn đặt lịch hẹn
def dl():
    speak('Tạo hàm hướng dẫn đặt lịch hẹn')

# Tạo hàm hướng dẫn sử dụng Genius Music
def music():
    speak('Tạo hàm hướng dẫn sử dụng Genius Music')


# Setup app
app = tk.Tk()
app.configure(bg='#fefbed')
# Tạo main window
app.geometry('500x420+560+165')
app.title('Genius Help')
app.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
app.resizable(False, False)

# Tạo label 
lb = tk.Label(app, text='Genius Help' ,font='Lato 24 bold', background='#fefbed', fg='#4b4b4b')
lb.place(relx=0.1, rely=0.11)

img = Image.open('ai.png')
reimg = img.resize((img.width // 5, img.height // 5))
reimg.save('resized_ai.png')
reip = PhotoImage(file='resized_ai.png')
lbi = tk.Label(app, image=reip, background='#fefbed')
lbi.place(relx=0.63, rely=0.05)


# Tạo Button
btn1 = tk.Button(app, text='Trò Chuyện' , font=('Lato' , 14 , 'bold'), width=11, height=3,
                background='#d5faf1', borderwidth=2, relief='solid', command=tc)
btn1.place(x=65, y=145)

btn2 = tk.Button(app, text='Tìm kiếm TT' , font=('Lato' , 14 , 'bold'),  width=11, height=3, 
                background='#d5faf1', borderwidth=2, relief='solid', command=search)
btn2.place(x=290, y=145)

btn3 = tk.Button(app, text='Đặt lịch', font=('Lato', 14, 'bold'),  width=11, height=3,
                background='#d5faf1', borderwidth=2, relief='solid', command=dl)
btn3.place(x=65, y=270)

btn4 = tk.Button(app, text='Music', font=('Lato', 14, 'bold'),  width=11, height=3, 
                background='#d5faf1', borderwidth=2, relief='solid', command=music)
btn4.place(x=290, y=270)



app.mainloop()