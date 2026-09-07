# 1강 
# Reserved Words 
# Sentences or Lines
x=2 #x에 2를 넣어라 = 할당한다
#프로그래밍 방법
    #Interactive 
    #Python Scripts 

# 1. Sequential steps 순차문
x=2
print (x)
x = x+2
print (x)

# 2. Conditional Steps 조건문
x=5
if x < 10 :
    print ('smaller')
if x > 20 :
    print ('Bigger')
print ('Finish')

# 3. Repeated Steps 반복문 (조건에 해당하는 동안 반복)
n=5
while n >0 :
    print (n)
    n= n-1
print ('Blastoff!') 

print ('Hello Wolrd')

#2강 : 변수, 표현식 및 코드
x=1+2*3-4 #3
print (x)
y=2**3 #8
print (y)
z=1+2**3/4*5 #11
print (z)

# Type 함수
eee ='hello' + 'there'
"eee = eee + 1 (1 > string type)"
eee = eee + "1"
xx = 1 #int 정수
type (xx)
temp=98.6 #float 소수 
print (type (temp))

# Type conversions
print (float(99)+100)
i=42
f=float (i)
print (f)
print (type (f))

# Integer Division
print (10/2)
print (9/2)
print (99/100)
print (10.0/2.0)
print (99.0/100.0)

# String Conversions
sval='123'
print (type(sval))
ival=int (sval)
print (type (ival))

# User input
name=input ('Who are you?') # input에 적은 값은 'string' type 으로 인식
print ('welcome', name) # , 띄어쓰기 한 칸 

# Mission : Converting User Input 
# 엘리베이터 층 변환
inp = input ('Europe floor?')
usf = int (inp)+1
print ('Us floor', usf)  

# 2강 실습
nzt = input('Enter your name : ')
print ("hello",nzt)

xh =input ("Enter Hours : ")
xr= input ("Enter Rate : ")
xp = float (xh) *float(xr)
print ("Pay :",xp)

print ('hello world' +'2018')



