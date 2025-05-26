from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from appWedding.models import EntryForm,FavoriteModel,GalleryModel

admin.site.register(EntryForm)
admin.site.register(FavoriteModel)
admin.site.register(GalleryModel)