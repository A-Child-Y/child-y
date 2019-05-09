# Generated by Django 2.0 on 2019-05-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('y1', '0003_childuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=2)),
                ('sig', models.CharField(max_length=20)),
                ('add', models.CharField(max_length=20)),
                ('pst', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
                ('pid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='y1.ChildUser')),
            ],
            options={
                'db_table': 'y_info',
            },
        ),
    ]