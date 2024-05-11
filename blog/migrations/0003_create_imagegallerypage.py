# Generated by Django 5.0.4 on 2024-05-11 22:12

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpage_body'),
        ('custom_media', '0001_initial'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGalleryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('size', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], help_text='Please ensure that you do not skip heading levels. For example, the next heading after an H2 should only be either an H3 or another H2. <a href="https://www.a11yproject.com/posts/how-to-accessible-heading-structure/" target="_blank">Learn more about heading structure</a>')), ('text', wagtail.blocks.CharBlock())])), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text="Use to override the image's default alt text.", required=False)), ('decorative', wagtail.blocks.BooleanBlock(help_text='If this image does not contain meaningful content or is described in nearby text, check this box to not output its alt text.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(max_height=400, max_width=800))]),
        ),
        migrations.CreateModel(
            name='ImageGalleryImageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('alt_text', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='custom_media.customimage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='blog.imagegallerypage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
