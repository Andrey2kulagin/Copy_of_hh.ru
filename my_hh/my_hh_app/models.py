from django.db import models
from django.contrib.auth.models import User
import datetime
# from django.conf import settings
from django.contrib import admin


class Skills(models.Model):
    skill = models.CharField("skill", max_length=200)
    is_checked = models.BooleanField("is_checked", default="False")

    def __str__(self):
        return self.skill


class UserCheckedSkills(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    skills_id = models.ManyToManyField(Skills)

    def __str__(self):
        return f"{self.user} skills"


class Resume(models.Model):
    name = models.CharField("name", max_length=200)
    option = (("male", "Мужской"), ("female", "Женский"))
    gender = models.CharField("gender", max_length=200, choices=option ,)
    spec = models.TextField("speciality", max_length=200)
    experience = models.TextField("experience")
    option = (("full-time", "full-time"), ("part-time", "part-time"))
    type_of_employment = models.CharField("type_of_employment", max_length=200, choices=option)
    skills = models.ManyToManyField(Skills)
    age = models.CharField("age", max_length=100)
    phone = models.CharField("phone", max_length=20)
    salary = models.CharField("salary", max_length=200)
    adres = models.CharField("adres", max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.spec


class UserStatus(models.Model):
    user = models.CharField("user", max_length=200)
    status = models.CharField("status", max_length=200)
    def __str__(self):
        return self.user


class Companies(models.Model):
    company_name = models.CharField("company_name", max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default="", null=True)
    foundation_data = models.DateField("foundation_data", default=datetime.datetime.now(), null=True)
    industry = models.CharField("industry", max_length=200, default="", null=True)
    strategy_description = models.TextField("Strategy_description", default="", null=True)

    def __str__(self):
        return self.company_name


class Vacancies(models.Model):
    title = models.CharField("Title", max_length=200)
    location = models.CharField("Location", max_length=200)
    salary = models.CharField("salary", max_length=200)
    skills = models.ManyToManyField(Skills)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company_name = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)
    description = models.TextField("description", default="")

    def __str__(self):
        return self.title


class ResponsesVacancy(models.Model):
    vacancy_id = models.ForeignKey(Vacancies, on_delete=models.SET_NULL, null=True)
    cover_letter = models.TextField("Cover_letter")
    resume_id = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    author_vacancy_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.resume_id}"


class Profile(models.Model):
    name = models.ForeignKey(Skills, verbose_name='Название теста', on_delete=models.SET_NULL, null=True)
    work_time = models.IntegerField(verbose_name='Время выполнения (мин)')
    questions_count = models.IntegerField(verbose_name='Количество вопросов')
    satisfactory = models.IntegerField(verbose_name='Удовлетворительно')
    good = models.IntegerField(verbose_name='Хорошо')
    perfect = models.IntegerField(verbose_name='Отлично')

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    text = models.TextField(verbose_name='Текст вопроса')
    weight = models.FloatField(default=1, verbose_name='Вес')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_right = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class Result(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    user_name = models.CharField(max_length=300, verbose_name="ФИО")
    date_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    rating = models.FloatField(verbose_name="Проценты")

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
    list_display = ("profile_id", "date_time", "user_name", "rating")

    def has_add_permission(self, request):
        return False
