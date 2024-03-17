import folium
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
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
    heading_text_small = blocks.RichTextBlock()
    button = HeroButton()
    display_scroll_down_button = blocks.BooleanBlock(required=False)
    panels = [
        FieldPanel("heading_text"),
        FieldPanel("button"),
        FieldPanel("display_scroll_down_button"),
        FieldPanel("heading_text_small")
    ]

    class Meta:
        icon = 'home'
        label = 'Hero'
        template = 'home/components/hero.html'


class AboutMeBlock(blocks.StructBlock):
    title = blocks.RichTextBlock()
    text = blocks.RichTextBlock()
    panels = [
        FieldPanel("title"),
        FieldPanel("text"),
    ]

    class Meta:
        icon = 'user'
        label = 'About me'
        template = 'home/components/about_me.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        return context


class FoliumMapBlock(blocks.StructBlock):
    latitude = blocks.FloatBlock(required=True, help_text='Enter the latitude')
    longitude = blocks.FloatBlock(required=True, help_text='Enter the longitude')
    pin_tooltip = blocks.TextBlock(required=False, help_text='Enter the pin tooltip text')
    zoom_level = blocks.IntegerBlock(default=10, min_value=1, max_value=20, help_text='Enter the zoom level')

    class Meta:
        icon = 'thumbtack-crossed'
        label = 'Folium Map'
        template = 'home/components/map.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        latitude = value.get('latitude')
        longitude = value.get('longitude')
        pin_tooltip = value.get('pin_tooltip')
        zoom_level = value.get('zoom_level')

        if latitude is not None and longitude is not None:
            f = folium.Figure(height=300)
            map = folium.Map(location=[latitude, longitude], zoom_start=zoom_level, scrollWheelZoom=False).add_to(f)
            # folium.TileLayer('MapBox Dark').add_to(map)
            popup_content = f'<div style="white-space: nowrap;">{pin_tooltip}</div>'

            folium.Marker(location=[latitude, longitude], popup=popup_content).add_to(map)
            context['map'] = map._repr_html_()  # Pass HTML representation of the map to the template
        return context


class ContactBlock(blocks.StructBlock):
    address = blocks.TextBlock(required=True)
    telephone = blocks.TextBlock(required=True)
    mail = blocks.TextBlock(required=True)
    folium_map = FoliumMapBlock()

    class Meta:
        icon = 'phone'
        label = 'Contact'
        template = 'home/components/contact.html'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        return context


class OpeningHoursBlock(blocks.StructBlock):
    monday = blocks.CharBlock(required=True, label="Monday")
    tuesday = blocks.CharBlock(required=True, label="Tuesday")
    wednesday = blocks.CharBlock(required=True, label="Wednesday")
    thursday = blocks.CharBlock(required=True, label="Thursday")
    friday = blocks.CharBlock(required=True, label="Friday")
    saturday = blocks.CharBlock(required=True, label="Saturday")
    sunday = blocks.CharBlock(required=True, label="Sunday")

    class Meta:
        icon = 'clock'
        label = 'Opening hours'
        template = 'home/components/opening_hours.html'


class HomePage(Page):
    max_count = 1
    body = StreamField([
        ('hero', Hero()),
        ('about_me', AboutMeBlock()),
        ('opening_hours', OpeningHoursBlock()),
        ('contact', ContactBlock())
    ], blank=True,
        null=True,
        use_json_field=True,
        block_counts={
            'hero': {'max_num': 1},
            'about_me': {'max_num': 1},
            'opening_hours': {'max_num': 1},
            'contact': {'max_num': 1}
        })
    content_panels = [
        FieldPanel("body")
    ]

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     return context
