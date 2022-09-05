from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Libros',
            new_name='Libro',
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ('-created_at',), 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='create_at',
            new_name='created_at',
        ),
    ]