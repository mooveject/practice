#4장 문자열 다루기
sentence1="나는 소년입니다"
print (sentence1)
print (sentence1, type (sentence1))
sentence2= """
나는 소년이고,
파이썬은 쉬워요.
"""
print (sentence2)
print ("파인"+"애플")

#슬라이싱 + 인덱스 (= 순서, 위치 [] 대괄호, 0부터 시작
#  )
jumin = "990229-1234567"
print ("성별 식별번호 : " + jumin[7])
print ("연 :" + jumin [0:2]) #0부 2직전까지 
print ("월 :" + jumin[2:4] )
print ("일 :"+jumin[4:6])
print ("생년월일:"+jumin[:6]) #처음부터 6직전까지
print ("주민번호 뒷자리 :"+jumin[7:]) #7부터 끝까지
print ("주민등록번호 :" + jumin[:]) #처음부터 끝까지
#뒤에서부터 슬라이싱 -1부터 시작
print ("주민등록번호 뒷자리 (뒤에서부터)"+jumin[-7:]) #-7부터 끝까지

#문제 풀이
msg="나도코딩"
print(msg[1])
print(msg[:2])
fruit = "apple"
print (fruit)
print (fruit[0:5]) #0부터 5번쨰까지
print (fruit[:-1]) #0부터 -1 직전까지

#함수로 문자열 처리하기 
#형식 : 문자열/변수 . 함수
#lower, upper, islower, isupper, replace, index, find, count
python = "Python is Amazing"
print (python.lower())
print (python.upper())
print (python[0].islower())
print (python[:3].isupper())
print (python.replace("Python", "Java"))

#find (찾는 문자, 식작 인덱스, 종료 인덱스) -> 찾는 문자열이 없으면 -1 반환
find = python.find("n")
find = python.find("n", find + 1)  #인덱스 6이후부터 찾아 발견한 처음 n의 인덱스
print(find) 
find = python.find("Java") #Java가 없으면 -1 반환
print(find)

#index (찾는 문자, 식작 인덱스, 종료 인덱스) -> 찾는 문자열이 없으면 error
index = python.index("n")
print(index)
index=python.index("n",index +1) #인덱스 6 이후부터 찾아 발견한 처음 n의 인덱스
print(index)
index=python.index("n",2,6) #인덱스 2부 6 직전까지 찾아 발견한 n의 인덱스
print (index)
#index=python.index("Java")
#print(index)
#여기서 알 수 있는 점 : 변수가 계속 업데이트 되고 있다는 점

#count() : 해당 문자열이 몇 번 나왔는지 
print(python.count("n"))
print(python.count("v"))
#len() : 문자열 길이 정보 제공 (공백도 문자에 포함)
    #형식  : len(문자열/변수)
print (len(python))

