from django import forms
from django.apps import apps

Vacancies = apps.get_model("my_hh_app", "Vacancies")
Skills = apps.get_model("my_hh_app", "Skills")
Profile = apps.get_model("my_hh_app", "Profile")
Question = apps.get_model("my_hh_app", "Question")
Answer = apps.get_model("my_hh_app", "Answer")
Companies = apps.get_model("my_hh_app", "Companies")


class VacanciesForm(forms.ModelForm):
    title = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"spec__input" ,"placeholder":"Введите название вашей специальности"}))
    location = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"city__input" ,"placeholder":"Укажите город, в котором планируете работать"}))
    salary = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"salary__input" ,"placeholder":"Ожидаемая зарплата(с указанием валюты)"}))
    skills_option = ((i.id, str(i)) for i in Skills.objects.all())
    skills = forms.MultipleChoiceField(choices=skills_option, widget=forms.SelectMultiple( attrs={"class":"skills__input" ,"placeholder":"Укажите ваши навыки", 'size': '5'}))
    description = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'vacancy__description__input', 'placeholder':'Подробно опишите, чем предстоит заниматься'})
    )
    class Meta:
        model = Vacancies
        fields = ["title",
                  "location",
                  "salary",
                  "skills",
                  "description"
                  ]


class TestForm(forms.Form):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profile_id = Profile.objects.get(name=name)
        question_ids = Question.objects.filter(profile_id=profile_id)
        for i in question_ids:
            cure = Answer.objects.filter(question_id=i.id)
            choices = [("empty", "------")]
            for j in cure:
                choices.append((str(j.id), str(j.text)))
            self.fields[i.text] = forms.ChoiceField(
                choices=choices)
                


class CompaniesForm(forms.ModelForm):
    company_name = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"edit__input" ,}))
    foundation_data = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"edit__input" ,}))
    industry = forms.CharField(max_length=200,widget=forms.TextInput( attrs={"class":"edit__input" ,}))
    strategy_description = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'strategy__description__input'})
    )
    class Meta:
        model = Companies
        fields = ["company_name",
                  "foundation_data",
                  "industry",
                  "strategy_description",
                  ]