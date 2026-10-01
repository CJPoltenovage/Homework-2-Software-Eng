from django.db import models

STARVING = 8            
SNACKING_HUNGER = 6    
HUNGER = 5             
LOW_ENERGY = 2         
MIN_HUNGER = 0
MAX_ENERGY = 10


FEED_NOW = "FEED NOW"
REST = "REST"
OFFER_SNACK = "OFFER SNACK"
ALL_CLEAR = "ALL CLEAR"


def is_starving(hunger):
    return hunger >= STARVING


def is_snacking_hungry(hunger):
    return hunger >= SNACKING_HUNGER


def is_exhausted(energy):
    return energy <= LOW_ENERGY


def care_recommendation(hunger, energy):
    # Checked in priority order: the first rule that matches wins.
    if is_starving(hunger):
        return FEED_NOW
    if is_exhausted(energy):
        return REST
    if is_snacking_hungry(hunger):
        return OFFER_SNACK
    return ALL_CLEAR


class Dragon(models.Model):
    name = models.CharField(max_length=50, default="Puff")
    hunger = models.IntegerField(default=5)
    energy = models.IntegerField(default=5)
    mood = models.CharField(max_length=20, default="content")

    def feed(self):
        if is_starving(self.hunger):
            self.hunger -= 3
            self.energy += 1
            self.mood = "relieved"
        elif self.hunger >= HUNGER:
            self.hunger -= 2
            self.mood = "happy"
        else:
            self.hunger -= 1
            self.mood = "sleepy"

        if self.hunger < MIN_HUNGER:
            self.hunger = MIN_HUNGER
        if self.energy > MAX_ENERGY:
            self.energy = MAX_ENERGY

    def recommendation(self):
        return care_recommendation(self.hunger, self.energy)

    def status_message(self):
        recommendation = self.recommendation()
        if recommendation == FEED_NOW:
            return f"{self.name} is very hungry!"
        if recommendation == REST:
            return f"{self.name} is exhausted."
        if recommendation == OFFER_SNACK:
            return f"{self.name} could use a snack."
        if self.mood == "happy":
            return f"{self.name} is happy."
        if self.mood == "relieved":
            return f"{self.name} looks relieved."
        if self.mood == "sleepy":
            return f"{self.name} is sleepy."
        return f"{self.name} is doing fine."
    
    def needs_attention(self):
        return (
            is_starving(self.hunger) or is_exhausted(self.energy) or self.mood == "sleepy"
        )

    def __str__(self):
        return self.name
