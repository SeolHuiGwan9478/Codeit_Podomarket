from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import *

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=15,
        validators=[validate_no_special_characters]
    )
    kakao_id = models.CharField(max_length=20,
        validators=[validate_no_special_characters]
    )
    address = models.CharField(max_length=40,
        validators=[validate_no_special_characters]
    )
    profile_pic = models.ImageField(upload_to="profile_pic", default="default_profile_pic.jpg")
    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=60)
    item_price = models.IntegerField()

    CONDITION_CHOICES = [
        ('새재품', '새제품'),
        ('최상', '최상'),
        ('상', '상'),
        ('중', '중'),
        ('하', '하'),
    ]

    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=None)
    item_details = models.TextField()
    image1 = models.ImageField(upload_to='item_pics')
    image2 = models.ImageField(upload_to='item_pics', blank = True)
    image3 = models.ImageField(upload_to='item_pics', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    