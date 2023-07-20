from django.contrib import admin

from .models import Topic
from .models import Question
from .models import Answer

admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
