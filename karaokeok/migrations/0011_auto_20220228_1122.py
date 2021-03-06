# Generated by Django 4.0.2 on 2022-02-28 11:22
from django.db import migrations

from karaokeok.models import Song


def update_song(apps, schema_editor, old_title, new_title):
    """
    :type apps:
    :type schema_editor:
    :type old_title: str
    :type new_title: str
    :rtype: Song
    """
    song = Song.objects.get(title=old_title)
    song.title = new_title
    song.save()

    return song


def migration_0011(apps, schema_editor):
    update_song(apps, schema_editor, old_title='Quand j\'serai ko', new_title='Quand j\'serai KO')
    update_song(apps, schema_editor, old_title='Hey jude', new_title='Hey Jude')
    update_song(apps, schema_editor, old_title='Rockolletion', new_title='Rockollection')
    update_song(apps, schema_editor, old_title='Au café des délices', new_title='Au Café des Délices')


class Migration(migrations.Migration):

    dependencies = [
        ('karaokeok', '0010_proposal_updated_at'),
    ]

    operations = [
        migrations.RunPython(migration_0011),
    ]
