# 6.2 반복문
# for문 : 범위 안에서 반복하기 : for 변수 in 반복 대상 : 실행할 명령 1,2... (반복 대상 값을 하나씩 변수로 가져와 for문에 사용)
for waiting in [1,2,3,4,5] :
    print("대기번호 : {0}".format(waiting))

for waiting in range(5):
    print("대기번호 : {0}".format(waiting))

for waiting in range(1,6): # 1부터 6 직전까지
    print("대기번호 : {0}".format(waiting))
for waiting in range(1,6,2): # 1부터 6 직전까지 2씩 간격 주기
    print("대기번호 : {0}".format(waiting))

orders=["아이언맨","토르","스파이더맨"] #손님 닉네임 리스트
for customer in orders :
    print ("{0}님, 커피가 준비됐습니다. 픽업대로 와주세요.".format(customer))

# while문: 조건을 만족할 동안 반복  : while 조건 : 실행할 명령 1

customer ="토르"
index = 5

while index >= 1 :
    print("{}님, 커피가 준비됐습니다.".format(customer))
    index -= 1
    print ("{}번 남았어요.".format(index))
    if index == 0:
        print ("커피를 폐기 처분합니다.")

"""
customer = "아이언맨"
index=1
while True :
    print ("{0}님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index +=1
# 무한 루프 (infinite loop) - ctrl + c (강제종료)
"""
customer = "토르"
person = None
while person != customer :
    print ("{0}님, 커피가 준비됐습니다.".format(customer))
    person = input ("이름이 어떻게 되세요? ") #토르 라고 답할 때까지 input 반복

# continue와 break : 흐름 제어하기

# 1~10번 학생이 한 문단씩 읽는 상황. 2,5번은 결석.
absent = [2,5]
no_book = [7]

for student in range (1,11) : #1부터 11 직전
    if student in absent :
        continue # 다음 학생으로 넘어가기 | 반복문 안에 continue = 명령 실행 중단 후 다음 반복 대상으로 넘어가서 실행
    elif student in no_book: # 책 안 가져온 학생 있으면 수업 즉시 종료
        print ("오늘 수업을 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break # 반복문 탈출 (=종료)
    print("{0}번 학생, 책을 읽어보세요.".format(student))

# with claude : 만약 바깥까지 한 번에 탈출하려면:
for i in range(3): # 바깥쪽 반복문

    for j in range(3): # 안쪽 반복문
        if j == 1:
            break #안쪽 반복문 종료
    else:
        continue
    break  # 바깥쪽 반복문 for도 탈출
# 지금 네 코드는 반복문이 하나뿐이라 신경 안 써도 되는데, 나중에 for 안에 for 중첩할 때 중요해지는 개념이야.
