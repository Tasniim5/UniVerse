from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from event.models import Event

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile_image = CloudinaryField('image', default='placeholder')
    events = models.ManyToManyField(Event)
    username = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, username=instance.username)
