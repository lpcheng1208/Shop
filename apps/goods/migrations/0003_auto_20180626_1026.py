# Generated by Django 2.0.2 on 2018-06-26 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180619_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类目级别'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='indexad',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='goods', to='goods.Goods'),
        ),
    ]
