from django.db import models
from users.models import CustomUser

class notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null = True, blank = True, upload_to = 'api/')
    created = models.DateTimeField(auto_now=True,)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # to show the title of the note in the admin panel, shell, etc.
    def __str__(self) -> str:
        return self.title
