import tkinter as tk
import speech_recognition as sr
import pyttsx3
from PIL import Image, ImageTk
import os
from gtts import gTTS
import playsound
import re
import pygame
from time import strftime
import wikipedia
import urllib.request as urllib2
import datetime
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
        self.text_widget = tk.Text(self.frame, bg='#c6f4be', width=50, height=14, font='Inter 16 ')        
        self.text_widget.place(relx=0.5, rely=0.52, anchor=tk.CENTER)         
        img = Image.open("13.png")
        img = img.resize((50, 50), Image.LANCZOS)
        self.button_img = ImageTk.PhotoImage(img)
        self.button = tk.Button(root, image=self.button_img, command=self.AI, borderwidth=0, bg='#cafafe')
        self.button.place(x=400, y=535, width=50, height=50)       
        self.sb() 
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
    
    # Hàm tối ưu hóa khi đọc text
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
        self.split_sentences(f'{self.robot_name} có một số câu chuyện xoay quanh tình yêu, chiến tranh, hòa bình, cuộc sống hàng ngày, phiêu lưu, khoa học viễn tưởng, lịch sử và văn hóa ')
        self.split_sentences(f'Bạn muốn nghe {self.robot_name} kể câu chuyện nào không?')
        text = self.get_audio()
        while True:
            if 'không' in text or 'no' in text or 'thôi' in text:
                self.split_sentences(f'Bạn cần {self.robot_name} giúp gì khác không?')
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
                    self.split_sentences('Tôi có câu chuyện tình yêu lãng mạn về Romeo và Juliet nó rất hay bạn hãy lắng nghe câu chuyện này')
                    self.split_sentences(""" 
                        Romeo và Juliet được viết vào khoảng 1594 - 1595, dựa trên một cốt truyện có sẵn kể về một mối tình oan trái vốn là câu chuyện có thật, từng xảy ra ở Ý thời Trung Cổ.
                        Câu chuyện bắt đầu tại thành Verona, hai dòng họ nhà Montague và nhà Capulet có mối hận thù lâu đời. Romeo, con trai họ Montague và Juliet, con gái họ Capulet đã yêu nhau say đắm ngay từ cái nhìn đầu tiên tại buổi dạ tiệc tổ chức tại nhà Capulet, do là dạ tiệc hoá trang nên Romeo mới có thể trà trộn vào trong đó. Đôi trai gái này đã đến nhà thờ nhờ tu sĩ Friar Laurence bí mật làm lễ cưới.
                        Đột nhiên xảy ra một sự việc: do xung khắc, anh họ của Juliet là Tybalt đã giết chết người bạn rất thân của Romeo là Mercutio. Để trả thù cho bạn, Romeo đã đâm chết Tybalt. Mối thù giữa hai dòng họ càng trở nên sâu nặng. Vì tội giết người nên Romeo bị trục xuất khỏi Verona và bị đi đày biệt xứ. Tưởng như mối tình của Romeo và Juliet bị tan vỡ khi Romeo đi rồi, Juliet bị cha mẹ ép gả cho Bá tước Paris. Juliet cầu cứu sự giúp đỡ của tu sĩ Laurence. Tu sĩ cho nàng uống một liều thuốc ngủ, uống vào sẽ như người đã chết, thuốc có tác dụng trong vòng 42 tiếng. Tu sĩ sẽ báo cho Romeo đến hầm mộ cứu nàng trốn khỏi thành Verona.
                        Đám cưới giữa Juliet và Paris trở thành đám tang. Xác Juliet được đưa xuống hầm mộ. Tu sĩ chưa kịp báo cho Romeo thì từ chỗ bị lưu đày nghe tin Juliet chết, Romeo đau đớn trốn về Verona. Trên đường về chàng kịp mua một liều thuốc cực độc dành cho mình. Tại nghĩa địa, gặp Paris đến viếng Juliet, Romeo đâm chết Paris rồi uống thuốc độc tự tử theo người mình yêu. Romeo vừa gục xuống thì thuốc của Juliet hết hiệu nghiệm. Nàng tỉnh dậy và nhìn thấy xác Romeo bên cạnh đã chết, Juliet rút dao tự vẫn.
                        Cái chết tang thương của đôi bạn trẻ đã thức tỉnh hai dòng họ. Bên xác hai người, hai dòng họ đã quên mối thù truyền kiếp và bắt tay nhau đoàn tụ, nhưng câu chuyện tình yêu ấy vẫn mãi sẽ là nỗi đau rất lớn trong lòng những người biết đến họ.""")
                    # time.sleep(2.5)
                    self.split_sentences('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'chiến tranh' in text2 or 'trận chiến' in text:
                    self.split_sentences('Tôi có câu chuyện chiến tranh khốc liệt về trận chiến trân châu cảng nó rất hay bạn hãy lắng nghe câu chuyện này')
                    self.split_sentences("""
                        Trận Trân Châu Cảng là một trận tấn công bất ngờ của không quân hải quân Nhật Bản vào căn cứ chính Hạm đội Thái Bình Dương của Mỹ tại Trân Châu Cảng thuộc quần đảo Hawaii. Trận chiến diễn ra vào ngày 7 tháng 12 năm 1941, đánh dấu sự khởi đầu của cuộc chiến tranh Nhật-Mỹ ở Thái Bình Dương trong Chiến tranh thế giới lần thứ Hai1
                        Vào lúc 7h55 ngày 7/12/1941, một buổi sáng yên tĩnh, khi lính Mỹ trong cảng đang ngủ say sau một tối thứ Bảy vui vẻ, nơi đây bất ngờ bị 374 chiếc máy bay Nhật tấn công. Cuộc tấn công kéo dài 90 phút đã để lại hậu quả là 2.403 binh sĩ và thủy thủ Mỹ thiệt mạng, hơn 1.000 người khác bị thương, sáu tàu chiến lớn bị đánh chìm và thiệt hại nặng, 169 máy bay chiến đấu của Mỹ đỗ tại sân bay bị phá hủy2
                        Với thắng lợi tại Trân Châu Cảng, hải quân Nhật đã loại ra khỏi vòng chiến đấu Hạm đội Thái Bình Dương của Mỹ trong nhiều tháng, tạo điều kiện thuận lợi cho quân đội Nhật đánh chiếm nhiều nước trong khu vực Đông Nam Á và làm chủ vùng biển châu Á - Thái Bình Dương trong giai đoạn đầu của Thế chiến II
                        """)
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'hòa bình' in text2 or 'độc lập' in text2:
                    self.split_sentences('Một câu chuyện nổi tiếng về hòa bình mà tôi muốn kể cho bạn nghe là câu chuyện về cô bé Sadako Sasaki và những con sếu bằng giấy.')
                    self.split_sentences("""
                        Sadako Sasaki là một cô bé người Nhật Bản, sinh ra vào năm 1943. Khi cô mới 2 tuổi, quả bom nguyên tử đã rơi xuống Hiroshima, nơi cô đang sống. Mặc dù cô đã sống sót sau vụ tấn công khủng khiếp này, nhưng vào năm 1955, khi cô 12 tuổi, cô đã được chẩn đoán mắc bệnh bạch cầu do phóng xạ
                        Trong thời gian điều trị tại bệnh viện, Sadako đã nghe về truyền thuyết Nhật Bản: nếu ai đó gấp được 1000 con sếu bằng giấy, ước muốn của họ sẽ trở thành hiện thực. Với hy vọng vào sự sống và hòa bình, Sadako đã bắt đầu công cuộc gấp 1000 con sếu từ những tờ giấy nhỏ
                        Dù rất cố gắng, nhưng cuối cùng Sadako chỉ gấp được 644 con sếu trước khi qua đời vào ngày 25 tháng 10 năm 1955. Các bạn học của Sadako đã hoàn thành phần còn lại để đạt được con số 1000 và tất cả đã được chôn cùng với Sadako
                        Câu chuyện về Sadako và những con sếu giấy đã trở thành biểu tượng cho hòa bình và hi vọng. Ngày nay, tại Công viên Hòa bình Hiroshima, bạn có thể thấy Tượng đài Trẻ em - một tượng của Sadako đang giữ một con sếu giấy - được dựng lên để tưởng nhớ đến những nạn nhân nhỏ tuổi của bom nguyên tử
                        """)
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'cuộc sống hàng ngày' in text2 or 'cuộc sống' in text2 or 'sinh hoạt' in text2 or 'đơn giản' in text2:
                    self.split_sentences('Một câu chuyện về cuộc sống hàng ngày nổi tiếng mà tôi muốn kể cho bạn nghe là câu chuyện về việc xây dựng cầu Brooklyn')
                    self.split_sentences("""
                        Câu chuyện bắt đầu vào năm 1869, khi một kỹ sư tên là John Roebling đã mơ ước xây dựng một cây cầu kỳ diệu để nối Manhattan và Brooklyn. Tuy nhiên, ông đã gặp một tai nạn thảm khốc và qua đời. Con trai của ông, Washington Roebling, đã tiếp quản dự án này
                        Trong quá trình xây dựng, Washington cũng gặp một tai nạn và bị liệt toàn bộ cơ thể, chỉ có thể nhìn và nhấp nháy. Mọi người nghĩ rằng dự án sẽ phải dừng lại. Nhưng Washington không từ bỏ. Ông đã sử dụng đôi mắt của mình để chỉ dẫn cho vợ mình, Emily, cách tiếp tục công việc
                        Emily đã học tất cả những gì cần thiết để hoàn thành cây cầu. Cô đã trở thành người phụ nữ đầu tiên giám sát một công trình lớn như vậy. Sau 14 năm, cây cầu Brooklyn cuối cùng đã hoàn thành vào năm 188
                        Câu chuyện này cho thấy rằng, dù cuộc sống hàng ngày có thể đầy rẫy khó khăn và thử thách, nhưng với lòng kiên trì và niềm tin, chúng ta có thể vượt qua mọi trở ngại để đạt được mục tiêu của mình""")
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'phiêu lưu' in text2 or 'khám phá' in text2 or 'thám hiểm' in text2:
                    self.split_sentences('Một câu chuyện phiêu lưu nổi tiếng mà tôi muốn kể cho bạn nghe là “Những Cuộc Phiêu Lưu Của Huckleberry Finn” của tác giả Mark Twain')
                    self.split_sentences("""
                        Truyện kể về cuộc phiêu lưu của cậu bé Huckleberry Finn sau khi trốn thoát khỏi cuộc sống bị ràng buộc bởi xã hội. Huck đã bắt đầu một cuộc phiêu lưu mới dọc theo sông Mississippi cùng với Jim, một nô lệ đang trốn chạy. Trong suốt cuộc hành trình, Huck đã gặp phải nhiều khó khăn và thử thách, từ việc bị cuốn vào một cuộc đấu súng chết người giữa hai gia đình, đến việc phải đối mặt với những định kiến ​​xã hộ
                        Tuy nhiên, chính trong những hoàn cảnh khó khăn nhất, Huck mới nhận ra giá trị của sự tự do và lòng trắc ẩn. Dù chỉ là một cậu bé phá phách, nhưng Huck đã biết phân biệt đúng sai và thoát khỏi những định kiến ​​méo mó do nuôi dạy sai lầ
                        “Những Cuộc Phiêu Lưu Của Huckleberry Finn” không chỉ là một câu chuyện phiêu lưu hấp dẫn, mà còn là một tác phẩm văn học sâu sắc, phản ánh rõ nét văn hóa và xã hội Mỹ vào thế kỷ 19
                          """)
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'khoa học viễn tưởng' in text2 or 'khoa học' in text2 or 'viễn tưởng' in text2 or 'tương lai' in text2:
                    self.split_sentences('Một câu chuyện khoa học viễn tưởng nổi tiếng mà tôi muốn kể cho bạn nghe là “Dune” của tác giả Frank Herbert')
                    time.sleep(0.5)
                    self.split_sentences("""“Dune” là câu chuyện về một hành tinh sa mạc tên Arrakis, nơi sản sinh ra một loại gia vị quý hiếm có khả năng gia tăng trí tuệ và kéo dài tuổi thọ con người. Đây cũng là nơi sinh sống của những con sán dầu khổng lồ. Cuốn sách xoay quanh cuộc đấu tranh quyền lực giữa các gia đình quý tộc để kiểm soát nguồn cung cấp gia vị này
                    Trong cuốn sách, Paul Atreides, con trai của một người cai trị hành tinh, đã trở thành một nhân vật trung tâm. Sau khi gia đình ông bị phản bội và cha ông bị giết, Paul đã trở thành một nhà lãnh đạo tinh thần và dẫn dắt người dân bản địa trong cuộc chiến chống lại sự áp bức
                    “Dune” không chỉ là một câu chuyện khoa học viễn tưởng hấp dẫn, mà còn là một tác phẩm phê phán xã hội, thể hiện sự lo lắng về môi trường và khám phá các khía cạnh tâm linh""")
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'lịch sử' in text2 or 'xưa' in text2 or 'lâu' in text2 or 'trước kia' in text2:
                    self.split_sentences('Một câu chuyện lịch sử nổi tiếng mà tôi muốn kể cho bạn nghe là câu chuyện về Thánh Gióng - một trong bốn vị thánh bất tử trong tín ngưỡng dân gian Việt Nam')
                    self.split_sentences("""Theo truyền thuyết, Thánh Gióng sinh ra tại xã Phù Đổng, huyện Gia Lâm, Hà Nội, thời vua Hùng thứ 6. Ông là người trời đầu thai làm đứa trẻ, lên ba rồi mà không biết nói cười, đi đứng. Nhưng khi giặc Ân tràn xuống thì Gióng cất tiếng gọi mẹ nhờ ra gọi sứ giả của nhà vua, rồi bỗng chốc vươn vai thành một thanh niên cường tráng đi đánh giặc                                
                                    Sau khi đánh tan kẻ xâm lược, ông bay về trời. Nơi ông hóa chính là núi Sóc thuộc huyện Sóc Sơn, Hà Nội. Đại Việt sử ký toàn thư kể chi tiết về Thánh Gióng như sau: Đời Hùng Vương thứ 6, ở làng Gióng có hai vợ chồng ông bà lão nghèo chăm chỉ làm ăn và có tiếng là phúc đức thế mà họ vẫn chưa có con""")
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
                elif 'văn hóa' in text2 or 'tốt đẹp' in text2 or 'truyền thống' in text2:
                    self.split_sentences('Một câu chuyện về văn hóa nổi tiếng mà tôi muốn kể cho bạn nghe là câu chuyện về “Rāmāyaṇa” - một bộ truyện cổ điển của Ấn Độ')
                    self.split_sentences("""“Rāmāyaṇa” bao gồm 24.000 câu thơ đôi trong bảy tập (kāṇḍas) và kể về câu chuyện của một hoàng tử, Rama của xứ Ayodhya, vợ là Sita bị bắt đi bởi vua quỷ (Rākshasa) vua xứ Lanka, Rāvana. Truyện không chỉ là một tác phẩm văn học xuất sắc mà còn phản ánh rõ nét văn hóa và tín ngưỡng của người Ấn Độ.
                        Ngoài ra, câu chuyện “Chim Sẻ Bị Cắt Lưỡi” cũng là một câu chuyện mang ý nghĩa đạo đức kinh điển của Nhật Bản về lòng tham và lòng tốt. Câu chuyện này đã trở thành một phần quan trọng của văn hóa Nhật Bản và được truyền từ thế hệ này sang thế hệ khác.
                        Cả hai câu chuyện trên đều là những biểu tượng văn hóa quan trọng, phản ánh giá trị và tinh thần của các nền văn hóa khác nhau.""")
                    self.speak('The end')
                    time.sleep(1)
                    self.speak(f'Bạn muốn nghe {self.robot_name} kể chuyện tiếp không')
                    textx = self.get_audio()
                    if 'có' in textx or 'yes' in textx or 'kể' in textx:
                        self.kechuyen()
                    elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                        self.stopstr()
    def stopstr(self):
        self.speak(f'Bạn muốn nghe {self.robot_name} kể câu chuyện nào nữa không?')
        time.slep(3)
        text5 = self.get_audio()
        if 'có' in text5 or 'yes' in text5 or 'chuyện' in text5:
            self.kechuyen()
        elif 'không' in text5 or 'no' in text5 or 'thôi' in text5:
            self.speak(f"Thank you bạn đã nghe câu chuyện này của {self.robot_name}")           
    
    def hello(self, name):
        day_time = int(strftime('%H'))
        if 0 <= day_time < 11:
            self.speak(f"Chào bạn {name}. Chúc bạn buổi sáng tốt lành.")
        elif 11 <= day_time < 13:
            self.speak(f"Chào bạn {name}. Chúc bạn có một buổi trưa thật vui vẻ.")
        elif 13 <= day_time < 18:
            self.speak(f"Chào bạn {name}. Chúc bạn buổi chiều vui vẻ.")
        elif 18 <= day_time < 22:
            self.speak(f"Chào bạn {name}. Tối rồi, Bạn đã cơm nước gì chưa ?")
        elif 22 <= day_time <= 23:
            self.speak(f"Chào Bạn {name}. Muộn rồi bạn nên đi nghủ sớm nha.")
        else:
            self.speak(f"Thời gian bên tôi chưa đúng hoặc gặp lỗi. Bạn nên xem lại nha.")

    def get_time(self, text):
        now = datetime.datetime.now()
        if 'giờ' in text:
          self.speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
        elif "ngày" in text:
          self.speak(f"hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
        else:
          self.speak("Lý Hành chưa hiểu ý bạn.")


    def current_weather(self):
        self.speak("Bạn muốn xem thời tiết ở đâu ạ.")
        # Đường dẫn trang web để lấy dữ liệu về thời tiết
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        # lưu tên thành phố vào biến city
        city = self.get_audio()
        # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
        if not city:
            pass
        # api_key lấy trên open weather map
        api_key = "b4750c6250a078a943b3bf920bb138a0"
        # tìm kiếm thông tin thời thời tiết của thành phố
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
        response = self.requests.get(call_url)
        # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
        data = response.json()
        # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
        if data["cod"] != "404":
            # lấy value của key main
            city_res = data["main"]
            # nhiệt độ hiện tại
            current_temperature = city_res["temp"]
            # áp suất hiện tại
            current_pressure = city_res["pressure"]
            # độ ẩm hiện tại
            current_humidity = city_res["humidity"]
            # thời gian mặt trời
            suntime = data["sys"]
            # 	lúc mặt trời mọc, mặt trời mọc
            sunrise = self.datetime.datetime.fromtimestamp(suntime["sunrise"])
            # lúc mặt trời lặn
            sunset = self.datetime.datetime.fromtimestamp(suntime["sunset"])
            # thông tin thêm
            wthr = data["weather"]
            # mô tả thời tiết
            weather_description = wthr[0]["description"]
            # Lấy thời gian hệ thống cho vào biến now
            now = self.datetime.datetime.now()
            # hiển thị thông tin với người dùng
            content = f"""
            Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
            Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
            Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
            Nhiệt độ trung bình là {current_temperature} độ C
            Áp suất không khí là {current_pressure} héc tơ Pascal
            Độ ẩm là {current_humidity}%
            """
            self.speak(content)
        else:
            # nếu tên thành phố không đúng thì nó nói dòng dưới 227
            self.speak("Không tìm thấy địa chỉ của bạn")


    def tell_me_about(self):
        try:
            self.speak("Hãy nói cho tôi nghe Bạn muốn tìm gì ạ ?")
            text = self.get_audio()
            contents = wikipedia.summary(text).split('\n')
            self.speak(contents[0])
            dem = 0
            for content in contents[1:]:
                if dem < 2:
                    self.speak("Bạn có muốn biết thêm không ???")
                    ans = self.get_audio()
                    if 'có' not in ans:
                        break
                dem += 1
                self.speak(content)
            self.speak("Đây là nội dung tôi vừa tìm được cảm ơn bạn đã lắng nghe")
        except:
            self.speak(f"{self.name} không định nghĩa được thuật ngữ của bạn !!!")


    def baothuc(self):
        invalid = True
        while (invalid):
            # Get a valid user input for the alarm time
            self.speak("bạn muốn đặt báo thức vào lúc mấy giờ")
            text = self.get_audio()
            alarmTime = [int(n) for n in text.split(":")]
            if alarmTime[0] >= 24 or alarmTime[0] < 0:
                invalid = True
            elif alarmTime[1] >= 60 or alarmTime[1] < 0:
                invalid = True
            else:
                invalid = False

        # Number of seconds in an Hour, Minute, and Second
        seconds_hms = [3600, 60, 1]

        # Convert the alarm time to seconds
        alarmSeconds = sum(
            [a*b for a, b in zip(seconds_hms[:len(alarmTime)], alarmTime)])

        now = datetime.datetime.now()
        currentTimeInSeconds = sum(
            [a*b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])

        secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

        if secondsUntilAlarm < 0:
            secondsUntilAlarm += 86400  # number of seconds in a day

        print("Alarm is set!")
        print("The alarm will ring at %s" %
            datetime.timedelta(seconds=secondsUntilAlarm))

        time.sleep(secondsUntilAlarm)

        pygame.mixer.init()
        pygame.mixer.music.load(r'Am_Thanh\baothuc.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            # stop = get_text()
            # if "tắt báo thức" in stop:
            pygame.time.Clock().tick(1)


    def demnguoc(self):
        self.speak("Bạn muốn đếm ngược bao nhiêu thời gian")
        text = self.get_audio()
        alarmTime = re.findall(r'\d+', str(text))
        if int(alarmTime[0]) > 0:
            secondsUntilAlarm = int(alarmTime[0])*60

        self.log("Alarm is set!")
        self.log("The alarm will ring at %s" %
                 datetime.timedelta(seconds=secondsUntilAlarm))

        for i in range(0, secondsUntilAlarm):
            time.sleep(1)
            secondsUntilAlarm -= 1
            self.log(datetime.timedelta(seconds=secondsUntilAlarm))

        pygame.mixer.init()
        pygame.mixer.music.load(r'Am_Thanh\baothuc.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        self.stop_audio()
        pygame.mixer.quit()

    def recognize_speech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Nghe...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="vi")
            print(f"Bạn đã nói: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Không thể nhận diện giọng nói.")
            return ""
        except sr.RequestError as e:
            print(f"Lỗi kết nối đến Google API: {e}")
            return ""

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
            tt1 = self.get_audio()
            if 'có' in tt1 or 'yes' in tt1:
                self.chat_human()
            else:
                self.stop()
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
                self.chat_human()
            elif 'kể' in text or 'kể chuyện' in text or 'chuyện' in text or 'buồn' in text or 'chán' in text or 'nói' in text or 'truyện' in text:
                self.story()
            elif 'thời gian' in text or 'bây giờ' in text or 'mấy giờ' in text or 'time' in text:
                self.ttime()
            elif "chào" in text:
                self.hello(os.getlogin())
            elif "hiện tại" in text:
                self.get_time(text)
            elif "thời tiết" in text:
                self.current_weather()
            elif "định nghĩa" in text:
                self.tell_me_about()
            elif "đặt báo thức" in text:
                self.baothuc()
            elif "đếm ngược" in text:
                self.demnguoc()
            

    def sb(self):
        lb = tk.Label(self.root, text='TRỢ LÝ ẢO GENIUS', font='Inter 28 bold', fg='black', bg='#cafafe')
        lb.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

root = tk.Tk()
root.geometry('850x650+320+90')
root.title('Genius')
root.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
root.resizable(False, False)
app = VoiceToTextApp(root)
root.after(1000, app.greet)
root.mainloop()
