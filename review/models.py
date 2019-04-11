from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50,primary_key=True)


class Review(models.Model):
    title = models.CharField(max_length=64)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    summary = models.TextField(validators=[MaxLengthValidator(10000)])
    ip_address = models.CharField(max_length=64)
    submission_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,to_field='name')
    user = models.ForeignKey(User, on_delete=models.CASCADE,to_field='username')
