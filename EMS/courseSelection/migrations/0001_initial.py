# Generated by Django 2.1.7 on 2019-05-15 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backstage', '0001_initial'),
        ('courseScheduling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('common_score', models.FloatField(default=0)),
                ('final_score', models.FloatField(default=0)),
                ('is_finish', models.BooleanField(default=False)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseScheduling.Teacher_Schedule_result')),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student')),
            ],
            options={
                'db_table': 'course_selected',
            },
        ),
    ]
