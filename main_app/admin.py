from django.contrib import admin
from .models import Frog, Feeding, LilyPad

# Register your models here.
admin.site.register(Frog)
admin.site.register(Feeding)
admin.site.register(LilyPad)