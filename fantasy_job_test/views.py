from django.shortcuts import HttpResponse, render
import pysqlite

def main(request):
    return render(request, "main.html")

def username(request):
    if request.method == "POST":
        template = render(request, "Home.html", {"name": request.POST.get('username')})
        template.set_cookie(key="username", value=request.POST.get('username'))
        return template
    else:
        return render(request, 'error.html')
   

def test_page(request, page):
    template = render(request, f"{page}.html")
    template.set_cookie(key="")
