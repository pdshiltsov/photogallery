# Generated by Django 3.2.5 on 2021-07-25 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='название альбома')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos/', verbose_name='картинка')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('description', models.CharField(max_length=256, verbose_name='описание')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.album')),
            ],
        ),
    ]