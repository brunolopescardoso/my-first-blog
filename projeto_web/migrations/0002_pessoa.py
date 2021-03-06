# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cpf', models.IntegerField()),
                ('nom_pessoa', models.CharField(max_length=200)),
                ('end_email', models.EmailField(max_length=254)),
                ('dt_nascimento', models.DateTimeField()),
                ('dt_cadastro', models.DateTimeField()),
            ],
        ),
    ]
