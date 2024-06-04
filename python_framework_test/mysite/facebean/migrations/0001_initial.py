# Generated by Django 5.0.6 on 2024-06-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('username', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=200)),
            ],
        ),
    ]