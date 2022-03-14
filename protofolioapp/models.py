from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
# Create your models here.
class Project(models.Model):
    image= models.ImageField( null=True,blank=True)

    heading = models.CharField(max_length=200, null=True,blank=True)
    text = RichTextUploadingField(default="projects")
    time = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.heading
    def save(self,*args,**kwargs):
        if self.slug==None:
            slug=slugify(self.heading)
            hasslug=Project.objects.filter(slug=slug).exists()
            count=1

            while hasslug:
                count+=1
                slug=slugify(self.heading) +"-"+str(count)
                hasslug=Project.objects.filter(slug=slug).exists()

            self.slug=slug


        super().save(*args,**kwargs)
class Message(models.Model):
    name= models.CharField(max_length=200, null=True,blank=True)
    email= models.EmailField(max_length=200, null=True,blank=True)
    subject=models.CharField(max_length=100, null=True,blank=True)
    text = models.TextField(max_length=500, null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)
