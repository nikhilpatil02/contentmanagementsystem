from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('user-save',views.userSave,name = 'user-save'),
    path('content-save',views.contentSave,name = 'content-save'),
    path('content-view/<str:user_id>',views.contentView,name = 'content-view'),
    path('content-update',views.contentUpdate,name = 'content-update'),
    path('content-delete',views.contentDelete,name = 'content-delete'),
]