from django.contrib import admin

from app.models import Qstion, User, Answer, Tags

admin.site.register(Qstion)
admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Tags)