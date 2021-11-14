from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from django import forms


class SlideshowBlock(StructBlock):
    """Класс для формирования слайда в слайд-шоу"""

    figure = ImageChooserBlock(label='Картинка')
    caption = RichTextBlock(features=['link'], label='Название картинки', blank=True)

    class Meta:
        icon = 'view'
        label = 'Слайд'


class ArticleBlockTwo(StructBlock):
    """Класс для формирования блока Статья (картинка справа)"""

    figure_second = ImageChooserBlock(label='Картинка справа')
    description_second = RichTextBlock(label='Статья (текст слева)')

    class Meta:
        icon = 'form'
        label = 'Статья (картинка справа)'


class ImagesShowBlock(StructBlock):
    """Класс для формирования изображения в блок изображений"""

    figure = ImageChooserBlock(label='Картинка')

    class Meta:
        icon = 'image'
        label = 'Изображение'


class CardProductBig(StructBlock):
    """Класс для формирования большой карточки продукции"""

    figure = ImageChooserBlock(label='Картинка')
    caption = RichTextBlock(features=['link'], label='Название продукта', blank=True)

    class Meta:
        # icon = 'view'
        label = 'Карточка продукции (большая)'


class CardProductLittle(StructBlock):
    """Класс для формирования маленькой карточки продукции"""

    figure = ImageChooserBlock(label='Картинка')
    caption = RichTextBlock(features=['link'], label='Название продукта', blank=True)

    class Meta:
        # icon = 'view'
        label = 'Карточка продукции (маленькая)'


class YoutubeBlock(StructBlock):
    """Класс для формирования карточки видео"""

    video_field = CharBlock(label='Ссылка на видео')
    caption = RichTextBlock(label='Название видео', blank=True)

    class Meta:
        icon = 'media'
        label = 'Карточка видео'


class LibraryDoc(StructBlock):
    """Класс для формирования документа библиотеки"""

    related_document = DocumentChooserBlock()
    caption = RichTextBlock(label='Название документа', blank=True)

    class Meta:
        icon = 'doc-full'
        label = 'Документ библиотеки'


class QuestionAnswerBlock(StructBlock):
    """Класс для формирования элемента Вопрос-ответ"""

    question = RichTextBlock(label='Вопрос', blank=True)
    answer = RichTextBlock(label='Вопрос', blank=True)

    class Meta:
        icon = 'doc-full'
        label = 'Вопрос с ответом'


class PublicationBlock(StructBlock):
    """Класс для формирования карточки публикации"""

    event_data = CharBlock(max_length=2, label="Число месяца")
    event_month = CharBlock(max_length=8, label="Месяц")
    event_name = RichTextBlock(
        null=True,
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        label='Название публикации',
        help_text='Введите название публикации',
    )
    event_description = RichTextBlock(
        blank=True,
        null=True,
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        label='Описание публикации',
        help_text='Введите описание',
    )

    class Meta:
        icon = 'doc-full'
        label = 'Мероприятие'


class MapBlock(StructBlock):
    """Класс для формирования блока с яндекс-картой"""

    class Meta:
        # template = 'tags/map.html'
        label = 'Яндекс карта'
