# Generated by Django 3.2.9 on 2021-11-14 14:51

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('slideshow', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, features=['link'], label='Название картинки'))]), label='Слайды')), ('heading', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'hr', 'bold', 'italic'], help_text='Введите название заголовка', label='Заголовок №1')), ('caption', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'h6', 'hr', 'bold', 'italic'], help_text='Введите название заголовка', label='Заголовок №2')), ('title_blue_stripe_full', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Введите название заголовка', label='Заголовок на широкой синей полосе')), ('title_blue_stripe_short', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], help_text='Введите название заголовка', label='Заголовок на узкой синей полосе')), ('article_two', wagtail.core.blocks.StructBlock([('figure_second', wagtail.images.blocks.ImageChooserBlock(label='Картинка справа')), ('description_second', wagtail.core.blocks.RichTextBlock(label='Статья (текст слева)'))])), ('image_big', wagtail.images.blocks.ImageChooserBlock(label='Изображение на всю ширину')), ('image_content', wagtail.images.blocks.ImageChooserBlock(label='Изображение на ширину контента')), ('images_show', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]), label='Блок изображений')), ('article_text', wagtail.core.blocks.RichTextBlock(help_text='Введите текст статьи', icon='form', label='Текстовый блок')), ('product_card_big', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, features=['link'], label='Название продукта'))]), label='Блок карточек продукции (больших)')), ('product_card_little', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, features=['link'], label='Название продукта'))]), label='Блок карточек продукции (маленьких)')), ('photo_gallery', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]), label='Фотогалерея')), ('youtube_block', wagtail.core.blocks.ListBlock(wagtail.embeds.blocks.EmbedBlock(icon='media'), label='Видео галерея стандарт')), ('youtube_handmade', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('video_field', wagtail.core.blocks.CharBlock(label='Ссылка на видео')), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, label='Название видео'))], icon='media'), label='Видео галерея')), ('library_doc', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('related_document', wagtail.documents.blocks.DocumentChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, label='Название документа'))], icon='doc-full-inverse'), label='Библиотека')), ('question_answer', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.RichTextBlock(blank=True, label='Вопрос')), ('answer', wagtail.core.blocks.RichTextBlock(blank=True, label='Вопрос'))], icon='doc-full'), label='Вопрос - ответ')), ('publication', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('event_data', wagtail.core.blocks.CharBlock(label='Число месяца', max_length=2)), ('event_month', wagtail.core.blocks.CharBlock(label='Месяц', max_length=8)), ('event_name', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'], help_text='Введите название публикации', label='Название публикации', null=True)), ('event_description', wagtail.core.blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'], help_text='Введите описание', label='Описание публикации', null=True))], icon='doc-full'), label='Список статей и публикаций')), ('map_map', wagtail.core.blocks.StructBlock([]))], blank=True),
        ),
    ]
