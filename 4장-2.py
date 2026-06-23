#4.4 문자열 포매팅 : 형변환 없이 문자열과 다른 자료형 연결하기 
print ("ab"+"ab")
print ("ab","ab")
# 1. 서식 지정자 %d (정수), %s (str 문자열), %c (character 문자), %f (float실수)
print ("나는 %d살입니다." % 20 ) # %d 정수
print ("나는 %s을 좋아합니다" % "파이썬") # %s 문자열, 정숫값 표현 가능
print ("Apple은 %c로 시작해요" % "A") # %c 문자
print ("나는 %s살 입니다" % 20)
print ("물컵에 물이 %f 만큼 있습니다." % 0.4) # %f 실수
print ("나는 %s색과 %s색을 좋아해요." % ("파란", "분홍") )# 값이 여럿일 때

# 2.format () 함수 pritnt ("나는 {} 이고 {}입니다" .format("사람", "회사원") )
print ("나는 {}살 입니다.".format (20))
print ("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print ("나는 {0}색과 {1}색을 좋아해요" .format ("파란", "빨간"))
print ("나는 {1}색과 {0}색을 좋아해요." .format ("파란", "빨간")) #인덱스 순서 0,1에 맞춰 {1} 자리에 빨간 , {0}에 파란이 들어감
print ("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간")) #format에 이름을 지정 시, 괄호 속 순서와 관계없이 변수명 안에 해당 값이 들어감
print ("나는 {age}살이며, {color}색을 좋아해요." .format (color="빨간", age=20))

# input 응용해보기 (자율)
# color = input ("좋아하는 색 : ")
# age = int(input("나이 :"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color=color, age=age))

# f-문자열 (f-string) print (f"문자열{변수명1} 문자열{변수명2}...") 이전에 정의한 변수를 변수명 자리에 넣는 것.
age = 20
color = "빨간"
print (f"나는 {age}살이며, {color}색을 좋아해요.")

#4.5 탈출 문자 escape character : 문장 안에서 원하는 동작 수행하기

# 1) \n : 문장 줄바꿈
print ("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

# 2) \ 와 \ : 문자열 안에서 따옴표 사용하기 > 따옴표 앞에 \" \'
# Q. 저는 "나도코딩" 입니다. 쓰기
print ("저는 '나도코딩' 입니다.")
print ('저는 "나도코딩" 입니다.')
print ("저는 \"나도코딩\" 입니다")
print ("저는 \'나도코딩\' 입니다.")

# 3) \\ (역슬레시)
# print ("c:\users\nadocoding\desktop\pythonworkspace") -> 실제 없는 탈출 문자를 폼함하면 오류가 남. 
print ("c:\\users\\Nadocoding\\Desktop\\pythonWorkspace")
print (r"c:\users\nadocoding\desktop\pythonworkspace") #문자열 앞에 r 추가하기 (문자열내 뭔 일이 일어나든 그냥 출력)

# 4) \r : 커서를 맨앞으로 이동시킴
print ("Red Apple\rPine") # Red (4글자)를 Pine(4글자가)으로 덮어 쓰는 효과
print ("PineApple\rRed") # Red (3글자)로 Pine(4글자)을 다 지우지 못해서 e까지 덮어씌우지 못함.

# 5) \b : 키보드 Backspace와 비슷. 비파괴 백스페이스. 
# 원리 : \b 만큼 커서 이동 후 덮어씌우는 것
print ("Redd\bApple")
print ("Banana\b\b\b\b\b\bApple") #뒤에서부터 커서를 6칸 이동 B부터 Apple로 덮어씌우기 -> Applea가 됨

# 6) \t : 키보드의 tab 역할. 여러 칸 띄어쓰기
print ("Red\tApple") #터미널 기준 8칸 띄어쓰기, 전체 문자열의 첫번째 글자로부터 8칸. > R부터 8칸 떨어진 곳에 Apple 출력
print ("I\tlove you") #I부터 8칸 뒤 loveyou. I 1칸 + 공백 7칸 > 8칸 뒤 love you

# 4.6 실습 문제 : 사이트별로 비밀번호 생성하는 프로그램 작성하기

site = "http://naver.com"
site = (site[7:])
site = (site[:-4])

# 안 잡혀 있는 개념 체크 with claude
# str은 인자 하나만 받음. 여러 값을 묶으려면 f-string
password = site[:3] + str(len(site)) + str(site.count("e")) + "!"  # ✅

# % 방식
print("%s의 비밀번호는 %s 입니다." % (site, password))

# f-string 방식 (추천)
print(f"{site}의 비밀번호는 {password} 입니다.")

site = "http://naver.com"
site = site[7:]    # "naver.com"
site = site[:-4]   # "naver"
password = site[:3] + str(len(site)) + str(site.count("e")) + "!"
print(f"{site}의 비밀번호는 {password} 입니다.")

#답지 
url = "http://daum.net"
my_str = url.replace ("http://","") # http:// 를 없애버림. > daum.net
my_str = my_str[:my_str.index(".")] # . 위치 찾아서 앞만 자름 > daum
password = my_str[:3] + str (len(my_str)) +str(my_str.count("e"))+"!"
print ("{0}의 비밀번호는 {1}입니다.".format(url, password))
#셀프 체크 : 영어 문장에서 첫 글자는 대문자, 나머지는 소문자 변환 프로그램 작성
sentence1 ="The Early Bird Catches the worm."
sentence2 ="actions speak louder than words."
sentence3= "practice makes perfect."

print(sentence1[0].upper()+ sentence1[1:].lower())
print(sentence2[0].upper()+ sentence2[1:].lower())     
print(sentence3[0].upper()+ sentence3[1:].lower())

#반복문 사용하기 (자율학습)
sentences=[
    "the early bird catches the worm",
    "actions speak louder than words.",
    "practice makes perfect."
]
for sentence in sentences :
    print(sentence[0].upper()+sentence[1:].lower())

for s in range(3):
    print(sentences[s][0].upper() + sentences[s][1:].lower())


