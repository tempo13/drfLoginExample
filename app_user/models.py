from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserMbtiHistory(models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mbti')
    mbti = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "t_user_mbti_type"
