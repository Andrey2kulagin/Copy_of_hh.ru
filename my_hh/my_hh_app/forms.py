
from .models import Resume, UserStatus, Skills, ResponsesVacancy, Question, Profile, Answer
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _


class ResumeForm(forms.ModelForm):
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
    username = forms.CharField(max_length=200, label='Username', help_text="")
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
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


