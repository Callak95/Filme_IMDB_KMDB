from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("stars", models.IntegerField()),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(default=False)),
                (
                    "recomendation",
                    models.CharField(
                        choices=[
                            ("Must Watch", "Must"),
                            ("Should Watch", "Should"),
                            ("Avoid Watch", "Avoid"),
                            ("No Opinion", "Default"),
                        ],
                        default="No Opinion",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
