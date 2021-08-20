from api.permissions import IsOwner
from django.contrib.auth.models import User
from api.models import notes
from rest_framework import generics, permissions
from .serializers import NotesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class NotesList(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    queryset = notes.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = notes.objects.filter(owner = user)
        return queryset

class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

@api_view(['GET'])
def get_routes(request): # separate function to display the available routes for the user to access and test the api
    
    """
    List of available routes that can be tested on Postman.
    """


    routes = [
        'api/v1//notes/ : To view the notes of the logged in user',
        'api/v1/notes/<int:pk>/ : To retrieve, update, or delete the note with the specified primary key',
        '/rest_auth/registration/ : To register a new account using the django_rest_auth package',
        '/rest_auth/login/ : To login to a registered account by providing the username/email-id and password',
        '/account/signup/ : To register a new account by providing username, email-id and password',
        '/account/login/ : To login to an existing account by username and password OR via your Gmail Account',
        '/account/logout/ : To logout of the signed in account',
        '/account/password/change/ : To change the password of the current logged in user', 
    ]
    return Response(routes)


