# 5장 : 자료구조
# 5-1 리스트 : 변수 하나에 여러 값 [] 대괄호 사용
# 지하철 칸별로 10명, 20명, 30명 승차
subway1 =10
subway2 = 20
subway3 = 30
subway = [10,20,30]
print (subway)

subway = ["푸", "피글렛", "티거"] # 리스트에서도 인덱스로 데이터 위치 표시 0,1,2
print (subway)
# 피글렛이 몇 번째 칸에 있는지 확인해보자
print (subway.index("피글렛"))

# 리스트에 값 추가하기 : append(추가할 값)
subway.append("이요르")
print (subway)

# 리스트 중간에 값 삽입하기 : insert (인덱스, 삽입할 값)
subway.insert(1,"루")
print (subway)

#지하철 역마다 한 명씩 내림 = pop() 리스트 끝에서부터 값 하나씩 반환 후 삭제
print (subway.pop())
print (subway)

print (subway.pop())
print(subway)

print (subway.pop())
print (subway)

# 리스트 값이 필요없을 때 or 새 값을 저장하고 싶을 때 > clear () 모든 값 삭제
subway.clear()
print(subway)

#중복 값 확인하기  - .count() 함수
subway = ["푸", "피글렛","티거"]
subway.append ("푸")
print (subway)
print(subway.count("푸"))

#리스트 정렬하기 | sort() 오름차순 정렬 , sort(reverse=True) 내림차순 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print (num_list) # 1,2,3,4,5

# sorted () 함수 : 원래 리스트 (your_list) 변경 없이 정렬된 새 리스트 생성
your_list = [1,3,2]
new_list = sorted(your_list)
print (your_list)
print (new_list)

num_list.sort(reverse=True)
print(num_list) # 5,4,3,2,1

num_list.reverse() #값 순서 뒤집기
print(num_list) # 1,2,3,4,5

#리스트 확장하기
mix_list =["푸",20, True, [5,2,4,3,1 ]]
print(mix_list)

# 리스트 합치기 : extend()
mix_list = ["푸",20,True]
num_list = [5,2,4,3,1]
num_list.extend(mix_list)  # num_list에 mix_list 합치기
print (mix_list)
print (num_list)

# 5.2 딕셔너리 { } 중괄호 사용 : 딕셔너리명 {k1:v1, k2:v2}
cabinet = {3:"푸", 100:"피글렛"}
empty_dict={} # 빈 딕셔너리
print (cabinet[3]) # key 3에 해당하는 value 출력
print (cabinet[100])
# .get() 함수 : .get(keyk, default=none)
print (cabinet.get(3)) #key 값이 없어도 none 출력
"""\
print (cabinet.get(5))
print ("hi")
"""
print (cabinet.get(5,"사용가능")) #key 5 값이 없어도 (value 빈값), none 대신 "사용 가능" 출력
#in 연산자 사용 -> 해당 자료 구조에 key가 있을 때 True, 없을 때 False
print (3 in cabinet) 
print (5 in cabinet)
print ("곰" in "곰돌이") # "곰"이라는 문자가 "곰돌이"라는 문자 안에 있는지 확인
print ("돌이"in "곰돌이")
print ("푸"in"곰돌이")

cabinet = {3: "유재석", 5: "김종국"}
print(3 in cabinet)  # True  ← key 3이 있냐?
print(5 in cabinet)  # True  ← key 5가 있냐?
print(7 in cabinet)  # False ← key 7이 있냐?

cabinet= {"A-3":"푸", "B-100":"피글렛"}
print (cabinet["A-3"])
print (cabinet["B-100"])

cabinet = {"A-3" : "푸", "b-100" : "피글렛"}
print (cabinet)
cabinet ["A-3"]="티거" # 대괄호 이용 : value 값을 변경, 새로 추가
cabinet ["c-20"]="이요르"
print (cabinet)

# del 키워드 : key 값에 해당하는 값 삭제
# keyword 란 파이썬에서 사용이 예약된 문자열. 다른 용도 사용 불가능.
del cabinet ["A-3"]
print (cabinet)

# .keys () 함수 :  딕셔너리 속 key 값만 확인하고 싶을 때
print (cabinet.keys()) 
# .values() 함수 : 딕셔너리 속 value 값만 확인하고 싶을 때
print (cabinet.values())
# .items() : key, value 둘다 확인하고 싶을 때 (한 쌍으로 출력)
print (cabinet.items())

cabinet.clear() #값 전체 삭제 
print (cabinet)
