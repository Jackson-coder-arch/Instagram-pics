# Generated by Django 3.1.7 on 2021-03-30 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pictures', '0003_auto_20210329_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_posts',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='image_posts',
            name='image_caption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image_posts',
            name='image_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
