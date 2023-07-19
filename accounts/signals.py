from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender,instance,created, **kwargs):
    if created:
        print('User created create user profile')
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            profile = UserProfile.objects.create(user=instance)
            
@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
  
    