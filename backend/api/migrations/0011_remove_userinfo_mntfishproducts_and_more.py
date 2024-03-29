# Generated by Django 5.0.2 on 2024-03-28 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_userinfo_numdealspurchases_alter_user_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='MntFishProducts',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='MntFruits',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='MntGoldProds',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='MntMeatProducts',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='MntSweetProducts',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='MntWines',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='api.product'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
