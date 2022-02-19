from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<hr>'
    line3 = '<img src="https://img0.baidu.com/it/u=3622652768,1092461940&fm=253&fmt=auto&app=138&f=JPEG?w=640&h=360" width=800>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line4 + line2 + line3)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<img src="https://img2022.cnblogs.com/blog/2101447/202202/2101447-20220219234955933-718684292.jpg" width=500>'
    line3 = '<a href="/">返回主页面</a>'
    line4 = '<hr>'
    return HttpResponse(line1 + line3 + line4 + line2)

