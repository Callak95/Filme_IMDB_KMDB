from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
        ("users", "0003_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reviews",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="reviews.review",
            ),
        ),
    ]
