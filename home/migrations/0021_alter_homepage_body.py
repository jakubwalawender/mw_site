# Generated by Django 4.2.7 on 2024-03-23 21:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('motto_text', wagtail.blocks.RichTextBlock()), ('motto_text_small', wagtail.blocks.RichTextBlock()), ('heading_text', wagtail.blocks.RichTextBlock()), ('heading_text_small', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock()), ('link_url', wagtail.blocks.CharBlock(blank=True, max_length=500))])), ('display_scroll_down_button', wagtail.blocks.BooleanBlock(required=False))])), ('about_me', wagtail.blocks.StructBlock([('title', wagtail.blocks.RichTextBlock()), ('text', wagtail.blocks.RichTextBlock())])), ('opening_hours', wagtail.blocks.StructBlock([('monday', wagtail.blocks.CharBlock(label='Monday', required=True)), ('tuesday', wagtail.blocks.CharBlock(label='Tuesday', required=True)), ('wednesday', wagtail.blocks.CharBlock(label='Wednesday', required=True)), ('thursday', wagtail.blocks.CharBlock(label='Thursday', required=True)), ('friday', wagtail.blocks.CharBlock(label='Friday', required=True)), ('saturday', wagtail.blocks.CharBlock(label='Saturday', required=True)), ('sunday', wagtail.blocks.CharBlock(label='Sunday', required=True))])), ('contact', wagtail.blocks.StructBlock([('address', wagtail.blocks.TextBlock(required=False)), ('telephone', wagtail.blocks.ListBlock(wagtail.blocks.TextBlock(required=False))), ('mail', wagtail.blocks.TextBlock(required=False)), ('fax', wagtail.blocks.TextBlock(required=False)), ('folium_map', wagtail.blocks.StructBlock([('latitude', wagtail.blocks.FloatBlock(help_text='Enter the latitude', required=True)), ('longitude', wagtail.blocks.FloatBlock(help_text='Enter the longitude', required=True)), ('pin_tooltip', wagtail.blocks.TextBlock(help_text='Enter the pin tooltip text', required=False)), ('zoom_level', wagtail.blocks.IntegerBlock(default=10, help_text='Enter the zoom level', max_value=20, min_value=1))], required=False))]))], blank=True, null=True, use_json_field=True),
        ),
    ]