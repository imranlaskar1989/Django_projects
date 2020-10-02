from django.shortcuts import render
from django.http import HttpResponse


def IndexView(request) :
    print(request.COOKIES)



    oldval = request.COOKIES.get('za', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval :
        resp.set_cookie('za', 'f5f3b8d7') # No expired date = until browser close
    else :
        resp.set_cookie('za', 'f5f3b8d7') # No expired date = until browser close




     # seconds until expire


    num_visits = request.session.get('num_visits', 0) + 1

    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])

    return HttpResponse('view count='+str(num_visits)+', Cookie='+request.COOKIES.get('za','f5f3b8d7'))
# Create your views here.
