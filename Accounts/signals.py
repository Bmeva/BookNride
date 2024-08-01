from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile



@receiver(post_save, sender=User) 
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
   
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
       
    else: 
        try: #if the user is updated
            profile = UserProfile.objects.get(user = instance)
            profile.save()
        except: 
            UserProfile.objects.create(user=instance)
            #after creating signal you have to set the ready function in the apps.py

#post_save.connect(post_save_create_profile_receiver, sender=User) #this is also a decorator and would also work 


#this is for presave but was not used. It works before the user is created
@receiver(pre_save, sender=User) 
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')