from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.models import Page
from django.utils.translation import pgettext_lazy


class HeroButton(blocks.StructBlock):
    text = blocks.CharBlock()
    link_url = blocks.CharBlock(
        max_length=500,
        blank=True
    )
    panels = [
        FieldPanel("text"),
        FieldPanel("link_url")
    ]


class Hero(blocks.StructBlock):
    heading_text = blocks.RichTextBlock()
    button = HeroButton()
    display_scroll_down_button = blocks.BooleanBlock(required=False)
    panels = [
        FieldPanel("heading_text"),
        FieldPanel("button"),
        FieldPanel("display_scroll_down_button")
    ]


class HomePage(Page):
    max_count = 1
    body = StreamField([
        ('hero', Hero())
    ], blank=True,
        null=True,
        use_json_field=True,
        block_counts={
            'hero': {'max_num': 1},
        })
    content_panels = [
        FieldPanel("body")
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context
