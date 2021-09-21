from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    confirmpassword = models.CharField(max_length = 20)
    class meta:
        db_table  = 'tbluser'

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    date = models.DateField(max_length= 20)
    gender = models.CharField(max_length= 6)
    address = models.CharField(max_length= 50)
    message = models.CharField(max_length= 100)
    class meta:
        db_table  = 'tblappointment'
 
class StaffList(models.Model):
    seqid  = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    appointment_id = models.ForeignKey(Appointment, on_delete = models.CASCADE)  
    class meta:
        db_table  = 'tblstafflist'

        
