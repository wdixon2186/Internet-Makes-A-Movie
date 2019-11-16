# Generated by Django 2.2.7 on 2019-11-15 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('logline', models.CharField(max_length=140)),
                ('upload', models.FileField(blank=True, default='default.pdf', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='imam.Script')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='imam.Video')),
            ],
        ),
    ]
