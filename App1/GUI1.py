import re
import os
import time
import datetime
from time import strftime
import playsound
import speech_recognition as sr
from gtts import gTTS
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import pygame
import wikipedia
import requests


#Set up
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


app = Tk()
app.title('Genius')
app.iconbitmap('E:\\cnpm\\da1\\pmcode\\ai.ico')
app.geometry('750x550+380+110')
app.configure(background='#cafafe')


# chuyển văn bản thành âm thanh
def speak(text):
    print(f"{robot_name}:  ", text)
    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")


# chuyển giọng nói thành văn bản
def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{robot_name}:  Đang nghe ! -- __ -- !")
        audio = ear_robot.record(source , duration= 4)
        try:
            print((f"{robot_name} :  ...  "))
            text = ear_robot.recognize_google(audio, language="vi-VN")
            print("Tôi:  ", text)
            return text
        except Exception as ex:
            print(f"{robot_name}:  Lỗi Rồi ! ... !")
            return 0

def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        ear_robot.pause_threshold = 2
        print("Đang nghe ======")
        audio = ear_robot.listen(source)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        speak("Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
        text = input("Mời nhập: ")
    return text.lower()


# Dừng 
def stop():
    speak("Hẹn gặp lại sau nha ! ... ")
    text = get_text()
    if 'ok' in text or ' ' in text or 'dừng' in text or 'stop' in text:
        exit()

# Văn bản
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak(f"Hiện {robot_name} không nghe rõ bạn nói. Vui lòng nói lại nha !")
    time.sleep(3)
    stop()
    return 0

# thông báo thời gian và các buổi trong ngày    
def ttime():
    Time = strftime("%H:%M:%S")
    text = get_text()
    time.sleep(0.5)
    while True:
        if Time >= "05:30:00" and Time <= "11:45:00":
            speak(f"Bây giờ là {Time} sáng")
        elif Time >="11:46:00" and Time <= "17:30:00":
            speak(f"Bây giờ là {Time} chiều ! Sắp tối rồi đó bạn đã về chưa?")
        elif Time >= "17:31:00" and Time <= "22:30:00":
            speak(f"Bây giờ là {Time} tối! Bạn đã ăn cơm chưa?")
        else:
            speak(f"Bây giờ là {Time}. Đêm rồi đó! Bạn đã ngủ chưa?")
            text1 = get_text()
            if 'chưa' in text1:
                speak('Muộn rồi đó ngủ sớm thôi bạn')
                stop()
            elif ' ' in text1 or 'không' in text1 or 'hủy' in text or 'ok' in text or 'được rồi' in text:
                speak('Hẹn gặp lại sau nha ! ... ')
                stop()


def split_sentences(long_paragraph):
    
    # Bộ nhớ đệm để lưu trữ các đoạn văn đã xử lý
    cache = {}
    
    # Kiểm tra xem đoạn văn đã có trong bộ nhớ đệm hay chưa
    if long_paragraph in cache:
        return cache[long_paragraph]
    
    paragraphs = []
    sentences = re.split(r'(?<=[.!?])\s+', long_paragraph)
    
    for sentence in sentences:
        paragraphs.append(sentence)
    
    cache[long_paragraph] = paragraphs
    
    for paragraph in paragraphs:
        speak(paragraph)
        
    return paragraphs
def story():
    speak(f'Bạn muốn tâm sự với {robot_name} một chút cho thư giãn không')
    time.sleep(1)
    text3 = get_text()
    if 'có' in text3 or 'yes' in text3 or 'truyện' in text3:
        def kechuyen():
            split_sentences(f'{robot_name} có một số câu chuyện xoay quanh tình yêu, chiến tranh, hòa bình, cuộc sống hàng ngày, phiêu lưu, khoa học viễn tưởng, lịch sử và văn hóa ')
            split_sentences(f'Bạn muốn nghe {robot_name} kể câu chuyện nào không?')
            text = get_text()
            while True:
                if 'không' in text or 'no' in text or 'thôi' in text:
                    split_sentences(f'Bạn cần {robot_name} giúp gì khác không?')
                    textt = get_text()
                    if 'có' in textt or 'yes' in textt:
                        helpm()
                        break
                    elif 'không' in textt or 'no' in textt or 'thôi' in textt:
                        stop()
                elif 'có' in text or 'yes' in text or 'truyện' in text:
                    speak('Bạn muốn nghe chuyện gì nào?')
                    time.sleep(5)
                    text2 = get_text()
                    if 'tình yêu' in text2 or 'tình' in text:
                        split_sentences('Tôi có câu chuyện tình yêu lãng mạn về Romeo và Juliet nó rất hay bạn hãy lắng nghe câu chuyện này')
                        split_sentences(""" 
                            Romeo và Juliet được viết vào khoảng 1594 - 1595, dựa trên một cốt truyện có sẵn kể về một mối tình oan trái vốn là câu chuyện có thật, từng xảy ra ở Ý thời Trung Cổ.
                            Câu chuyện bắt đầu tại thành Verona, hai dòng họ nhà Montague và nhà Capulet có mối hận thù lâu đời. Romeo, con trai họ Montague và Juliet, con gái họ Capulet đã yêu nhau say đắm ngay từ cái nhìn đầu tiên tại buổi dạ tiệc tổ chức tại nhà Capulet, do là dạ tiệc hoá trang nên Romeo mới có thể trà trộn vào trong đó. Đôi trai gái này đã đến nhà thờ nhờ tu sĩ Friar Laurence bí mật làm lễ cưới.
                            Đột nhiên xảy ra một sự việc: do xung khắc, anh họ của Juliet là Tybalt đã giết chết người bạn rất thân của Romeo là Mercutio. Để trả thù cho bạn, Romeo đã đâm chết Tybalt. Mối thù giữa hai dòng họ càng trở nên sâu nặng. Vì tội giết người nên Romeo bị trục xuất khỏi Verona và bị đi đày biệt xứ. Tưởng như mối tình của Romeo và Juliet bị tan vỡ khi Romeo đi rồi, Juliet bị cha mẹ ép gả cho Bá tước Paris. Juliet cầu cứu sự giúp đỡ của tu sĩ Laurence. Tu sĩ cho nàng uống một liều thuốc ngủ, uống vào sẽ như người đã chết, thuốc có tác dụng trong vòng 42 tiếng. Tu sĩ sẽ báo cho Romeo đến hầm mộ cứu nàng trốn khỏi thành Verona.
                            Đám cưới giữa Juliet và Paris trở thành đám tang. Xác Juliet được đưa xuống hầm mộ. Tu sĩ chưa kịp báo cho Romeo thì từ chỗ bị lưu đày nghe tin Juliet chết, Romeo đau đớn trốn về Verona. Trên đường về chàng kịp mua một liều thuốc cực độc dành cho mình. Tại nghĩa địa, gặp Paris đến viếng Juliet, Romeo đâm chết Paris rồi uống thuốc độc tự tử theo người mình yêu. Romeo vừa gục xuống thì thuốc của Juliet hết hiệu nghiệm. Nàng tỉnh dậy và nhìn thấy xác Romeo bên cạnh đã chết, Juliet rút dao tự vẫn.
                            Cái chết tang thương của đôi bạn trẻ đã thức tỉnh hai dòng họ. Bên xác hai người, hai dòng họ đã quên mối thù truyền kiếp và bắt tay nhau đoàn tụ, nhưng câu chuyện tình yêu ấy vẫn mãi sẽ là nỗi đau rất lớn trong lòng những người biết đến họ.""")
                        # time.sleep(2.5)
                        split_sentences('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'chiến tranh' in text2 or 'trận chiến' in text:
                        split_sentences('Tôi có câu chuyện chiến tranh khốc liệt về trận chiến trân châu cảng nó rất hay bạn hãy lắng nghe câu chuyện này')
                        split_sentences("""
                            Trận Trân Châu Cảng là một trận tấn công bất ngờ của không quân hải quân Nhật Bản vào căn cứ chính Hạm đội Thái Bình Dương của Mỹ tại Trân Châu Cảng thuộc quần đảo Hawaii. Trận chiến diễn ra vào ngày 7 tháng 12 năm 1941, đánh dấu sự khởi đầu của cuộc chiến tranh Nhật-Mỹ ở Thái Bình Dương trong Chiến tranh thế giới lần thứ Hai1.

                            Vào lúc 7h55 ngày 7/12/1941, một buổi sáng yên tĩnh, khi lính Mỹ trong cảng đang ngủ say sau một tối thứ Bảy vui vẻ, nơi đây bất ngờ bị 374 chiếc máy bay Nhật tấn công. Cuộc tấn công kéo dài 90 phút đã để lại hậu quả là 2.403 binh sĩ và thủy thủ Mỹ thiệt mạng, hơn 1.000 người khác bị thương, sáu tàu chiến lớn bị đánh chìm và thiệt hại nặng, 169 máy bay chiến đấu của Mỹ đỗ tại sân bay bị phá hủy2.

                            Với thắng lợi tại Trân Châu Cảng, hải quân Nhật đã loại ra khỏi vòng chiến đấu Hạm đội Thái Bình Dương của Mỹ trong nhiều tháng, tạo điều kiện thuận lợi cho quân đội Nhật đánh chiếm nhiều nước trong khu vực Đông Nam Á và làm chủ vùng biển châu Á - Thái Bình Dương trong giai đoạn đầu của Thế chiến II
                            """)
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'hòa bình' in text2 or 'độc lập' in text2:
                        split_sentences('Một câu chuyện nổi tiếng về hòa bình mà tôi muốn kể cho bạn nghe là câu chuyện về cô bé Sadako Sasaki và những con sếu bằng giấy.')
                        split_sentences("""
                            Sadako Sasaki là một cô bé người Nhật Bản, sinh ra vào năm 1943. Khi cô mới 2 tuổi, quả bom nguyên tử đã rơi xuống Hiroshima, nơi cô đang sống. Mặc dù cô đã sống sót sau vụ tấn công khủng khiếp này, nhưng vào năm 1955, khi cô 12 tuổi, cô đã được chẩn đoán mắc bệnh bạch cầu do phóng xạ.

                            Trong thời gian điều trị tại bệnh viện, Sadako đã nghe về truyền thuyết Nhật Bản: nếu ai đó gấp được 1000 con sếu bằng giấy, ước muốn của họ sẽ trở thành hiện thực. Với hy vọng vào sự sống và hòa bình, Sadako đã bắt đầu công cuộc gấp 1000 con sếu từ những tờ giấy nhỏ.

                            Dù rất cố gắng, nhưng cuối cùng Sadako chỉ gấp được 644 con sếu trước khi qua đời vào ngày 25 tháng 10 năm 1955. Các bạn học của Sadako đã hoàn thành phần còn lại để đạt được con số 1000 và tất cả đã được chôn cùng với Sadako.

                            Câu chuyện về Sadako và những con sếu giấy đã trở thành biểu tượng cho hòa bình và hi vọng. Ngày nay, tại Công viên Hòa bình Hiroshima, bạn có thể thấy Tượng đài Trẻ em - một tượng của Sadako đang giữ một con sếu giấy - được dựng lên để tưởng nhớ đến những nạn nhân nhỏ tuổi của bom nguyên tử
                            """)
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'cuộc sống hàng ngày' in text2 or 'cuộc sống' in text2 or 'sinh hoạt' in text2 or 'đơn giản' in text2:
                        split_sentences('Một câu chuyện về cuộc sống hàng ngày nổi tiếng mà tôi muốn kể cho bạn nghe là câu chuyện về việc xây dựng cầu Brooklyn')
                        split_sentences("""
                            Câu chuyện bắt đầu vào năm 1869, khi một kỹ sư tên là John Roebling đã mơ ước xây dựng một cây cầu kỳ diệu để nối Manhattan và Brooklyn. Tuy nhiên, ông đã gặp một tai nạn thảm khốc và qua đời. Con trai của ông, Washington Roebling, đã tiếp quản dự án này.

                            Trong quá trình xây dựng, Washington cũng gặp một tai nạn và bị liệt toàn bộ cơ thể, chỉ có thể nhìn và nhấp nháy. Mọi người nghĩ rằng dự án sẽ phải dừng lại. Nhưng Washington không từ bỏ. Ông đã sử dụng đôi mắt của mình để chỉ dẫn cho vợ mình, Emily, cách tiếp tục công việc.

                            Emily đã học tất cả những gì cần thiết để hoàn thành cây cầu. Cô đã trở thành người phụ nữ đầu tiên giám sát một công trình lớn như vậy. Sau 14 năm, cây cầu Brooklyn cuối cùng đã hoàn thành vào năm 1883

                            Câu chuyện này cho thấy rằng, dù cuộc sống hàng ngày có thể đầy rẫy khó khăn và thử thách, nhưng với lòng kiên trì và niềm tin, chúng ta có thể vượt qua mọi trở ngại để đạt được mục tiêu của mình""")
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'phiêu lưu' in text2 or 'khám phá' in text2 or 'thám hiểm' in text2:
                        split_sentences('Một câu chuyện phiêu lưu nổi tiếng mà tôi muốn kể cho bạn nghe là “Những Cuộc Phiêu Lưu Của Huckleberry Finn” của tác giả Mark Twain')
                        split_sentences("""
                            Truyện kể về cuộc phiêu lưu của cậu bé Huckleberry Finn sau khi trốn thoát khỏi cuộc sống bị ràng buộc bởi xã hội. Huck đã bắt đầu một cuộc phiêu lưu mới dọc theo sông Mississippi cùng với Jim, một nô lệ đang trốn chạy. Trong suốt cuộc hành trình, Huck đã gặp phải nhiều khó khăn và thử thách, từ việc bị cuốn vào một cuộc đấu súng chết người giữa hai gia đình, đến việc phải đối mặt với những định kiến ​​xã hội

                            Tuy nhiên, chính trong những hoàn cảnh khó khăn nhất, Huck mới nhận ra giá trị của sự tự do và lòng trắc ẩn. Dù chỉ là một cậu bé phá phách, nhưng Huck đã biết phân biệt đúng sai và thoát khỏi những định kiến ​​méo mó do nuôi dạy sai lầm

                            “Những Cuộc Phiêu Lưu Của Huckleberry Finn” không chỉ là một câu chuyện phiêu lưu hấp dẫn, mà còn là một tác phẩm văn học sâu sắc, phản ánh rõ nét văn hóa và xã hội Mỹ vào thế kỷ 19
                              """)
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'khoa học viễn tưởng' in text2 or 'khoa học' in text2 or 'viễn tưởng' in text2 or 'tương lai' in text2:
                        split_sentences('Một câu chuyện khoa học viễn tưởng nổi tiếng mà tôi muốn kể cho bạn nghe là “Dune” của tác giả Frank Herbert')
                        time.sleep(0.5)
                        split_sentences("""“Dune” là câu chuyện về một hành tinh sa mạc tên Arrakis, nơi sản sinh ra một loại gia vị quý hiếm có khả năng gia tăng trí tuệ và kéo dài tuổi thọ con người. Đây cũng là nơi sinh sống của những con sán dầu khổng lồ. Cuốn sách xoay quanh cuộc đấu tranh quyền lực giữa các gia đình quý tộc để kiểm soát nguồn cung cấp gia vị này
                        Trong cuốn sách, Paul Atreides, con trai của một người cai trị hành tinh, đã trở thành một nhân vật trung tâm. Sau khi gia đình ông bị phản bội và cha ông bị giết, Paul đã trở thành một nhà lãnh đạo tinh thần và dẫn dắt người dân bản địa trong cuộc chiến chống lại sự áp bức
                        “Dune” không chỉ là một câu chuyện khoa học viễn tưởng hấp dẫn, mà còn là một tác phẩm phê phán xã hội, thể hiện sự lo lắng về môi trường và khám phá các khía cạnh tâm linh""")
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'lịch sử' in text2 or 'xưa' in text2 or 'lâu' in text2 or 'trước kia' in text2:
                        split_sentences('Một câu chuyện lịch sử nổi tiếng mà tôi muốn kể cho bạn nghe là câu chuyện về Thánh Gióng - một trong bốn vị thánh bất tử trong tín ngưỡng dân gian Việt Nam')
                        split_sentences("""Theo truyền thuyết, Thánh Gióng sinh ra tại xã Phù Đổng, huyện Gia Lâm, Hà Nội, thời vua Hùng thứ 6. Ông là người trời đầu thai làm đứa trẻ, lên ba rồi mà không biết nói cười, đi đứng. Nhưng khi giặc Ân tràn xuống thì Gióng cất tiếng gọi mẹ nhờ ra gọi sứ giả của nhà vua, rồi bỗng chốc vươn vai thành một thanh niên cường tráng đi đánh giặc                                
                                        Sau khi đánh tan kẻ xâm lược, ông bay về trời. Nơi ông hóa chính là núi Sóc thuộc huyện Sóc Sơn, Hà Nội. Đại Việt sử ký toàn thư kể chi tiết về Thánh Gióng như sau: Đời Hùng Vương thứ 6, ở làng Gióng có hai vợ chồng ông bà lão nghèo chăm chỉ làm ăn và có tiếng là phúc đức thế mà họ vẫn chưa có con""")
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
                    elif 'văn hóa' in text2 or 'tốt đẹp' in text2 or 'truyền thống' in text2:
                        split_sentences('Một câu chuyện về văn hóa nổi tiếng mà tôi muốn kể cho bạn nghe là câu chuyện về “Rāmāyaṇa” - một bộ truyện cổ điển của Ấn Độ')
                        split_sentences("""“Rāmāyaṇa” bao gồm 24.000 câu thơ đôi trong bảy tập (kāṇḍas) và kể về câu chuyện của một hoàng tử, Rama của xứ Ayodhya, vợ là Sita bị bắt đi bởi vua quỷ (Rākshasa) vua xứ Lanka, Rāvana. Truyện không chỉ là một tác phẩm văn học xuất sắc mà còn phản ánh rõ nét văn hóa và tín ngưỡng của người Ấn Độ.
                            Ngoài ra, câu chuyện “Chim Sẻ Bị Cắt Lưỡi” cũng là một câu chuyện mang ý nghĩa đạo đức kinh điển của Nhật Bản về lòng tham và lòng tốt. Câu chuyện này đã trở thành một phần quan trọng của văn hóa Nhật Bản và được truyền từ thế hệ này sang thế hệ khác.
                            Cả hai câu chuyện trên đều là những biểu tượng văn hóa quan trọng, phản ánh giá trị và tinh thần của các nền văn hóa khác nhau.""")
                        speak('The end')
                        time.sleep(1)
                        speak(f'Bạn muốn nghe {robot_name} kể chuyện tiếp không')
                        textx = get_text()
                        if 'có' in textx or 'yes' in textx or 'kể' in textx:
                            kechuyen()
                        elif 'không' in textx or 'no' in textx or 'thôi' in textx:
                            stopstr()
            
            def stopstr():
                speak(f'Bạn muốn nghe {robot_name} kể câu chuyện nào nữa không?')
                time.slep(3)
                text5 = get_text()
                if 'có' in text5 or 'yes' in text5 or 'chuyện' in text5:
                    kechuyen()
                elif 'không' in text5 or 'no' in text5 or 'thôi' in text5:
                    speak(f"Thank you bạn đã nghe câu chuyện này của {robot_name}")           
        kechuyen()
                                       
    else:
        speak(f'Bạn cần {robot_name} giúp gì nữa không?')
        text4 = get_text()
        if 'có' in text4 or 'yes' in text4:
            helpm()
        elif 'không' in text4 or 'no' in text4 or 'thôi' in text4:
            stop()

def recognize_speech():
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


def hello(name):
    day_time = int(strftime('%H'))
    if 0 <= day_time < 11:
        speak(f"Chào bạn {name}. Chúc bạn buổi sáng tốt lành.")
    elif 11 <= day_time < 13:
        speak(f"Chào bạn {name}. Chúc bạn có một buổi trưa thật vui vẻ.")
    elif 13 <= day_time < 18:
        speak(f"Chào bạn {name}. Chúc bạn buổi chiều vui vẻ.")
    elif 18 <= day_time < 22:
        speak(f"Chào bạn {name}. Tối rồi, Bạn đã cơm nước gì chưa ?")
    elif 22 <= day_time <= 23:
        speak(f"Chào Bạn {name}. Muộn rồi bạn nên đi nghủ sớm nha.")
    else:
        speak(f"Thời gian bên tôi chưa đúng hoặc gặp lỗi. Bạn nên xem lại nha.")


def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
    elif "ngày" in text:
        speak(f"hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        speak("Lý Hành chưa hiểu ý bạn.")


def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    # lưu tên thành phố vào biến city
    city = get_text()
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "b4750c6250a078a943b3bf920bb138a0"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    response = requests.get(call_url)
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
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
    else:
        # nếu tên thành phố không đúng thì nó nói dòng dưới 227
        speak("Không tìm thấy địa chỉ của bạn")


def tell_me_about():
    try:
        speak("Hãy nói cho tôi nghe Bạn muốn tìm gì ạ ?")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        dem = 0
        for content in contents[1:]:
            if dem < 2:
                speak("Bạn có muốn biết thêm không ???")
                ans = get_text()
                if 'có' not in ans:
                    break
            dem += 1
            speak(content)
        speak("Đây là nội dung tôi vừa tìm được cảm ơn bạn đã lắng nghe")
    except:
        speak(f"{name} không định nghĩa được thuật ngữ của bạn !!!")


def baothuc():
    invalid = True
    while (invalid):
        # Get a valid user input for the alarm time
        speak("bạn muốn đặt báo thức vào lúc mấy giờ")
        text = get_text()
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
    pygame.mixer.music.load(r'Am_Thanh\Báo Thức iPhone.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # stop = get_text()
        # if "tắt báo thức" in stop:
        pygame.time.Clock().tick(1)


def demnguoc():
    speak("bạn muốn đếm ngược bao nhiêu thời gian")
    text = get_text()
    alarmTime = re.findall(r'\d+', text)
    if int(alarmTime[0]) > 0:
        secondsUntilAlarm = int(alarmTime[0])*60
    print("Alarm is set!")
    print("The alarm will ring at %s" %
          datetime.timedelta(seconds=secondsUntilAlarm))

    for i in range(0, secondsUntilAlarm):
        time.sleep(1)
        secondsUntilAlarm -= 1
        print(datetime.timedelta(seconds=secondsUntilAlarm))

    # speak("Ring Ring... time to wake up!")
    # playsound.playsound(r'D:\CHATBOX\MUSICAL\baothuc.mp3')
    # sound = pygame.mixer.Sound('baothuc.mp3')
    # sound.play()
    pygame.mixer.init()
    pygame.mixer.music.load(r'Am_Thanh\Báo Thức iPhone.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def helpm():
    speak(f"""{robot_name} có một số công việc sau:
          1. kể chuyện
          2. đếm ngược thời gian
          3. đặt báo thức
          4. tìm kiếm thông tin
          5. dự báo thời tiết
          6. thông báo thời gian hiện tại
          7. định nghĩa
          và một số thông tin khác
          """)

robot_name = "Genius"

# Thực thi các chức năng
def AI():
    global robot_name
    speak("Xin chào. Bạn tên là gì ?")
    global name
    name = get_text()
    # find_username()
    
    if name:
        speak(f'Xin chào bạn {os.getlogin()}.')
        speak(f'Bạn cần trợ lý ảo giúp gì không ạ ?')
        while True:
            text = get_text()
            if ('tạm biệt' in text) or ('hẹn gặp lại' in text):
                stop()
                break
            elif "chào trợ lý" in text:
                hello(os.getlogin())
            elif "hiện tại" in text:
                get_time(text)
            elif "thời tiết" in text:
                current_weather()
            elif "định nghĩa" in text:
                tell_me_about()
            elif "đặt báo thức" in text:
                baothuc()
            elif "đếm ngược" in text:
                demnguoc()
            elif 'kể' in text or 'kể chuyện' in text or 'chuyện' in text or 'buồn' in text or 'chán' in text or 'nói' in text:
                story()
            elif "kết thúc" in text:
                n = 0
                break


# Biến để lưu trữ text hiện tại trong frame
default = 'Chào bạn, tôi là trợ lý Genius!!! Tôi có thể giúp gì?'
def greet():
    speak(default)
# Gọi hàm greet khi phần mềm được mở
app.after(1000, greet)
# Text
def ft():
    # Cập nhật text
    # def update_defa():
    #     default=get_audio()
    #     default=get_text()

    # GUI chức năng
    frame = Frame(app, highlightbackground='#2b8091' , highlightthickness=1.5 , width=500, height = 300, bd=2, bg='#c6f4be')
    frame.place(relx=0.5, rely=0.5, relwidth=0.7 ,relheight=0.5 , anchor=CENTER)

    def ft1():
        fr = Frame(frame, highlightbackground='black' , highlightthickness=0 , width=500, height = 300, bd=0, bg='#c6f4be')
        fr.place(relx=0.48, rely=0.5, relwidth=0.9 , relheight=0.9 , anchor=CENTER)

        # **Đặt hàm ft2() bên trong hàm ft1()**
        def ft2():
            fr1 = Label(fr, highlightbackground='black' , highlightthickness=0 , width=500, height = 300, bd=0, anchor='w', justify='left', bg='#c6f4be')
            fr1.place(relwidth=1 , relheight=0.5)

            # Thêm thuộc tính wraplength để text tự động chuyển sang dòng tiếp theo khi đạt đến chiều rộng của frame
            fr2 = Label(fr1, highlightbackground='black' , highlightthickness=0 ,bd=0, text=default, font='Inter 16', bg='#c6f4be', wraplength=400)
            fr2.pack(side=TOP, anchor=NW)
        ft2()

        # **Đặt hàm ft3() bên trong hàm ft1()**
        def ft3():
            fr3 = Label(fr, highlightbackground='black' , highlightthickness=0 , width=500, height = 300, bd=0, anchor='w', justify='left', bg='#c6f4be')
            fr3.place(rely= 0.5, relwidth=1 , relheight=0.5)

            # Thêm thuộc tính wraplength để text tự động chuyển sang dòng tiếp theo khi đạt đến chiều rộng của frame
            fr4 = Label(fr3, highlightbackground='black' , highlightthickness=0, bd=0, text=default, font='Inter 16', bg='#c6f4be', wraplength=400)
            fr4.pack(side='bottom' , anchor= 'nw')

        ft3()

    ft1()

    # def update():
    #     global default
    #     default = default + "a"

    #     # Kiểm tra xem text đã đầy frame hay chưa
    #     if fr2.winfo_width() >= 400:
    #         # Nếu đã đầy, xóa text đó đi
    #         fr2.destroy()

    #         # Thay bằng text tiếp theo
    #         fr2 = Label(ft1(), highlightbackground='black' , highlightthickness=0 ,bd=0, text=default, font='Inter 16', bg='#c6f4be', wraplength=400)
    #         fr2.pack(side=TOP, anchor=NW)

    #     # Gọi hàm update sau 1 giây
    #     app.after(1000, update)
    # update()

# Micro
def micro():
    ina = Image.open('Vector.png').resize((39, 50))
    act = Image.open('Ellipse 1.png').resize((80, 80))

    # Tạo một hình ảnh mới kết hợp cả hai hình ảnh
    combined = Image.new('RGBA', act.size)
    combined.paste(act, (0,0), act)
    combined.paste(ina, ((act.width-ina.width)//2, (act.height-ina.height)//2), ina)

    app.ina = ImageTk.PhotoImage(ina)
    app.act = ImageTk.PhotoImage(combined)

    def enter(event):
        button.config(image=app.act)

    def leave(event):
        button.config(image=app.act)

    button = Button(app, image=app.act, bg='#cafafe', width=79.5, height=79.5, bd=0, relief='sunken', activebackground='#cafafe',  command=lambda: AI())
    button.place(relx=0.5, rely=0.85, anchor=CENTER)

    button.bind('<Enter>', enter)
    button.bind('<Leave>', leave)
    
micro()


# Chủ đề
def sb():
    lb = Label(app, text = 'TRỢ LÝ ẢO GENIUS', font = 'arial 30 bold', fg = 'black', bg='#cafafe')
    lb.place(relx=0.5, rely=0.15, anchor=CENTER)
    
sb()
ft()




app.mainloop()