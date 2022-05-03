from django.shortcuts import render

# Create your views here.


def showmain(request):
    return render(request, 'main/show.html')


def showwrite(request):
    return render(request, 'main/writepage.html')


def showhistory(request):
    return render(request, 'main/historypage.html')


def showphoto(request):
    return render(request, 'main/photopage.html')


def showcharacter(request):
    return render(request, 'main/characterpage.html')


def showhobby(request):
    return render(request, 'main/hobbypage.html')
