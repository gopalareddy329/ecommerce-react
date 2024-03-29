# Generated by Django 5.0.2 on 2024-03-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_marital_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_Birth', models.CharField(blank=True, max_length=20, null=True)),
                ('Marital_Status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Together', 'Together'), ('Divorced', 'Divorced'), ('Widow', 'Widow'), ('Alone', 'Alone'), ('Absurd', 'Absurd'), ('YOLO', 'YOLO')], max_length=20, null=True)),
                ('Education', models.CharField(blank=True, choices=[('Graduation', 'Graduation'), ('PhD', 'PhD'), ('Master', 'Master'), ('Basic', 'Basic'), ('2n Cycle', '2n Cycle')], max_length=20, null=True)),
                ('Income', models.CharField(blank=True, max_length=20, null=True)),
                ('Dt_Customer', models.DateField(blank=True, null=True)),
                ('MntWines', models.PositiveIntegerField(default=0)),
                ('MntFruits', models.PositiveIntegerField(default=0)),
                ('MntMeatProducts', models.PositiveIntegerField(default=0)),
                ('MntFishProducts', models.PositiveIntegerField(default=0)),
                ('MntSweetProducts', models.PositiveIntegerField(default=0)),
                ('MntGoldProds', models.PositiveIntegerField(default=0)),
                ('NumDealsPurchases', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Dt_Customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Income',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Marital_Status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MntFishProducts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MntFruits',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MntGoldProds',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MntMeatProducts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MntSweetProducts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='MntWines',
        ),
        migrations.RemoveField(
            model_name='user',
            name='NumDealsPurchases',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Year_Birth',
        ),
    ]
