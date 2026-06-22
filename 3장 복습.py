# 3장 연산자 - 복습 문제

"""
# Q1. 아래 코드의 출력값은?
print(7 % 3) = 1
print(7 // 3) = 1
print(2 ** 10) = 2의 10 거듭제곱


# Q2. 아래 중 True가 출력되는 것은? 실행 전에 예측해봐.
print(5 >= 10) F
print((3 > 1) and (5 > 2)) T
print((3 > 5) or (2 > 10)) F
print(not (5 == 5)) F


# Q3. 연산자 우선순위대로 계산하면 결과는? 손으로 먼저 계산해봐.
print(2 + 3 * 4 ** 2) =50


# Q4. 빈칸을 채워서 number가 최종적으로 3이 나오게 해봐.
#     (힌트: //= 과 %= 중 어떤 걸 조합할지 생각해봐)
number = 10
number //= 3
print(number)


#Q5. 아래 코드 실행 후 number 값은? 실행 전에 예측해봐.
number = 2 + 3 * 4 = 14
number //= 2 몫 : 7 (정수형)
number /= 2 몫 : 3.5 (실수형)


# Q6. 각 함수의 출력값은?
print(abs(-100)) 절댓값 : 100
print(pow(3, 3)) x, y 제곱 = 27
print(max(7, 2, 9, 4)) 최댓값 : 9
print(min(7, 2, 9, 4)) 최솟값 : 2
print(round(2.567, 1)) 소수점 아래 첫번째까지 반올림 2.6


# Q7. round()의 동작 — 아래 결과를 예측해봐.
#     (힌트: 파이썬의 round()는 일반 반올림과 살짝 달라. 뭐가 다른지 설명해봐)
print(round(0.5)) 
print(round(1.5)) 
print(round(2.5))

# 포인트 : n.5로 중간 값일 때는 무조건 가까운 짝수로 반올림 한다. 1.5면 2, 0.5면 0. 4.5면 4


# Q8. 두 import 방식의 차이는? 언제 A를, 언제 B를 쓰는 게 좋을지 주석으로 적어봐. - 차이를 잘 모르겠음

# 방식 A : floor 형식으로 바로 호출 가능. 다른 모듈 함수 구분, 충돌 가능성 우려
from math import *
print(floor(4.9))

# 방식 B : 코드가 길어지지만 어느 모듈 함수인지 바로 알 수 있음. 실무 선호 방식
import math
print(math.floor(4.9))

# Q9. 출력값 예측:
from math import *
print(floor(3.9)) 
print(ceil(3.1)) 
print(sqrt(25)) 


# Q10. randrange(1, 10)과 randint(1, 10)의 차이점을 주석으로 설명해봐.
randrange(1, 10)  
randint(1, 10)   


# Q11. 1~6 사이 정수 난수를 생성하는 코드를 세 가지 방법으로 작성해봐.
from random import *

# 방법 1: random() 사용
print (random(1,6))
print(int(random() * 6) + 1)  # 이렇게 해야 함
# 방법 2: randrange() 
print (randrange(1,7))
# 방법 3: randint() 사용
print (randint(1,6))

# Q12. 아래 코드에서 범위 오류를 찾아서 고쳐봐.
#      목표: 1~45 사이 로또 번호 1개 생성
from random import *
print(int(random() * 45)+1)      
print(randint(1, 45))        
"""

# Q14. 로또 번호 6개를 뽑는 코드를 작성해봐. (중복 허용, 6줄 출력)
from random import *
for i in range (6) :
    print (randint(1,45))



# Q15. 아래 코드에서 str() 없이 + 를 쓰면 왜 오류가 나는지 설명하고,
#오류 없이 출력하는 방법 2가지를 작성해봐. - 정수형 데이터를 str로 문자열로 변경해야 함.
from random import *
date = randint(4, 28)
print("모임 날짜는 " + str(date) + "일입니다.") 
