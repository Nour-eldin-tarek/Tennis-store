from django.contrib import admin
from .models import Post
from .models import Racet
from .models import Racet2
from .models import Cloth
from .models import Shose
from .models import Mix

# Register your models here.
# admin.site.register(Post)
admin.site.register(Racet)
admin.site.register(Racet2)
admin.site.register(Shose)
admin.site.register(Mix)


@admin.register(Cloth)
class CLothAdmin(admin.ModelAdmin):
    list_display=('name','catagry','price','image','date_added','id')
    ordering=('name','-price')
    search_fields=('name','price')
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display=('id','name','catagry','price','image','date_added')
    ordering=('name','-price')
    search_fields=('name','price')
