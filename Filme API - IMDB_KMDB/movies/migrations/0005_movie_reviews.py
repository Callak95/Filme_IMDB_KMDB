from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_alter_review_stars"),
        ("movies", "0004_remove_movie_reviews"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="reviews",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movie",
                to="reviews.review",
            ),
        ),
    ]
