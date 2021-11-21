from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 500,default = '')
    category = models.CharField(max_length = 100,default="")
    date = models.DateTimeField(auto_now = True)
    author_name = models.CharField(max_length=500,default = '')
    desc = tinymce_models.HTMLField()
    prgmngImg = models.ImageField(default ='Programming.png', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title + ' Programming' 


# for profile 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True, help_text="Year/Moth/Date")
    profile_image = models.ImageField(default='users/default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Contact(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    messages = tinymce_models.HTMLField()
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name + ' contact'