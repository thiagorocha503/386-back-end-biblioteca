# Generated by Django 2.2.5 on 2019-09-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
            ],
        ),
    ]