from django.db import models



# Create your models here.

class Title(models.Model):
	title= models.CharField(max_length=255)
	priority = models.IntegerField(default=0, null=False)
	def __str__(self):
		return self.title


class Member(models.Model):
	title = models.ForeignKey(Title, on_delete = models.CASCADE)
	name  = models.CharField(max_length=255)
	phone = models.CharField(max_length=10)
	email = models.TextField(null=True)
	image = models.ImageField(upload_to = "team", default='default.jpg', blank=True)
	url   = models.CharField(max_length=255, default="#")
	

	def __str__(self):
		return self.name

class Image(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert');
	image		= models.ImageField(upload_to = "gallery", default='default.jpg', blank=True)

	def __str__(self):
		return self.title

class nustartup(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert');
	organised   = models.TextField(default='insert');
	logo		= models.ImageField(upload_to = "events",default='default.jpg', blank=True)
	
	
	def __str__(self):
		return self.title

class Createevents(models.Model):
	title = models.CharField(max_length=225)
	description = models.TextField(default='insert');
	organised = models.TextField(default='insert');
	logo = models.ImageField(upload_to ="media",default='default.jpg', blank=True)

	def __str__(self):
		return self.title



class join(models.Model):
	first_name = models.CharField(max_length=50)
	event_name  = models.CharField(max_length=50)
	email      = models.EmailField()
	enrollment_no  = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=20)

	

	def __str__(self):
		return self.first_name+'_____________'+self.event_name


class house(models.Model):
	first_name = models.CharField(max_length=50)
	event_name  = models.CharField(max_length=50)
	email      = models.EmailField()
	enrollment_no  = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=20)

	

	def __str__(self):
		return self.first_name+'_____________'+self.event_name



class contact(models.Model):
	first_name = models.CharField(max_length=225)
	write_your_message_here = models.CharField(max_length=225)
	email      = models.EmailField()
	phone_number = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name
