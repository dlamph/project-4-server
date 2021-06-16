from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # NEED TO ADD THE REVIEW TO THE USER PROFILE (TEACHER OR STUDENT). Is this doing it?
    user = models.ForeignKey(
    'jwt_auth.User',
    related_name='reviews_received',
    on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
    'jwt_auth.User',
    related_name='reviews_posted',
    on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Comment {self.id} on {self.user}'
