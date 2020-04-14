from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

def about(request):
    msg="This is an About Page"
    hello="hello, how are you?"
    list1=[10,20,30,40,50]
    x=12
    data={"msg":msg,"hello":hello,"list1":list1,"x":x}
    res=render(request,'testapp/about.html',context=data)
    return res
def employees_info_views(request):
    employees=Employee.objects.all()
    data2={'employees':employees}
    res=render(request,'testapp/employees.html',context=data2)
    return res
