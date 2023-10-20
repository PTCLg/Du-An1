import os
import playsound
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar, Style
import customtkinter as ctk
from mutagen.mp3 import MP3
import threading
import time

# Setup app
app = tk.Tk()
app.configure(bg='#f2f5f9')
# Tạo main window
app.geometry('500x420+560+165')
app.title('Genius Music')
app.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
app.resizable(False, False)

# Tạo label 
lb = tk.Label(app, text='Genius Music' ,font='Lato 20 bold', background='#f2f5f9', fg='#4b4b4b')
lb.place(relx=0.305, rely=0.04)

# Tạo pygame mixer
pygame.mixer.init()

#### Tạo chức năng 

# Tìm kiếm file.mp3 
def find_ms():
    pass 

# Chọn folder
def slt_ms():
    pass

# Next bài hát
def next_ms():
    pass

# Quay lại bài hát trước
def pre_ms():
    pass

# Play bài hát
def play_ms():
    pass

# Dừng bài hát
def pause_ms():
    pass

# Tạo Button
btn_find = ctk.CTkButton(app, text='Find Music' , font=('Lato' , 14 , 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=50, command=find_ms)
btn_find.place(x=23, y=45)

btn_slt = ctk.CTkButton(app, text='Select Folder' , font=('Lato' , 14 , 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=10, command=slt_ms)
btn_slt.place(x=364, y=45)

btn_pre = ctk.CTkButton(app, text='<', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=25, height=28, command=pre_ms)
btn_pre.place(x=125, y=335)

btn_next = ctk.CTkButton(app, text='>', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=25, height=28, command=next_ms)
btn_next.place(x=355, y=335)

btn_play = ctk.CTkButton(app, text='Play', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=70, height=28, command=play_ms)
btn_play.place(x=175, y=335)

btn_pause = ctk.CTkButton(app, text='Pause', font=('Lato', 14, 'bold'), border_width=2, bg_color='transparent', corner_radius=8, width=30, height=28, command=pause_ms)
btn_pause.place(x=270, y=335)

# Tạo Frame
fr = tk.Frame(app, height=100, width=360, bg='#f8fafc', highlightbackground='#677489' , highlightthickness=2)
fr.place(anchor='center', x=254, y=205, relheight=0.55)

# Tạo thanh tiến trình chạy của bài hát
lds = Progressbar(app, cursor='hand2', length=300, mode='determinate')
lds.place(anchor='center', x=253, y=380, relheight=0.02, relwidth=0.6)


# class VoiceToTextApp:
#     pass


app.mainloop()