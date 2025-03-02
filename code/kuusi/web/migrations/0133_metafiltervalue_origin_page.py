# Generated by Django 4.2.14 on 2025-03-01 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0132_remove_metafilterwidget_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="metafiltervalue",
            name="origin_page",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meta_filter_value_page",
                to="web.page",
            ),
            preserve_default=False,
        ),
    ]
