from django.shortcuts import render

def tpage(request):
    return render(request, "test.html", {})
