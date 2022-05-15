# Generated by Django 3.0.5 on 2020-04-24 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('price', models.FloatField(default=0)),
                ('image', models.CharField(default='https://sneakertown.kz/bitrix/templates/styleshop_club/components/bitrix/catalog.top/catalog/images/no_photo.png', max_length=200)),
                ('color', models.CharField(max_length=200, null=True)),
                ('size', models.CharField(default='no left sizes', max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
    ]
