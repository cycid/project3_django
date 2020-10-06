# Generated by Django 2.1.5 on 2020-05-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=50)),
                ('dish_type', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('adds_amount', models.IntegerField()),
                ('comparison', models.CharField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='toppings',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='toppings',
            name='dishes',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.menu'),
        ),
    ]