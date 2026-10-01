from django.shortcuts import get_object_or_404, redirect, render

from .models import FEED_NOW, OFFER_SNACK, REST, Dragon


def home(request):
    puff, _ = Dragon.objects.get_or_create(name="Puff")

    recommendation = puff.recommendation()
    if recommendation == FEED_NOW:
        banner = "URGENT: Puff needs food now."
    elif recommendation == REST:
        banner = "Puff needs rest."
    elif recommendation == OFFER_SNACK:
        banner = "Puff may need a snack soon."
    else:
        banner = "Puff is doing fine."

    return render(
        request,
        "daycare/home.html",
        {
            "puff": puff,
            "banner": banner,
            "care_board": recommendation,
            "status": puff.status_message(),
        },
    )


def feed_puff(request, dragon_id):
    puff = get_object_or_404(Dragon, id=dragon_id)
    if request.method == "POST":
        puff.feed()
        puff.save()
    return redirect("home")
