from django.shortcuts import render

def indexView(request):
    #do something
    return render(request,'index.html')