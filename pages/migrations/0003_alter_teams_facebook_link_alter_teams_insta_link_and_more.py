# Generated by Django 4.0.2 on 2022-03-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_teams_options_alter_teams_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='facebook_link',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='teams',
            name='insta_link',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='teams',
            name='twitter_link',
            field=models.URLField(default='', max_length=100),
        ),
    ]