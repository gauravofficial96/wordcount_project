from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	return render(request,'index.html')
def count(request):
	fulltext=request.GET['fulltext']
	return render(request,'count.html',{'fulltext':fulltext})
def check(request):
    return render(request,'check.html')	