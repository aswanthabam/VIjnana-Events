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
				db["post"] = True
				db["valid"] = True
				db["message"]["text"] = obj.hint_html
			except:
				db["post"] = True
				db["valid"] = False
				db["message"]["text"] = """
				<span class="info">Wrong code. Search more... and try again. 🤗</span>
				<br/><a href=""><button>Try again</button></a>
				"""
			return render(request,"index.html",db)
	return render(request,"index.html",db)