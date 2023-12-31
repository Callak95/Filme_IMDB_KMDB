import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0004_review_critic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ]
            ),
        ),
    ]
