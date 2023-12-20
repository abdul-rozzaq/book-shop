from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Badge)
admin.site.register(Discount)