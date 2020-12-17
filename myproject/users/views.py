from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
import json
import requests


def index(request):
    #return HttpResponse("Welcome to my users app")
    return render(request,"index.html")


def home(request):
    return HttpResponse("THIS IS MY HOME OF DJANGO")

def login(request):
    form = Login()
    return render(request,"login.html",{'form':form})

def signup(request):
    form = Signup()
    return render(request,"signup.html",{'form':form})  #form = form, name=data

def aftersignup(request):
    form = Signup(request.POST)
    if form.is_valid():
        name = form.cleaned_data['fullname']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        return HttpResponse(f"{email},{name}")
    else:
        error = "Invalid Form"
        form = Signup()
        return render(request,"signup.html",{'form':form})

        
        


    




  #url_for(fun_name)



# Create your views here.



def news6(request):
    import requests
    import json
    from pprint import pprint as pp
    url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=357d4ee9e0c644768b0c48072d000701"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data = json.loads(resp.text)
        lis=['author','description','publishedAt','title']
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        full=[]
        for i in data['articles']:
            a.append(i['url'])
            b.append(i['description'])
            c.append(i['publishedAt'])
            d.append(i['title'])
            e.append(i['urlToImage'])
            f.append(i['source']['name'])
        full.append(a)
        full.append(b)
        full.append(c)
        full.append(d)
        full.append(e)
        z=zip(a,b,c,d,e,f)

        return render(request,"news6.html",{'z':z})

def entertainment(request):
    import requests
    import json
    from pprint import pprint as pp
    url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=357d4ee9e0c644768b0c48072d000701"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data = json.loads(resp.text)
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        for i in data['articles']:
            a.append(i['url'])
            b.append(i['description'])
            c.append(i['publishedAt'])
            d.append(i['title'])
            e.append(i['urlToImage'])
            f.append(i['source']['name'])
        z=zip(a,b,c,d,e,f)

        return render(request,"entertainment.html",{'z':z})

def tech(request):
    import requests
    import json
    from pprint import pprint as pp
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=357d4ee9e0c644768b0c48072d000701"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data = json.loads(resp.text)
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        for i in data['articles']:
            a.append(i['url'])
            b.append(i['description'])
            c.append(i['publishedAt'])
            d.append(i['title'])
            e.append(i['urlToImage'])
            f.append(i['source']['name'])
        z=zip(a,b,c,d,e,f)

        return render(request,"tech.html",{'z':z})

def buisiness(request):
    import requests
    import json
    from pprint import pprint as pp
    url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=357d4ee9e0c644768b0c48072d000701"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data = json.loads(resp.text)
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        for i in data['articles']:
            a.append(i['url'])
            b.append(i['description'])
            c.append(i['publishedAt'])
            d.append(i['title'])
            e.append(i['urlToImage'])
            f.append(i['source']['name'])
        z=zip(a,b,c,d,e,f)

        return render(request,"buisiness.html",{'z':z})
def corona(request):
    import requests
    import json
    from pprint import pprint as pp
    url="https://api.rootnet.in/covid19-in/stats/latest"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data=json.loads(resp.text)
        loc=[]
        confirmcasesindian=[]
        confirmcasesforeign=[]
        discharged=[]
        deaths=[]
        totalconfirmed=[]
        for j in data['data']['regional']:
            loc.append(j['loc'])
            confirmcasesindian.append(j['confirmedCasesIndian'])
            confirmcasesforeign.append(j['confirmedCasesForeign'])
            discharged.append(j['discharged'])
            deaths.append(j['deaths'])
            totalconfirmed.append(j['totalConfirmed'])
        a=data['data']['summary']['total']
        d=data['data']['summary']['deaths']
        c=data['data']['unofficial-summary'][0]['recovered']
        b=data['data']['unofficial-summary'][0]['active']
        sn=[a for a in range(1,37)]
        z=zip(sn,loc,totalconfirmed,discharged,deaths)
        return render(request,"corona.html",{'a':a,'b':b,'c':c,'d':d,'z':z})

def helpline(request):
    import requests
    import json
    from pprint import pprint as pp
    url="https://api.rootnet.in/covid19-in/contacts"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data=json.loads(resp.text)
        region=[]
        contact=[]
        sn=[a for a in range(1,38)]
        for j in data['data']['contacts']['regional']:
            region.append(j['loc'])
            contact.append(j['number'])
        z=zip(region,contact,sn)
        return render(request,"helpline.html",{'z':z})

def health(request):
    import requests
    import json
    from pprint import pprint as pp
    url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=357d4ee9e0c644768b0c48072d000701"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data = json.loads(resp.text)
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        for i in data['articles']:
            a.append(i['url'])
            b.append(i['description'])
            c.append(i['publishedAt'])
            d.append(i['title'])
            e.append(i['urlToImage'])
            f.append(i['source']['name'])
        z=zip(a,b,c,d,e,f)

        return render(request,"entertainment.html",{'z':z})

def front(request):
    import requests
    import json
    from pprint import pprint as pp
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=357d4ee9e0c644768b0c48072d000701"
    resp=requests.get(url)
    a=resp.status_code
    if(a==200):
        data = json.loads(resp.text)
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        for i in data['articles']:
            a.append(i['url'])
            b.append(i['description'])
            c.append(i['publishedAt'])
            d.append(i['title'])
            e.append(i['urlToImage'])
            f.append(i['source']['name'])
        z=zip(a,b,c,d,e,f)

       
    return render(request,"front.html",{'z':z})
       
def hey(request):
    return render(request,"hey.html")

    

    






    




  #url_for(fun_name)



# Create your views here.

