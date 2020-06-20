from django.contrib import admin

from .models import Tip, TipUser, Vote



# Register your models here.

admin.site.register(Tip)
admin.site.register(TipUser)
admin.site.register(Vote)

