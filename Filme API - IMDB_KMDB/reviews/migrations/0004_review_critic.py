from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0003_review_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="critic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
