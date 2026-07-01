# 6장 : 제어문
# 6.1 조건문 
    # if 조건 1 : 실행할 명령 1
    # elif 조건 2  :실행할 명령 2
weather="맑음" 
if weather =="비" :
    print("우산을 챙기세요.")
elif weather =="미세먼지" :
    print("마스크를 챙기세요.") # 둘다 아니면 아무것도 출력 X, 조건이 더 있다면 elif 추가, ! : (콜론 붙이기)
else :
    print ("준비물이 필요없어요") # else문 : 나열된 조건에 모두 해당되지 않을 때 실행 

# input() 함수 ! 사용자가 입력하는 값은 항상 str(문자열) 형식으로 인식됨
weather = input("오늘 날씨는 어때요? ")

if weather =="비" or weather =="눈" : # 조건 변경 : 눈 추가 # 3.1 조건 연산자 or (하나라도 참이면 참)
    print ("우산을 챙기세요.")
elif weather == "미세먼지" :
    print ("마스크를 챙기세요.")
else :
    print ("준비물이 필요없어요.")

# input에 기온 (정수 넣기) -> 형 변환
temp =int(input("오늘 기온이 어때요? "))

if 30 <=temp: 
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp and temp < 30: # 10 <= temp < 30
    print("활동하기 좋은 날씨에요.")
elif 0 <= temp and temp <10: # 0 <= temp < 10
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

temp =int(input("오늘 기온이 어때요? "))

if temp>=30 :
    print("너무 더워요. 외출을 자제하세요.")
elif temp>=10 : # 30 미만 10 이상
    print("활동하기 좋은 날씨에요.")
elif temp >=0 : # 10미만 0 이상
    print("외투를 챙기세요.")
else: # 0 미만
    print("너무 추워요. 나가지 마세요.")

# 문제 풀이 
tem = 40 #체온
if tem >=39:
    print ("고열입니다.")
elif tem>=38:
    print ("미열입니다")
else :
    print("정상입니다.")
