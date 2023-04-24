from django.db import models
from django.utils import timezone


class Applied_Science_Engineering(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Architecture(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    roject_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Convocation_Office(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    roject_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Dala_Lana_School_of_Public_Health(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    roject_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Data_Governance_Group(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    roject_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Dentistry(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Electrical_Computer_Eng(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Harthouse(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Information(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Health_Policy_Management_Evaluation(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Health_Wellness(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Law(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Mechanical_Industrial_Eng(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Music(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Nursing(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Ontario_Institute_for_Studies_in_Education(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Pharmacy(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Research_Oversight_Compliance(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Rotman(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class Social_Work(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class UTM(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class UTSClibrary(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
class UTSC(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Kinesiology(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)
