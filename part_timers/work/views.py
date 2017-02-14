from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from .models import Work 

class UserFormView(View):
	form_class = UserForm
	template_name = 'work/registration_form.html'
	
	#login
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#register
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns user object when credientials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')

		return render(request, self.template_name, {'form':form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                works = Work.objects.all()
                return render(request, 'work/index.html', {'works':works})
            else:
                return render(request, 'work/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'work/login.html', {'error_message': 'Invalid login'})
    return render(request, 'work/login.html')

def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			works = Work.objects.all()
			return render(request, 'work/index.html', {'work':works})
	context = {
		'form':form
	}
	return render(request, 'work/register.html', context)


def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {'form':form}
	return render(request, 'work/login.html', context)


def index(request):
	works = Work.objects.all()
	return render(request, 'work/index.html', {'works':works})


def profile(request):
	works = Work.objects.all()
	return render(request, 'work/profile.html', {'works':works})

def request(request, user_id, work_id):
	works = Work.objects.all()
	return render(request, 'work/request.html', {'works':works})


def response(request):
	works = Work.objects.all()
	return render(request, 'work/response.html', {'works':works})

def new_work_post(request):
	works = Work.objects.all()
	return render(request, 'work/new_work_post.html', {'works':works})