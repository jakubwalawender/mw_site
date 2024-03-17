# Generated by Django 4.2.7 on 2023-12-10 00:49

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock())])), ('display_scroll_down_button', wagtail.blocks.BooleanBlock(blank=True))]))], blank=True, null=True, use_json_field=True),
        ),
    ]