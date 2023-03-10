# Generated by Django 3.2.17 on 2023-02-11 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appartments', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MastersRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_type', models.CharField(choices=[('electrician', 'электри'), ('plumber', 'сантехник'), ('locksmith', 'слесарь')], max_length=200)),
                ('date_work', models.DateField()),
                ('time_work', models.TimeField()),
                ('desctiption', models.TextField()),
                ('status', models.CharField(choices=[('new', 'ноывая'), ('is_performing', 'в работе'), ('have_done', 'выполнена')], max_length=200)),
                ('admin_comment', models.TextField()),
                ('appartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appartments.appartment')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
