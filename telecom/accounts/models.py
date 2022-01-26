from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

def path_and_rename(instance,filename):
    upload_to = 'Images/'
    ext= filename.split('.')[-1]
    if instance.user.username:
        filename = 'User_profile_picture/{}.{}'.format(instance.user.username,ext)
    return os.path.join(upload_to,filename)

class UserPro(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to=path_and_rename,verbose_name="profile_picture",blank=True)

    teacher = 'teacher '
    student = 'student'
    parent = 'parent'

    user_types = [
        (teacher , 'teacher'),
        (student , 'student'),
        (parent , 'parent'),
    ]
    user_type = models.CharField(max_length=20, choices=user_types,default=student)

    def __str__(self):
        return self.user.username
