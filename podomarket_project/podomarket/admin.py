from django.contrib import admin
from .models import User, Post
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname","kakao_id","address","profile_pic")}),)

admin.site.register(Post)