from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_reviews"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="reviews",
        ),
    ]