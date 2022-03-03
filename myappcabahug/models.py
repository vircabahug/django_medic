from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 20)
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    confirmpassword = models.CharField(max_length = 20)
    class meta:
        db_table  = 'tbluser'

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    timeslot = models.CharField(max_length = 50)
    date = models.DateField(max_length= 20)
    roomtype = models.CharField(max_length= 50)
    class meta:
        db_table  = 'tblreservation'
 
class Conference(models.Model):
    conferenceid  = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    reservation_id = models.ForeignKey(Reservation, on_delete = models.CASCADE)  
    status = models.CharField(max_length=50)
    class meta:
        db_table  = 'tblconference'

        
