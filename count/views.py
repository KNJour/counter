from django.shortcuts import render, redirect

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0

    data = {
        'count': request.session['count']
    }
    return render(request, "index.html", data)

def reset(request):
    request.session['count'] = 0
    return redirect("/")
