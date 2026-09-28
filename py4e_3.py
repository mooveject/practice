# 3강 복습 퀴즈
astr = 'bob '
try :
    print ('Hello')
    istr =int (astr)
    print ('there')
except :
    istr = -1
print('Done',istr)

hours=input ("Enter Hours : ")
    
rate = input ("Enter Rate : ")
try : 
    fh = int(hours)
    fr = int (rate)
    xp = fh * fr
    print ("Your Pay is ", xp)
except :
    print ("Error, please Enter numeric number.")
    
# 4강 : Python Functions 함수
# Built in  Functions 내장 함수
big =max("Hello world")
print (big) 
tiny = min ("Hello world")
print (tiny)

sval = '123'
print (type (sval))
ival = int (sval)
print (ival + 1)

nsv = "Hellow bob"
try : 
    niv = int (nsv)
except :
    niv = -1
    print (niv)

# Building our Own Functions 사용자 지정 함수
x=5
print ('Hello')

def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ("I sleep all night and I work all day.")
"함수 정의 = 획득, 함수 호출 시 실행됨"
print ("Yo")
print_lyrics()
x= x+2
print (x,"days")

 # parameters 매개 변수

def greet (lang) :
    if lang == 'es' :
        print ("Hola")
    elif lang == 'fr':
        print ('Bonjuor')
    else :
        print ("Hello")

greet('en')
greet('es')
greet('fr')

# Return Values 반환문
def greet (lang) :
    if lang == "es" :
        return ("Hola")
    elif lang == 'fr':
        return ('Bonjuor')
    else :
        return ("Hello")
print (greet('fr'),'Glenn')

def gre (lang) :
    if lang == "en" :
        print ("Hi")
    else :
        print ("hola")
print (gre('es'))
# Claude : 

# 월급 계산 프로그램을 다시 프로그램하기
# 40시간 초과 근무 시간 시급 1.5배 지급
" 우선 강의 없이 혼자 작성해보기 "
def computepay (hours, rate) :
    if fh > 40 :
        reg = fh * fr 
        otp = (fh - 40) * (fr*0.5)
        xp = reg + otp 
        return (xp)
    else :
        xp = fh *fr
        return (xp)
    
sh = input ("Enter your hours : ")
sr = input ("Enter your rate : ")
fh = float (sh)
fr = float (sr)   
print ("Pay : ", computepay(fh,fr))

# ============================================
# 함수: print vs return
# Q. 함수 안에서 return을 해야 함수 밖에서 return 값을 쓸수 있다는 거지? print 하면 결과 반환이 아니라 말그대로 출력이라 함수밖에서는 반환값 (즉 저장값)이 없으니까 none 으로 뜨고?
# ============================================
# - return : 값을 함수 밖으로 "돌려줌" (프로그램용, 손에 쥐여주기)
#            → 변수에 저장하거나 계산에 쓸 수 있음
# - print  : 화면에 "보여주기만" 함 (화면용, 눈에 보여주기)
#            → 값이 함수 밖으로 나오지 않음
# - return이 없는 함수는 끝날 때 자동으로 None을 돌려줌
#   (None = "돌려준 값이 없다"는 정식 값, 에러가 아님)


def add_print(a, b):
    print(a + b)
    # 보이지 않는 return None이 자동으로 붙어 있음


def add_return(a, b):
    return a + b


# print 버전: 화면에 8이 뜨지만, x에는 None이 저장됨
x = add_print(3, 5)   # 출력: 8
print(x)              # 출력: None

# return 버전: 화면엔 안 뜨지만, y에는 8이 저장됨
y = add_return(3, 5)
print(y)              # 출력: 8
print(y * 2)          # 출력: 16 (반환값은 계산에 재사용 가능)

# 안쪽 print가 8을 출력하고, 바깥 print가 반환값 None을 출력함
print(add_print(3, 5))  # 출력: 8 다음 줄에 None