# Generated by Django 5.1.2 on 2024-10-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_user_remove_todoitem_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.CharField(default='-1', max_length=150),
        ),
    ]
