# Generated by Django 4.1.4 on 2024-12-22 12:33

from django.db import migrations, models
import logic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_video', models.FileField(upload_to=logic.models.original_video_directory_path)),
                ('processed_video', models.FileField(blank=True, null=True, upload_to=logic.models.processed_video_directory_path)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('done', 'Done'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]