from django.contrib import admin
from sp.models import Student, StudyPlace, Address, Squad

# Register your models here.
admin.site.register(Student)
admin.site.register(Squad)
admin.site.register(StudyPlace)
admin.site.register(Address)