from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name='Username')
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Password')

    # Thêm hai trường này
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')

    def __str__(self):
        return self.username
