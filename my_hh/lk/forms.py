from django import forms
from django.apps import apps

Vacancies = apps.get_model("my_hh_app", "Vacancies")
Skills = apps.get_model("my_hh_app", "Skills")


class VacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ["title",
                  "location",
                  "salary",
                  "skills"
                  ]
