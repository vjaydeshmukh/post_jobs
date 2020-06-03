# Generated by Django 3.0.6 on 2020-06-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('Job_Description', models.TextField()),
                ('Experience', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Salary', models.CharField(max_length=100)),
            ],
        ),
    ]
