from django.shortcuts import render
from .models import *
from django.utils import timezone
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
		# Request sends some details like code and team_id
		# Takes the code the player gives and team_id
		post = request.POST
		code = post["code"]
		team_id = post["team_id"]
		
		try:
			# Try to run the below code. Exception may occur in the case of
			# Team data is not available then the except part of the code is executed
			# Find the team from the team_id 
			team = Team.objects.filter(team_id=team_id)[0]
		except Exception as e:
			db["post"] = True
			db["valid"] = False
			db["message"]["text"] = """
			<span class="info">Wrong Team Code. Make sure you entered the correct code 🤗</span>
			<br/><a href=""><button>Try again</button></a>
			"""
			return render(request,"index.html",db)
		# Find the next task the player want to do by adding 1 to the players current poaition in the database
		next_task = team.progress + 1
		# Get all tasks for getting how much task is available
		all_task = Task.objects.all()
		if next_task > len(all_task):
			# The next task is unavilable or the user completed all tasks
			next_task = None
		else:
			# The next task is available or not the last task
			next_task = Task.objects.filter(order=next_task)[0]
			
		# Find the task with the code player entered
		objs = Task.objects.filter(code=code)
		if len(objs) < 1:
			# The task with that code user enetered is not found
			db["post"] = True
			db["valid"] = False
			db["message"]["text"] = """
			<span class="info">Wrong code. Search more... and try again. 🤗</span>
			<br/><a href=""><button>Try again</button></a>
			"""
			
			return render(request,"index.html",db)
		else:
			# The task is available
			try:
				obj = objs[0]
				finished = False
				if next_task is None:
					# The next task is unavailable all task completed
					next_task = obj
					# Set the finshed flag to True because all task is finished and 
					# We dont want to increase the progress of the team
					finished = True
				if obj.order > next_task.order:
					# The order is greter than next task order
					# That is the user skipped a previous level
					db["post"] = True
					db["valid"] = False
					db["message"]["text"] = """
					<span class="info">Oops. you skipped a level go back and complete the level. 🤗</span>
					<br/><a href=""><button>Try again</button></a>
					"""
					return render(request,"index.html",db)
				else:
					# The task the user is doing is in sequence
					db["post"] = True
					db["valid"] = True
					db["message"]["text"] = obj.hint_html
					if obj.order == next_task.order and not finished:
						team.progress += 1
						team.save()
						# We also want to add the enter time of code
						try:
							# Find the game model of the team
							game = Game.objects.filter(team=team)[0]
							order = obj.order
							time = timezone.now()
							# check for which is the task or order and change the
							# corresponding field of model eg model.one,model.two
							if order == 1:game.one = time
							elif order == 2:game.two = time
							elif order == 3:game.three = time
							elif order == 4:game.four = time
							elif order == 5:game.five = time
							elif order == 6:game.six = time
							elif order == 7:game.seven = time
							elif order == 8:game.eight = time
							elif order == 9:game.nine = time
							elif order == 10:game.ten = time
							elif order == 11:game.eleven = time
							elif order == 12:game.twelve = time
							elif order == 13:game.twelve2 = time
							else:pass
							game.save()
						except:pass
					return render(request,"index.html",db)
			except:
				# Some error occured in the above code
				# That may be because of wrong code
				db["post"] = True
				db["valid"] = False
				db["message"]["text"] = """
				<span class="info">Wrong code. Search more... and try again. 🤗</span>
				<br/><a href=""><button>Try again</button></a>
				"""
				return render(request,"index.html",db)
	else:
		# The request is not post
		# That is the user is not entering any code the home page want to be shown
		return render(request,"index.html",db)