from django.db import models
from django.utils import timezone

class Medicine_Admin(models.Model):
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

class Obstetrics_and_Gynecology(models.Model):
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

class Family_Community_Medicine(models.Model):
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

class Anesthesiology_pain_and_Medicine(models.Model):
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

class Biochemistry(models.Model):
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

class Biomedical_Engineering(models.Model):
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

class Immunology(models.Model):
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

class Laboratory_Medicine_and_Pathobiology(models.Model):
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

class Medical_Biophysics(models.Model):
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

class Medical_Imaging(models.Model):
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

class Institute_Medical_Science(models.Model):
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

class Molecular_Genetics(models.Model):
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

class Nutritional_Sciences(models.Model):
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

class Occupational_Science_and_Occupational_Therapy(models.Model):
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

class Ophthamalogy_and_Vision_Sciences(models.Model):
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

class Otolaryngology_Head_and_Neck_Surgery(models.Model):
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


class Pediatrics(models.Model):
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

class Pharmacology_and_Toxicology(models.Model):
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

class Physical_Therapy(models.Model):
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

class Physiology(models.Model):
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

class Psychiatry(models.Model):
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

class Radiation_Oncology(models.Model):
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

class Rehabilitation(models.Model):
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

class Speech_Language_Pathology(models.Model):
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

class Surgery(models.Model):
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
