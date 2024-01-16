from django.shortcuts import render
from mtgsdk import Card as MTGCard
from .models import Card


def fetch_cards(request):
    # Example: Fetch cards from the MTG API
    mtg_cards = MTGCard.where(set='cmr').where(subtypes='angel').all()[:10]  # Adjust query as needed

    for mtg_card in mtg_cards:
        card, created = Card.objects.get_or_create(
            name=mtg_card.name,
            defaults={
                'mana_cost': mtg_card.mana_cost,
                'cmc': mtg_card.cmc,
                'type_line': mtg_card.type,
                'oracle_text': mtg_card.text,
                'colors': ','.join(mtg_card.colors),
                'image_url': mtg_card.image_url
            }
        )

    cards = Card.objects.all()

    return render(request, 'cards.html', {'cards': cards})


def fetch_commander_cards():
    # Fetching legendary creature cards
    commanders = Card.where(supertypes='legendary').where(types='creature').all()
    return commanders


def commanders_view(request):
    commanders = fetch_commander_cards()
    return render(request, 'commanders.html', {'commanders': commanders})
