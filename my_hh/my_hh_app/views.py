from django.shortcuts import render, redirect
from .models import Resume, UserStatus, Companies, Vacancies, Skills, UserCheckedSkills
from .forms import ResumeForm, UserRegistrationForm, RegistrationForm, UserStatusForm, SkillsForm, ResponsesForm, MyLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


def index(request):
    resume = None
    vacancies = None
    if request.method == "POST":
        if "resumes_search" in request.POST and "vacancies_search" in request.POST:
            resume = Resume.objects.filter(spec__contains=request.POST.get("resumes_search", ""))
            vacancies = Vacancies.objects.filter(title__contains=request.POST.get("vacancies_search", ""))
        elif "vacancies_search" in request.POST:
            vacancies = Vacancies.objects.filter(title__contains=request.POST.get("vacancies_search", ""))
            resume = Resume.objects.all()
        elif "resumes_search" in request.POST:
            resume = Resume.objects.filter(spec__contains=request.POST.get("resumes_search", ""))
            vacancies = Vacancies.objects.all()
    else:
        resume = Resume.objects.all()
        vacancies = Vacancies.objects.all()
    skills = Skills.objects.all()
    context = {"resumes": resume, "vacancies": vacancies, "skills": skills, }
    return render(request, "my_hh_app/index.html", context)


@login_required
def send_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form.save_m2m()
            return redirect("http://127.0.0.1:8000/lk/")
        else:
            context = {"error":form.errors}
            return render(request, "my_hh_app/send_resume.html", context)
    form = ResumeForm()
    context = {"form": form, "user": request.user}
    return render(request, "my_hh_app/send_resume.html", context)


def registrations(request, int_status):
    context = {}
    user_status_form = UserStatusForm()
    is_valid = True
    reg = RegistrationForm()
    post = request.POST
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if int_status == 1:
                status = "candidate"
            elif int_status == 2:
                status = "employer"
            else:
                raise Exception("Неправильно передан параметр запроса")
            user_status = UserStatus()
            user_status.user = request.POST.__getitem__("username")
            user_status.status = status
            user_status.save()
            user = form.save()
            login(request,user)
            if int_status == 2:
                company = Companies(company_name=post.__getitem__("username"))
                company.author = User.objects.get(username=post.__getitem__("username"))
                company.save()
            if int_status == 1:
                checked_skill = UserCheckedSkills()
                checked_skill.user = User.objects.get(username=post.__getitem__("username"))
                checked_skill.save()
            return_path = "http://127.0.0.1:8000/"
            return redirect(return_path)
        else:
            context["errors"]=form.errors   
            is_valid = False
    form = UserRegistrationForm()
    context["form"]= form
    context["is_valid"]= is_valid
    context["user_status_form"] = user_status_form
    return render(request, "my_hh_app/registrations.html", context)


@login_required
def resume_view(request, pk):
    resume = Resume.objects.get(id=pk)
    checked_skills = UserCheckedSkills.objects.get(user=resume.author)
    context = {"resume": resume, "checked_skills": checked_skills}
    context["checked_skills_count"] = len(checked_skills.skills_id.all())
    cure_user = request.user
    cure_user_status = UserStatus.objects.get(user=cure_user).status
    if cure_user_status == "candidate":
        return render(request, "my_hh_app/be_employer.html", )
    elif cure_user_status == "employer":
        return render(request, "my_hh_app/be_top_employer.html", context)
    elif cure_user_status == "top_employer":
        return render(request, "my_hh_app/resume_view.html", context)


def add_to_skills(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
    form = SkillsForm()
    context = {"form": form}
    return render(request, "my_hh_app/add_skill.html", context)


@login_required
def vacancy_view(request, id, is_own):
    cure_user = request.user
    cure_user_status = UserStatus.objects.get(user=cure_user).status
    vacancy = Vacancies.objects.get(id=id)
    context = {"status":cure_user_status}
    if cure_user_status == "candidate":
        resume = Resume.objects.filter(author=cure_user)
        if request.method == "POST":
            if len(resume) == 0:
                return render(request, "my_hh_app/send_resume_pls.html")
            form = ResponsesForm(cure_user, request.POST)
            if form.is_valid():
                vacancy_form = form.save(commit=False)
                vacancy_form.vacancy_id = vacancy
                vacancy_form.resume_id = Resume.objects.get(id=request.POST["resumes"])
                vacancy_form.author_vacancy_name = vacancy.author
                vacancy_form.save()
                #надо  бы добавить страницу в стиле резюме отправлено. МБ потом добавлю.
                return(redirect("http://127.0.0.1:8000/"))
        form = ResponsesForm(cure_user)
        context["vacancy"]= vacancy
        context["form"]= form
        return render(request, "my_hh_app/vacancy_view.html", context)
    elif cure_user_status == "employer" or cure_user_status == "top_employer":
        context["vacancy"] = vacancy
        if is_own == 0:
            return render(request,"my_hh_app/vacancy_view.html", context)
        else:
            if request.method == "POST":
                Vacancies.objects.get(id=id).delete()
                return redirect("http://127.0.0.1:8000/lk/")
            return render(request, "my_hh_app/vacancy_view_employer_own.html", context)

def login_view(request):
    context = {} 
    if request.method == "POST":
        my_form = MyLoginForm(data=request.POST)
        if my_form.is_valid():
            user = my_form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect("http://127.0.0.1:8000/")
    else:
        my_form = MyLoginForm()
    context['my_form'] = my_form
    return render(request,"registration/login.html", context)
