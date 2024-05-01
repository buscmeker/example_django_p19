from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=155)),
                ('phone_number', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]