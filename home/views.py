from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	db = {
		"post":False,
		"valid":False,
		"message":{
			"text":"",
		}
	}
	if request.method == "POST":
		post = request.POST
		code = post["code"]
		team_id = post["team_id"]
		
		try:
			team = Team.objects.filter(team_id=team_id)[0]
			next_task = team.progress + 1;
			all_task = Task.objects.all()
			if next_task > len(all_task):
				db["post"] = True
				db["valid"] = False
				db["message"]["text"] = """
				<span class="info">Games finished. Please contact event organizers for next task 🤗</span>
				<br/><a href=""><button>Try again</button></a>
				"""
				return render(request,"index.html",db)
			next_task = Task.objects.filter(order=next_task)[0]
			
		except:
			db["post"] = True
			db["valid"] = False
			db["message"]["text"] = """
			<span class="info">Wrong Team Code. Make sure you entered the correct code 🤗</span>
			<br/><a href=""><button>Try again</button></a>
			"""
			return render(request,"index.html",db)
		objs = Task.objects.filter(code=code)
		if len(objs) < 1:
			db["post"] = True
			db["valid"] = False
			db["message"]["text"] = """
			<span class="info">Wrong code. Search more... and try again. 🤗</span>
			<br/><a href=""><button>Try again</button></a>
			"""
			
			return render(request,"index.html",db)
		else:
			try:
				obj = objs[0]
				if obj.order > next_task.order:
					db["post"] = True
					db["valid"] = False
					db["message"]["text"] = """
					<span class="info">Oops. you skipped a level go back and complete the level. 🤗</span>
					<br/><a href=""><button>Try again</button></a>
					"""
					return render(request,"index.html",db)
				db["post"] = True
				db["valid"] = True
				db["message"]["text"] = obj.hint_html
				team.progress += 1
				team.save()
				return render(request,"index.html",db)
			except:
				db["post"] = True
				db["valid"] = False
				db["message"]["text"] = """
				<span class="info">Wrong code. Search more... and try again. 🤗</span>
				<br/><a href=""><button>Try again</button></a>
				"""
			return render(request,"index.html",db)
	return render(request,"index.html",db)