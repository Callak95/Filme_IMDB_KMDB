from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="reviews",
        ),
    ]
