from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]
