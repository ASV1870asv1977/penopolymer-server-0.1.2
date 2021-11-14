# Generated by Django 3.2.9 on 2021-11-12 11:07

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('slideshow', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, features=['link'], label='Название картинки'))])))], blank=True),
        ),
    ]
