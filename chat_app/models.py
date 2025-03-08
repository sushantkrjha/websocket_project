from django.db import models
from django.contrib.auth.models import User

# Model for ChatRoom
class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Room name, unique
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the room is created
    
    def __str__(self):
        return self.name

# Model for Message
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who sent the message
    room = models.ForeignKey(ChatRoom, related_name="messages", on_delete=models.CASCADE)  # The chat room where message is sent
    content = models.TextField()  # Content of the message
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp when message is sent

    def __str__(self):
        return f"Message from {self.user.username} in room {self.room.name}"

    class Meta:
        ordering = ['timestamp']  # Ensure messages are ordered by the time they were sent
