from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_review_movie"),
        ("users", "0004_user_reviews"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="reviews",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="critic",
                to="reviews.review",
            ),
        ),
    ]
