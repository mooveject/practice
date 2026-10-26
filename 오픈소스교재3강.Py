# 3.3.1 파일
#  1. CSV
import pandas as pd 

df = pd.read_csv ('오픈소스/학습자료/Chapter 3/data.csv', encoding = 'utf-8',sep=',', header =0,  # 폴더 계층 다 써주기
                  index_col=None, skiprows=None, nrows=None)
print (df)

# 2. JSON
import json 
import pandas as pd 
with open('오픈소스/학습자료/Chapter 3/data.json', 'r' , encoding ='utf-8' )as f :
    data = json.load (f)
print (data)
df = pd.read_json ('오픈소스/학습자료/Chapter 3/data.json',orient='records',encoding='utf-8',lines=False)
print (df)

#3 텍스트파일 
import re
with open ('오픈소스/학습자료/Chapter 3/callcenter20250301.log','r',encoding ='utf-8') as f :
    content = f.read()
pattern = re.compile (r'(\d{6})-(\d{7})') # \d{6} 숫자 6자리, \d{7} 숫자 7자리 라는 패턴 정의
masked_content = pattern.sub (r'\1-*******', content)
with open ('오픈소스/학습자료/Chapter 3/callcenter20250301.log','w',encoding = 'utf-8') as f :
    f.write (masked_content)
print ("주민등록번호 마스킹 완료. 'callcenter20250301_masked.log.txt' 파일로 저장되었습니다.")

#3.3.2 API
# 2) Requests 라이브러리
import requests
import json

url = 'https://api.open-meteo.com/v1/forecast?=&=&current=temperature_2m'
params={
    'latitude' : '37.58638333',
    'latitude' : '127.0203333',
    'current' : 'temperature_2m'
}

try :
    response = requests.get(url, params=params, timeout =5)
    response.raise_for_status()

    data = response.json()
    print ('API 응답 : ', data)
    print ('서울시 종로구의 현재 온도는 : {0}{1} 입니다.'
           .foramt (data['current']['temperature_2m'],data['current_units']['temperature_2m']))
except requests.exceptions.RequestException as e :
    print (f'API 호출 실패 : {e}')
except json.JSONDecodeError as e :
        print (f'JSON 파싱 실패 : {e}')

# 3.3.3 웹 스크래핑
# 3) 데이터 스크래핑 | 교재 p.121~122

# 3.4.1 파일
# 1) CSV
import pandas as pd
data = {
     'student_id' : [101,102,103,104,105],
     'database_score' : [85,76,92,63,88],
     'python_score' : [92,78,85,75,91]
}
df = pd.DataFrame(data)
df.to_csv('student_analysis.csv',encoding='utf-8',index=False)
print (df)

# 2) JSON
import json
import pandas as pd

data = {
    'Name' : 'cutie',
    'Age' : '900',
    'Favorite_food' : 'chocolate latte'
}

with open ('cuties_secret.json','w',encoding='utf-8') as f :
     json.dump(data, f,indent=4,ensure_ascii=False)

df = pd.DataFrame([data])
df.to_json('cuties_secret.json',orient ='records',indent=4, force_ascii = False)
print (df)

import json
import pandas as pd

data2 = {
    'Name' : ['cutie','sweetpotato'],
    'Age' : [900,1200],
    'Favorite_food' : ['chocolate latte','Matcha_latte']
}
# Json 라이브러리 방식
with open ('friends.json','w',encoding='utf-8') as f :
     json.dump(data2, f,indent=4,ensure_ascii=False)
#Pandas 라이브러리 방식
df = pd.DataFrame([data2])
df.to_json('friends.json',orient ='records',indent=4, force_ascii = False)
print (df)

