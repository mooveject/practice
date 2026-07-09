# 7장 : 함수 Function(x입력값)=y(전달값)
# 내장 함수 | 사용자 정의 함수 : def 함수명 () : 실행할 문장 

def open_account():
    print ("새로운 계좌를 개설합니다.") #여기까지가 함수 정의. 홤수를 사용해야 함수가 작동함 
    # 대체로 변수는 명사, 함수는 동사로 이름 짓는다
open_account() # 함수 호출

# 7.2 전달값과 반환값
# 실습 : 입금하기
def open_account():
    print ("새로운 계좌를 개설합니다.")
open_account()

def deposit(balance, money): # 전달값을 받는 변수 = 매개변수 parameter
    print ("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance+money))
    return balance+money

balance=0
balance=deposit(balance,1000)

# with claude 
# Q. def (balance)의 balance는 함수 안에서만 작동하는 , 통로 같은 역할인거고 실제로 값이 계속 저장되고 업데이트 되는 곳은 함수 밖에 있는 balance?
# 밖의 balance(저장소, 예: 0) → 함수 호출하며 값을 복사해서 통로로 전달 → 함수 안에서 계산(0+1000) → return으로 결과(1000)를 밖으로 다시 던짐 → 밖의 balance = 그 결과를 받아서 재저장(1000)
# 그래서 만약 balance = deposit(balance, 1000)에서 앞의 balance =를 빼먹으면, 함수는 계산은 하지만 그 결과가 밖으로 저장이 안 돼서 잔액이 그대로 0으로 남아있는 흔한 버그가 생겨. 실무에서도 "함수 호출만 하고 반환값을 안 받아서 값이 안 바뀌는" 실수가 정말 자주 나오는 포인트야.

# 실습 : 출금하기
def open_account() :
    print ("새로운 계좌를 개설합니다.")
open_account()
def deposit (balance, money):
    print ("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money,balance+money))
    return balance+money

def withdraw (balance, money):
    if balance >=money :
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money,balance-money))
        return balance -money
    else :
        print ("잔액이 부족합니다.잔액은 {0}원입니다.".format(balance))
        return balance
balance = 0
balance = deposit(balance, 1000)

#출금
balance = withdraw (balance, 2000)
balance =withdraw (balance, 500)

# 실습 : 수수료 부과하기
def open_account() :
    print ("새로운 계좌를 개설합니다.")
open_account()
def deposit (balance, money):
    print ("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money,balance+money)) # 1000원 입금, 잔액 1000원
    return balance+money # 0+1000=1000원 반환

def withdraw_night (balance, money) :
    commission=100 # 은행 미운영 시간 수수료 100원
    print ("업무 시간 외에 {}원을 출금헀습니다.".format(money)) # 500원 출금
    return commission, balance-money-commission #수수료 100원, 1000-500-100=400원

balance=0 #초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금

# 업무 시간 외 출금 시도
commission , balance = withdraw_night (balance, 500) # 수수료 100원, 잔액 = 시간 외 출금 (1000-500) 
print ("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance)) # 수수료 100원, 1000-500-100=400원

"""def withdraw_night(balance, money): 를 보면 괄호 안에 정의된 매개변수는 딱 두 개, balance와 money뿐이야. commission은 저 괄호 안에 없어. 대신 함수 본문 첫 줄에서 commission = 100이라고 함수 안에서 새로 만들어낸 값이야.
매개변수 vs 지역 변수 차이
매개변수(balance, money)는 함수 밖에서 값을 받아와야만 채워지는 빈 칸이야. 반면 commission = 100은 함수가 실행되는 그 순간에 함수 안에서 직접 만들어낸 값이지, 밖에서 받아온 게 아니야.
비유: 라면 끓이는 함수를 생각해봐. def cook_ramen(water, noodle): 처럼 물이랑 면은 밖에서 받아와야(매개변수) 하는데, 스프는 이미 봉지 안에 들어있어서(코드 안에 commission=100처럼 이미 정해져 있어서) 따로 안 받아와도 돼. 스프는 요리 과정에서 "당연히 쓰는 고정값"이라 매개변수로 넣을 필요가 없는 거야.
즉 수수료 100원은 "이 함수를 쓸 때마다 항상 똑같이 적용되는 고정 규칙"이라서, 굳이 밖에서 값을 받아올 필요 없이 함수 안에서 바로 100이라고 박아둔 거야. 만약 수수료가 상황마다 달라질 수 있다면 그때는 def withdraw_night(balance, money, commission): 처럼 매개변수로 빼서 받아야겠지.
return 부분도 같이 이해하면 좋아
return commission, balance-money-commission처럼 두 개 값을 콤마로 같이 반환하면 파이썬은 이걸 튜플로 묶어서 돌려줘. 그래서 밖에서 commission, balance = withdraw_night(balance, 500)처럼 두 변수로 나눠 받을 수 있는 거야. 이때 commission은 함수 안에서 만든 지역 변수였지만, return을 통해 함수 밖으로 나오면서 밖에 있는 새로운 commission 변수에 저장되는 거지.
실무 팁: 이렇게 "함수 안에서 고정된 상수값을 미리 박아두는 것"은 나쁜 습관은 아니지만, 실무에서는 나중에 이 수수료가 은행 정책 변경으로 바뀔 수도 있으니 보통 함수 밖에 NIGHT_COMMISSION = 100 같은 상수로 따로 빼두는 걸 선호해. 매개변수로 만들지, 함수 안에 고정할지, 아예 전역 상수로 뺄지 판단하는 게 코드 설계 감각이고, 이건 실무에서 "이 값이 나중에 바뀔 가능성이 있는가?"를 기준으로 결정하면 돼."""

#7.3 함수 호출하기
def profile (name, age, main_lang):
    print ("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format (name,age,main_lang))

profile ("찰리",20,"파이썬")
profile ("루시",25, "자바")

def profile (name, age=20, main_lang="파이썬") : #age, main_lang을 매개변수에 미리 지정해둔 "기본값"
    print ("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age,main_lang)) #\t 탈출 문자

profile("찰리")
profile("루시")
profile("톰",22)
profile("제임스",24,"자바")

#전달값 작성 순서
def buy (item1, item2="음료수"): # 일반 전달값 (item1) 먼저 작성 후 기본값이 있는 전달값 쓰기
    print (item1, item2)
buy ("빵") # 빵, 음료수

# 키워드 인자 (keyword argument) : 어디에 어떤 값을 전달할지 명시적으로 지정
# 위치 인자 (postional argument) = 일반 전달값
def profile (name, age, main_lang):
    print (name, age, main_lang)
profile ("찰리", age=20, main_lang="파이썬") # 일반 전달값(=위치 인자)을 먼저 작성, 키워드 인자 값은 후에 작성
profile ("찰리", main_lang="파이썬", age=20) # 위 식과 똑같은 값이 출력됨

# 가변 인자 (variable argument) : 개수가 변할 수 있는 인자 = *전달값1 "*" 붙이기
# 가변 인자 : 전달값의 개수와 상관없이 튜플로 인식

def profile (name, age, lang1,lang2, lang3, lang4,lang5):
# 줄 바꿈 대신 띄어쓰기 매개변수 end 사용 | print()함수는 end 기본값이 \n (줄바꿈) > end의 매개변수를 바꾸기

    print ("이름 : {0}\t나이 : {1}\t".format(name,age),end="")
    print (lang1, lang2,lang3,lang4,lang5)

profile ("찰리",20, "파이썬", "자바","C","C++","C#")
profile ("루시", 25,"코틀린","스위프트","","","")

def profile (name, age,*language) : # 가변 인자
    print ("이름 : {0}\t나이:{1}\t".format(name, age,end=" "))
    print(language, type(language))

profile ("찰리",20, "파이썬", "자바","C","C++","C#","자바스크립트")
profile ("루시", 25,"코틀린","스위프트","","","")

def profile (name, age,*language) :
    print ("이름 : {0}\t나이:{1}\t".format(name, age,end=" "))
    for lang in language :
        print (lang, end=" ") #언어를 모두 한 줄에 표시
    print ()

profile ("찰리",20, "파이썬", "자바","C","C++","C#","자바스크립트")
profile ("루시", 25,"코틀린","스위프트")