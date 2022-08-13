from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  date_of_birth = models.DateField(blank=True, null=True)
  photo = models.ImageField(blank=True, default='default.jpg', upload_to='users/%Y/%m/%d')
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"Profile for user {self.user.username}"
    
class Contact(models.Model):
  user_from = models.ForiegnKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
  user_to = models.ForiegnKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True, db_index=True)
  
  class Meta:
    ordering = ('-created',)
    
  def __str__(self):
    return f"{self.user_from} followed {self.user_to}"
    
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))