from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from pokequest.models import Player

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.session['name'] = username #add session var name
        request.session['invalidity'] = 0
        request.session['invalidity_answer'] = 0
        players_list = Player.objects.all()
        for player in players_list:
            if player.name == username:
                request.session['counter'] = player.counter #add session var counter
                player.present = True
                player.save()

        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    name = request.session['name'] #access session var name
    return render_to_response('loggedin.html',
                 { 'full_name':request.user.username, 'name':name})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')