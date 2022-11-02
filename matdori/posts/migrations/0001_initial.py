
# Generated by Django 3.2.13 on 2022-11-02 02:45


from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('sectors', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(blank=True, max_length=30)),
                ('characteristic', models.CharField(blank=True, max_length=50)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('like_user', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('glade', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
