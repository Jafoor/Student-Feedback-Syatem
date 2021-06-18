from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Subject)
admin.site.register(SemesterSubject)
admin.site.register(Question)
admin.site.register(ReviewSet)
admin.site.register(Review)
admin.site.register(ReviewDetails)
