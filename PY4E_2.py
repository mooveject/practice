# 3강 Conditional Steps 조건부 실행
" Point : 블럭 단위로 생각하기 "
x=5
if x < 10 :
    print ('Smallar')
if x > 20 :
    print ('Bigger')
print ('Finish!')

# Comparison Operators 비교 연산자
'< , <= , == equal  , >= , > , != not  equal'

x=5
if x ==5 :
    print ('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >=5 :
    print ('Great3r than or Equals 5')
if x < 6 : 
    print ('Less than 6')
if x <= 5 :
    print ('Less than or E quals 5')
if x != 6 :
    print ('Not equal')

# Indentaion : Think about Begin / End blocks
' 4 spaces '
' 탭 사용 지양 > 탭이 4번 스페이스로 설정되어 있지 않으면 에러 원인'
' increae / maintain : after if or for'
' decrease / to indicate end of block'
# Nested Decisions 중첩된 들여쓰기
'4 space 블럭 단위로 구분하기 like 마트료시카 인형처럼'
# Two - way Decisions : 둘 중에 한 갈래만 실행
'if (True일 때 실행) / else (False일 때 실행)'


# Multi - way  
x = 20
if x < 2 :
    print ('small')
elif x < 10 :
    print ('medium')
else :
    print ('large')
print ('All done') 

# No else 'else'는 필수가 아니다.
x=50
if x < 2 :
    print ('small')
elif x < 10 :
    print ('medium')
print ('All done')

# The try / except Structure   
'except 블록은 잘못된 입렵값 / 잘못됐을 때만 실행'
astr = 'Hello Bob'
try : 
    istr = int (astr)
except :
    istr = -1
print ('First', istr)

astr = '123'
try :
    istr =int (astr)
except : 
    istr = -1
print ('Second',istr)

# Sample try / except 
rawstr = input ('Enter a number :')
try:
    ival = int (rawstr)
except :
    ival = -1

if ival > 0 :
    print ('Nice work')
else :
    print ('Not a number')

# 03_01 quiz : 급여 계산
sh = input ("Enter Hours : ")
sr = input ("Enter Rate : ")
fh = float (sh)
fr = float (sr)
# print (fh, fr)
if fh > 40 :
   # print ("Overtime")
    reg = fr * fh 
    otp = (fh - 40) * (fr * 0.5)  
    # 초과근무 수당 : (총 근무 시간 - 40) * (시급 *0.5)
    # 최종 급여 : reg + otp(초과 근무 시간 * 시급 1/2 만큼 추가 부여)
    #print (reg, otp)
    xp = reg + otp 
else :
   # print ("Regular")
    xp = fh * fr 
print ("Pay :",xp)

# 03_02 quiz : 급여 계산 try, except 활용
sh = input ("Enter Hours :")
sr = input ("Enter Rates :")
try :
    fh = float (sh)
    fr = float (sr)
except :
    print ("Error, pleas enter numeric input")
    quit ()
print (fh *fr)
if fh > 40 :
    reg = fh * fr
    otp = (fh-40)*(fr*0.5)
    xp = reg + otp
else : 
    xp = fh * fr
print ("Pay :", xp)