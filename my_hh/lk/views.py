from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .forms import VacanciesForm, TestForm
from django.views.generic import UpdateView

Resume = apps.get_model('my_hh_app', 'Resume')
UserStatus = apps.get_model('my_hh_app', 'UserStatus')
Companies = apps.get_model('my_hh_app', 'Companies')
Vacancies = apps.get_model('my_hh_app', 'Vacancies')
Skills = apps.get_model('my_hh_app', 'Skills')
ResponsesVacancy = apps.get_model('my_hh_app', 'ResponsesVacancy')
UserCheckedSkills = apps.get_model('my_hh_app', 'UserCheckedSkills')
Answer = apps.get_model('my_hh_app', 'Answer')
Profile = apps.get_model('my_hh_app', 'Profile')
Question = apps.get_model('my_hh_app', 'Question')


@login_required
def lk(request):
    cure_user = request.user
    cure_user_status = UserStatus.objects.get(user=cure_user).status
    resume = Resume.objects.all()
    user = request.user
    author_resume = Resume.objects.filter(author=user)
    context = {"resume": resume, "author_resume": author_resume, }
    if request.method == "POST":
        user_status = UserStatus.objects.get(user=cure_user)
        user_status.status = "top_employer"
        user_status.save()
    if cure_user_status == "candidate":
        checked_skills = UserCheckedSkills.objects.filter(user=user)
        if len(checked_skills) == 0:
            context["checked_skills"] = "0"
        else:
            context["checked_skills"] = checked_skills
        return render(request, "lk/candidate_lk.html", context)
    elif cure_user_status == "employer" or cure_user_status == "top_employer":
        company_info = Companies.objects.get(author=cure_user, )
        context["company_info"] = company_info
        responses = ResponsesVacancy.objects.filter(author_vacancy_name=cure_user)
        context["responses"] = responses
        return render(request, "lk/employer_lk.html", context)


def resume_view(request, pk):
    resume = Resume.objects.filter(id=pk)
    context = {"resume": resume[0]}
    return render(request, "lk/resume_view.html", context)


class NewUpdateView(UpdateView):
    model = Resume
    template_name = "my_hh_app/send_resume.html"
    fields = ["name",
              "gender",
              "phone",
              "age",
              "spec",
              "type_of_employment",
              "adres",
              "experience",
              "skills",
              "salary"
              ]
    success_url = "http://127.0.0.1:8000/lk/resume_view"


class CompanyUpdate(UpdateView):
    model = Companies
    template_name = "lk/change_company_info.html"
    fields = [
        "company_name",
        "foundation_data",
        "industry",
        "strategy_description",
    ]
    success_url = "http://127.0.0.1:8000/lk"


def send_vacation(request):
    if request.method == "POST":
        form = VacanciesForm(request.POST)
        # skills_ids1 = form.cleaned_data.get('skills')
        if form.is_valid():
            vacation1 = form.save(commit=False)
            vacation1.author = request.user
            vacation1.company_name = Companies.objects.get(author=request.user)
            vacation1.save()
            form.save_m2m()
    form = VacanciesForm()
    context = {"VacanciesForm": form, }
    return render(request, "lk/send_vacation.html", context)


def skills_for_check(request):
    user = request.user
    all_skills = [x.skill for x in Skills.objects.filter(is_checked=True)]
    checked_skills = UserCheckedSkills.objects.filter(user=user)
    if len(checked_skills) > 0:
        checked_skills = [x.skill for x in UserCheckedSkills.objects.get(user=user).skills_id.all()]
    skills_without_checked = [x for x in all_skills if x not in checked_skills]
    if len(skills_without_checked) == 0:
        skills_without_checked = "0"
    context = {"skills_without_checked": skills_without_checked,
               "a": all_skills,
               "b": checked_skills}
    return render(request, "lk/skills_for_check.html", context)


def check_skill(request, name):
    post = 1
    skills_object = Skills.objects.get(skill=name)
    if request.method == "POST":
        number_of_points = 0
        post = request.POST
        # ЗАДАЧА - ПОСЧИТАТЬ КОЛ-ВО ПРАВИЛЬНЫХ ОТВЕТОВ


    test_form = TestForm(name=skills_object)
    context = {"test_form": test_form, "post": post}
    return render(request, "lk/check_skill.html", context)
