# Generated by Django 3.2.17 on 2023-02-11 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'активен'), ('new', 'новый'), ('disable', 'отключен')], max_length=200)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('surname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('patronymic', models.CharField(max_length=200)),
                ('burn', models.DateField()),
                ('note', models.TextField()),
                ('phone', models.CharField(max_length=200)),
                ('viber', models.CharField(max_length=200)),
                ('telegam', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='galery/', verbose_name='Аватар')),
                ('role', models.CharField(blank=True, choices=[('director', 'директор'), ('manager', 'управляющий'), ('accounter', 'бухгалтер'), ('electrician', 'электри'), ('plumber', 'сантехник'), ('locksmith', 'слесарь')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='users.user')),
                ('to_users', models.ManyToManyField(related_name='to_users', to='users.User')),
            ],
        ),
    ]