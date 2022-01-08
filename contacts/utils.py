import random

import string
# from django.db.models import
# =================================
#          GIS CONSULTING 4 RANDOM
#             START
# =================================
def random_string_generator():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    result = ''
    for i in range(0, 11):
        result += random.choice(characters)
    return result

def unique_post_id_generator(instance):
    code_post_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(code_person=code_post_new_id).exists()
    if qs_exists:
        return unique_post_id_generator(instance)
    return code_post_new_id




# =================================
#         GIS CONSULTING 4 RANDOM
#             END
# =================================