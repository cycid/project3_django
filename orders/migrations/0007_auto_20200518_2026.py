# Generated by Django 2.1.5 on 2020-05-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='dishes',
            field=models.ManyToManyField(blank=True, related_name='toppingsss', to='orders.menu'),
        ),
    ]
