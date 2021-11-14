from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Header(models.Model):
    """Класс для формирования фрагмента хедера сайта"""

    logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    telephones = RichTextField(
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    email = RichTextField(
        features=['link'],
        verbose_name="Email предприятия",
    )

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    panels = [
        ImageChooserPanel('logo'),
        FieldPanel('telephones'),
        FieldPanel('email'),
        FieldPanel('address'),
    ]

    class Meta:
        verbose_name = 'Хедер'
        verbose_name_plural = 'Хедеры'

    def __str__(self):
        return 'Хедер'


@register_snippet
class Footer(models.Model):
    """Класс для формирования фрагмента футера сайта"""

    logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    email = RichTextField(
        features=['link'],
        verbose_name="Email предприятия",
    )

    panels = [
        ImageChooserPanel('logo'),
        FieldPanel('address'),
        FieldPanel('telephones'),
        FieldPanel('email'),
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return 'Футер'
