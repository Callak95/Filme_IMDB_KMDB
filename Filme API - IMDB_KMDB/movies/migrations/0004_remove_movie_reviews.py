from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movie_reviews"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="reviews",
        ),
    ]
