from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length= 250 , default=" https://www.clipartkey.com/mpngs/m/152-1520367_user-profile-default-image-png-clipart-png-download.png")
    STUDENT='Student'
    TEACHER ='Teacher'
    USER_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
    )


    def __str__(self):
        return self.username
