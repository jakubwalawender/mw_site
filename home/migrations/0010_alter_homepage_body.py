# Generated by Django 4.2.7 on 2024-03-14 20:18

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock()), ('link_url', wagtail.blocks.CharBlock(blank=True, max_length=500))])), ('display_scroll_down_button', wagtail.blocks.BooleanBlock(required=False))])), ('map', wagtail.blocks.StructBlock([('location', wagtail.blocks.CharBlock(help_text='Enter the location (latitude, longitude)', required=True)), ('zoom_level', wagtail.blocks.IntegerBlock(default=10, help_text='Enter the zoom level', max_value=20, min_value=1))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
