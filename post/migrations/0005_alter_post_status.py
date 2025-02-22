# Generated by Django 5.1.6 on 2025-02-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published')], default='DR', max_length=2),
        ),
    ]
