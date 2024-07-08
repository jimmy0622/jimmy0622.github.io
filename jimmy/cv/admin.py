# cv/admin.py
from django.contrib import admin
from .models import Profile, Experience, Education, ProgramSkill, Project

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ProgramSkill)
admin.site.register(Project)