from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Status)
admin.site.register(Task)