# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('description', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PossibleDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('poll', models.ForeignKey(related_name=b'possible_dates', to='datefinder.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='maybe',
            field=models.ManyToManyField(related_name=b'maybe_answers', to='datefinder.PossibleDate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(related_name=b'answers', to='datefinder.Poll'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='yes',
            field=models.ManyToManyField(related_name=b'positive_answers', to='datefinder.PossibleDate'),
            preserve_default=True,
        ),
    ]
