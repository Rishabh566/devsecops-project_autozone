from django.db import models

# Create your models here.

class Team(models.Model):
	first_name= models.CharField(max_length=245)
	last_name= models.CharField(max_length=245)
	designation= models.CharField(max_length=245)
	photo= models.ImageField(upload_to='photos/%Y/%m/%d/')
	facebook_link= models.CharField(max_length=100)
	twitter_link= models.CharField(max_length=100)
	google_plus_link= models.CharField(max_length=100)
	created_date= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name