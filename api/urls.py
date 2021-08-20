from django.conf.urls import url
from django.urls import path
from rest_framework import views
from .views import NotesDetail, NotesList, get_routes

from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [ path('api/v1/notes/', NotesList.as_view(), name='notes-list'),
                path('api/v1/notes/<int:pk>/', NotesDetail.as_view(), name='notes-detail'),
                url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'), # path that will generate the token
                path('', get_routes, name='routes'),
] 

