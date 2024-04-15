# Generated by Django 5.0.4 on 2024-04-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='product')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('HT', 'Harvesting tools'), ('ER', 'Educational resources'), ('PM', 'Packaging materials'), ('SE', 'Seeds'), ('PE', 'PPE'), ('GB', 'Growing Bags'), ('TC', 'Temperature Control'), ('HU', 'Humidifier')], max_length=2)),
            ],
        ),
    ]