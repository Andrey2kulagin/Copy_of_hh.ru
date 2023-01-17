
from .models import Resume, UserStatus, Skills, ResponsesVacancy, Question, Profile, Answer
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _


class ResumeForm(forms.ModelForm):
    type_of_employment_option = (("full-time", "full-time"), ("part-time", "part-time"))
    spec = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"spec__input" ,"placeholder":"Введите название вашей специальности"}))
    name = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"username__input" ,"placeholder":"ФИО"}))
    gender_option = (("male", "Мужской"), ("female", "Женский"))
    gender = forms.ChoiceField(choices=gender_option,widget=forms.Select( attrs={"class":"gender__input" }))
    age = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"age__input" ,"placeholder":"Укажите ваш возраст"}))
    adres = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"city__input" ,"placeholder":"Укажите город, в котором планируете работать"}))
    experience = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"exp__input" ,"placeholder":"Ваш опыт работы(Сколько лет?)"}))
    type_of_employment = forms.ChoiceField(choices=type_of_employment_option, widget=forms.Select( attrs={"class":"type__input" ,"placeholder":"Выберите предпочитаемый тип занятости"}))
    skills_option = ((i.id, str(i)) for i in Skills.objects.all())
    skills = forms.MultipleChoiceField(choices=skills_option, widget=forms.SelectMultiple( attrs={"class":"skills__input" ,"placeholder":"Укажите ваши навыки", 'size': '5'}))
    phone = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"contact__input" ,"placeholder":"Укажите ваши контакты"}))
    salary = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"salary__input" ,"placeholder":"Ожидаемая зарплата(с указанием валюты)"}))
    class Meta:
        model = Resume
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


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=200,
     label='Username', 
     help_text="",
     widget=forms.TextInput(attrs={"autocomplete": "username", "class": "username__input", "placeholder" : "Введите имя пользователя" }))
    first_name = forms.CharField(widget = forms.TextInput(attrs={"autocomplete":"name", "class": "name__input", "placeholder" : "Как к вам можно обращаться?"}))
    email = forms.EmailField(widget = forms.TextInput(attrs={"autocomplete":"email", "class": "email__input", "placeholder" : "Введите email"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "password__input", "placeholder" : "Введите пароль"}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "password__input", "placeholder" : "Введите пароль ещё раз"}),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2',)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserStatusForm(forms.ModelForm):
    option = (("candidate", "Ищу работу"), ("employer", "Ищу работника"))
    status = forms.Select(choices=option)

    class Meta:
        model = UserStatus
        fields = ["status"]


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ["skill"]


class ResponsesForm(forms.ModelForm):
    cover_letter = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'cover__letter__input', 'placeholder':'Заполните сопроводительное письмо'})
    )
    def __init__(self, user, *args, **kwargs):
        resume = Resume.objects.filter(author=user)
        options = []
        super().__init__(*args, **kwargs)
        for i in resume:
            options.append((i.id, str(i)))
        self.fields['resumes'] = forms.ChoiceField(
            choices=[(i.id, str(i)) for i in resume], 
            widget=forms.Select(attrs={'class':'resume__choise'}))
    class Meta:
        model = ResponsesVacancy
        fields = ["cover_letter", ]

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=200,
        label='Username', help_text="",
        widget=forms.TextInput(attrs={'class':'username__input', 'placeholder':'Введите имя пользователя'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "password", 'class':"password__input", 'placeholder':"Введите пароль"}),
    )
    class Meta:
        model = User
        fields = ('username',  'password' )


