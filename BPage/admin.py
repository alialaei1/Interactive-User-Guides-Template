from django.contrib import admin

from .models import Devices
from .models import Question
from .models import Answer

admin.site.register(Devices)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
