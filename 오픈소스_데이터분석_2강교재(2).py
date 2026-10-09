# 2.3 파이썬 문법 요소
# 1. 언패킹 : 시퀀스 자료형에서 여러 개의 값을 개별 변수에 분리하여 할당 
# = 시퀀스 (튜플, 리스트, 문자열 등)를 하나씩 쪼개 각 변수에 할당

# 1)
coordinates = (10,20) # 튜플
x,y = coordinates 
print (f'x좌표 : {x}, y좌표 :{y}')
rgb = [255, 128,0] # 리스트 
red, green, blue = rgb
print (f'빨강 : {red}, 초록 :{green}, 파랑 :{blue}')
word = 'ABC' #문자열 
first, second, third = word
print (f'첫번째문자 : {first}, 두번쨰문자 : {second}, 세번째문자 : {third}')

# 2) 여러 값을 반환하는 언패킹
def get_dataset_stats (values) :
    return min (values), max (values), sum (values) / len(values) # len 함수 : 전체 값 개수 세기
data = [12,8,21,17,5,32,14]
minimum, maximum, average = get_dataset_stats(data)
print (f'최솟값 : {minimum}, 최댓값 : {maximum}, 평균 : {average :.2f}') # average :.2f (소수점 둘째자리까지만 표기한다는 뜻)

# 3)
scores = [
    ("kim",85,92,78),
    ("lee",92,88,95),
    ("park",75,83,90)
]
for name, db, python, cloud in scores :
    average = (db+python+cloud) / 3
    print (f'{name}의 평균 점수 : {average : .1f}') # float 소수점 1자리까지

# 4) 확장 언패킹 
monthly_sales = [ 1200,1350, 1420,1500,1300,2000,1900]
first, second, *remaining = monthly_sales
print (f'1월 : {first} ')
print (f'2월 : {second}')
print (f'나머지 : {remaining}')

first, *middle, last = monthly_sales
print (f'1월 : {first}')
print (f'마지막 달 : {last}')
print (f'중간 : {middle}')

# 2. 언더스코어 (_)

# 1) for 문에서 언더스코어 사용 > 단순 반복 작업에서 불필요한 변수를 선언하지 않음 > 코드 가독성⬆️
# = 필요 없는 항목은 버리고 추출한 항목에만 변수를 선언한다 = 효율성⬆️
for _ in range (5) :
    print ('Hello, Data Analysis with open source!')

# 2) 
students = [
    (1234, 'kim', 'cs',2, 3.8),
    (5678, 'lee', 'ss', 3, 4.2),
    (9100,'park','vd', 1,3.5)
]
print ('이름과 성적 출력 :')
for _, name, _, _, grade in students :
    print (f'{name}의 성적 : {grade}')

a = students [:2]
print (a)
b = [row [:3] for row in a] #row 가로열 
print (b)

# 3)
def coordinates () :
    return (10,20,30)

_,y,_ = coordinates ()
print (y)

# 3. 예외 처리 (exception) = 강제 종료를 막고 오류를 처리하는 방식
# 1) try - except
number = int (input("수를 입력하시오."))
try : 
    result = 10/number
    print (f'결과 {result}')
except ZeroDivisionError :
    print ('0으로 나눌 수 없습니다.')

 # 2) try - except 

try :
    number = int (input("수를 입력하시오."))
    result = 10/number
    print (f'결과 {result}')
except ValueError :
    print ('유효한 숫자를 입력해야 합니다.')
except ZeroDivisionError :
    print ('0으로 나눌 수 없습니다.')

# 3) finally 블록 : 예외 발생 여부와 관계 없이 반드시 실행되는 코드 블록
try : 
    numbers = [1,2,3]
    print (numbers[3])
except IndexError as e : # 예외 객체를 변수 e에 저장,
    print (f'예외 발생 : {e}')

# 4) finally 블록 사용 예
"""
try : 
    file = open ('data csv','r')
    content = file.read ()
    print (content)
except FileNotFoundError :
    print ('파일을 찾을 수 없습니다.')
finally :
    print ('파일 작업 종료')
    file.close () """

# 4. 함수형 프로그래밍
# (1) 람다 함수 : lambda 매개변수 : 표현식 = lamba 는 특정 상황, 연산에서 사용하기 좋다
def add (x) :
    return x + 2

add_lambda = lambda x : x + 2

print (add(3))
print (add_lambda(3))

# 2) 
concat = lambda s1, s2 : s1 + ' ' +s2
print (concat ('파이썬', '데이터 분석'))

# 3) 람다 함수 정의
is_even = lambda x : '짝수' if  x % 2 == 0 else '홀수'
print (is_even(10))
print (is_even(7))

# 4) 람다 함수 활용
employees = {
    '이지혜' : 300,
    '구민준' : 500,
    '방서연' : 400
}
adjust_salary = lambda salary : salary * 1.1
updated_salary = {name : adjust_salary(salary) for name, salary in employees.items()}
# 코드 해석 : 월급 조정 람다 함수 지정, 
# 업데이트 월급 {k:v} 딕셔너리 지정할 것임. for문 employees 딕셔너리에서  name, salry 튜플 형태로 변환 후 
print (updated_salary)

# 5) sorted () 함수를 통한 데이터 정렬 : sorted (a, key = lambda x : 표현식 )
# = key 매개변수를 통해 정렬 기준 지정저 
students = [
    ("lee", 85),
    ("park", 92),
    ("kim", 78),
    ("kang", 88)
]
sorted_student = sorted (students, key= lambda student : student [1])
print ('성적 오름차순 정렬 결과:')
for name, score in sorted_student :
    print (f'{name}: {score}점')

# (2) map, filter ,reduce 
# 1) map 함수 : 데이터 변환
temperature_c = [25.6, 27.8, 30.5, 22.3, 28.9]
c_to_f = lambda c : (c * 9/5) + 32
temperature_f = list (map(c_to_f, temperature_c))

print ('섭씨 온도 데이터 :',temperature_c)
print ('화씨 온도 데이터 :', temperature_f)

# 2) map 함수 2 
words = ['python', 'data','analysis']
upper_words = list (map (lambda word : word.upper(), words))
print (upper_words)

# 3) map 함수 3
employees = [
    {'name': '김지원', 'salary' : 370},
    {'name': '박민준', 'salary' : 700},
    {'name': '이서윤', 'salary' : 440}
] # "key:value 2개짜리 딕셔너리가 3개 들어있는 리스트
updated_employees = list (map (lambda emp : {'name' : emp['name'], 'salary' : emp['salary']*1.1}, employees))
print ('\n 급여 인상 후 :')
for emp in updated_employees :
    print(f"{emp['name']} : {int(emp['salary']):,}원")

print (employees)
# 코드 해석 : updated_employees 라는 새 리스트로 map (=변환), 이 안에서 lambda 함수를 사용해 k:v를 반환할 것이다.
# lambda emp 라는 매개 변수 : {k :v , k : v}= 여기서는 {'name' : emp['name'], 'salary' : emp['salary']*1.1}, employees라는 리스트 값에서 emp를 가져온다)
"""헷갈리는 지점 :  def 함수에서는 def 함수명 (a,b) 매개변수 2개를 지정해서 name, salary 인자를 매개변수 a,b에 각각 할당. 
람다에서는 lambda emp 라는 emp하나로 emp ['name'], emp['salary'] 다른 형태인 2개의 정보를  가져오는 게 헷갈림 """


# 1) filter 함수
numbers = [10,15,20,25,30]
even_numbers = list (filter (lambda x  : x % 2 == 0, numbers)) # list() 함수를 이용해 객체에서 []리스트로 변환
print (even_numbers)

# 2) filter 함수
osda_students = [
    {'name' : 'kim' , 'score' : 85},
    {'name' : 'lee' , 'score' : 65},
    {'name' : 'park' , 'score' : 90},
    {'name' : 'jeoung' , 'score' : 55},
    {'name' : 'choe' , 'score' : 78}
]
passed_s = list (filter(lambda student : student ['score']>=70,
                        osda_students))
for student in passed_s :
    print (f"이름 : {student['name']}, 점수 : {student['score']}")
# 코드 해석 : 람다 함수 매개변수 student : osda_students 리스트 안에 {key = score : value = [85,65,90,55,78]} >= 70
# 리스트 각 개별 항목 값이 > = 70 인 것을 필터링해서 리스트로 변환(마치 if 조건문처럼 )
# 리스트 인덱스 0부터 ~ 시퀀스를 진행하기 때문에 for i in 시퀀스할 목록. 

""" claude 답변  : student는 **"지금 이 순간 손에 들고 있는 카드"**를 가리키는 이름표예요. 
['score']는 그 카드에서 어느 칸을 읽을지 고르는 거고요. 둘 다 있어야 값 하나가 딱 정해져요.
핵심은 student가 매번 다른 카드로 바뀐다는 거예요. 
같은 student['score']라는 글자인데, 1번째엔 85, 2번째엔 65를 뜻해요. 이름표는 하나인데 붙는 대상이 계속 바뀌는 거죠."""

passed_s = []
for student in osda_students:      # 카드 한 장씩 꺼내서 student라고 부름
    if student['score'] >= 70:     # 그 카드의 score를 확인
        passed_s.append(student)

# 1) reduce 함수 : 누적 연산 
# = 반복문을 사용하지 않고도 반복 가능한 객체의 모든 요소를 누적해 하나의 값으로 축소

from functools import reduce # 모듈에서 누적 연산 함수인 reduce를 불러온다는 뜻
numbers= [1,2,3,4,5]
total_sum = reduce (lambda x, y : x + y, numbers)
print (total_sum)
""" 1=x , 2=y  lambda 함수 x+y =3
    3=x , 3=y lambda 함수 x+y =6
    6=x , 4=y lambda 함수 x+y =10
    10=x , 5=y lambda 함수 x+y =15
    이 모든 과정을 하나의 값으로 축소해 15만 반환
"""

# 2) reduce 함수 

from functools import reduce # 모듈에서 누적 연산 함수인 reduce를 불러온다는 뜻
numbers = [3,7,2,9,5]
max_value = reduce (lambda x,y : x if x> y else y, numbers)
print (max_value)

""" 3 = x ,  7 =y lambda 함수 3 < 7  : y 반환
    7 = x , 2 =y lambda 함수 7>2 : x 반환
    7= x, 9 =y lambda 함수 7<9 : y 반환
    9 = x, 5=y lambda 함수 9>5 :  x 반환
    최종 반환값이 9
"""