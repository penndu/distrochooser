# Generated by Django 4.2.14 on 2025-02-09 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0126_alter_metafilterwidget_structure"),
    ]

    operations = [
        migrations.CreateModel(
            name="MetaFilterValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meta_filter_value_session",
                        to="web.session",
                    ),
                ),
            ],
        ),
    ]
