""" # 7강 셀프체크
def get_air_quality ():
    if 0<=q<=30 :
        print ("좋음")
    elif 31<=q<=80:
         print ("보통")
    elif 81<=q<=150:
        print ("나쁨")
    elif 151<=q :
        print ("매우나쁨")
    return 
"""

def get_air_quality(q):
    if 0 <= q <= 30:
        print("좋음")
    elif 31 <= q <= 80:
        print("보통")
    elif 81 <= q <= 150:
        print("나쁨")
    elif 151 <= q:
        print("매우나쁨")

get_air_quality(15)
get_air_quality(85)

# 답지
def get_air_quality (fine_dust) :
    if  0<=fine_dust<=30:
        return "좋음"
    elif fine_dust<=80 :
        return "보통"
    elif fine_dust <=150:
        return "나쁨"
    else :
        return "매우 나쁨"
    
print (get_air_quality(15))
print (get_air_quality(85))

# 8장 : 입출력 1~7
# 8.1 표준 입력받기 : input ()
"""
answer=input("아무 값이나 입력하세요 : ")
print ("입력한 값은 " + answer + "입니다.") 
# , 콤마는 형이 달라도 가능,  + 연산자는 형변환을 해줘야 함. > 해당 코드에서 오류 X 
# Why? : input 함수는 무조건  입력값을 문자열 (str)로 인식함
print (f"입력한 값은 {answer}입니다.") # f-string 복습
print (type(answer))
answer=10
print (type(int(answer)))

dream = input("당신의 꿈은 무엇인가요?")
print (f"제 꿈은 {dream} 입니다.")
"""
# 8.2 표준 출력 (print)유용한 기능
# 구분자 넣기 : sep=
print ("파이썬","자바")
print ("파이썬"+ "자바")
print ("파이썬","자바",sep=",")

print ("파이썬","자바","자바스크립트")
print ("파이썬","자바","자바스크립트",sep=" vs ")

# 문장 끝 지정하기 : end (기본값 \n 줄바꿈)
print ("파이썬","자바", sep=", ", end="? ") 
print ("무엇이 더 재밌을까요?") #줄바꿈 없이 이어서 출력

# 출력 위치 지정하기 : file
import sys
print ("파이썬", "자바", file=sys.stdout) # 일반적인 내용을 남김
print ("파이썬","자바", file=sys.stderr) # 오류 발생 시 관련 내용 출력

# 공간 확보해 정렬하기 : ljust()와 rjust() = left , right () 숫자 값만큼 왼, 오 정렬. 이때 정렬하는 값은 문자열이어야 함.
scores={"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print (subject.ljust(8), str(score).rjust(4), sep=":") # score 정수를 str()로 문자열로 형전환
    # 영어________:____50

# 빈칸 0으로 채우기 : zfill() = zero 로 fill 채우기
for num in range (1,21):
    print ("대기번호 : "+str(num))

for num in range (1,21):
    print ("대기번호 : "+ str(num).zfill(3)) # 전달하는 숫자만큼 예 :3칸 공간 확보. 앞 빈칸을 0으로 fill

# 8.3 다양한 형식으로 출력하기 : format (), {0: }  | 채울 것, 정렬 방향, 기호, n칸인지
# {인덱스:[[빈칸채우기]정렬][기호][공간확보][쉼표][.자릿수][자료형]}
print ("{0}".format (500))
print ("{0:>10}".format(500)) # 오른쪽으로 10칸 밀고 정렬
print ("{0:>+10}".format (500)) # 양수 표시 +500
print ("{0:>+10}".format (-500)) #음수일 때
print ("{0:_<10}".format(500)) # 빈칸을 _로 채우기, 왼쪽 < 정렬, 공간 10칸

print ("{0:,}".format(100000000000)) # 3자리마다 쉼표
print ("{0:+,}".format(100000000000)) # + 기호 붙이기, 3자리마다 쉼표
print ("{0:+,}".format(-100000000000)) # - 기호 붙이기, 3자리마다 쉼표

print ("{0:^<+30,}".format(100000000000)) # 30칸 확보, 왼쪽 정렬 , + 기호 포함, 빈칸은 ^ = 채울 것, 정렬 방향, 기호, n칸인지

print ("{0}".format(5/3))
print ("{0:f}".format(5/3)) # f를 추가해 소수점 이하 6자리 출력 # 1.666667
print ("{0:.2f}".format(5/3)) # .n f를 통해 원하는 자리까지만 출력

# 8.4 파일 입출력
# 1. 파일 열고 닫기 : open(), close ()
# open ("파일명","모드",encoding="인코딩 형식")
# r (read) 파일 읽기 | w (write) 쓰기 모드 * 같은 이름 파일 덮어씀 | a (append) 쓰기 모드 * 같은 이름 파일이면 기존 내용에 이어씀

# score.txt 파일을 쓰기 모드로 열기 
score_file = open ("score.txt","w",encoding="utf8")
print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
print ("영어 : 50", file =score_file) #score.txt 파일에 내용 쓰기
score_file.close() # score.txt 파일 닫기

# 2. 파일 쓰기 (write)
score_file=open("score.txt","a",encoding="utf8")
# write()함수는 줄 바꿈이 없으므로 \n 추가
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100\n")
score_file.close()

# 3. 파일 읽기 read(), readline(), readlines()
# score.txt 파일 읽기 모드로 열기 
score_file=open ("score.txt","r", encoding="utf8") 
print (score_file.read()) # 파일 전체 읽어오기
score_file.close()

score_file=open ("score.txt","r", encoding="utf8") 
print(score_file.readline(), end="") # 한 줄씩 읽어오기 + 줄바꿈 \n
print(score_file.readline(), end="") # end 값 설정, 줄 바꿈 후 중복 수행 방지
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file=open ("score.txt","r", encoding="utf8") 
while True:
    line = score_file.readline()
    if not line: # 읽어 올 내용이 없을 때
        break # 반복문 탈출
score_file.close()

score_file=open ("score.txt","r", encoding="utf8") 
lines=score_file.readlines() # 파일에서 모든 줄을 읽어와 리스트 형태로 저장
for line in lines: #lines 내용이 있을 때까지
    print (line, end="") #읽어 온 내용 출력
score_file.close()

