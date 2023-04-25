from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('form/', views.FormModelViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('status/<int:UserId>/', views.user_status, name='user_status'),
    # path('status/', views.user_status, name='user_status'),
]
