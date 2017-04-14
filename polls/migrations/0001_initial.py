# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Author2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200, null=True)),
                ('votes', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField()),
                ('n_comments', models.IntegerField()),
                ('n_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('a', models.ManyToManyField(related_name='a', to='polls.Author')),
                ('au', models.ManyToManyField(related_name='b', to='polls.Author')),
                ('blog', models.ForeignKey(to='polls.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('details', models.TextField()),
                ('entry', models.OneToOneField(to='polls.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, null=True, blank=True)),
                ('group', models.ForeignKey(blank=True, to='polls.Group', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i', models.IntegerField(default=0)),
                ('c', models.CharField(default=b'abc', max_length=19, null=True)),
                ('im', models.ImageField(upload_to=b'', blank=True)),
                ('f', models.FileField(upload_to=b'', blank=True)),
                ('year_in_school', models.CharField(default=b'JR', max_length=2, choices=[(b'FR', b'Freshman'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('mychoices', models.CharField(max_length=10, null=True, choices=[(b'Audio', ((b'vinyl', b'Vinyl'), (b'cd', b'CD'))), (b'Video', ((b'vhs', b'VHS Tape'), (b'dvd', b'DVD'))), (b'unknown', b'Unknown')])),
                ('mc', models.IntegerField(default=2, choices=[(1, b'one'), (2, b'two')])),
            ],
        ),
        migrations.CreateModel(
            name='OpinionPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200, null=True, blank=True)),
                ('poll_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_published_at', models.DateTimeField(null=True, blank=True)),
                ('book', models.ForeignKey(blank=True, to='polls.Book', null=True)),
            ],
            options={
                'ordering': ['_published_at'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=50, null=True, blank=True)),
                ('response', models.TextField(null=True, blank=True)),
                ('poll', models.ForeignKey(blank=True, to='polls.OpinionPoll', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
                ('registered_users', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(blank=True, to='polls.Publisher', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='inviter',
            field=models.ForeignKey(related_name='membership_invites', blank=True, to='polls.Person', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(related_name='a', blank=True, to='polls.Person', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='polls.Person', blank=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=8, to='polls.Question', null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(related_name='b', through='polls.Publication', to='polls.Publisher', blank=True),
        ),
    ]
