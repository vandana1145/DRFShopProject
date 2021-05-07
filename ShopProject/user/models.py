from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(models.Model):
#     user = models.OneToOneField(AuthUser, null=True, blank=True, on_delete=models.CASCADE)
#     username = models.CharField(max_length=100, unique=True, verbose_name='User Name', default='username')
#     fname = models.CharField(max_length=100, verbose_name='First Name', default='fname')
#     lname = models.CharField(max_length=100, verbose_name='Last Name', default='lname')
#     profile_photo = models.ImageField(upload_to="profile_images", blank=True)
#     phone = models.CharField(max_length=20, blank=True)

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="media/profile_images", blank=True)
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
       ordering = ['-id']

    # def __str__(self):
    #     return self.user.username

    # def get_absolute_url(self):
    #     return reverse("user_detail", kwargs={"pk": self.pk})
    
