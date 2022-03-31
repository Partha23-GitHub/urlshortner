from django.shortcuts import render,redirect
import pyshorteners as ps

# Create your views here.
def index(request):
    return render(request,'urlapp/index.html')

def urlShotrener(request):
    if request.method=='POST':
        input_url=request.POST['input-url']
        short_url=ps.Shortener().tinyurl.short(input_url)
        return render(request,'urlapp/index.html',{'key':short_url})
    else:
        return render(request,'urlapp/index.html',{'key':'Please try again'})
