from django.contrib import admin
from .models.users import *
from .models.miscellaneous import *

admin.site.register(User)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Subject)