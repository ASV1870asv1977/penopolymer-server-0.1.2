# Generated by Django 3.2.9 on 2021-11-12 11:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('slideshow', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, features=['link'], label='Название картинки'))]))), ('heading', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'hr', 'bold', 'italic'], help_text='Введите название заголовка', label='Заголовок №1')), ('caption', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'h6', 'hr', 'bold', 'italic'], help_text='Введите название заголовка', label='Заголовок №2')), ('title_blue_stripe', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Введите название заголовка', label='Заголовок на синей полосе'))], blank=True),
        ),
    ]
