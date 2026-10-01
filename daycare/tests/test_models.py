import pytest

from daycare.models import Dragon, care_recommendation


def test_care_recommendation_feed_now():
    assert care_recommendation(8, 5) == "FEED NOW"


def test_care_recommendation_rest():
    assert care_recommendation(3, 2) == "REST"


def test_care_recommendation_offer_snack():
    assert care_recommendation(6, 5) == "OFFER SNACK"


def test_care_recommendation_all_clear():
    assert care_recommendation(5, 5) == "ALL CLEAR"


def test_care_recommendation_feed_now_beats_rest():
    assert care_recommendation(9, 1) == "FEED NOW"


def test_care_recommendation_rest_beats_offer_snack():
    assert care_recommendation(7, 1) == "REST"


@pytest.mark.django_db
def test_feed_reduces_moderate_hunger():
    puff = Dragon.objects.create(hunger=6, energy=5, mood="content")

    puff.feed()

    assert puff.hunger == 4
    assert puff.mood == "happy"


@pytest.mark.django_db
def test_feed_reduces_severe_hunger_more_aggressively():
    puff = Dragon.objects.create(hunger=9, energy=5, mood="content")

    puff.feed()

    assert puff.hunger == 6
    assert puff.energy == 6
    assert puff.mood == "relieved"


@pytest.mark.django_db
def test_feed_never_makes_hunger_negative():
    puff = Dragon.objects.create(hunger=0, energy=5, mood="content")

    puff.feed()

    assert puff.hunger == 0


@pytest.mark.django_db
def test_status_message_for_very_hungry_dragon():
    puff = Dragon.objects.create(name="Puff", hunger=8, energy=5, mood="content")

    assert puff.status_message() == "Puff is very hungry!"

@pytest.mark.django_db
def test_status_message_says_need_snack_at_hunger_6():
    puff = Dragon.objects.create(name="Puff", hunger=6, energy=5, mood="content")

    assert puff.status_message() == "Puff could use a snack."

@pytest.mark.django_db
def test_mood_changes_between_hunger_5_and_4_feeding():
    puff_at_5 = Dragon.objects.create(hunger=5, energy=5, mood="content")
    puff_at_4 = Dragon.objects.create(hunger=4, energy=5, mood="content")

    puff_at_5.feed()
    puff_at_4.feed()

    assert puff_at_5.hunger == 3
    assert puff_at_5.mood == "happy"
    assert puff_at_4.hunger == 3
    assert puff_at_4.mood == "sleepy"

@pytest.mark.django_db
def test_feed_does_not_raise_energy_above_10():
    puff = Dragon.objects.create(hunger=8, energy=10, mood="content")

    puff.feed()

    assert puff.energy == 10

