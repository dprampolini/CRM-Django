from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Ereditarietà da User e in on_delete si comporta come Model
    #Seguono i campi che si vogliono aggiungere al modello User già esistente
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

    #Funzione che definisce come si visualizza il Profilo dalla console admin
    def __str__(self):
        return '%s - %s %s' % (self.user.username,self.user.first_name, self.user.last_name)

#Ricezione dei segnali

#Quando viene creato un User crea anche un Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#Quando viene creato un User il profile viene anche salvato
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()