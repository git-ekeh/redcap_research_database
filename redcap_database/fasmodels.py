from django.db import models
from django.utils import timezone

class Anthropology(models.Model):
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

class Art_History(models.Model):
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

class Astronomy_Astrophysics(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now)
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Cells_and_Systems_Biology(models.Model):
    first_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    utorid        = models.CharField(max_length = 20)

class Chemistry(models.Model):
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

class Classics(models.Model):
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

class Computer_Science(models.Model):
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

class Earth_Sciences(models.Model):
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

class East_Asian_Studies(models.Model):
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

class Ecology_and_Evolutionary_Biology(models.Model):
    ufirst_name    = models.CharField(max_length = 20, default = "")
    last_name     = models.CharField(max_length = 30, default= "")
    etoken_use    = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    mfa_use       = models.BooleanField(blank=True, null= True) # will allow the database to record a null in the database if left blank
    usage_type    = models.CharField(max_length = 100)
    project_begin = models.DateField(default=None)
    project_end   = models.DateField(default=None)
    date_recorded = models.DateTimeField(default=timezone.now) #set the time stamp to current date and time
    email         = models.EmailField(max_length = 150)
    utorid        = models.CharField(max_length = 20)

class Economics(models.Model):
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

class English(models.Model):
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

class French(models.Model):
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

class Geography_and_Planning(models.Model):
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

class Germanic_Language_and_Literature(models.Model):
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

class History(models.Model):
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

class Italian_Studies(models.Model):
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

class Linguistics(models.Model):
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

class Mathematics(models.Model):
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

class Near_and_Middle_Eastern_Civilizations(models.Model):
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

class Philosophy(models.Model):
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

class Physics(models.Model):
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

class Political_Science(models.Model):
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

class Psychology(models.Model):
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

class Religion(models.Model):
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

class Slavic_Languages_and_Literatures(models.Model):
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

class Sociology(models.Model):
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

class Spanish_and_Portuguese(models.Model):
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

class Statistical_Sciences(models.Model):
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
