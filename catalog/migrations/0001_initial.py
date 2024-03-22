from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('price', models.IntegerField(default=0, verbose_name='цена за покупку')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='main/', verbose_name='изображение(превью)')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('last_change', models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')),
                ('category', models.CharField(max_length=150, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
