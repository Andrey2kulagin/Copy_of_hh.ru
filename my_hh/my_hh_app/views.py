from django.shortcuts import render, redirect
from .models import Resume, UserStatus, Companies, Vacancies, Skills, UserCheckedSkills
from .forms import ResumeForm, UserRegistrationForm, RegistrationForm, UserStatusForm, SkillsForm, ResponsesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        form.save_m2m()
    form = ResumeForm()
    context = {"form": form, "user": request.user}
    return render(request, "my_hh_app/send_resume.html", context)


def registrations(request, int_status):
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
            form.save()
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
            is_valid = False
    form = UserRegistrationForm()
    context = {"form": form, "is_valid": is_valid, "reg": reg, "user_status_form": user_status_form, "post": post}
    return render(request, "my_hh_app/registrations.html", context)


@login_required
def resume_view(request, pk):
    resume = Resume.objects.get(id=pk)
    checked_skills = UserCheckedSkills.objects.get(user=resume.author)
    context = {"resume": resume, "checked_skills": checked_skills}
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
    return render(request, "my_hh_app/add_to_model.html", context)


@login_required
def vacancy_view(request, id, is_own):
    cure_user = request.user
    cure_user_status = UserStatus.objects.get(user=cure_user).status
    vacancy = Vacancies.objects.get(id=id)
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
        form = ResponsesForm(cure_user)
        context = {
            "vacancy": vacancy,
            "form": form,
        }
        return render(request, "my_hh_app/vacancy_view.html", context)
    elif cure_user_status == "employer" or cure_user_status == "top_employer":
        context = {"vacancy": vacancy}
        if is_own == 0:
            return render(request,"my_hh_app/vacancy_view_base.html", context)
        else:
            if request.method == "POST":
                Vacancies.objects.get(id=id).delete()
                return redirect("http://127.0.0.1:8000/lk/")
            return render(request, "my_hh_app/vacancy_view_employer_own.html", context)

