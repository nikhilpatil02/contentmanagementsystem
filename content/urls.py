from django.urls import path
from . import views

urlpatterns = [
    path('save',views.contentSave,name = 'save'),
    path('view/<str:user_id>',views.contentView,name = 'view'),
    path('update',views.contentUpdate,name = 'update'),
    path('delete',views.contentDelete,name = 'delete'),
]