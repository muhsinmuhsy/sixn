# Generated by Django 4.2.3 on 2023-09-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='brand-image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purchase_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purchase_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
