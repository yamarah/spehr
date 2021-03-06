# Generated by Django 3.2.5 on 2022-01-08 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import spehr.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spehr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=100, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=200)),
                ('father_name', models.CharField(blank=True, max_length=200)),
                ('designation', models.CharField(blank=True, max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('id_card_NO', models.IntegerField(blank=True, null=True)),
                ('volume_NO', models.IntegerField(blank=True, null=True)),
                ('page_NO', models.IntegerField(blank=True, null=True)),
                ('id_card_pic', models.ImageField(blank=True, upload_to=spehr.models.save_emp_image, verbose_name='ID Image')),
                ('all_contacts', models.IntegerField(blank=True, null=True)),
                ('emp_pic', models.ImageField(blank=True, upload_to=spehr.models.save_emp_image, verbose_name='emp pic')),
                ('Orginization_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empolyees', to='spehr.orginization')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='identify',
            name='empoly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empolys', to='spehr.empolyee'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
