# Generated by Django 4.2.6 on 2023-11-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0004_databasedb_alter_registertable_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('phone_number', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=7)),
                ('confirm_password', models.CharField(max_length=7)),
            ],
        ),
        migrations.DeleteModel(
            name='databasedb',
        ),
        migrations.DeleteModel(
            name='RegisterTable',
        ),
    ]
