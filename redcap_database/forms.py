from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from datetimewidget.widgets import DateTimeWidget
from redcap_database.models import (Applied_Science_Engineering,
Architecture,
Convocation_Office,
Dala_Lana_School_of_Public_Health,
Data_Governance_Group,
Dentistry,
Electrical_Computer_Eng,
Harthouse,
Information,
Health_Policy_Management_Evaluation,
Health_Wellness,
Law,
Mechanical_Industrial_Eng,
Music,
Nursing,
Ontario_Institute_for_Studies_in_Education,
Pharmacy,
Research_Oversight_Compliance,
Rotman,
Social_Work,
UTM,
UTSClibrary,
UTSC)

from redcap_database.fasmodels import(Anthropology,
Art_History,
Astronomy_Astrophysics,
Cells_and_Systems_Biology,
Chemistry,
Classics,
Computer_Science,
Earth_Sciences,
East_Asian_Studies,
Ecology_and_Evolutionary_Biology,
Economics,
English,
French,
Geography_and_Planning,
Germanic_Language_and_Literature,
History,
Italian_Studies,
Linguistics,
Mathematics,
Near_and_Middle_Eastern_Civilizations,
Philosophy,
Physics,
Political_Science,
Psychology,
Religion,
Slavic_Languages_and_Literatures,
Sociology,
Spanish_and_Portuguese,
Statistical_Sciences)

from redcap_database.fasmodelscis import (Centre_for_Jewish_Studies,
Archaeology_Centre,
Asian_Institute,
Canadian_Institute_for_Theoretical_Astrophysics,
Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre,
d_etude_de_la_Frances_et_du_monde_francophone,
Centre_for_Comparative_Literature,
Centre_for_Criminology_and_Sociolegal_studies,
Centre_for_Diaspora_and_Transnational_studies,
Centre_for_Drama_Theatre_Performance_studies,
Centre_for_Entrepreneurship,
Centre_for_Ethics,
Centre_for_European_Russian_and_Eurasian_studies,
Centre_for_Global_Change_Science,
Centre_for_Global_Social_Policy,
Centre_for_Indigenous_studies,
Centre_for_Industrial_Relations_and_Human_Resources,
Centre_for_Medieval_Studies,
Centre_for_Quantum_Information_and_Quantum_Control,
Centre_for_Quantum_materials,
Centre_for_Research_in_Early_English_Drama,
Centre_for_South_Asian_Studies,
Centre_for_the_Study_of_Global_Japan,
Centre_for_the_study_of_Korea,
Centre_for_the_Study_of_the_United_States,
Cinema_studies,
India_Innovation_Institute,
Institute_for_the_History_and_philosophy_of_science_and_technology,
Institute_of_Islamic_Studies,
Jackman_Humanities_Building,
Koffler_Scientific_Reserve,
Centre_for_Sexual_Diversity_Studies,
Munk_School_of_Global_Affairs_and_PublicPolicy,
Centre_for_Buddhist_Studies,
School_of_Cities,
School_of_Environment,
Statisc_Canada_Research_Data_Centre,
Trudeau_Centre_for_PeaceConflictJustice,
Women_and_Gender_Studies_Institute)

from redcap_database.fasmodelscoll import(Urban_Studies,
Writing_and_Rhetoric,
African_studies,
Buddhism_psychology_mental_health,
Caribbean_studies,
Equity_studies,
Book_and_Media_Studies,
Celtic_studies,
Christianity_Culture,
Medieval_Studies,
Ethics_Society_Law,
International_Relations,
Canadian_Studies,
Cognitive_Science,
Health_Studies,
Creative_Expression_Society,
Education_Society,
Literature_Critical_Theory,
Material_Culture,
Renaissance_Studies,
Science_and_Society,
Semiotics_and_Communication_Studies,
Digital_Humanities)

from redcap_database.fommodels import(Medicine_Admin,
Obstetrics_and_Gynecology,
Family_Community_Medicine,
Anesthesiology_pain_and_Medicine,
Biochemistry,
Biomedical_Engineering,
Immunology,
Laboratory_Medicine_and_Pathobiology,
Medical_Biophysics,
Medical_Imaging,
Institute_Medical_Science,
Molecular_Genetics,
Nutritional_Sciences,
Occupational_Science_and_Occupational_Therapy,
Ophthamalogy_and_Vision_Sciences,
Otolaryngology_Head_and_Neck_Surgery,
Pediatrics,
Pharmacology_and_Toxicology,
Physical_Therapy,
Physiology,
Psychiatry,
Radiation_Oncology,
Rehabilitation,
Speech_Language_Pathology,
Surgery)

#   Original Faculty forms from .models file

class Applied_Science_Engineering(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Applied_Science_Engineering
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Architecture(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Architecture
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Convocation_Office(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Convocation_Office
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Dala_Lana_School_of_Public_Health(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Dala_Lana_School_of_Public_Health
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Data_Governance_Group(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Data_Governance_Group
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Dentistry(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Dentistry
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Electrical_Computer_Eng(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Electrical_Computer_Eng
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Harthouse(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Harthouse
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Information(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Information
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }
class Health_Policy_Management_Evaluation(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Health_Policy_Management_Evaluation
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Health_Wellness(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Health_Wellness
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Law(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Law
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Mechanical_Industrial_Eng(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Mechanical_Industrial_Eng
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Music(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Music
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Nursing(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Nursing
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Ontario_Institute_for_Studies_in_Education(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Ontario_Institute_for_Studies_in_Education
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Pharmacy(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Pharmacy
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Research_Oversight_Compliance(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Research_Oversight_Compliance
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Rotman(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Rotman
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Social_Work(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Social_Work
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }
class UTM(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = UTM
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class UTSClibrary(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = UTSClibrary
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class UTSC(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = UTSC
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

# below are the Department forms from the Faculty of Arts and Science

class Anthropology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Anthropology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Art_History(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Art_History
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Astronomy_Astrophysics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Astronomy_Astrophysics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Cells_and_Systems_Biology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Cells_and_Systems_Biology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Chemistry(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Chemistry
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Classics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Classics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Computer_Science(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Computer_Science
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Earth_Sciences(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Earth_Sciences
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class East_Asian_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = East_Asian_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Ecology_and_Evolutionary_Biology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Ecology_and_Evolutionary_Biology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Economics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Economics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class English(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = English
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class French(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = French
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Geography_and_Planning(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Geography_and_Planning
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Germanic_Language_and_Literature(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Germanic_Language_and_Literature
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class History(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = History
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Italian_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Italian_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Linguistics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Linguistics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Mathematics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Mathematics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Near_and_Middle_Eastern_Civilizations(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Near_and_Middle_Eastern_Civilizations
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Philosophy(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Philosophy
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Physics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Physics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Political_Science(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Political_Science
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Psychology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Psychology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Religion(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Religion
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Slavic_Languages_and_Literatures(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Slavic_Languages_and_Literatures
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Sociology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Sociology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Spanish_and_Portuguese(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Spanish_and_Portuguese
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Statistical_Sciences(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Statistical_Sciences
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


# below are the FAS tables from fasmodelscis

class Centre_for_Jewish_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Jewish_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Archaeology_Centre(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Archaeology_Centre
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Asian_Institute(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Asian_Institute
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Canadian_Institute_for_Theoretical_Astrophysics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Canadian_Institute_for_Theoretical_Astrophysics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Canadian_Statistical_Sciences_Institute_Ontario_Regional_Centre
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class d_etude_de_la_Frances_et_du_monde_francophone(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = d_etude_de_la_Frances_et_du_monde_francophone
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Comparative_Literature(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Comparative_Literature
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Criminology_and_Sociolegal_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Criminology_and_Sociolegal_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Diaspora_and_Transnational_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Diaspora_and_Transnational_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Drama_Theatre_Performance_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Drama_Theatre_Performance_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Entrepreneurship(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Entrepreneurship
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Centre_for_Ethics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Ethics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_European_Russian_and_Eurasian_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_European_Russian_and_Eurasian_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Global_Change_Science(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Global_Change_Science
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Global_Social_Policy(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Global_Social_Policy
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Indigenous_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Indigenous_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Industrial_Relations_and_Human_Resources(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Industrial_Relations_and_Human_Resources
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Centre_for_Medieval_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Medieval_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Quantum_Information_and_Quantum_Control(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Quantum_Information_and_Quantum_Control
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Quantum_materials(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Quantum_materials
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Research_in_Early_English_Drama(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Research_in_Early_English_Drama
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_South_Asian_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_South_Asian_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_the_Study_of_Global_Japan(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_the_Study_of_Global_Japan
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_the_study_of_Korea(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_the_study_of_Korea
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_the_Study_of_the_United_States(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_the_Study_of_the_United_States
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Cinema_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Cinema_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class India_Innovation_Institute(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = India_Innovation_Institute
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Institute_for_the_History_and_philosophy_of_science_and_technology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Institute_for_the_History_and_philosophy_of_science_and_technology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Institute_of_Islamic_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Institute_of_Islamic_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Jackman_Humanities_Building(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Jackman_Humanities_Building
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Koffler_Scientific_Reserve(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Koffler_Scientific_Reserve
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Sexual_Diversity_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Sexual_Diversity_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Munk_School_of_Global_Affairs_and_PublicPolicy(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Munk_School_of_Global_Affairs_and_PublicPolicy
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Centre_for_Buddhist_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Centre_for_Buddhist_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class School_of_Cities(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = School_of_Cities
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class School_of_Environment(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = School_of_Environment
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Statisc_Canada_Research_Data_Centre(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Statisc_Canada_Research_Data_Centre
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Trudeau_Centre_for_PeaceConflictJustice(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Trudeau_Centre_for_PeaceConflictJustice
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Women_and_Gender_Studies_Institute(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Women_and_Gender_Studies_Institute
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

# below are the tables associated with the College system at UofT

class Urban_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Urban_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Writing_and_Rhetoric(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Writing_and_Rhetoric
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class African_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = African_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Buddhism_psychology_mental_health(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Buddhism_psychology_mental_health
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Caribbean_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Caribbean_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Equity_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Equity_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Book_and_Media_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Book_and_Media_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Celtic_studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Celtic_studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Christianity_Culture(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Christianity_Culture
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Medieval_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Medieval_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Ethics_Society_Law(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Ethics_Society_Law
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class International_Relations(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = International_Relations
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Canadian_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Canadian_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Cognitive_Science(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Cognitive_Science
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Health_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Health_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Creative_Expression_Society(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Creative_Expression_Society
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Education_Society(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Education_Society
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Literature_Critical_Theory(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Literature_Critical_Theory
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Material_Culture(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Material_Culture
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Renaissance_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Renaissance_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Science_and_Society(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Science_and_Society
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }


class Semiotics_and_Communication_Studies(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Semiotics_and_Communication_Studies
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Digital_Humanities(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Digital_Humanities
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

# Below are the tables from .fommodela file

class Medicine_Admin(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Medicine_Admin
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Obstetrics_and_Gynecology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Obstetrics_and_Gynecology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Family_Community_Medicine(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Family_Community_Medicine
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Anesthesiology_pain_and_Medicine(forms.ModelForm):
    nfirst_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Anesthesiology_pain_and_Medicine
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Biochemistry(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Biochemistry
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Biomedical_Engineering(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Biomedical_Engineering
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Immunology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Immunology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Laboratory_Medicine_and_Pathobiology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Laboratory_Medicine_and_Pathobiology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Medical_Biophysics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Medical_Biophysics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Medical_Imaging(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Medical_Imaging
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Institute_Medical_Science(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Institute_Medical_Science
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Molecular_Genetics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Molecular_Genetics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Nutritional_Sciences(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Nutritional_Sciences
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Occupational_Science_and_Occupational_Therapy(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Occupational_Science_and_Occupational_Therapy
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Ophthamalogy_and_Vision_Sciences(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Ophthamalogy_and_Vision_Sciences
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Otolaryngology_Head_and_Neck_Surgery(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Otolaryngology_Head_and_Neck_Surgery
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Pediatrics(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Pediatrics
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Pharmacology_and_Toxicology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Pharmacology_and_Toxicology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Physical_Therapy(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Physical_Therapy
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Physiology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Physiology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Psychiatry(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Psychiatry
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Radiation_Oncology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Radiation_Oncology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Rehabilitation(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Rehabilitation
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Speech_Language_Pathology(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Speech_Language_Pathology
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }

class Surgery(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label="Last Name")
    etoken_user = forms.BooleanField(required = False, label="Etoken Use")
    mfa_use = forms.BooleanField(required = False, label="MFA Use")
    usage_type = forms.CharField(label="Usage Type")
    email = forms.EmailField(label="Email")
    utorid = forms.CharField(label="UTORid")
    project_begin = forms.DateTimeField(label="Project Start Date")
    project_end = forms.DateTimeField(label="Project End Date")
    date = forms.DateTimeField(label="Date") # date just time stamp the date they are using

    class Meta: #tells django which model should be used to create the form
        model = Surgery
        fields = ('first_name','last_name','etoken_user', 'mfa_use','usage_type','email','utorid','date', 'project_begin', 'project_end')
        widgets = {
        'datetime':DateTimeWidget(attrs={'id':'UTC' },usel10n=True, bootstrap_version=4)
        }
