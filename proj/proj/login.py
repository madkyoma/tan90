from django.http import HttpResponse

def do_login(request):
    return HttpResponse('hello world!')

def do_logout(request):
    return HttpResponse('hello world!')

def do_register(request):
    return HttpResponse('hello world!')