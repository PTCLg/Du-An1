import re
import nltk
import os
# import pyttsx3
import time
from time import strftime
import playsound
import speech_recognition as sr
from gtts import gTTS

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

def stop():
    speak("Hẹn gặp lại sau nha ! ... ")
    text = get_text()
    if 'ok' in text or ' ' in text or 'dừng' in text or 'stop' in text:
        exit()

    
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

# def optimize_reading(long_paragraph, max_length=100):
#     words = long_paragraph.split()
#   split_sentencess = []
#     current_paragraph = []
#     current_length = 0

#     for word in words:
#         if current_length + len(word) <= max_length:
#             current_paragraph.append(word)
#             current_length += len(word) + 1
#         else:
#           split_sentencess.append(' '.join(current_paragraph))
#             current_paragraph = [word]
#             current_length = len(word)

#   split_sentencess.append(' '.join(current_paragraph))
    
#     for paragraph in paragraphs:
#         speak(paragraph)

# def read_long_paragraph(paragraph):
#   # Tạo bộ nhớ đệm.
#   sentences_cache = {}

#   # Kiểm tra xem đoạn văn đã có trong bộ nhớ đệm hay chưa.
#   if paragraph in sentences_cache:
#     return sentences_cache[paragraph]

#   # Nếu không có, thực hiện cắt đoạn văn và trả về kết quả.
#   sentences = paragraph.split(".|,")
#   sentences = [sentence for sentence in sentences if sentence]
#   sentences_cache[paragraph] = sentences
#   return sentences


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
            
# Xác định quê quán người dùng
# def Hometown():
#     text = get_text()
#     while True:
#         if ' ' in text:
#             speak(f"Bạn đến từ {text} à. Thật tuyệt vời!")


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

# def greet_by_name(text):
#     # Sử dụng thư viện re để tìm kiếm tên trong văn bản
#     name = re.search(r'\b[A-Z][a-z]*\b', text)
    
#     # Kiểm tra xem có tên trong văn bản hay không
#     if name:
#         # Nếu có, chào mừng người dùng bằng tên
#         speak(f'Xin chào bạn {name.group(0)}.')
#     else:
#         # Nếu không, chào mừng người dùng một cách chung chung
#         speak('Xin chào bạn.')

# def get_audio3():
#     ear_robot = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = ear_robot.record(source , duration= 4)
#         try:
#             print((f"{robot_name} :  ...  "))
#             text = ear_robot.recognize_google(audio, language="vi-VN")
#             print("Tôi:  ", text)
#             return text
#         except Exception as ex:
#             print(f"{robot_name}:  Lỗi Rồi ! ... !")
#             return 0

# def find_username():
#   # Giả sử get_audio() là hàm trả về văn bản từ âm thanh
#   text = get_audio3()

#   # Phân tích văn bản thành các từ
#   words = nltk.word_tokenize(text)

#   # Tạo danh sách các danh từ
#   nouns = [word for (word, pos) in nltk.pos_tag(words) if pos[:2] == 'NN']

#   # Sử dụng regex để xác định xem danh từ đó có phải là tên người dùng hay không
#   name_regex = re.compile("^[a-zA-Z0-9]+$")

#   for noun in nouns:
#     if name_regex.match(noun):
#         return noun

#   return None


robot_name = "Genius"

def AI():
    global robot_name
    speak("Xin chào. Bạn tên là gì ?")
    global name
    name = get_text()
    # find_username()
    
    if name:
        speak(f'Xin chào bạn {name}.')
        speak(f'Bạn cần {robot_name} giúp gì không ?')
        time.sleep(1)
        tt = get_text()
        if 'có' in tt or 'yes' in tt:
            def chat_human():         
                speak(f'Bạn muốn {robot_name} làm gì nào ?')
                text = get_text()
                while True:
                    # text = get_text() 
                    if not text:
                        stop()
                    elif "dừng" in text or "tạm biệt" in text:
                        stop()
                    elif 'chưa rõ' in text or 'help' in text or 'gợi ý' in text or 'giúp đỡ' in text or 'hướng dẫn' in text or 'show' in text or 'không' in text:
                        helpm()
                        chat_human()
                    elif 'kể' in text or 'kể chuyện' in text or 'chuyện' in text or 'buồn' in text or 'chán' in text or 'nói' in text or 'truyện' in text:
                        story()
                    elif 'thời gian' in text or 'bây giờ' in text or 'mấy giờ' in text or 'time' in text:
                        ttime()
            chat_human()
        else:
            stop()
AI()
            # elif 'nhà' in text or 'hometown' in text or 'nơi' in text or 'sống' in text or 'chỗ' in text or 'ở' in text or 'quê' in text:
            #     Hometown()
            # elif ''
    #     Hometown = get_text()
    #     if ' ' in Hometown:
    #         speak(f"Bạn đến từ {Hometown} à. Thật tuyệt vời!")


    # # Xác định quê quán người dùng
    #     Hometown = get_text()
    #     if ' ' in Hometown:
    #         speak(f"Bạn đến từ {Hometown} à. Thật tuyệt vời!")


    # # Xác định tuổi người dùng
    #     age = get_text()
    #     if age.isdigit():
    #         age = int(age)
    #         speak(f"Bạn năm nay {age} tuổi rồi à. Tuổi trẻ đáng giá ngàn vàng!")

    # # Xác định nghề nghiệp người dùng
    #     job = get_text()
    #     if job:
    #         speak(f"Bạn đang làm {job} à. Thật tuyệt vời! Chúc bạn thành công trong công việc và cuộc sống.")

    # # Xác định sở thích người dùng
    #     hobby = get_text()
    #     if hobby:
    #         speak(f"Bạn thích {hobby} à. Thật thú vị! Chúc bạn có nhiều niềm vui với sở thích của mình.")

    # # Kết thúc phần chào hỏi
    #         speak(f"Vậy bạn cần LÝ HÀNH giúp gì không ạ ?")                      