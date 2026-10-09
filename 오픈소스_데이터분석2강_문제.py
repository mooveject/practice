# 2강 교재 문제 
# 1) 짝수 인덱스 요소만 추출
numbers = [10,20,30,40,50,60,70,80,90]
a= numbers [::2]
print (a)

# 2) f-문자열 사용,  이름 : 홍길동, 나이 : 25세, 월급 : 350만원 출력 코드 작성
name = "홍길동"
age= 25
salary = 350
print (f"이름 : {name}, 나이 : {age}세, 월급 : {salary}만원")

"""# 3)try - execpt - finally 구문 사용 > data.txt 파일 읽고 닫는 코드 작성.
# 모르겠음
try :
    file = open ('data.txt','r') 
except :
    FileNotFoundError 
    print ("파일을 찾을 수 없습니다.")
finally : 
    file.close()"""
# 4) 람다 함수, sorted () 함수로 점수 기준 내림차순 리스트 작성 
# 헷갈림
students = [
    ("kim", 85),
    ("lee", 92),
    ("park",78),
    ("choe", 95)
]
good_score = sorted (students, key = lambda student : student [-1])
for name, score in good_score :
    print (f"{name}:{score}점")

# 5) reduce () 함수로 리스트 numbers 의 모든 요소를 곱한 결과 구하기
from functools import reduce 
numbers = [1,2,3,4,5]
new = reduce (lambda x,y : x * y, numbers )
print (new)