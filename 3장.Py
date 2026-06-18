#3장 : 연산자
#산술연산자
print (3+1)
print (3-2)
print (6/2)
print (6*2)
print (6**2)
print (6//2)
print (6%4)
#비교연산자
print (6>=4)
print (6<=8)
#논리연산자
print ((3>0)and (3>4))
print ((3>0)or (3>4))
print (not (1!=3))

# 연산자 우선 순위 
# [], {}, (), **, * / //(정수나눗셈)) %(나머지), + - 
# 부정-비교 연산자, 논리 연산자 (and,or), 대입연산자 (=)

# 변수로 계산하기
number= 2+3*4
print (number)
#number 값에 +2를 하고 싶다면? -> 복합 대입 연산자 += 꼴 (연산자로 계산 후 그 값을 변수에 적용한다)
number//=2
print (number)
number/=2
print(number)

# 3-4 함수로 연산하기
# 숫자 처리 함수
print (abs(-5)) #절대값
print (pow(4,2)) # (x,y) x를 y만큼 제곱
print (max(5,12))  #둘 중 큰 값
print (min (5,12)) #둘 중 작은 값
print (round (3.14)) #첫째자리에서 반올림
print (round (4.678,2))  #4.678을 소수점 2번쨰 자리에서 반올림

# math 모듈 
from math import * #math 모듈의 모든 기능을 가져다 쓰겠다는 의미 (*)
result = floor (4.99) # 내림
print(result)
result=ceil (3.14) #올림
print (result)
result = sqrt (16) #제곱근 = 루트
print(result) 

# import 모듈의 기능을 가져다 쓸 때 쓰는 구문 (math.꼴로 쓰기)
import math
result=math.floor (4.99)
print(result)
result=math. ceil (3.14)
print (result)
result=math. sqrt (16)
print (result)

#random 모듈 0이상 1 미만 사이 수 출력
from random import * 
print(random()) #0이상 1미만 난수 생성
print(random())
print(random()*10) #0.0~10.0미만 난수생성
print(int(random()*10)) #0~10 미만 정수에서 난수 생성 후 정수로 변환
print(int(random()*10)+1) #1~11 미만 정수에서 난수 생성 후 정수 변환 후 1 더하기
print (int(random()*45)+1) #로또 번호 뽑기 #1 이상 46 미만 정수에서 난수 생성 
print (randrange(1,46)) #주어진 범위 내에서 정수인 난수 생성  (끝숫자 미포함)
print (randint(1,46)) #주어진 범위 내에서 정수인 난수 생성 (끝숫자 포함)

#실습 문제
from random import *
day = str(int(randint(4,28)))
print ("오프라인 스터디 모임 날짜는 매월" +day+"일로 선정됐습니다.")

#정답
date = randint (4,28)
print ("오프라인 스터디 모임 날짜는 매월 " +str(date)+"일로 선정됐습니다.")

#셀프 체크 : 온도 단위 변환 프로그램 생성
#섭씨 온도가 10도일 때
tem=10
hwa=(tem*9/5)+32
print ("섭씨 온도 :", tem)
print ("화씨 온도 :", hwa)

#섭씨 온도가 30도일 때
tem=30
hwa=(tem*9/5)+32
print ("섭씨 온도 :", tem)
print ("화씨 온도 :", hwa)

#정답
celsious = 30
fahrenheit =(celsious *9/5)+32
print ("섭씨 온도 :" + str(celsious))
print ("화씨 온도 : " + str(fahrenheit))

#클로드
def celsius_to_fahrenheit(tem):
    return (tem * 9 / 5) + 32

for tem in [10, 30]:
    print(f"섭씨 온도 : {tem}")
    print(f"화씨 온도 : {celsius_to_fahrenheit(tem)}")
    