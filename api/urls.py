from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('user-save',views.userSave,name = 'user-save')
]