# Generated by Django 5.0.6 on 2024-08-20 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_rename_snapshot_snapshottag_snapshot_old_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshottag',
            name='snapshot_old',
            field=models.ForeignKey(db_column='snapshot_old_id', on_delete=django.db.models.deletion.CASCADE, to='core.snapshot', to_field='old_id'),
        ),
    ]
