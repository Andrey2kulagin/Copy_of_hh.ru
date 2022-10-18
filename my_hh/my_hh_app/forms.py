from .models import Resume, UserStatus, Skills, ResponsesVacancy, Question, Profile, Answer
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


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
    def __init__(self, user, *args, **kwargs):
        resume = Resume.objects.filter(author=user)
        options = []
        super().__init__(*args, **kwargs)
        for i in resume:
            options.append((i.id, str(i)))
        self.fields['resumes'] = forms.ChoiceField(
            choices=[(i.id, str(i)) for i in resume])

    class Meta:
        model = ResponsesVacancy
        fields = ["cover_letter", ]




