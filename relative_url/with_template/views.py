from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"with_template/index.html")

def relative(request):
    return render(request,"with_template/relative.html")

def others(request):
    return render(request,"with_template/others.html")