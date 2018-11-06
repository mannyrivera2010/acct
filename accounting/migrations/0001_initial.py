# Generated by Django 2.1.3 on 2018-11-06 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('ASSET', 'ASSET'), ('LIABILITY', 'LIABILITY'), ('EQUITY', 'EQUITY')], default='ASSET', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=32)),
                ('first_entry_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_entry', to='accounting.Account')),
                ('second_entry_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_entry', to='accounting.Account')),
            ],
        ),
    ]
