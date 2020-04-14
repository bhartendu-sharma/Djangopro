from django.shortcuts import render
from django.http import HttpResponse 

def showTest(request):
    que="Who developed C Language?"
    a="Ken Thomson"
    b="Dennis Ritchie"
    c="Bjarne Stroustrup"
    d="James Gosling"
    level="Easy"
    data= {'que':que,'a':a,"b":b,"c":c,"d":d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res
