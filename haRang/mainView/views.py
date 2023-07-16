from django.shortcuts import render, redirect
import requests
from .models import Bus
from bs4 import BeautifulSoup as bs

url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId'


# Create your views here.
def index(request):
    return render(request,'mainView/index.html')

def com(request):
    return render(request,'mainView/com.html')

def res(request):
    if request.method == 'POST':
        st = request.POST['station']
        params ={'serviceKey' : 'api키를 넣으시면 됩니다', 'stId' : st}
        response = requests.get(url, params=params)
        soup = bs(response.text, "xml")
        Bus.objects.all().delete()
        for result in soup.find_all("itemList"):
            if result.find("arrmsg1").get_text() == "운행종료":
                print('done')
            elif result.find("arrmsg1").get_text() == "운행 종료":
                print('done')
            else:
                bus = Bus()
                bus.num = result.find("busRouteAbrv").get_text()
                bus.min = str(int(result.find("exps1").get_text())//60)
                bus.congestion = {"0" : "데이터없음", "3" : "여유", "4": "보통", "5" : "혼잡"}.get(result.find("reride_Num1").get_text(), "오류")
                bus.save()
        postlist = Bus.objects.all()

        return render(request,'mainView/list.html', {'postlist' : postlist})
    return redirect('mainView/index.html')