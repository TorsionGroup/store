# Generated by Django 2.1.5 on 2019-01-30 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=120, verbose_name='Имя')),
                ('last_name', models.CharField(default='', max_length=120, verbose_name='Фамилия')),
                ('company_name', models.CharField(blank=True, default='', max_length=120, verbose_name='Компания')),
                ('address', models.CharField(default='', max_length=250, verbose_name='Адрес')),
                ('postcode', models.CharField(default='', max_length=120, verbose_name='Индекс')),
                ('phone', models.IntegerField(default=100000000, verbose_name='Телефон')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.City', verbose_name='Город')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.Country', verbose_name='Страна')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.State', verbose_name='Республика/Штат')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
