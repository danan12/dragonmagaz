# Generated by Django 2.2.2 on 2019-06-06 15:42

from django.db import migrations, models
import ecomap.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomap', '0003_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=ecomap.models.image_folder),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Товар'),
        ),
    ]
