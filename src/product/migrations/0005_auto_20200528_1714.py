# Generated by Django 3.0.6 on 2020-05-28 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200528_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='catageoryId',
            field=models.ManyToManyField(related_name='offers', to='product.catageory'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='product',
            field=models.ManyToManyField(related_name='offers', to='product.product'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='subCatageoryId',
            field=models.ManyToManyField(related_name='offers', to='product.subCatageory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCatageoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.subCatageory'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productimage', to='product.product'),
        ),
        migrations.AlterField(
            model_name='productserial',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productserial', to='product.product'),
        ),
        migrations.AlterField(
            model_name='subcatageory',
            name='catageoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcatageory', to='product.catageory'),
        ),
    ]
