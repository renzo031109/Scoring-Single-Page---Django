from django.contrib import admin
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

# Register your models here.
admin.site.register(Score, ScoreAdmin)