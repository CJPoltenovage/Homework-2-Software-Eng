import pytest
from django.urls import reverse

from daycare.models import Dragon


@pytest.mark.django_db
def test_home_page_shows_urgent_banner_for_very_hungry_puff(client):
    Dragon.objects.create(name="Puff", hunger=8, energy=5, mood="content")

    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "URGENT: Puff needs food now." in response.content.decode()


@pytest.mark.django_db
def test_feed_endpoint_changes_puff_and_redirects(client):
    puff = Dragon.objects.create(name="Puff", hunger=6, energy=5, mood="content")

    response = client.post(reverse("feed_puff", args=[puff.id]))

    puff.refresh_from_db()
    assert response.status_code == 302
    assert puff.hunger == 4


@pytest.mark.django_db
def test_home_page_hungry_and_exhausted_recommends_rest(client):
    Dragon.objects.create(name="Puff", hunger=7, energy=1, mood="content")

    response = client.get(reverse("home"))

    assert response.context["banner"] == "Puff needs rest."
    assert "Care Board: REST" in response.content.decode()
    assert response.context["status"] == "Puff is exhausted."

