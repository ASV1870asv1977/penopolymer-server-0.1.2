from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock, RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from home.blocks import SlideshowBlock, ArticleBlockTwo, ImagesShowBlock, CardProductBig, CardProductLittle, \
    YoutubeBlock, LibraryDoc, QuestionAnswerBlock, PublicationBlock, MapBlock


class HomePage(Page):
    body = StreamField(
        [

            ('slideshow', blocks.ListBlock(SlideshowBlock(), label='Слайды')),
            ('heading', RichTextBlock(
                features=['h1', 'h2', 'h3', 'hr', 'bold', 'italic'],
                label='Заголовок №1',
                help_text='Введите название заголовка')),
            ('caption', RichTextBlock(
                features=['h4', 'h5', 'h6', 'hr', 'bold', 'italic'],
                label='Заголовок №2',
                help_text='Введите название заголовка')),
            ('title_blue_stripe_full', RichTextBlock(
                features=['bold', 'italic'],
                label='Заголовок на широкой синей полосе',
                help_text='Введите название заголовка')),
            ('title_blue_stripe_short', RichTextBlock(
                features=['bold', 'italic'],
                label='Заголовок на узкой синей полосе',
                help_text='Введите название заголовка')),
            ('article_two', ArticleBlockTwo()),
            ('image_big', ImageChooserBlock(label='Изображение на всю ширину')),
            ('image_content', ImageChooserBlock(label='Изображение на ширину контента')),
            ('images_show', blocks.ListBlock(ImagesShowBlock(), label='Блок изображений')),
            ('article_text', RichTextBlock(
                label='Текстовый блок',
                help_text='Введите текст статьи',
                icon='form',
            )),
            ('product_card_big', blocks.ListBlock(CardProductBig(), label='Блок карточек продукции (больших)')),
            ('product_card_little', blocks.ListBlock(CardProductLittle(), label='Блок карточек продукции (маленьких)')),
            ('photo_gallery', blocks.ListBlock(ImagesShowBlock(), label='Фотогалерея')),
            ('youtube_block', blocks.ListBlock(EmbedBlock(icon='media'), label='Видео галерея стандарт')),
            ('youtube_handmade', blocks.ListBlock(YoutubeBlock(icon='media'), label='Видео галерея')),
            ('library_doc', blocks.ListBlock(LibraryDoc(icon='doc-full-inverse'), label='Библиотека')),
            ('question_answer', blocks.ListBlock(QuestionAnswerBlock(icon='doc-full'), label='Вопрос - ответ')),
            ('publication', blocks.ListBlock(PublicationBlock(icon='doc-full'), label='Список статей и публикаций')),
            ('map_map', MapBlock()),

        ],
        # block_counts={
        #     'events_news': {'max_num': 1},
        #     'products': {'max_num': 1},
        # },
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
