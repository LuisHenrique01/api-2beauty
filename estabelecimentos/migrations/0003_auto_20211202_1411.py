# Generated by Django 3.2.7 on 2021-12-02 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0002_auto_20211202_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='horarios',
        ),
        migrations.AddField(
            model_name='horarios',
            name='agenda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='estabelecimentos.agenda'),
            preserve_default=False,
        ),
    ]
