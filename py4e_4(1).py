# 5강 : 루프와 반복문 
# Indefinite loops를 주의하기 
# While Loop 
"""n = 5

while n>0 :
    print (n)
    n=n+1
print ('Blastoff!')  
print (n)  """

'n은 양수이고 n+1 동안 실행됨 > 무한실행 상태'

# How to control Loop : break, continue (특정 조건에서 종료되는 루프)

# 1. Break : 해당 루프 실행 종료 > while문 탈출, 다음 코드 실행
while True :
    line = input ('>')
    if line == 'Done' :
        break 
    print (line)
print ('Done!')

# 2. continue : 해당 루프 실행 종료 > 루프 시작 지점부터 다시 루프 실행 
# (= 출발지로 돌아가 루프 재실행)
while True :
    line = input ('>')
    if line [0]=='#' :
        continue
    if line == "Done" :
        break
    print (line)
print ('Done!')

"""break는 루프를 종료하고 나오기 때문에 무한루프에 빠질 가능성이 낮지만,
continue는 조건 및 변수의 업데이트 없이 설계해두면 무한루프에 빠질 수 있어 주의해야함."""

# Definite Loops : 유한 루프 생성하기
# For Loop : 변수 i에 리스트 값을 순서대로 넣고 실행(리스트 = 범위 설정)
for i in [5,4,3,2,1] :
    print (i)
print ('Blastoff!')

friends=['Joseph','Glenn','Sally']
for friend in friends :
    print ('Happy New Year : ', friend)
print ('Done!')

'Q.while과 for을 언제 사용해야 하는가.'