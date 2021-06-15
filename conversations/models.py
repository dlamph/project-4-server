from django.db import models
# from jwt_auth import User 


class Conversation(models.Model):
    text = models.TextField(max_length=700)

    sender = models.ForeignKey(
        'jwt_auth.User',
        related_name="sent_messages",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        'jwt_auth.User',
        related_name="received_messages",
        on_delete = models.CASCADE
    )
    