# 오픈 소스 2강 교재
# 다차원 슬라이싱
matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
a = matrix [:2]
print (a)
b = [row[:2] for row in a] 
"row 가로 열, column 세로 열"

print (b)

# 리스트 슬라이싱 리스트 값 변경
numbers = [1,2,3,4,5,6,7]
numbers[2:5] = [300,400,500]
print (numbers)

# 리스트 컴프리헨션  : 표현식 for 변수 , 리스트 이름 (if 조건)
# 1) 일반적인 리스트 생성
numbers = []
for i in range (5) :
    numbers.append(i)
print (numbers)
# 1) 리스트 컴프리헨션을 사용한 리스트 생성
numbers = [i for i in range (5)] 
" 0부터 5 이전까지 수를 변수 i에 할당, 변수 i에 할당된 수로 만들어진 리스트명이 numbers "
print (numbers)

# 2) 일반적인 리스트 값 변경을 통한 리스트 생성
numbers = [1,2,3,4,5]
squares = []
for num in numbers :
    squares.append(num**2)
print (squares)
# 2) 리스트 컴프리헨션을 사용한 값 변경 리스트 생성
numbers = [1,2,3,4,5]
squares = [num**2 for num in numbers ]
print (squares)

# 3) 조건을 만족하는 원소만 선택하여 리스트 생성 ( = 조건에 맞는 원소만 추출하여 리스트 생성)
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers= []
for num in numbers :
    if num % 2 == 0 : # 2로 나누어떨어지는 숫자만 even_numbers에 할당한다.
        even_numbers.append(num)
print (even_numbers)

# 3) 리스트 컴프리헨션을 사용한 특정 원소만 선택 후 리스트 생성
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers= [num for num in numbers if num%2==0 ]
print (even_numbers)

# 4) 두 리스트의 모든 조합을 포함하는 리스트 생성 (중첩 반복문)
list1= ['사과', '복숭아', '바나나']
list2 = ['주스','잼','복숭아']
pairs = []
for fruit in list1 :
    for product in list2 :
        pairs.append ((fruit,product)) # 중첩 > 괄호 2개 
print (pairs)

# 4) 리스트 컴프리헨션을 사용해 두 리스트의 모든 조합을 포함하는 리스트 생성 (중첩 반복문)
list1= ['사과', '복숭아', '바나나']
list2 = ['주스','잼','복숭아']
pairs = [(fruit,product) for fruit in list1 for product in list2]
print (pairs) # 쌍을 이루는 (a,b) 튜플 형태로 나옴

# 튜플 (a,b)과 딕셔너리 {k,v}의 차이 정리하기 with gemini
# 1. 반복문으로 만들어진 튜플 리스트
list3 = [('apple', 1000), ('banana', 1500), ('cherry', 2000)]

# 2. dict()를 이용해 "a를 호출하면 b가 나온다" 형태로 변환
my_dict = dict(list3)

print(my_dict)  
# 출력: {'apple': 1000, 'banana': 1500, 'cherry': 2000}

# 3. 이름표(Key)로 호출해보기
print(my_dict['banana'])  
# 출력: 1500

# 딕셔너리 컴프리헨션 : 키 : 값 for 변수 in 반복가능객체 ( if 조건 )
# 1) 일반적인 반복문 사용
a = {}
for i in range (5):
    a [i] = i**2
print (a)

# 1) 딕셔너리 컴프리헨션을 사용
a ={i:i **2 for i in range (5)}
print (a)
print (a[2]) # key 호출 , value 출력

# 2) 딕셔너리 컴프리헨션 +  특정 조건을 적용한 방법
even_s={num : num ** 2 for num in range (10) if num %2 ==0}
print (even_s)

# 3) 다양한 조건을 사용한 데이터 필터링 
# Q.왜 꼭 튜플로 가져와야 할까. 
# A. 딕셔너리는 키 : 값, 즉 정확히 200일 때의 키/값이 있을 때만 반환하므로 튜플 리스트로 변경한 후, 
# 리스트 내에서 200>= 조건을 적용시킨 후 조건에 맞는 것들을 새로운 딕셔너리로 생성한다
city_population = {'서울':957, '부산':339, '인천':254 , '광주' : 145, '울산' : 114, '용인' : 108}
large_cities = {city: pop for city, pop in city_population.items() if pop>=200} 
#items() 매서드는 딕셔너리의 각 항목을 (키,값) 튜플 리스트로 반환한다
print ('인구 200만명 이상인 도시:', large_cities)
large_short_name = {city : pop for city, pop in city_population.items() if pop>=200 and '산' in city}
# 수 필터링, 텍스트 필터링 둘다 적용
print (large_short_name)

# 4) 일반적인 딕셔너리 값 변경
scores ={'nana' : 45, 'jina' : 38, 'suji':30}
percentage_scores_old = {}
for name ,score in scores.items() :
    percentage_scores_old[name] = (score/50) * 100
     # name 이라는 key에 score/50*100 이라는 value 값을 새로 할당 =변경.
print ('기존 방식 결과 :', percentage_scores_old)
names_containing_na = {name:score for name, score in scores.items () if 'na'in name}
print (names_containing_na)

# 4) 딕셔너리 컴프리헨션을 사용한 값 변경 :  키 : 값 for 변수 in 반복가능객체 ( if 조건 )
scores ={'nana' : 45, 'jina' : 38, 'suji':30}
percentage_scores_new = {name:(score/50)*100 for name, score in scores.items()}
print ('딕셔너리 컴프리헨션 결과 :', percentage_scores_new)

# 데이터 입출력 
# 1) C 스타일 (%연산자) 포맷팅
item = '프린터'
price = 360000
print ('상품명: %s, 가격 : %d' % (item, price))

# 2) str.format () 매서드 포맷팅 : '문자열 [위치 또는 이름]'.format (인자)
name ='홍길동'
age = 30
salary = 3500000
tax_rate = 0.1

# 순서대로 삽입
basic_format = '이름 : {}, 나이 : {}, 월급 ; {}원'.format (name, age, salary)
# 인덱스 번호 지정 
index_format = '직원 :{1}의 나이는 {0}세이고, {0}의 세후 월급은 {2}원입니다.'.format (age, name, int (salary *(1-tax_rate)))
# 중괄호 안에 변수명 지정, .format (변수명에 값 할당)
keyword_format = '직원 정보 : 이름 {employee} 나이 : {years} \
    월급 : {income} 세금 : {tax} 실수령액 : {net_income}원'.format (employee=name, years =age,income=salary,tax=tax_rate,net_income=int (salary *(1-tax_rate)))
print (basic_format)
print (index_format)
print(keyword_format)

# 3) ⭐️ f-문자열 : 문자열 내에 직접 삽입
# (1)
name = '홍길동'
age = 30
print (f'이름 : {name}, 나이 : {age}')

# (2)
basic = f'이름 : {name}, 나이 :{age}'
index = f'직원 {name}의 나이는 {age}세'
keyword = f'직원 {name} 나이 {age}세 \
    월급: {salary} tax: {tax_rate: .1%}\
        실수령액 : {int (salary *(1-tax_rate))}원' 
# tax)rate : .1% = 소수를 백분율로 변환해 소수 첫째자리까지 표시 
print (keyword)

# 컨텍스트 관리 : 사용 후 종료해야 하는 자원의 획득, 해체를 자동 처리하는 것 ⭐️with
# 1) open () 함수와 close () 함수 
file = open ('output.txt','w')
file.write ('hello, world!\n')
file.close()

# with 문 사용 (1)
with open ('output.txt','w') as file :
    file.write ('hello, world!\n')

# with 문 사용 (2)
with open ('input.txt','r') as in_file, open ('output.txt','w') as out_file :
    for line in in_file : #for 문 루프 
        out_file.write (line.upper())

# with 문 사용 (3)
import urllib.request
with urllib.request.urlopen ('http://raw.githubusercontent.com/jaehwachung/Data-Analysis-with-Open-Source/refs/heads/main/chapeter%203/students.csv')as response:
    data= response.read().decode ('utf-8')
print (data)








