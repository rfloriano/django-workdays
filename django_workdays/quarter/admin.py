from django.contrib import admin

from .models import Quarter, Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    pass


@admin.register(Quarter)
class QuarterAdmin(admin.ModelAdmin):
    pass
