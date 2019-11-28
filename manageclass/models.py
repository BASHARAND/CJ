from django.db import models
class Classroom(models.Model):
    num=models.IntegerField()
    max=models.IntegerField()
    proj=models.IntegerField(default=0)

    def __str__(self):
        return str(self.num)
class Course(models.Model):
    num=models.IntegerField()
    name=models.CharField(max_length=30,null=False)
    Chour=models.IntegerField()
    def __str__(self):
        return str(self.num)
class has(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    Class = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=False)
    day = models.CharField(max_length=9,null=False)
    a=models.BooleanField(default=False,blank=True)
    b=models.BooleanField(default=False,blank=True)
    c=models.BooleanField(default=False,blank=True)
    d=models.BooleanField(default=False,blank=True)
    e=models.BooleanField(default=False,blank=True)
    f=models.BooleanField(default=False,blank=True)
    g=models.BooleanField(default=False,blank=True)
    h=models.BooleanField(default=False,blank=True)
    m=models.BooleanField(default=False,blank=True)
    n=models.BooleanField(default=False,blank=True)
    l=models.BooleanField(default=False,blank=True)
    w=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.category


# Create your models here.
