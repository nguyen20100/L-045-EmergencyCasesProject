# Generated by Django 2.0.7 on 2018-08-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_hajj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hajjdata',
            fields=[
                ('id', models.TextField(db_column='ID', primary_key=True, serialize=False)),
                ('first_name', models.TextField(blank=True, db_column='FIRST_NAME', null=True)),
                ('season', models.TextField(blank=True, db_column='SEASON', null=True)),
                ('age', models.TextField(blank=True, db_column='AGE', null=True)),
                ('entry_date', models.TextField(blank=True, db_column='ENTRY_DATE', null=True)),
                ('exit_date', models.TextField(blank=True, db_column='EXIT_DATE', null=True)),
                ('entry_time', models.TextField(blank=True, db_column='ENTRY_TIME', null=True)),
                ('exit_time', models.TextField(blank=True, db_column='EXIT_TIME', null=True)),
                ('gender', models.TextField(blank=True, db_column='GENDER', null=True)),
                ('passport_issue_pla', models.TextField(blank=True, db_column='PASSPORT_ISSUE_PLA', null=True)),
                ('lk_visa_issue_plac', models.TextField(blank=True, db_column='LK_VISA_ISSUE_PLAC', null=True)),
                ('lk_nationality_des', models.TextField(blank=True, db_column='LK_NATIONALITY_DES', null=True)),
                ('lk_airline_name_le', models.TextField(blank=True, db_column='LK_AIRLINE_NAME_LE', null=True)),
            ],
            options={
                'db_table': 'hajjdata',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Hajj',
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
