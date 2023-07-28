from user_models import UserProfile
from django.db import models
# Nhập mô hình UserProfile từ mô-đun user_models

# Tạo mô hình của bạn ở đây.

class MyModel(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)







