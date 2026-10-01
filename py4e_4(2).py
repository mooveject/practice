# 1. 반복문
# (1) Finding the largest value
largest_so_far = -1
print ('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print (largest_so_far, the_num)
print ('After', largest_so_far)



# 2. 반복문 응용
# (1) Counting in a loop 
zork = 0
print ('Before', zork)
for thing in [9,41,12,3,74,15] :
    zork = zork +1
    print (zork, thing )
print ('After',zork)

 # (2) Summing in a loop
zork = 0
print ('Before', zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + thing 
    print (zork, thing )
print ('After',zork)

# (3) Finding the Average in a loop
count = 0
sum  = 0
print ('Before', count , sum)
for value in [9,41,12,3,74,15] :
    count = count +1
    sum = sum + value
    print (count, sum,value)
print ('After', count , sum, sum/count)

# (4) Filtering in a loop
print ('Before')
for value in  [9,41,12,3,74,15] :
    if value > 20 :
        print ('Large number', value)
print ('After')

# 스스로 응용
print ('Before')
for value in  [9,41,12,3,74,15] :
    if value > 20 : # if 라는 조건을 for 안에 추가해서 필터링
        print ('Large number', value)
    elif value < 20 :
        print ('Small number', value)
    elif value == 20 :
        print ('Same number',value)
print ('After')

# (5) Search Using a Boolean Variable : 
found = False
print ('Before',found)
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found ==True 
    print (found, value)
print ('After', found)

# (6) Finding the smalles t value : None을 사용 
# 부울 변수 사용. 부울 변수는 True / False 의 값을 가짐
smallest_so_far = 100
print ('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print (smallest_so_far, the_num)
print ('After', smallest_so_far)
# None = 상수 
smallest= None 
print ('Before')
for value in  [9,41,12,3,74,15] :
   if smallest is None : #처음 9가 value에 들어갈 때, #is도 연산자 a==b 보다 강함 
       smallest = value
   elif value < smallest : # 두번째부턴 elif로 계속 감 
        smallest = value
   print (smallest, value)
print ('After', smallest)

# (7) The "is" and "is not" Operators
0 == 0.0 # True
0 is 0.0 # False
