# Generated by Django 3.1.4 on 2021-05-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_order_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]