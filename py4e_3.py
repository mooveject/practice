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
