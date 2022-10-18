from django.contrib import admin
from .models import Resume, UserStatus, Companies, Vacancies, Skills, ResponsesVacancy, Profile, Answer


admin.site.register(Resume)
admin.site.register(UserStatus)
admin.site.register(Companies)
admin.site.register(Vacancies)
admin.site.register(Skills)
admin.site.register(ResponsesVacancy)
admin.site.register(Profile)
admin.site.register(Answer)

