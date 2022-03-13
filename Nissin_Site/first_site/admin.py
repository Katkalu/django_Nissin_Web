from django.contrib import admin

from .models import News
from .models import Delta_Time
from .models import Product_value
from .models import Slide
from .models import Announcement
from .models import Document
from .models import Event

# Register your models here.

admin.site.register(News)
admin.site.register(Delta_Time)
admin.site.register(Product_value)
admin.site.register(Slide)
admin.site.register(Announcement)
admin.site.register(Document)
admin.site.register(Event)