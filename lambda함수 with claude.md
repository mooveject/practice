# Python 학습 노트 — 딕셔너리 리스트 · map · filter · lambda

> 2026-10-09
> 핵심 주제: list of dicts 구조 이해, `map` / `filter`와 `lambda`의 매개변수

---

## 목차

1. [데이터 구조: 딕셔너리가 담긴 리스트](#1-데이터-구조-딕셔너리가-담긴-리스트)
2. [map + lambda: 급여 인상](#2-map--lambda-급여-인상)
3. [lambda 매개변수는 왜 하나인가](#3-lambda-매개변수는-왜-하나인가)
4. [filter + lambda: 합격자 거르기](#4-filter--lambda-합격자-거르기)
5. [헷갈렸던 지점 요약](#5-헷갈렸던-지점-요약)
6. [확장: 실무와 다른 언어](#6-확장-실무와-다른-언어)

---

## 1. 데이터 구조: 딕셔너리가 담긴 리스트

```python
employees = [
    {'name': '김지원', 'salary': 370},
    {'name': '박민준', 'salary': 700},
    {'name': '이서윤', 'salary': 440}
]
```

### 헷갈렸던 지점

> `employees`는 key:value가 두 개씩인 구조인가,
> 아니면 `name = [김지원, 박민준, 이서윤]` 형태인가?

### 정리

- **key:value 2개짜리 딕셔너리 3개가 들어 있는 리스트**이다. (list of dicts)
- `'name'` key는 하나가 아니라 **딕셔너리마다 하나씩, 총 3번** 존재한다.
- 한 사람의 정보(이름과 급여)가 **한 딕셔너리에 묶여 있다.**

비유하면 `employees`는 카드지갑이고, 각 딕셔너리는 사원증 한 장이다.

```python
employees[0]            # {'name': '김지원', 'salary': 370}  ← 몇 번째 카드 (인덱스)
employees[0]['name']    # '김지원'                            ← 카드의 어느 칸 (key)
```

### 비교: 내가 떠올렸던 구조 (dict of lists)

```python
employees2 = {
    'name':   ['김지원', '박민준', '이서윤'],
    'salary': [370, 700, 440]
}
```

| 구분 | list of dicts (실제 코드) | dict of lists (비교용) |
|---|---|---|
| 묶는 기준 | 사람 단위 (행) | 항목 단위 (열) |
| 김지원의 이름 | `employees[0]['name']` | `employees2['name'][0]` |
| 장점 | 한 사람의 정보가 흩어지지 않음 | 한 항목 전체를 한 번에 꺼내기 쉬움 |

list of dicts에서 이름만 모으려면 반복문으로 한 장씩 넘긴다.

```python
names = [e['name'] for e in employees]   # ['김지원', '박민준', '이서윤']
```

---

## 2. map + lambda: 급여 인상

```python
updated_employees = list(map(
    lambda emp: {'name': emp['name'], 'salary': emp['salary'] * 1.1},
    employees
))

print('\n 급여 인상 후 :')
for emp in updated_employees:
    print(f"{emp['name']} : {int(emp['salary']):,}원")

print(employees)
```

### 실행 결과

```
 급여 인상 후 :
김지원 : 407원
박민준 : 770원
이서윤 : 484원
[{'name': '김지원', 'salary': 370}, {'name': '박민준', 'salary': 700}, {'name': '이서윤', 'salary': 440}]
```

### 구조

```python
map(규칙, 재료)
map(lambda emp: {...}, employees)
```

- `map` : 컨베이어 벨트. 재료를 하나씩 꺼내 규칙에 넣는다.
- `lambda` : 규칙(작업 지시서). 매번 **새 딕셔너리 한 개**를 반환한다.
- `list()` : `map`은 결과를 미리 만들지 않는 map object를 돌려준다. `list()`로 감싸야 실제 결과가 리스트로 담긴다.

### 주목할 점

1. **원본은 바뀌지 않는다.**
   lambda가 기존 딕셔너리를 수정하지 않고 새 딕셔너리를 만들었기 때문에 `print(employees)`는 원래 값을 출력한다.
   반면 `emp['salary'] *= 1.1`처럼 쓰면 원본이 직접 바뀐다.

2. **부동소수점 오차**
   `370 * 1.1`은 `407.00000000000006`이 된다. `int()`는 소수점을 버리므로 값이 `406.999...`로 계산되면 406이 된다.
   금액 계산에는 반올림을 사용하는 편이 안전하다.

   ```python
   int(round(emp['salary']))
   ```

---

## 3. lambda 매개변수는 왜 하나인가

### 헷갈렸던 지점

> `def 함수(a, b)`는 매개변수 2개로 name과 salary를 따로 받는다.
> 그런데 `lambda emp`는 매개변수 하나로 `emp['name']`, `emp['salary']` 두 정보를 꺼낸다. 왜 그런가?

### 정리

- 이것은 **lambda와 def의 차이가 아니다.**
- 매개변수 개수는 **정보의 개수가 아니라, 한 번 호출될 때 건네받는 덩어리의 개수**로 정해진다.
- `map`은 lambda를 호출할 때마다 **딕셔너리 한 개**를 건넨다. 따라서 받는 매개변수도 하나이다.

비유하면 택배 상자 하나에 책과 과자가 함께 들어 있는 상황이다. 상자는 한 손으로 받고, 받은 뒤에 열어서 내용물을 꺼낸다.

| 코드 | 의미 |
|---|---|
| `emp` | 받은 상자 (딕셔너리 한 개) |
| `emp['name']` | 상자를 열어 이름을 꺼냄 |
| `emp['salary']` | 상자를 열어 급여를 꺼냄 |

### def로 바꿔도 매개변수는 하나

```python
def raise_salary(emp):
    return {'name': emp['name'], 'salary': emp['salary'] * 1.1}

updated = list(map(raise_salary, employees))
```

### 매개변수가 2개인 경우와의 차이: 누가 상자를 여는가

```python
def raise_salary2(name, salary):
    return {'name': name, 'salary': salary * 1.1}

raise_salary2('김지원', 370)                                   # OK
raise_salary2(employees[0])                                     # 에러: salary 인자 누락
raise_salary2(employees[0]['name'], employees[0]['salary'])     # OK
```

- 매개변수 1개 : 함수 **안에서** 상자를 연다.
- 매개변수 2개 : 함수 **밖(호출하는 쪽)에서** 상자를 열어 따로 넘긴다.

### lambda도 매개변수 2개가 가능한 경우

재료를 두 줄로 따로 주면 `map`이 매번 두 개를 꺼내 건넨다.

```python
names = ['김지원', '박민준', '이서윤']
salaries = [370, 700, 440]

updated = list(map(lambda name, salary: {'name': name, 'salary': salary * 1.1},
                   names, salaries))
```

| 데이터 구조 | map이 한 번에 건네는 것 | 매개변수 |
|---|---|---|
| list of dicts | 딕셔너리 1개 | `lambda emp` |
| 리스트 2개 | 이름 1개 + 급여 1개 | `lambda name, salary` |

---

## 4. filter + lambda: 합격자 거르기

```python
osda_students = [
    {'name': 'kim',    'score': 85},
    {'name': 'lee',    'score': 65},
    {'name': 'park',   'score': 90},
    {'name': 'jeoung', 'score': 55},
    {'name': 'choe',   'score': 78}
]

passed_s = list(filter(lambda student: student['score'] >= 70, osda_students))
```

### 헷갈렸던 지점

> 처음 해석: `{key = score : value = [85, 65, 90, 55, 78]} >= 70`
> 그리고 `['score']` 앞에 왜 `student`를 붙여야 하는지 와닿지 않음.

### 정리

- `score`에 점수 5개가 묶여 있는 것이 아니다. **학생 딕셔너리마다 score가 하나씩** 있다.
- 따라서 `'score'`만으로는 "누구의 점수인지"가 정해지지 않는다.
- `student`는 **지금 이 순간 검사 중인 학생 딕셔너리**를 가리키는 이름이다.

| 코드 | 의미 |
|---|---|
| `student` | 지금 부른 학생 한 명 |
| `['score']` | 그 학생의 어느 칸을 읽을지 |
| `student['score']` | 지금 부른 학생의 점수 (숫자 하나) |

### filter의 실제 동작: 학생 수만큼 lambda를 호출

| 호출 | student에 들어온 값 | `student['score']` | `>= 70` | 결과 |
|---|---|---|---|---|
| 1 | `{'name': 'kim', 'score': 85}` | 85 | True | 통과 |
| 2 | `{'name': 'lee', 'score': 65}` | 65 | False | 제외 |
| 3 | `{'name': 'park', 'score': 90}` | 90 | True | 통과 |
| 4 | `{'name': 'jeoung', 'score': 55}` | 55 | False | 제외 |
| 5 | `{'name': 'choe', 'score': 78}` | 78 | True | 통과 |

같은 `student['score']`라는 코드가 호출될 때마다 다른 값을 가리킨다. 이름은 하나이고, 가리키는 대상이 매번 바뀐다.

### for문으로 풀어 쓰면

```python
passed_s = []
for student in osda_students:
    if student['score'] >= 70:
        passed_s.append(student)
```

lambda의 `student`는 이 for문의 `student`와 같은 역할이다. lambda는 for문 안의 **조건 부분만 떼어 함수로 만든 것**으로 볼 수 있다.

### 매개변수 이름은 자유

```python
filter(lambda x: x['score'] >= 70, osda_students)        # 동작 동일
filter(lambda x: student['score'] >= 70, osda_students)  # 에러: student가 정의되지 않음
```

`lambda x`는 "받은 값을 x라고 부르겠다"는 선언이므로, 콜론 뒤에서도 같은 이름을 써야 한다.

### 수정한 해석

```python
# 매개변수 student : osda_students에서 꺼낸 딕셔너리 한 개 (학생 한 명)
# student['score'] : 그 학생의 점수 (숫자 하나)
# filter가 학생 5명을 차례로 검사하고, 조건이 True인 학생만 남긴다
# list()로 담은 결과 → kim, park, choe
```

---

## 5. 헷갈렸던 지점 요약

| 헷갈린 내용 | 바로잡은 내용 |
|---|---|
| `name`에 이름 3개가 리스트로 묶여 있다 | 딕셔너리 3개가 각자 `name`을 하나씩 가진다 |
| lambda는 k:v를 반환한다 | lambda는 **딕셔너리 한 개를 통째로** 반환한다 |
| `list()`의 역할이 불분명 | `map`/`filter`의 결과(이터레이터)를 실제 리스트로 만든다 |
| 정보가 2개면 매개변수도 2개여야 한다 | 매개변수 개수는 **건네받는 덩어리 개수**로 정해진다 |
| `score`에 점수 5개가 묶여 있다 | 학생마다 score가 하나씩 있다 |
| `['score']` 앞의 `student`가 왜 필요한가 | "누구의" 점수인지 지정해야 값이 하나로 정해진다 |

### 한 줄 요약

> `map`과 `filter`는 리스트에서 **항목을 하나씩 꺼내** lambda에 넣는다.
> lambda의 매개변수는 **그 항목 하나**를 받는 이름이고, 항목이 딕셔너리라면 `이름['key']`로 안의 값을 꺼낸다.

---

## 6. 확장: 실무와 다른 언어

### 리스트 컴프리헨션 (실무에서 더 자주 쓰는 형태)

```python
updated  = [{'name': e['name'], 'salary': e['salary'] * 1.1} for e in employees]
updated  = [{**e, 'salary': e['salary'] * 1.1} for e in employees]   # 기존 값 복사 후 덮어쓰기
passed_s = [s for s in osda_students if s['score'] >= 70]
```

### 딕셔너리를 매개변수로 풀어 넘기기

```python
raise_salary2(**employees[0])   # name='김지원', salary=370 으로 자동 분배
```

### JavaScript 대응

```javascript
employees.map(emp => ({...emp, salary: emp.salary * 1.1}))
employees.map(({name, salary}) => ({name, salary: salary * 1.1}))   // 구조 분해
students.filter(student => student.score >= 70)
```

JavaScript의 `map`/`filter`는 바로 배열을 반환하므로 `list()` 같은 변환이 필요 없다.

### 연관 개념

- **JSON** : 웹 API 응답의 대부분이 list of dicts 형태이다.
- **데이터베이스** : 딕셔너리 하나는 표의 한 행, key는 열 이름에 해당한다. `filter`는 SQL의 `WHERE score >= 70`과 같은 역할이다.
- **pandas** : `pd.DataFrame(employees)`로 표를 만들고, `df[df['score'] >= 70]`으로 필터링한다.
- **불변성** : 원본을 수정하지 않고 새 값을 만드는 방식은 React 등 프론트엔드에서 핵심 원칙이다.

### 다음에 해볼 것

```python
sorted(employees, key=lambda e: e['salary'])   # 급여순 정렬
```
