import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ]
            ),
        ),
    ]
