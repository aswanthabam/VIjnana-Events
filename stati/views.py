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
		try:g["one"] = date_string = datetime.strftime(x.one, '%H:%M:%S')
		except:pass
		try:g["two"] = date_string = datetime.strftime(x.two, '%H:%M:%S')
		except:pass
		try:g["three"] = date_string = datetime.strftime(x.three, '%H:%M:%S')
		except:pass
		try:g["four"] = date_string = datetime.strftime(x.four, '%H:%M:%S')
		except:pass
		try:g["five"] = date_string = datetime.strftime(x.five, '%H:%M:%S')
		except:pass
		try:g["six"] = date_string = datetime.strftime(x.six, '%H:%M:%S')
		except:pass
		try:g["seven"] = date_string = datetime.strftime(x.seven, '%H:%M:%S')
		except:pass
		try:g["eight"] = date_string = datetime.strftime(x.eight, '%H:%M:%S')
		except:pass
		try:g["nine"] = date_string = datetime.strftime(x.nine, '%H:%M:%S')
		except:pass
		g["ten"] = date_string = datetime.strftime(x.ten, '%H:%M:%S')
		game.append(g)
	return render(request,"st.html",{"game":game})