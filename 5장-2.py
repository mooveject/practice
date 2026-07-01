# 5-3 튜플 ( ) 값 변경, 추가, 삭제 불가. 속도 빠름. 읽기 전용 : 튜플명(값1,값2)
menu=("돈가스","치즈돈가스")
print(menu[0])
print(menu[1])

name = "피글렛"
age=20
hobby="코딩"
print (name, age, hobby)

# 튜플로 한 줄에 쓰기
(name, age, hobby)=("피글렛", 20, "코딩")
print (name, age, hobby)

(departure, arrival) = ("김포", "제주")
print (departure,">",arrival) # 김포 > 제주
(departure, arrival) =(arrival, departure)
print (departure, ">", arrival) # 제주 > 김포

# 5-4 세트 { } 중복 X, 순서 X -> 출력시 순서가 계속 바뀜 : 세트명 { } or set( )
my_set = {1,2,3,3,3}
print (my_set)

# 빈 세트 생성하기
empty_set=set()
print(empty_set)

java={"푸", "피글렛", "티거"}
python=set(["푸","이요르"])

# 교집합 (java와 파이썬을 둘다 다룰 수 있는 사람 = and : .intersection (교차)
print(java & python)
print (java.intersection(python))

# 합집합 (둘 중 하나라도 다룰 수 있는 사람) = or : .union (조합)
print(java| python)
print (java.union(python))

# 차집합 (자바만 할 줄 아는 사람) : .difference (차)
print (java - python)
print(java.difference(python))

# 파이썬 개발자 추가 (기존 개발자 : 푸, 이요르) : .add
python.add("피글렛")
print (python)

# 자바 개발자 삭제 (기존 개발자 : 푸, 피글렛, 티거) : .remove
java.remove ("피글렛")
print (java)

# 1분 퀴즈
set1={1,2,3,4,5}
set2={3,4,4,5,6,7}
print(set1.intersection(set2))

# 5.5 자료구조 변환하기
menu={"커피", "우유","주스"} #세트 : 순서, 중복 x
print(menu)
print(type(menu))

menu=list(menu) # 변환 방법 : 바꿀 자료 구조 형식(자료구조명)
print(menu, type(menu)) # 순서 O, list [] 대괄호

menu=tuple(menu)
print(menu, type(menu)) # 변경 불가 튜플 ()

menu=set(menu)
print(menu, type(menu))

# 5.6 실습 문제 : 당첨자 뽑기
# 댓글 추첨 1명 치킨 쿠폰, 3명 커피 쿠폰, 20명이 댓글 작성, 무작위 추첨, 중복은 허용하지 않는다
# random 모듈의 shuffle() 과 sample() 함수 사용
id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
from random import*
shuffle(id)
print ("-- 당첨자 발표 --")
print ("치킨 당첨자 :" + str(sample(id,1)))
print("커피 당첨자 : " + str(sample(id,3)))
print ("-- 축하합니다! -- " )

# 답안
from random import* # random 모듈 추가
users=range(1,21) # 리스트 생성, 1부터 21직전까지. range 함수를 이용할 것. <- 유저가 1000명이면 언제 다 쓰게!
users=list(users) # user를 리스트 자료구조로 변환
shuffle(users) # 리스트 섞기
winners=sample(users,4)
print ("-- 당첨자 발표 -- ")
print ("치킨 당첨자 : {0}".format(winners[0])) #0번째 인덱스 출력
print ("커피 당첨자 : {0}".format(winners[1:])) #1번째부터 마지막까지 슬라이싱 3명
print ("-- 축하합니다! --")

shuffle(users)
chicken = sample(users,1)
remain = set(users)-set(chicken)
coffee = sample(list(remain),3)
print ("치킨 당첨자 : {}".format(chicken))
print ("커피 당첨자 : {0}".format(coffee))

# shuffle 함수, sample 함수
from random import*
lst=[1,2,3,4,5] # 리스트 1~5
print(lst) 
shuffle(lst) # 자료구조 lst 1~5 섞기
print(lst) 
print(sample(lst,1)) #리스트 값에서 무작위로 값 1개 출력

# 셀프 체크 : 수강 신청 기간에 일부 과목이 중복 신청됨. 중복 과목을 없애는 프로그램 작성하기
subject=["자료구조","알고리즘","운영체제","자료구조"]
subject=set(subject)
subject=list(subject)
print ("신청한 과목은 다음과 같습니다 \n",subject)