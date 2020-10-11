from django.contrib import admin
from dashboard.models import NeedPost, Comment, HaveToilet
# Register your models here.
admin.site.register(NeedPost)
admin.site.register(Comment)
admin.site.register(HaveToilet)
