from django.shortcuts import render

def home(request):
    if request.method == "POST":
        inte=int(request.POST.get('intensity'))
        res=int(request.POST.get('resistance'))
        power=(inte**2)*res
        return render(request,'math.html',{'output':power})
    return render(request,'math.html')