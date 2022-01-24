from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here
class Profile(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True, blank=True)
    last_name = models.CharField(max_length=200,null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "user_profile"


class Role(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isPdfDownload = models.BooleanField(default=True)
    apiCurrentLimit = models.IntegerField(default=10)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "user_role"