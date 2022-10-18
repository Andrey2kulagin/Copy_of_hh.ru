from django.db import models
from django.contrib.auth.models import User
import datetime
#from django.conf import settings
from django.contrib import admin


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


class Profile(models.Model):
    Name = models.CharField(max_length=200, verbose_name='Название теста')
    WorkTime = models.IntegerField(verbose_name='Время выполнения (мин)')
    QuestionsCount = models.IntegerField(verbose_name='Количество вопросов')
    Statisfactorily = models.IntegerField(verbose_name='Удовлетворительно')
    Good = models.IntegerField(verbose_name='Хорошо')
    Perfect = models.IntegerField(verbose_name='Отлично')

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.Name


class Question(models.Model):
    ProfileId = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    Text = models.TextField(verbose_name='Текст вопроса')
    Weight = models.FloatField(default=1, verbose_name='Вес')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.Text


class Answer(models.Model):
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=300)
    IsRight = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.Text


class Result(models.Model):
    ProfileId = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    UserName = models.CharField(max_length=300, verbose_name="ФИО")
    DateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    Rating = models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'


class QuestionsInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("ProfileId", "DateTime", "UserName", "Rating")

    def has_add_permission(self, request):
        return False
