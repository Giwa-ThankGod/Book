# Generated by Django 4.0.2 on 2022-06-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_remove_book_category_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='App.Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
