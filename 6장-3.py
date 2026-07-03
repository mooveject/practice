students = [1,2,3,4,5]
print (students)

# 한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
print (students)
# students 리스트에서 변수 i로 하나씩 값을 가져옴 > 변수 i+100 > 다시 students에 저장 | 값들에 해당 동작 수행 > 수행결과 새리스트 작성
# students = i += 100
# students = [students[0]+100,students[1]+100 ... ]
# students = [1+100, 2+100, 3+100 ... ]

# 한 줄 for 문으로 각 이름을 이름의 길이 정보로 변환
students = ["Iron man", "Thor", "Spider Man"]
print (students)
students = [len(i) for i in students] # 반복 대상 students 값을 변수 i에 저장, i 값 글자수 세기 (len)
print (students)

students = ["Iron man", "Thor", "Spider Man"]
print (students)
students = [i.upper() for i in students]
print (students)

# 6.3 실습 문제 : 택시 승객 수 구하기
"""person=range(1,51)
time = range(5,51)
for i in person :
    if 5 <= time <15 :
        print ("[O] {0}번째 손님 (소요시간 :{1}분)".format(person, time))
    elif time < 5 or time >15 :
        print("[ ] {0}번째 손님 (소요시간 :{1}분)".format(person, time))
"""
# 답지
from random import *

cnt = 0
for i in range (1,51):
    time = randrange(5,51)
    if 5<= time <=15:
        print("[O] {0}번째 손님 (소요시간 :{1}분)".format(i,time))
        cnt +=1
    else:
        print("[ ] {0}번째 손님 (소요시간 :{1}분)".format(i,time))
print ("총 탑승객 :{0}명".format(cnt))

from random import*
cnt = 0 # 총 탑승객 값을 저장해야 하므로 0으로 시작
for i in range (1,51):
    time = randrange (5,51) 
    if 5<=time <=15 :
        print ("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt +=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print ("총 탑승객 : {0}명".format(cnt))

""" 중간 정리
1) if, elif, else 
2) for문 (반복 대상만큼 반복)
3) while문 (주어진 조건을 만족하는 동안 반복)
4) continue (해당 반복을 종료 후 다른 반복으로 넘어감)
5) break (해당 반복문 탈출)
"""

#셀프 체크 : 편의점에서 2+1 이벤트 진행 중. 구매 상품 수에 따라 가격을 계산하는 프로그램 만들기
#상품 1개 가격 : 1,000원. 고객이 항상 3의 배수에 해당하는 상품구매 가정. 상품 스캔할 때마다 '2+1 상품입니다.' 출력
     

price = 1000
goods = 6
total = 0

for i in range (1,goods +1):
    print ("2+1 상품입니다.")
    if i %3==0: # 3의 배수인 경우 
        continue
    total +=price # goods 2 , total = 1000 +1000
print ("총 가격은" + str(total)+ "원입니다.")

#total = 0 으로 시작해서 반복문이 돌면서 누적으로 쌓이는 구조야. 계산식이 한 줄에 다 보이는 게 아니라 반복문 전체가 계산 과정인 거야.

