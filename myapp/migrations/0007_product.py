# Generated by Django 4.1.5 on 2023-05-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_products_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('FT', 'Fantasy'), ('DC', 'Detective'), ('PL', 'Politics'), ('NV', 'Novel'), ('AU', 'Autobiography'), ('PR', 'Poetry'), ('BU', 'Business'), ('MD', 'Medicine')], max_length=2)),
                ('product_image', models.ImageField(blank=True, upload_to='media/product')),
            ],
        ),
    ]
