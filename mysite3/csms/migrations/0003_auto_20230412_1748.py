# Generated by Django 3.1.3 on 2023-04-12 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csms', '0002_auto_20230412_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='csms.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='ccode',
            field=models.CharField(max_length=10),
        ),
    ]
