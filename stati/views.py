from django.shortcuts import render
from home.models import *
from datetime import datetime

# Create your views here.
def index(request):
	games = Game.objects.all()
	game = []
	g = {
		"team":{
			"team_id":"",
		},
		"one":"",
		"two":"",
		"three":"",
		"four":"",
		"five":"",
		"six":"",
		"seven":"",
		"eight":"",
		"nine":"",
		"ten":"",
	}
	i = 0
	for x in games:
		g["team"]["team_id"] = x.team.team_id
		try:g["one"] = datetime.strftime(x.one, '%H:%M:%S')
		except:pass
		try:g["two"] = datetime.strftime(x.two, '%H:%M:%S')
		except:pass
		try:g["three"] = datetime.strftime(x.three, '%H:%M:%S')
		except:pass
		try:g["four"] = datetime.strftime(x.four, '%H:%M:%S')
		except:pass
		try:g["five"] = datetime.strftime(x.five, '%H:%M:%S')
		except:pass
		try:g["six"] = datetime.strftime(x.six, '%H:%M:%S')
		except:pass
		try:g["seven"] = datetime.strftime(x.seven, '%H:%M:%S')
		except:pass
		try:g["eight"] = datetime.strftime(x.eight, '%H:%M:%S')
		except:pass
		try:g["nine"] = datetime.strftime(x.nine, '%H:%M:%S')
		except:pass
		try:g["ten"] = date_string = datetime.strftime(x.ten, '%H:%M:%S')
		except:pass
		game.append(g)
	return render(request,"st.html",{"game":game})