# Generated by Django 3.2.7 on 2021-09-30 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='users',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='movie',
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='movie',
                to='movies.movie'
            ),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user',
                to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
