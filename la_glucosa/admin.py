from django.contrib import admin

from .models import GlucoseRecord, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin): ...

@admin.register(GlucoseRecord)
class GlucoseRecordAdmin(admin.ModelAdmin): ...
