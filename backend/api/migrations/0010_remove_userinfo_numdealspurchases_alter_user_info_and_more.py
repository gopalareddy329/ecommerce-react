# Generated by Django 5.0.2 on 2024-03-28 18:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_product_category_alter_user_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='NumDealsPurchases',
        ),
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.userinfo'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Income',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
