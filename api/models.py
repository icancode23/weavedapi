from django.db import models
class time(models.Model):
	lasttimehour=models.BigIntegerField(null=True)
	lasttimeminute=models.BigIntegerField(null=True)
	proxyadd=models.CharField(max_length=50,blank=True,null=True)


	def __unicode__(self):
	 	return "status"





# Create your models here.
