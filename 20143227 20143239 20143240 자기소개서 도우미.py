from tkinter import * 

def Save():     #입력한 텍스트를 저장하기 위해 Save함수를 정의
        global read_data  
        global editor
        fileD = open("c:\\python34\\test.txt","w", encoding="utf-8")    #txt 파일 열고 1열 0행부터 끝까지 읽고 저장한다.
        fileD.write("%s" % editor.get("1.0",END))       #editor의 쓰여진 데이터를 갖는다.
        editor.delete("1.0",END)         #그 다음 1열 0행부터 끝까지 텍스트를 지운다. 저장한 내용은 txt파일에 저장된다.
        fileD.close()  

        
def Load():         #저장된 텍스트를 불러오기 위해 load함수를 정의
        global read_data
        global editor
        f = open("c:\\python34\\test.txt", "r", encoding = "utf-8")
        read_data.set(f.read())
        editor.insert(INSERT, read_data.get())     #editor창에 read_data를 출력한다.
        f.close()       #파일을 불러오고 editor창에 텍스트를 출력한다.
        
def hyperlink1():
        import webbrowser
        webbrowser.open("http://speller.cs.pusan.ac.kr/")       
def hyperlink2():
        import webbrowser
        webbrowser.open("http://s.lab.naver.com/autospacing/")
def hyperlink3():
        import webbrowser
        webbrowser.open("http://loanword.cs.pusan.ac.kr/")   #hyperlink를 위해 도메인주소를 여는 함수를 정의한다.

def count ():
        from string import punctuation   #문자 함수 지정한다.
        from operator import itemgetter        #문자 빈도수를 위해 함수를 지정한다.
        global rank       #중복된 단어를 순위대로 찾기 위해 rank함수를 정의한다.
        
        file = open("c:\\python34\\test.txt","r", encoding="utf-8")  #카운트할 텍스트파일을 읽기 전용으로 읽어오고 utf - 8로 인코딩한다.         
        n_letters = 0
        n_words = 0
        n_lines = 0     #글자 수, 단어, 라인을 계산을 위해 0으로 맞춘다.

        for line in file:       #객체 file에서  변수 line지정
            words = line.split()        #split으로 쪼갠다.
            n_lines += 1        #라인을 세는 변수를 지정한다.
            n_words += len(words) #len을 이용해 단어를  세도록한다.
            n_letters += len(line)-1    #len을이용해 단어를 세도록한다.

        rank.insert(END, "텍스트 검사 결과")   
        rank.insert(END, "총문자 수:" + str(n_letters))
        rank.insert(END, "단어의 수:" + str(n_words))
        rank.insert(END, "라인의 수:" + str(n_lines),"\n")
        rank.insert(END, "중복률 검사")      #우측의 리스트박스에 결과를 출력한다.

        overlap = 15  #중복되는 결과를 15개 보이게 한다.
        words = {} 
        words_gen = (word.strip(punctuation).lower()    #words변수의 punctuation의 양쪽 공백을 제거한다.
        for line in open("c:\\python34\\test.txt", encoding="utf-8")    #txt파일을 연다.
        
        for word in line.split())  #객체 line.split와 변수 word지정

        for word in words_gen:
            words[word] = words.get(word, 0) + 1 #단어의 데이터를 갖는다 그리고 중복시 횟수를 센다.

        top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:overlap]#변수top_words에 단어를 배열하고 가장 많이 나온 단어를 정한다.

        for word, frequency in top_words:
                rank.insert(END, "%s %d" % (word, frequency)) #반복단어를 회수와 함께  출력한다.

        file.close()    #파일을 닫는다.
            
app = Tk()
app.title("My name is")
app.geometry('1000x600')  #살행된 창의 크기를 조절한다.

scrollbar=Scrollbar(app) #scrollbar로 스크롤기능을 지정
scrollbar.pack(side='right',fill=Y)#오른쪽에 스크롤기능 
rank=Listbox(app,yscrollcommand=scrollbar.set)#
rank.pack(side='right',fill=BOTH)
scrollbar.config(command=rank.yview)

b1 = Button(app,text = "불러오기",width = 10,command=Load)  
b1.pack(side = 'bottom', padx = 10, pady = 10)  
b2 = Button(app,text = "저장",width = 10,command=Save)
b2.pack(side = 'bottom', padx = 10, pady = 10)
b3 = Button(app,text = "맞춤법 검사",width = 10,command = hyperlink1)
b3.pack(anchor = 'ne', padx = 10, pady = 10)
b4 = Button(app,text = "띄어쓰기 검사",width = 10,command = hyperlink2)
b4.pack(anchor = 'ne', padx = 10, pady = 10)
b5 = Button(app,text = "외래어 검사",width = 10,command = hyperlink3)
b5.pack(anchor = 'ne', padx = 10, pady = 10)
b6 = Button(app,text = "텍스트 검사",width = 10,command = count)     #text = 버튼에 출력될 텍스트를 입력하다. width =  넓이를 조절한다.  command = 버튼을 누르면 일어날 이벤트를 연결한다.
b6.pack(side = 'right', padx = 10 , pady = 10)  #버튼의 위치와 텍스트와 칸의 간격을 조절한다.

read_data = StringVar()
read_data2 = StringVar() #read_data에 값을 저장한다.
L1 = Label(app, text="자기소개서 작성 프로그램")  #라벨에 텍스트를 출력한다.
L1.pack(side = TOP) #라벨에 출력된 텍스트의 위치를 지정한다.
L2 = Label(app, text="◎크기가 안맞으시면 상단바를 더블클릭 하셔서 크기를 맞춰주세요.")
L2.pack(side = TOP)

editor = Text(app, bd =3) #글자를 입력 할 수 있는 메모장 생성
editor.pack(side = LEFT) #메모장을 왼쪽에 지정

app.mainloop()
