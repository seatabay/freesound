from django.core.management.base import BaseCommand
from sounds.models import Sound
from similarity.client import Similarity
import sys

class Command(BaseCommand):
    args = ''
    help = 'Check if the field \'similarity_status\' of each sound is correctly synchronized with the similarity index. If a sound marked as \'OK\' is not found in the index, set it to \'PE\' (pending)'

    def handle(self, *args, **options):

        sounds_ok = 0
        sounds_set_to_pending = 0

        sounds = Sound.objects.filter(analysis_state='OK', moderation_state='OK').exclude(similarity_state='PE').only("id","similarity_state")
        print "Iterating over sounds with similarity_state != 'PE' (%i)..."%len(sounds)
        sys.stdout.flush()
        for sound in sounds:
            sys.stdout.write("\r%i of %i"%(sounds_ok+sounds_set_to_pending+1,len(sounds)))
            sys.stdout.flush()

            is_in_similarity_index = Similarity.contains(sound.id)

            if not is_in_similarity_index:
                sound.set_similarity_state('PE')
                sounds_set_to_pending += 1
            else:
                sounds_ok += 1

        print "\t- %i sounds set again to Pending"%sounds_set_to_pending
        print "\t- %i already Ok"%sounds_ok
