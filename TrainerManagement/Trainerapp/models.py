from django.db import models

# Create your models here.
class City(models.Model):
    objects = None
    city_name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.city_name}"

class Course(models.Model):
    course_name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.course_name}"

class Trainer_Register(models.Model):
    tname=models.CharField(max_length=30)
    tage=models.IntegerField(max_length=5)
    tphone=models.BigIntegerField()
    tpswd=models.CharField(max_length=20)
    temail=models.CharField(max_length=50)
    tcity=models.ForeignKey(City,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'{self.tname}'

    # def __str__(self):
    #     return f'{self.tname},{self.tage},{self.tphone},{self.tpswd},{self.temail}'

class Trainer_Assign(models.Model):
    tname = models.ForeignKey(Trainer_Register,on_delete=models.CASCADE,default=None)
    batchno = models.IntegerField(max_length=5)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.batchno},{self.date}'

