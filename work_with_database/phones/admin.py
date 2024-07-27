from django.contrib import admin
from phones.models import Phone
# Register your models here.
@admin.register(Phone)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price','image','release_date','lte_exists','slug']