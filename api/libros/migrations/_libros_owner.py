from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '_rename_libros'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='libros', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]