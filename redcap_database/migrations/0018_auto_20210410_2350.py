# Generated by Django 3.0 on 2021-04-10 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcap_database', '0017_auto_20210410_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='african_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='african_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='african_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book_and_media_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book_and_media_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book_and_media_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='buddhism_psychology_mental_health',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='buddhism_psychology_mental_health',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='buddhism_psychology_mental_health',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='canadian_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='canadian_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='canadian_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='caribbean_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='caribbean_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='caribbean_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='celtic_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='celtic_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='celtic_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='christianity_culture',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='christianity_culture',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='christianity_culture',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cognitive_science',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cognitive_science',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cognitive_science',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='creative_expression_society',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='creative_expression_society',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='creative_expression_society',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='digital_humanities',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='digital_humanities',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='digital_humanities',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='education_society',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='education_society',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='education_society',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='equity_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='equity_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='equity_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ethics_society_law',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ethics_society_law',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ethics_society_law',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='health_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='health_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='health_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='international_relations',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='international_relations',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='international_relations',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='literature_critical_theory',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='literature_critical_theory',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='literature_critical_theory',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='material_culture',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='material_culture',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='material_culture',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='medieval_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='medieval_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='medieval_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='renaissance_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='renaissance_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='renaissance_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='science_and_society',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='science_and_society',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='science_and_society',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='semiotics_and_communication_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='semiotics_and_communication_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='semiotics_and_communication_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='urban_studies',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='urban_studies',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='urban_studies',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='writing_and_rhetoric',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='writing_and_rhetoric',
            name='project_begin',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='writing_and_rhetoric',
            name='project_end',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
