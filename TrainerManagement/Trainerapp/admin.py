import django.contrib.admin
from django.contrib import admin
from Trainerapp.models import City,Course,Trainer_Register,Trainer_Assign
# Register your models here.


admin.site.register(City)
admin.site.register(Course)
admin.site.register(Trainer_Register)
admin.site.register(Trainer_Assign)
