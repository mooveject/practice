# 오픈소스 데이터 분석 2강 — 2번 파일 복습 오답 노트

> **학습 자료:** `오픈소스_데이터분석_2강교재(2).py` — 언패킹, `_`, 예외 처리, 람다, `sorted()`, `map()`, `filter()`, `reduce()`  
> **작성 기준:** 실제 복습 대화에서 드러난 오답·질문·교정 과정 우선. 교재에 등장하지만 대화에서 직접 풀지 않은 예제는 별도로 표시.  
> **상태:** 2번 파일 주요 개념 1회 복습 완료. `sorted(key=...)`와 `reduce()`의 중간 실행 과정은 주기적 재점검 권장.

## 핵심 진단 — 반복적으로 헷갈린 지점

| 우선순위 | 개념 | 실제 혼동·실수 | 교정 핵심 |
|---|---|---|---|
| 높음 | `sorted(..., key=함수)` | `key`를 딕셔너리 키와 혼동. `key`가 계산한 값이 최종 결과에 저장된다고 생각 | `key`는 **정렬 기준을 계산할 함수**를 전달받음. 정렬 결과에는 **원래 요소**가 남음 |
| 높음 | `sorted()` vs `map()` | `sorted(numbers, key=lambda x: x+1)`로 각 값에 1을 더한 리스트를 만들 수 있다고 예상 | `sorted`는 **순서 변경**, `map`은 **각 요소 변환** |
| 높음 | `reduce()`의 누적 변수 | 비교에서 `x`, `y`를 뒤바꾸거나 첫 비교를 건너뜀 | `x=이전 누적 결과`, `y=다음 원소`; 첫 계산은 기본적으로 처음 두 요소 |
| 중간 | `reduce()`의 연산자 | `x * y`를 `x + y`로 읽어 결과 9로 계산 | 연산자부터 확인: `*`, `+`, `-`는 결과가 전혀 다름 |
| 중간 | 문자열 언패킹 | `'ABC'` 전체가 `first`에 저장된다고 예상 | 문자열은 글자 단위로 반복 가능: `'A'`, `'B'`, `'C'` |
| 중간 | `_` 변수 | `_`에는 값이 할당되지 않는다고 생각 | `_`도 일반 변수이며 값이 **할당됨**. 사용하지 않을 값이라는 관례적 표시 |
| 중간 | 예외 처리 + 파일 닫기 | `finally`에서 `file.close()`를 항상 호출해도 되는지 점검 필요 | `open()` 실패 시 `file`에 객체가 없을 수 있음. 파일은 `with`로 관리하는 편이 안전 |
| 낮음 | `filter()`의 결과 | 참/거짓 두 그룹으로 나누는 듯한 표현 | 조건의 반환값은 참/거짓, 결과에는 **True인 원래 요소만** 남음 |

---

## 1. 언패킹: 자료형별로 무엇이 나누어지는가?

**실제 오답:** `word = 'ABC'`에서 `first = 'ABC'`, 나머지 변수는 빈칸이라고 답함.

```python
coordinates = (10, 20)
x, y = coordinates              # x=10, y=20

rgb = [255, 128, 0]
red, green, blue = rgb          # 255, 128, 0

word = 'ABC'
first, second, third = word     # 'A', 'B', 'C'
```

**핵심:** 언패킹은 반복 가능한 객체의 요소를 **순서대로 하나씩** 왼쪽 변수에 할당한다. 문자열의 요소는 문자 한 개씩이다. 이후 `'Python'`을 `P/y/t/h/o/n`으로 나누는 문제는 모두 맞힘.

### 확장 언패킹 `*`

```python
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
# first = 10
# middle = [20, 30, 40]
# last = 50

*front, last = numbers
# front = [10, 20, 30, 40]
# last = 50
```

**초기 공백:** `first, *rest = scores`에서 `rest`가 무엇인지 모른다고 답했음. 설명 후 **나머지 값을 리스트로 묶는다**고 정확하게 설명함. `*`는 할당 문법이며 변수 이름은 `rest`다 (`*rest`라는 이름이 아님).

> **교재 연결:** `monthly_sales` 예제에서는 `first, second, *remaining`과 `first, *middle, last` 두 위치를 모두 사용한다.

## 2. 언더스코어 `_`: 값을 버리는 특별한 문법인가?

**실제 오답:** `name, _, major = student`에서 가운데 값은 **할당되지 않는다**고 답함.

```python
student = ('민지', 23, '컴퓨터과학')
name, _, major = student

print(name)   # 민지
print(_)      # 23
print(major)  # 컴퓨터과학
```

**정정:** `_`는 일반 변수명이다. 값 `23`이 실제로 할당된다. 단지 **이후 쓰지 않을 값**이라는 의도를 드러내는 관례다. 이후 `a, _, c = [10, 20, 30]`에서 `print(_) == 20`을 맞혔음.

```python
for _ in range(5):
    print('Hello')
```

이 코드에서도 반복 변수 `_`에는 `0, 1, 2, 3, 4`가 차례대로 들어간다. 값을 본문에서 사용하지 않을 뿐이다.

> **교재 연결:** `for _, name, _, _, grade in students:`는 다섯 요소 중 이름과 성적만 사용한다. `_`가 여러 번 등장하면 같은 변수명에 값이 다시 할당된다는 점을 기억할 것.

## 3. `try` / `except` / `finally`: 오류 뒤 실행 흐름

```python
try:
    number = int('abc')
    print('변환 성공')
except ValueError:
    print('변환 실패')
finally:
    print('작업 종료')
# 변환 실패
# 작업 종료
```

**정확히 이해한 부분:** `int('abc')`가 `ValueError`를 발생시키므로 뒤의 `print('변환 성공')`을 건너뛰고 `except`가 실행된다. `finally`도 실행된다. 반대로 `int('100')`이면 `except`는 건너뛰고 `try`와 `finally`가 실행된다.

**표현 보충:** `finally`를 단순히 `if` 블록 밖의 `print()`와 같다고 볼 수는 없다. 예외 처리의 종료 과정에서 실행되도록 보장하는 구문이다(프로세스 강제 종료 등 특수 상황은 제외).

### 교재의 파일 처리 예제에서 주의할 점

교재에는 다음 구조의 예제가 주석 처리되어 있다.

```python
try:
    file = open('data.csv', 'r')
    content = file.read()
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')
finally:
    file.close()  # open() 실패 시 위험
```

`open()`이 실패하면 **할당문 오른쪽에서 오류가 나므로** `file`에 파일 객체가 저장되지 않을 수 있다. 이 상태에서 `file.close()`를 호출하면 다른 오류가 발생할 수 있다.

**권장 구조:**

```python
try:
    with open('data.csv', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')
finally:
    print('작업 종료')
```

`with`가 정상적으로 열린 파일의 닫기를 담당하고, `except`가 파일 없음 오류를 처리한다. 사용자는 파일이 열린 상태에서 `ZeroDivisionError`가 발생하더라도 `with`가 파일을 닫는다는 점을 맞혔다.

> **추가 점검(교재 원문):** 첫 번째 예외 처리 예제에서는 `int(input(...))`가 `try` 바깥에 있다. 이 경우 잘못된 숫자 입력으로 생기는 `ValueError`는 아래 `except ZeroDivisionError`에서 처리되지 않는다. 다음 예제에서는 입력 변환을 `try` 안으로 넣고 `ValueError`도 처리한다.

## 4. `lambda`: 함수 정의와 함수 호출 구분

```python
def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

print(add_lambda(3, 5))  # 8
```

**이해한 부분:** `x`, `y`는 매개변수이며 호출 시 인자 `3`, `5`를 받아 계산한다. `lambda x, y: x + y`는 **함수 생성**이고 `add_lambda(3, 5)`가 **함수 호출**이다.

> **교재 연결:** `lambda x: '짝수' if x % 2 == 0 else '홀수'`, 급여 인상 함수 `lambda salary: salary * 1.1`, 문자열 결합 함수 등으로 응용한다.

## 5. 가장 큰 맹점: `sorted()`의 `key`는 무엇인가?

**실제 질문:** “딕셔너리도 아닌데 왜 `key`라고 하나?”, “왜 `key=lambda ...`라고 쓰나?”

```python
students = [('민수', 85), ('지연', 92), ('철수', 78)]

def get_score(student):
    return student[1]

result = sorted(students, key=get_score)
# [('철수', 78), ('민수', 85), ('지연', 92)]
```

- `students`: 정렬 대상.
- `key=get_score`: **정렬 기준을 계산하는 함수**를 `sorted()`에 전달. 딕셔너리 키와 무관.
- `get_score(('철수', 78))`: `78` 반환.
- **하지만 `sorted()`의 결과는 `78` 하나가 아니라 정렬된 원래 튜플들의 리스트.**
- `key=get_score`처럼 **함수 자체**를 전달한다. `key=get_score()`는 인자 없이 지금 호출하려는 다른 표현이므로 이 예제에 맞지 않음.

람다로 쓰면 같은 뜻:

```python
sorted(students, key=lambda x: x[1])
```

### 기준값은 계산되지만 원본 요소로 바뀌지 않는다

**실제 오해:** `sorted(numbers, key=lambda x: x + 1)`이 1을 더한 새 리스트를 만들 것이라고 예상함.

```python
numbers = [30, 10, 20]

sorted(numbers, key=lambda x: x + 1)  # [10, 20, 30]
[x + 1 for x in numbers]              # [31, 11, 21]
list(map(lambda x: x + 1, numbers))    # [31, 11, 21]
```

`key`가 계산한 `31`, `11`, `21`은 **정렬 순서 결정에만 사용**된다. `sorted()`는 원본을 변경하지 않고 **새 리스트**를 반환한다. 원본이 튜플이어도 반환 자료형은 리스트다.

### 음수 기준값과 `reverse`

```python
numbers = [5, 2, 8]

sorted(numbers, key=lambda x: x * -10)
# [8, 5, 2] : 기준값 -80, -50, -20의 오름차순

sorted(numbers, key=lambda x: x * -10, reverse=True)
# [2, 5, 8] : 기준값 -20, -50, -80의 내림차순
```

**이 부분은 스스로 논리적으로 설명했음.** `reverse=False`가 기본값이고 `reverse=True`면 **기준값에 따른 내림차순**이다. 이해할 때 ‘오름차순 결과를 뒤집는다’고 생각해도 되지만, 실제로 정렬을 두 번 하는 것은 아니다.

## 6. `map()` vs `filter()`: 변환과 선택

```python
numbers = [5, 2, 8]

a = sorted(numbers, key=lambda x: x * 10)  # [2, 5, 8]
b = list(map(lambda x: x * 10, numbers))    # [50, 20, 80]
```

**정확히 맞힌 비교 문제.** `sorted()`도 `x * 10`을 실제로 계산하지만 **정렬 기준으로만 사용**한다. `map()`은 계산 결과 자체를 차례대로 생성한다.

```python
numbers = [10, 15, 20, 25, 30]
selected = list(filter(lambda x: x > 20, numbers))
# [25, 30]
```

**이해한 부분:** `filter()`는 조건을 평가해서 참인 **원래 요소만 남긴다**. `False`인 항목은 결과에서 제외된다. `filter()`가 참·거짓 두 그룹을 반환하는 것은 아니다.

```python
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x * 10,
                  filter(lambda x: x % 2 == 0, numbers)))
# [20, 40, 60]
```

**복합 문제도 정확히 해석함:** 짝수 선택 → 각 값 10배 → `list()` 변환.

- `map()`과 `filter()`는 **반복자**를 반환한다. `list()`로 감싸야 리스트가 된다.
- `map()`은 원래 순서를 따라 **변환한 결과**를 제공한다.
- `filter()`는 원래 순서를 따라 **통과한 원래 요소**를 제공한다.

> **교재에서 추가 연습할 예제:** 섭씨→화씨 변환, 문자열 `.upper()`, 딕셔너리 직원 급여 인상 `lambda emp: {'name': emp['name'], 'salary': emp['salary'] * 1.1}`, 학생 딕셔너리의 `student['score'] >= 70` 필터링. 대화에서는 주로 숫자 리스트로 검증했으므로 **딕셔너리 요소를 받는 람다**는 별도 복습 가치가 높다.

## 7. `reduce()`: 중간 결과는 버리는가?

**실제 오답 ①:** 곱셈 예제 `lambda x, y: x * y`를 덧셈으로 읽어 `9`라고 답함.

```python
from functools import reduce
numbers = [2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
# (2 * 3) * 4 = 24
```

**실제 오답 ②:** 최댓값 찾기에서 두 번째 비교를 `x=8, y=42`라고 설명함. 실제로는 `x=42, y=8`.

```python
numbers = [15, 42, 8, 30]
result = reduce(lambda x, y: x if x > y else y, numbers)
```

| 단계 | x (이전 결과) | y (다음 요소) | 새 결과 |
|---|---:|---:|---:|
| 1 | 15 | 42 | 42 |
| 2 | 42 | 8 | 42 |
| 3 | 42 | 30 | 42 |

**실제 오답 ③:** `[50, 10, 80, 20]` 예제에서 `50`과 `10`의 첫 비교를 건너뛰고 `50`과 `80`부터 설명함. 이후 두 번째 비교에서 `50, 80`, 세 번째에서 `80, 20`으로 진행한다는 것은 맞았음.

**표현 수정:** `reduce()`는 ‘중간 계산을 생략’하는 함수가 아니다. **중간 계산을 수행하고, 그 결과를 다음 단계에 넘기며, 마지막 누적 결과 하나를 반환**한다.

```python
numbers = [10, 2, 3]
reduce(lambda x, y: x - y, numbers)  # (10 - 2) - 3 = 5
```

이 뺄셈 문제는 각 단계 `10,2→8`, `8,3→5`를 정확히 답함.

> **교재 연결:** `reduce()`를 `functools`에서 import하고, 합계와 최댓값을 구하는 예제가 있다. 최댓값만 구할 때는 내장 함수 `max(numbers)`가 더 간단하지만, 교재에서는 누적 계산 구조를 배우기 위해 `reduce()`를 사용한다.

---

## 직접 풀어보는 재복습 문제

**정답을 보지 말고, 각 문제에서 ‘입력 → 함수의 계산 → 최종 자료형/출력’을 말로 설명해 보기.**

1. `a, b, c = 'DOG'`일 때 `a`, `b`, `c`는?
2. `first, *rest, last = [1, 2, 3, 4, 5]`에서 `rest`의 값과 자료형은?
3. `name, _, age = ('지수', '서울', 22)` 다음 `print(_)`는 무엇을 출력할까?
4. `try: int('abc')`에서 `ValueError`가 발생하면 같은 `try` 블록의 뒤쪽 코드는 실행될까? `finally`는?
5. `sorted([4, 1, 3], key=lambda x: -x)`의 결과는? 각 기준값은?
6. `sorted([4, 1, 3], key=lambda x: x + 100)`의 결과는? 왜 `[104, 101, 103]`이 아닌가?
7. `list(map(lambda x: x + 100, [4, 1, 3]))`의 결과는?
8. `list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4]))`의 결과는? `True/False` 리스트인가?
9. `list(map(lambda x: x ** 2, filter(lambda x: x > 2, [1, 2, 3, 4])))`의 결과는?
10. `reduce(lambda x, y: x - y, [20, 5, 3])`의 첫 단계와 두 번째 단계는?
11. `reduce(lambda x, y: x if x > y else y, [6, 2, 9, 4])`의 **두 번째 비교**에서 `x`, `y`는?
12. `employees = [{'name':'A','salary':100}, {'name':'B','salary':200}]`일 때 `list(map(lambda emp: emp['salary'] * 2, employees))`의 결과는? `emp`의 자료형은?

<details>
<summary>정답 및 간단 해설 (먼저 풀고 펼치기)</summary>

1. `'D'`, `'O'`, `'G'` — 문자열 한 글자씩.
2. `[2, 3, 4]`, `list` — `*`가 나머지 값을 리스트로 수집.
3. `'서울'` — `_`에도 값이 할당됨.
4. `try`의 나머지는 건너뛰고, 대응하는 `except`가 있다면 실행; `finally`는 예외 처리 종료 과정에서 실행.
5. `[4, 3, 1]` — 기준값 `-4`, `-1`, `-3`; 기준값 오름차순 `-4 < -3 < -1`.
6. `[1, 3, 4]` — `key`는 정렬 기준만 계산, 원래 요소 유지.
7. `[104, 101, 103]` — 변환한 값 자체를 제공.
8. `[1, 3]` — 참인 **원래 숫자**만 남음.
9. `[9, 16]` — 3,4만 선택 후 제곱.
10. `20-5=15`, `15-3=12` — 이전 결과가 다음 `x`.
11. `x=6`, `y=9` — 첫 비교 `6 vs 2`의 결과 6을 이어받음.
12. `[200, 400]`, `dict` — `emp`는 리스트 속 딕셔너리 한 개.

</details>

## 다음 복습 때 확인할 체크리스트

- [ ] 언패킹의 각 변수에 실제로 어떤 값이 들어가는지 순서대로 적었는가?
- [ ] `_`를 값이 없는 특수 문법으로 오해하지 않았는가?
- [ ] `try`에서 오류가 발생한 **바로 그 줄**과 건너뛰는 줄을 표시했는가?
- [ ] `lambda`는 함수를 **정의**하는지, 지금 **호출**하는지 구분했는가?
- [ ] `sorted()`의 `key` 결과와 최종 정렬 리스트를 구분했는가?
- [ ] `map()`(변환), `filter()`(선택), `reduce()`(누적)의 최종 결과를 구분했는가?
- [ ] `reduce()`에서 **첫 두 요소부터**, 연산자를 확인하고 `x/y`를 적었는가?
- [ ] 최종 자료형이 `list`, `tuple`, `dict`, 반복자, 숫자 중 무엇인지 확인했는가?

> **다음 학습 목표:** 숫자 리스트 예제를 넘어, 교재의 **딕셔너리 리스트**(`employees`, `osda_students`)를 대상으로 `lambda`, `map`, `filter`를 다시 해석해 보기.
