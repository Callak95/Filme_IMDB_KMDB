from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("genres", "0001_initial"),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(max_length=127)),
                ("premiere", models.DateField()),
                ("classification", models.IntegerField()),
                ("synopsis", models.TextField()),
                (
                    "genres",
                    models.ManyToManyField(related_name="movies", to="genres.genre"),
                ),
                (
                    "reviews",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to="reviews.review",
                    ),
                ),
            ],
        ),
    ]
