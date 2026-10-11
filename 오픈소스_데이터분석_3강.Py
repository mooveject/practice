# 3강 : 데이터 수집과 저장

# 1
# try 문
try :
    number = int(input('정수를 입력하세요: '))
    result = 10 / number
    print(f'결과: {result}')
# except 문
except ZeroDivisionError :
    print('0으로 나눌 수 없습니다.')
# except 문 2
except ValueError :
    print('유효한 숫자를 입력해야 합니다.')

# 3 
try :
    file = open('data.csv', 'r')
    content = file.read( )
    print(content)
except  FileNotFoundError : 
    print('파일을 찾을 수 없습니다.')
# fianlly 블럭
finally :
    print('파일 작업 종료.')
    if 'file' in locals () :
        file.close()
    
# 4 
words = ['python', 'data', 'analysis']
# 함수 정의 및 대문자화
upper_words = list(map(lambda x :x.upper(), words))
print(upper_words)

lower_words = list (map(lambda y : y.lower(), words))
print (lower_words)

# 5. salary * 1.1
" 문제 해석 : 리스트 딕셔너리 > 급여 1.1배로 인상"
employees = [
    {'name': '김지원', 'salary': 3700000},
    {'name': '박민준', 'salary': 7000000},
    {'name': '이서연', 'salary': 4400000},
    {'name': '정현우', 'salary': 3500000}
]
updated_employees =list (map (lambda emp : {'name' : emp['name'], 'salary' : emp['salary']*1.1}, employees))
# map으로 기존 리스트로 새로운 리스트 생성. 이때 람다 함수 이용. 
# emp라는 매개인자에 리스트대로 슬라이싱. (김지원, 박민준, 이서연, 정현우 순) + 급여 인상 1.1 추가

print('\n급여 인상 후:')
for emp in updated_employees:
    print(f'{emp['name']}: {int(emp['salary']):,}원')


# 6
numbers = [10, 15, 20, 25, 30]
# 짝수 필터
even_numbers =[]
for x in numbers :
    if x %2 == 0 :
        even_numbers.append(x) #if조건문 들여쓰기 하기
print(even_numbers)

