from django.db import models

# Create your models here.

class Plane(models.Model):
	"""docstring for Plane"""
	name = models.CharField(max_length = 50) 
	reg_no = models.CharField(max_length = 50)
	owner = models.CharField(max_length = 50)
	plane_origin = models.CharField(max_length = 50)
	destination = models.CharField(max_length = 50)
	onboard = models.IntegerField(default = 0)
	mis_date = models.DateField()
	mis_location = models.CharField(max_length = 50)
	details = models.CharField(max_length=1000)
	plane_type = models.CharField(max_length=20)

	def __str__(self):
		return self.reg_no 


class Passenger(models.Model):
	plane_no = models.ForeignKey(Plane)
	ps_name = models.CharField(max_length = 50)
	ps_country = models.CharField(max_length = 50)
	ps_ticketno = models.CharField(max_length = 50)
	ps_gender = models.CharField(max_length = 1)
	ps_photo = models.CharField(max_length = 100)
	ps_details = models.CharField(max_length = 500)
	ps_role = models.CharField(max_length = 50) 	

	def __str__(self):
		return self.ps_name