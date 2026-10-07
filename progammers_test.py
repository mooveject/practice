# 1
def solution (num1, num2) :
    answer = float (num1)- float (num2)
    return answer

a = input ()
b = input ()
print (solution (a,b))

# 2
def solution(num1, num2):
    answer = num1 * num2
    return answer
a = float (input())
b = float (input())
print (solution (a,b))

# 2 다른 사람 답
def solution(num1, num2):
    answer = 0
    while i < num2:
        answer += num1
        i += 1
    return answer
"answer 0 , 변수 i < num2 보다 항상 작으면 실행"
"answer += num1 > "
"i +=1 > 변수 i는 1씩 증가"

# 3 
def solution(num1, num2):
    answer = num1 // num2
    return answer
# 3 다른 사람 풀이 
def solution(num1, num2):
    answer = num1 / num2
    return int(answer)

# 4 
def solution(num1, num2):
    answer = num1/num2*1000
    return int (answer)

# 4 다른 사람 풀이
def solution(num1, num2):
    answer = (num1/num2)*1000
    return answer//1

# 5
def solution(num1, num2):
    if num1 == num2 :
        answer = 1
    elif num1 !=num2 :
        answer = -1
    return answer

# 5 다른 사람 풀이
def solution(num1, num2):
    return 1 if num1==num2 else -1