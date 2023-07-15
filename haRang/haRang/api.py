import requests, json
from bs4 import BeautifulSoup as bs

url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId'
params ={'serviceKey' : '66p/4eKoNq1jRZNB006GUJHwQl5W0siU+hVT3usdjO+Z/ZKMkVPegS/fGPifbNafCbD+kP8NgLkuXGfzC6p6Kg==', 'stId' : '105000040'}

response = requests.get(url, params=params)
#print(response.text)
soup = bs(response.text, "xml")

for result in soup.find_all("itemList"):
    print('----------------------')
    print(result.find("busRouteAbrv").get_text())
    if result.find("arrmsg1").get_text() == "운행종료":
        print('done')
    elif result.find("arrmsg1").get_text() == "운행 종료":
        print('done')
    else:
        #print(result.find("dir").get_text())
        print(int(result.find("exps1").get_text())//60)
        congestion = {"0" : "데이터없음", "3" : "여유", "4": "보통", "5" : "혼잡"}.get(result.find("reride_Num1").get_text(), "오류")
        print(congestion)
print('----------------------')

