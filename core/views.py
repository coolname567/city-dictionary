from django.shortcuts import render

# Create your views here.
def main(request):
    path = request.path
    path = path.replace("/","")
    if path =="":
        path = 'main'
    cities=['Denver','Cape Cod','Buffalo','Manhattan']
    return render(request,f'{path}.html',{'cities':cities})

