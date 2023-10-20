import tkinter as tk
import speech_recognition as sr
import pyttsx3
from PIL import Image, ImageTk
import os
from gtts import gTTS
import playsound
import re
import time
class VoiceToTextApp:
    def __init__(self, root):
        self.root = root
        self.robot_name = "Genius"  
        self.root.configure(bg='#cafafe') 
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'vietnamese' in voice.languages:
                self.engine.setProperty('voice', voice.id)
                break
        current_voice = self.engine.getProperty('voice')
        print(current_voice)
        self.frame = tk.Frame(root, bg='#cafafe')
        self.frame.pack(fill='both', expand=True)
        self.text_widget = tk.Text(self.frame, bg='#c6f4be', width=50, height=14, font='Inter 16')        
        self.text_widget.place(relx=0.5, rely=0.52, anchor=tk.CENTER)         
        img = Image.open("Ellipse 1.png")
        img = img.resize((50, 50), Image.LANCZOS)
        self.button_img = ImageTk.PhotoImage(img)
        self.button = tk.Button(root, image=self.button_img, command=self.AI, borderwidth=0, highlightcolor='black', bg='#cafafe', highlightbackground='black')
        self.button.place(x=400, y=535, width=50, height=50)       
        self.sb() 
        self.AI()
    def greet(self):
        default = 'Chào bạn, tôi là trợ lý Genius!!! Tôi có thể giúp gì?'
        self.speak(default)
    def speak(self, text):
    # Thêm văn bản vào widget Text
        self.text_widget.insert(tk.END, "Genius: " + text + '\n')
        self.text_widget.see(tk.END)  # Auto-scroll to the end
        self.root.update_idletasks()  # Update the GUI
        tts = gTTS(text=text, lang="vi", slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", True)
        os.remove("sound.mp3")

    def get_audio(self):
        ear_robot = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"{self.robot_name}:  Đang nghe ! -- __ -- !")
            audio = ear_robot.record(source , duration= 4)
            try:
                print((f"{self.robot_name} :  ...  "))
                text = ear_robot.recognize_google(audio, language="vi-VN")
                print("Tôi:  ", text)
                self.text_widget.insert(tk.END, "User: " + text + '\n')  # Insert user's spoken text into Text widget
                self.text_widget.see(tk.END)  # Auto-scroll to the end
                self.root.update_idletasks()  # Update the GUI
                return text
            except Exception as ex:
                print(f"{self.robot_name}:  Lỗi Rồi ! ... !")
                return 0

    def get_audio_2(self):
        ear_robot = sr.Recognizer()
        with sr.Microphone() as source:
            ear_robot.pause_threshold = 2
            print(f"{self.robot_name}: Đang nghe ======")
            audio = ear_robot.listen(source)
            try:
                text = ear_robot.recognize_google(audio, language="vi-VN")
            except:
                self.speak(f"{self.robot_name}: Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
                text = input(f"{self.robot_name}: Mời nhập: ")
            return text.lower()
    
    def stop(self):
        self.speak("Hẹn gặp lại sau nha ! ... ")
        text = self.get_text()
        if 'ok' in text or ' ' in text or 'dừng' in text or 'stop' in text:
            exit()
    
    
def split_sentences(self, long_paragraph):
    
    # Bộ nhớ đệm để lưu trữ các đoạn văn đã xử lý
    self.cache = {}
    
    # Kiểm tra xem đoạn văn đã có trong bộ nhớ đệm hay chưa
    if long_paragraph in self.cache:
        return self.cache[long_paragraph]
    
    paragraphs = []
    sentences = re.split(r'(?<=[.!?])\s+', long_paragraph)
    
    for sentence in sentences:
        paragraphs.append(sentence)
    
    self.cache[long_paragraph] = paragraphs
    
    for paragraph in paragraphs:
        self.speak(paragraph)
        
    return paragraphs

def story(self):
        self.speak(f'Bạn muốn tâm sự với {self.robot_name} một chút cho thư giãn không')
        time.sleep(1)
        text3 = self.get_audio()
        if 'có' in text3 or 'yes' in text3 or 'truyện' in text3:
            self.kechuyen()
        else:
            self.speak(f'Bạn cần {self.robot_name} giúp gì nữa không?')
            text4 = self.get_audio()
            if 'có' in text4 or 'yes' in text4:
                self.helpm()
            elif 'không' in text4 or 'no' in text4 or 'thôi' in text4:
                self.stop()

def kechuyen(self):
    self.speak(f'{self.robot_name} có một số câu chuyện xoay quanh tình yêu, chiến tranh, hòa bình, cuộc sống hàng ngày, phiêu lưu, khoa học viễn tưởng, lịch sử và văn hóa ')
    self.speak(f'Bạn muốn nghe {self.robot_name} kể câu chuyện nào không?')
    text = self.get_audio()
    while True:
        if 'không' in text or 'no' in text or 'thôi' in text:
            self.speak(f'Bạn cần {self.robot_name} giúp gì khác không?')
            textt = self.get_audio()
            if 'có' in textt or 'yes' in textt:
                self.helpm()
                break
            elif 'không' in textt or 'no' in textt or 'thôi' in textt:
                self.stop()
        elif 'có' in text or 'yes' in text or 'truyện' in text:
            self.speak('Bạn muốn nghe chuyện gì nào?')
            time.sleep(5)
            text2 = self.get_audio()
            if 'tình yêu' in text2 or 'tình' in text:
                # Replace with a complete love story
                self.speak('Here is a love story...')
                time.sleep(1)
                self.stopstr()
            elif 'chiến tranh' in text2 or 'trận chiến' in text:
                # Replace with a complete war story
                self.speak('Here is a war story...')
                time.sleep(1)
                self.stopstr()

def stopstr(self):
    self.speak(f'Bạn muốn nghe {self.robot_name} kể câu chuyện nào nữa không?')
    time.sleep(3)
    text5 = self.get_audio()
    if 'có' in text5 or 'yes' in text5 or 'chuyện' in text5:
        self.kechuyen()
    elif 'không' in text5 or 'no' in text5 or 'thôi' in text5:
        self.speak(f"Thank you bạn đã nghe câu chuyện này của {self.robot_name}")

    
    
    def helpm(self):
        self.speak(f"""{self.robot_name} có một số công việc sau:
          1. kể chuyện
          2. đếm ngược thời gian
          3. đặt báo thức
          4. tìm kiếm thông tin
          5. dự báo thời tiết
          6. thông báo thời gian hiện tại
          7. định nghĩa
          và một số thông tin khác
          """)
    
    def AI(self):
        self.speak("Xin chào. Bạn tên là gì ?")
        name = self.get_audio()
        if name:
            self.speak(f'Xin chào bạn {name}.')
            self.speak(f'Bạn cần {self.robot_name} giúp gì không ?')
            tt = self.get_audio()
            if 'có' in tt or 'yes' in tt:
                def chat_human(self):         
                    self.speak(f'Bạn muốn {self.robot_name} làm gì nào ?')
                    text = self.get_audio()
                    while True:
                        if not text:
                            self.stop()
                        elif "dừng" in text or "tạm biệt" in text:
                            self.stop()
                        elif 'chưa rõ' in text or 'help' in text or 'gợi ý' in text or 'giúp đỡ' in text or 'hướng dẫn' in text or 'show' in text or 'không' in text:
                            self.helpm()
                            chat_human()
                        elif 'kể' in text or 'kể chuyện' in text or 'chuyện' in text or 'buồn' in text or 'chán' in text or 'nói' in text or 'truyện' in text:
                            self.story()
                        elif 'thời gian' in text or 'bây giờ' in text or 'mấy giờ' in text or 'time' in text:
                            self.ttime()
                self.chat_human()
            else:
                self.stop()

    def sb(self):
        lb = tk.Label(self.root, text='TRỢ LÝ ẢO GENIUS', font='Inter 28 bold', fg='black', bg='#cafafe')
        lb.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

root = tk.Tk()
root.geometry('850x650+320+90')
root.title('Genius')
root.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
app = VoiceToTextApp(root)
root.after(1000, app.greet)
root.mainloop()
