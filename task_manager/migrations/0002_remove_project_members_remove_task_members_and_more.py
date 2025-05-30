# Generated by Django 5.1.6 on 2025-04-23 07:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.RemoveField(
            model_name='task',
            name='members',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file_size',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='file',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.project'),
        ),
        migrations.AlterField(
            model_name='file',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.project'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taskmember',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
