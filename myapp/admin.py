from django.contrib import admin
from .models import Image

# Register your models here.


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display=['id','backgroundimg','brandtitle','photo','candidate1','candidate2','candidate3','candidate4','candidate5','candidate6','date',]
    
    
    
    
from django.contrib import admin
from .models import Vote

admin.site.register(Vote)