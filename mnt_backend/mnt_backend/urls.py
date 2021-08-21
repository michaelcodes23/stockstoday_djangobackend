from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views

router = routers.DefaultRouter()
#allows you to call /api/users giving you all of the users
#allows you to call /api/users/id - returning a single user using the id primary key
# Allows users to Update / Delete users
#Inside Django REST Framework you can edit your specific inputs aswell!!!
router.register(r'users', views.UserView, 'main_app')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]




