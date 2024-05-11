# Generated by Django 5.0.4 on 2024-05-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product18',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name18', models.CharField(max_length=200, null=True)),
                ('price18', models.FloatField()),
                ('digital18', models.BooleanField(default=False, null=True)),
                ('image18', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='LINK',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
