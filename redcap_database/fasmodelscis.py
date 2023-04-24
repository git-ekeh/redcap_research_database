from django.db import models
from django.utils import timezone

class Centre_for_Jewish_Studies(models.Model):
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

class Archaeology_Centre(models.Model):
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

class Asian_Institute(models.Model):
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

class Canadian_Institute_for_Theoretical_Astrophysics(models.Model):
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


class Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre(models.Model):
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

class d_etude_de_la_Frances_et_du_monde_francophone(models.Model):
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

class Centre_for_Comparative_Literature(models.Model):
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

class Centre_for_Criminology_and_Sociolegal_studies(models.Model):
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

class Centre_for_Diaspora_and_Transnational_studies(models.Model):
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

class Centre_for_Drama_Theatre_Performance_studies(models.Model):
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

class Centre_for_Entrepreneurship(models.Model):
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

class Centre_for_Ethics(models.Model):
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

class Centre_for_European_Russian_and_Eurasian_studies(models.Model):
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

class Centre_for_Global_Change_Science(models.Model):
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

class Centre_for_Global_Social_Policy(models.Model):
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

class Centre_for_Indigenous_studies(models.Model):
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

class Centre_for_Industrial_Relations_and_Human_Resources(models.Model):
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

class Centre_for_Medieval_Studies(models.Model):
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

class Centre_for_Quantum_Information_and_Quantum_Control(models.Model):
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

class Centre_for_Quantum_materials(models.Model):
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

class Centre_for_Research_in_Early_English_Drama(models.Model):
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

class Centre_for_South_Asian_Studies(models.Model):
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

class Centre_for_the_Study_of_Global_Japan(models.Model):
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

class Centre_for_the_study_of_Korea(models.Model):
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

class Centre_for_the_Study_of_the_United_States(models.Model):
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

class Cinema_studies(models.Model):
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

class India_Innovation_Institute(models.Model):
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

class Institute_for_the_History_and_philosophy_of_science_and_technology(models.Model):
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

class Institute_of_Islamic_Studies(models.Model):
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

class Jackman_Humanities_Building(models.Model):
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

class Koffler_Scientific_Reserve(models.Model):
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

class Centre_for_Sexual_Diversity_Studies(models.Model):
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

class Munk_School_of_Global_Affairs_and_PublicPolicy(models.Model):
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

class Centre_for_Buddhist_Studies(models.Model):
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

class School_of_Cities(models.Model):
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

class School_of_Environment(models.Model):
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

class Statisc_Canada_Research_Data_Centre(models.Model):
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

class Trudeau_Centre_for_PeaceConflictJustice(models.Model):
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

class Women_and_Gender_Studies_Institute(models.Model):
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
