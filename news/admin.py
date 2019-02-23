from django.contrib import admin

# Register your models here.
from .models import news
class newsAdmin(admin.ModelAdmin):
    class Meta:
        model = news


admin.site.register(news, newsAdmin)
