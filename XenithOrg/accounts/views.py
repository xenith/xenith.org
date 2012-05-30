from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth


def login(request):
    td = {}
    td['sections'] = {}
    td['next'] = request.GET.get('next', '')

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #next = request.POST.get('next', '/admin/')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/admin/')

    return render_to_response("accounts/login.html",
                              td,
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    next = request.GET.get('next', '/accounts/login/')

    return HttpResponseRedirect(next)
