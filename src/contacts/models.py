from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL  # -> "auth_user"


# Create your models here.
class Contact(models.Model):  # django -> database table -> migrations
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Deletes user and contacts
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # sets deleted User's contacts to null
    email = models.EmailField()
    notes = models.TextField(blank=True, default="")
