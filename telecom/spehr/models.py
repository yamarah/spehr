from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os
from django.urls import reverse

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Orginization(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=400,blank=True)



    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse("spehr:orgin_list",kwargs={'slug':self.slug})




def save_emp_image(instance,filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.emp_id:
        filename = 'Empolyee_pictures/{}.{}'.format(instance.emp_id,ext)
    return os.path.join(upload_to,filename)


class Empolyee(models.Model):
    emp_id = models.CharField(max_length=100,unique=True)
    Orginization_name = models.ForeignKey(Orginization,on_delete=models.CASCADE,related_name='empolyees')
    full_name = models.CharField(max_length=200,blank=True)
    father_name = models.CharField(max_length=200,blank=True)
    designation = models.CharField(max_length=200,blank=True)
    create_at = models.DateTimeField(auto_now_add =True,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    id_card_NO = models.IntegerField(null=True,blank=True)
    volume_NO = models.IntegerField(null=True,blank=True)
    page_NO = models.IntegerField(null=True,blank=True)
    id_card_pic = models.ImageField(null=True,blank=True,verbose_name='ID Image')
    all_contacts = models.IntegerField(null=True,blank=True)
    emp_pic = models.ImageField(null=True,blank=True,verbose_name='emp pic')



    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        return reverse("spehr:emp_detail",kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        self.slug = slugify(self.full_name)
        super().save(*args,**kwargs)
    # def get_absolute_url(self):
    #     return reverse("spehr:detail",kwargs={'slug':self.slug})
    # def get_absolute_url(self):
    #     return reverse('spehr:empolyee_detail', args=[str(self.id)])
        # return reverse("spehr:orgin_list", kwargs={"slug": self.slug})

    # def get_absolute_url(self):
    #     return reverse('spehr:empolyee_detail',kwargs={'slug':self.empolyee.slug, 'orginization':self.orginization.slug})

class Identify(models.Model):
    empoly = models.ForeignKey(Empolyee,on_delete=models.CASCADE,related_name='empolys')
    gsm = models.IntegerField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    full_ismi = models.IntegerField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse("spehr:identifydetail",kwargs={'slug':self.slug})



    # class Meta:
    #     ordering = ['position']
    def __str__(self):
        return str(self.gsm)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.gsm)
        super().save(*args,**kwargs)
