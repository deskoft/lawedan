from evennia.utils import gametime
from typeclasses.characters import Character

def at_sunrise():
    for character in Character.objects.all():
        #This will handle giving characters energy every day.
        character.db.energy = character.db.energy + 10

def start_sunrise_event():
    """Schedule at_sunrise()"""
    script = gametime.schedule(at_sunrise, repeat=True, hour=6, min=0, sec=0)
    script.key = "at sunrise"