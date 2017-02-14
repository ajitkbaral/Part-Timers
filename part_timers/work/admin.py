from django.contrib import admin
from .models import Skill, UserSkill, Job, Work, RequestedWork, ApprovedWork

admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Job)
admin.site.register(Work)
admin.site.register(RequestedWork)
admin.site.register(ApprovedWork)