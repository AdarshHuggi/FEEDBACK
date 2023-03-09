from django.contrib import admin

# Register your models here.
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    #displaying the columns in admin panel
    list_display =("user_name","review_text","rating",)

admin.site.register(Review,ReviewAdmin)