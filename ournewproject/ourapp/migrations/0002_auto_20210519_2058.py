# Generated by Django 3.2.3 on 2021-05-20 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='classYear',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ourapp.grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_graduation',
            field=models.IntegerField(),
        ),
    ]
