from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
	user = models.CharField(max_length = 70)
	contact  = models.CharField(max_length = 10)
	branch = models.CharField(max_length = 500, blank=False, null=False)
	github=models.CharField(max_length=200, blank=False, null=False)
	linkedin = models.CharField(max_length=1000, blank=False, null=False)
	tenth_school = models.CharField(max_length =500)
	tenth_year = models.CharField(max_length=10)
	tenth_percent = models.CharField(max_length = 7)
	twelve_school = models.CharField(max_length=500)
	twelve_year = models.CharField(max_length=10)
	twelve_percent = models.CharField(max_length=7)
	college=models.CharField(max_length=200, blank=False, null=True)
	btechmarks = models.CharField(max_length = 100)
	year=models.CharField(max_length=10)
	skills_set = models.CharField(max_length = 10000, blank=True, null=True)
	project_title = models.CharField(max_length = 1000, blank=True, null=True)
	project_desc = models.CharField(max_length  = 10000, blank=True, null=True)
	exp_title=models.CharField(max_length=10000, blank=True, null=True)
	exp_desc = models.CharField(max_length = 10000, blank=True, null=True)
	achieve_title = models.CharField(max_length = 10000, blank=True, null=True)
	achieve_desc = models.CharField(max_length=10000, blank=True, null=True)
	achieve_year=models.CharField()
	certification_title = models.CharField(max_length=10000, blank=True, null=True)
	certification_desc= models.CharField(max_length=10000, blank=True, null=True)
	interest_desc = models.CharField(max_length = 10000)
	recommend=models.TextField()
	cv=models.FileField()
