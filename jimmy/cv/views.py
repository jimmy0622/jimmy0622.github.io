# cv/views.py
from django.shortcuts import render
from .models import Profile

def cv_detail(request):
    profile = Profile.objects.first()
    if profile is None:
        context = {
            'profile': None,
            'experiences': [],
            'educations': [],
            'skills': [],
            'projects': [],
        }
    else:
        context = {
            'profile': profile,
            'experiences': profile.experience_set.all(),
            'educations': profile.education_set.all(),
            'skills': profile.programskill_set.all(),
            'projects': profile.project_set.all(),

        }
    return render(request, 'cv/cv_detail.html', context)
