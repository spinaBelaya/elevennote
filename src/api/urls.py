from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'notes', NoteViewSet) # r(/a) representates / just as a literal len("//a") = len(r'/a')

urlpatterns = [
    path('jwt-auth/', obtain_jwt_token), # получение JSON Web Token'a
    path('', include(router.urls)),
]
