from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'new/home.html')

# def red(request):
#     return render(request, 'new/red.html')
# def blue(request):
#     return render(request, 'new/blue.html')
# def white(request):
#     return render(request, 'new/white.html')
# def pink(request):
#     return render(request, 'new/pink.html')

