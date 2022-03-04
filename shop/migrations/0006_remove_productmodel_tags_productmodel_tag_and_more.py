# Generated by Django 4.0.2 on 2022-03-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_colormodel_options_alter_productmodel_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tag',
            field=models.ManyToManyField(related_name='products', to='shop.TagModel', verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='code',
            field=models.CharField(max_length=7, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.ColorModel', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.SizeModel', verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='sizemodel',
            name='name',
            field=models.CharField(max_length=5, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='name',
            field=models.CharField(max_length=54, verbose_name='name'),
        ),
    ]
