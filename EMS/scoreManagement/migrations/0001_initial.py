# Generated by Django 2.1.3 on 2019-05-13 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backstage', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.CharField(max_length=9)),
                ('cname', models.CharField(max_length=128)),
                ('course_type', models.CharField(max_length=128, null=True)),
                ('score', models.FloatField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.College')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('commen_score', models.FloatField(default=0)),
                ('final_score', models.FloatField(default=0)),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student')),
            ],
            options={
                'db_table': 'course_score',
            },
        ),
        migrations.CreateModel(
            name='EvaluationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.IntegerField(default=0)),
                ('item2', models.IntegerField(default=0)),
                ('item3', models.IntegerField(default=0)),
                ('item4', models.IntegerField(default=0)),
                ('item5', models.IntegerField(default=0)),
                ('item6', models.IntegerField(default=0)),
                ('item7', models.IntegerField(default=0)),
                ('item8', models.IntegerField(default=0)),
                ('description', models.TextField(default='无')),
                ('sum', models.FloatField(default=0)),
                ('is_finish', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'evaluation_form',
            },
        ),
        migrations.CreateModel(
            name='MajorCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_total', models.IntegerField()),
                ('hour_class', models.IntegerField()),
                ('hour_other', models.IntegerField()),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('exam_method', models.BooleanField(default=True)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.Course')),
                ('mno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorPlan')),
            ],
            options={
                'db_table': 'major_courses',
            },
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('mcno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.MajorCourses')),
                ('tno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher')),
            ],
            options={
                'db_table': 'teaching_table',
            },
        ),
        migrations.AddField(
            model_name='evaluationform',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.MajorCourses'),
        ),
        migrations.AddField(
            model_name='evaluationform',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backstage.Student'),
        ),
        migrations.AddField(
            model_name='evaluationform',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher'),
        ),
        migrations.AddField(
            model_name='coursescore',
            name='teaching',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.Teaching'),
        ),
        migrations.AlterUniqueTogether(
            name='teaching',
            unique_together={('tno', 'mcno')},
        ),
        migrations.AlterUniqueTogether(
            name='majorcourses',
            unique_together={('cno', 'mno', 'year', 'semester')},
        ),
        migrations.AlterUniqueTogether(
            name='coursescore',
            unique_together={('teaching', 'sno')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('cno', 'cname', 'course_type')},
        ),
    ]
