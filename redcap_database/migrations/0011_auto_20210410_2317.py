# Generated by Django 3.0 on 2021-04-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcap_database', '0010_auto_20210410_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architecture',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='convocation_office',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='dala_lana_school_of_public_health',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='data_governance_group',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='dentistry',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='electrical_computer_eng',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='harthouse',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='health_policy_management_evaluation',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='health_wellness',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='information',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='kinesiology',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='law',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='mechanical_industrial_eng',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='music',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='nursing',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='ontario_institute_for_studies_in_education',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='pharmacy',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='research_oversight_compliance',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='rotman',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='social_work',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='utm',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='utsc',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='utsclibrary',
            name='user_name',
        ),
        migrations.AddField(
            model_name='architecture',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='architecture',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='architecture',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='architecture',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='convocation_office',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='convocation_office',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='convocation_office',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='convocation_office',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='dala_lana_school_of_public_health',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='dala_lana_school_of_public_health',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='dala_lana_school_of_public_health',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='dala_lana_school_of_public_health',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='data_governance_group',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='data_governance_group',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='data_governance_group',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='data_governance_group',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='dentistry',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='dentistry',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='dentistry',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='dentistry',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='electrical_computer_eng',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='electrical_computer_eng',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='electrical_computer_eng',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='electrical_computer_eng',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='harthouse',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='harthouse',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='harthouse',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='harthouse',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='health_policy_management_evaluation',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='health_policy_management_evaluation',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='health_policy_management_evaluation',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='health_policy_management_evaluation',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='health_wellness',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='health_wellness',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='health_wellness',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='health_wellness',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='information',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='information',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='information',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='information',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='kinesiology',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='kinesiology',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='kinesiology',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='kinesiology',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='law',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='law',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='law',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='law',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='mechanical_industrial_eng',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='mechanical_industrial_eng',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='mechanical_industrial_eng',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='mechanical_industrial_eng',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='music',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='music',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='music',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='music',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='nursing',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='nursing',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='nursing',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='nursing',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='ontario_institute_for_studies_in_education',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ontario_institute_for_studies_in_education',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='ontario_institute_for_studies_in_education',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='ontario_institute_for_studies_in_education',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='research_oversight_compliance',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='research_oversight_compliance',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='research_oversight_compliance',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='research_oversight_compliance',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='rotman',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='rotman',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='rotman',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='rotman',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='social_work',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='social_work',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='social_work',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='social_work',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='utm',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='utm',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='utm',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='utm',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='utsc',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='utsc',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='utsc',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='utsc',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='utsclibrary',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='utsclibrary',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='utsclibrary',
            name='project_begin',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='utsclibrary',
            name='project_end',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='architecture',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='architecture',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='architecture',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='convocation_office',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='convocation_office',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='convocation_office',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dala_lana_school_of_public_health',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='dala_lana_school_of_public_health',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dala_lana_school_of_public_health',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data_governance_group',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='data_governance_group',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data_governance_group',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dentistry',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='dentistry',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dentistry',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electrical_computer_eng',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='electrical_computer_eng',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electrical_computer_eng',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='harthouse',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='harthouse',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='harthouse',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='health_policy_management_evaluation',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='health_policy_management_evaluation',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='health_policy_management_evaluation',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='health_wellness',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='health_wellness',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='health_wellness',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='information',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kinesiology',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='kinesiology',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kinesiology',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='law',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='law',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='law',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mechanical_industrial_eng',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='mechanical_industrial_eng',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mechanical_industrial_eng',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='music',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nursing',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='nursing',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nursing',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ontario_institute_for_studies_in_education',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='ontario_institute_for_studies_in_education',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ontario_institute_for_studies_in_education',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='research_oversight_compliance',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='research_oversight_compliance',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='research_oversight_compliance',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rotman',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='rotman',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rotman',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social_work',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='social_work',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social_work',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utm',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='utm',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utm',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utsc',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='utsc',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utsc',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utsclibrary',
            name='date_recorded',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='utsclibrary',
            name='etoken_use',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utsclibrary',
            name='mfa_use',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
