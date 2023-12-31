from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0006_remove_movie_reviews"),
        ("reviews", "0002_alter_review_stars"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="movie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review",
                to="movies.movie",
            ),
        ),
    ]
