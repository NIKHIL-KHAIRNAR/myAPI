# Generated by Django 2.0.7 on 2018-07-26 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_testtable_nm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testtable',
            options={'verbose_name': 'API', 'verbose_name_plural': "API's"},
        ),
        migrations.RenameField(
            model_name='testtable',
            old_name='nm',
            new_name='mobile',
        ),
    ]
