# Generated by Django 3.2.9 on 2021-11-12 07:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephones', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Телефоны предприятия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email предприятия')),
                ('address', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Адрес предприятия')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Хедер',
                'verbose_name_plural': 'Хедеры',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Адрес предприятия')),
                ('telephones', wagtail.core.fields.RichTextField(max_length=100, verbose_name='Телефоны предприятия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email предприятия')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футеры',
            },
        ),
    ]