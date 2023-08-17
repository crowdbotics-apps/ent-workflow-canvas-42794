# Generated by Django 2.2.28 on 2023-08-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.BigIntegerField()),
                ('name', models.TextField(blank=True, null=True)),
                ('contact_information', models.TextField(blank=True, null=True)),
                ('debt', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]