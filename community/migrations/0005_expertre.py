# Generated by Django 3.2.6 on 2021-08-10 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_auto_20210810_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertRe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(max_length=100)),
                ('thumbsUp', models.IntegerField(blank=True, default=0, null=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
