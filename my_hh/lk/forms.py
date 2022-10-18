from django import forms
from django.apps import apps

Vacancies = apps.get_model("my_hh_app", "Vacancies")
Skills = apps.get_model("my_hh_app", "Skills")
Profile = apps.get_model("my_hh_app", "Profile")
Question = apps.get_model("my_hh_app", "Question")
Answer = apps.get_model("my_hh_app", "Answer")


class VacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ["title",
                  "location",
                  "salary",
                  "skills"
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
