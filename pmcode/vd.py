import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.ttk import Progressbar, Style
import customtkinter as ctk
from PIL import Image

# Setup app
app = tk.Tk()
app.configure(bg='#fefbed')
# Tạo main window
app.geometry('500x420+560+165')
app.title('Genius Help')
app.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
# app.resizable(False, False)

# Tạo label 
lb = tk.Label(app, text='Genius Help' ,font='Lato 24 bold', background='#fefbed', fg='#4b4b4b')
lb.place(relx=0.1, rely=0.11)

img = Image.open('ai.png')
reimg = img.resize((img.width // 5, img.height // 5))
reimg.save('resized_ai.png')
reip = PhotoImage(file='resized_ai.png')
lbi = tk.Label(app, image=reip, background='#fefbed')
lbi.place(relx=0.63, rely=0.05)

# # Tạo Button
# import subprocess
# def openGe():
#   subprocess.Popen(['đường dẫn đến phần mềm Genius'])

btn1 = tk.Button(app, text='t' , font=('Lato' , 14 , 'bold'), width=11, height=3,
                background='#d5faf1', borderwidth=2, relief='solid')

btn1.place(x=65, y=145)

btn2 = tk.Button(app, text='p' , font=('Lato' , 14 , 'bold'),  width=11, height=3, 
                background='#d5faf1', borderwidth=2, relief='solid')

btn2.place(x=290, y=145)

btn3 = tk.Button(app, text='d', font=('Lato', 14, 'bold'),  width=11, height=3,
                background='#d5faf1', borderwidth=2, relief='solid')
btn3.place(x=65, y=270)

btn4 = tk.Button(app, text='#', font=('Lato', 14, 'bold'),  width=11, height=3, 
                background='#d5faf1', borderwidth=2, relief='solid')
btn4.place(x=290, y=270)

generate_btn_img = tk.PhotoImage("image_1.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=0, highlightthickness=0,
 relief="flat")
generate_btn.place(x=557, y=401, width=180, height=55)

app.mainloop()
