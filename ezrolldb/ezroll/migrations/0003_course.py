# Generated by Django 4.1.7 on 2023-02-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezroll', '0002_rename_members_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TERM_CODE', models.IntegerField()),
                ('CRN', models.IntegerField()),
                ('TERM_DESC', models.CharField(max_length=255)),
                ('SUBJ_CODE', models.CharField(max_length=255)),
                ('SUBJ_DESC', models.CharField(max_length=255)),
                ('CRSE_NUM', models.IntegerField()),
                ('SEQ_NUM', models.IntegerField()),
                ('XLST_GROUP', models.IntegerField()),
                ('MAX_ENRL', models.IntegerField()),
                ('CREDIT_HR', models.IntegerField()),
                ('COLL_DESC', models.CharField(max_length=255)),
                ('DEPT_DESC', models.CharField(max_length=255)),
                ('BLDG_DESC', models.CharField(max_length=255)),
                ('ROOM_CODE', models.IntegerField()),
                ('BEGIN_TIME', models.IntegerField()),
                ('END_TIME', models.IntegerField()),
                ('START_DATE', models.IntegerField()),
                ('END_DATE', models.IntegerField()),
                ('SUN_DAY', models.CharField(max_length=20)),
                ('MON_DAY', models.CharField(max_length=20)),
                ('TUE_DAY', models.CharField(max_length=20)),
                ('WED_DAY', models.CharField(max_length=20)),
                ('THU_DAY', models.CharField(max_length=20)),
                ('FRI_DAY', models.CharField(max_length=20)),
                ('SAT_DAY', models.CharField(max_length=20)),
                ('HRS_WEEK', models.CharField(max_length=20)),
            ],
        ),
    ]