from django.db import models
from django.utils import timezone

class Urban_Studies(models.Model):
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

class Writing_and_Rhetoric(models.Model):
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

class African_studies(models.Model):
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

class Buddhism_psychology_mental_health(models.Model):
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

class Caribbean_studies(models.Model):
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

class Equity_studies(models.Model):
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

class Book_and_Media_Studies(models.Model):
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

class Celtic_studies(models.Model):
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

class Christianity_Culture(models.Model):
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

class Medieval_Studies(models.Model):
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

class Ethics_Society_Law(models.Model):
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

class International_Relations(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now)#set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Canadian_Studies(models.Model):
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

class Cognitive_Science(models.Model):
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

class Health_Studies(models.Model):
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

class Creative_Expression_Society(models.Model):
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

class Education_Society(models.Model):
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

class Literature_Critical_Theory(models.Model):
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

class Material_Culture(models.Model):
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

class Renaissance_Studies(models.Model):
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

class Science_and_Society(models.Model):
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

class Semiotics_and_Communication_Studies(models.Model):
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

class Digital_Humanities(models.Model):
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
