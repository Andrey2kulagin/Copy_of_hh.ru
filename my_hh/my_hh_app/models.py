from django.db import models
from django.contrib.auth.models import User
import datetime

class Skills(models.Model):
    skill = models.CharField("skill", max_length=200)
    is_checked = models.BooleanField("is_checked", null=True)


class Resume(models.Model):
    name = models.CharField("name", max_length=200)
    option = (("male", "Мужской"), ("female", "Женский"))
    gender = models.CharField("gender", max_length=200, choices=option)
    spec = models.TextField("speciality", max_length=200)
    experience = models.TextField("experience")
    option = (("full-time", "full-time"), ("part-time", "part-time"))
    type_of_employment = models.CharField("type_of_employment", max_length=200, choices=option)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    age = models.CharField("age", max_length=3)
    phone = models.CharField("phone", max_length=20)
    salary = models.CharField("salary", max_length=200)
    adres = models.CharField("adres", max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class UserStatus(models.Model):
    user = models.CharField("user", max_length=200)
    status = models.CharField("status", max_length=200)



class Companies(models.Model):
    company_name = models.CharField("company_name", max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default="", null=True)
    foundation_data = models.DateField("foundation_data", default=datetime.datetime.now(), null=True)
    industry = models.CharField("industry", max_length=200, default="", null=True)
    strategy_description = models.TextField("Strategy_description", default="", null=True)


class Vacancies(models.Model):
    title = models.CharField("Title", max_length=200)
    location = models.CharField("Location", max_length=200)
    salary = models.CharField("salary", max_length=200)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company_name = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)



class ResponsesVacancy(models.Model):
    vacancy_id = models.ForeignKey(Vacancies, on_delete=models.SET_NULL, null=True)
    cover_letter = models.TextField("Cover_letter")
    resume_id = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    author_vacancy_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

